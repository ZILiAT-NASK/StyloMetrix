# Copyright (C) 2023  NASK PIB
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import re
from pathlib import Path
from typing import List, Union

import numpy as np
import pandas as pd
import spacy
from sklearn.base import BaseEstimator, TransformerMixin
from spacy_syllables import SpacySyllables
from tqdm import tqdm

from .metrics import *
from .pipeline import *
from .structures import *
from .structures import Lang


class StyloMetrix(BaseEstimator, TransformerMixin):
    """Class for counting linguistic metrics.

    Args:
        lang (str): Language. One of ['de','en', 'pl', 'ru', 'ukr']
        nlp (spacy.language.Language, optional): Language model to use from spacy. Defaults to None. If None predefined models are used.
        metrics (Union[MetricGroup, List[str], None], optional): List of Metrics to use. Defaults to None. If not defined all available metrics will be used.
        exceptions (Union[MetricGroup, List[str], None], optional): List of Metrics to remove. Defaults to None. If not defined no metric will be removed.
        debug (bool, optional): Should debug be collected?. Defaults to False.
        save_path (Union[str, Path], optional): Path to save result and between steps. Defaults to None.
        output_name (str, optional): Filename for SM output. Defaults to "sm_output".
        debug_name (str, optional): Filename for SM debug. Defaults to "sm_debug".
        save_step (int, optional): Define after how many steps StyloMetrix should be saved. Defaults to None. If not defined, no intermediate steps are saved.
        nlp_customization (_type_, optional): NLP customization. Defaults to None.
    """

    def __init__(
        self,
        lang: str,
        nlp: spacy.language.Language = None,
        metrics: Union[MetricGroup, List[str], None] = None,
        exceptions: Union[MetricGroup, List[str], None] = None,
        debug: bool = False,
        save_path: Union[str, Path] = None,
        output_name: str = "sm_output",
        debug_name: str = "sm_debug",
        save_step: int = None,
        nlp_customization=None,
    ):
        super().__init__()
        self._debug = debug
        self._customization = nlp_customization
        self._save_path = save_path
        self._save_step = save_step
        self.output_name = output_name
        self.debug_name = debug_name
        self._init_nlp(lang, nlp)
        self._init_metrics(metrics, exceptions, self.nlp)
        self._set_pipeline()
        if save_path:
            self._save_path = Path(save_path)
            self._save_path.mkdir(parents=True, exist_ok=True)
            self._file_number = self._determine_number()

    def fit(self, texts, outputs=None):
        return self

    def transform(self, texts):
        if isinstance(texts, str):
            texts = [texts]
        else:
            texts = list(texts)

        columns = list()
        m_columns = list()
        values = list()
        debugs = list()

        for i, text in tqdm(enumerate(texts), total=len(texts)):
            try:
                doc = self.nlp(text)
                doc_content = list()
                doc_content.append(text)
                if i == 0:
                    columns.append("text")
                metric_values = list()
                metric_debugs = list()
                for metric in self._metrics:
                    if i == 0:
                        m_columns.append(metric.code)
                    value, debug = doc._.metrics[metric]
                    metric_values.append(value)
                    metric_debugs.append(debug)
            except:
                doc_content = list()
                if i == 0:
                    columns.append("text")
                metric_values = list()
                metric_debugs = list()
                for metric in self._metrics:
                    if i == 0:
                        m_columns.append(metric.code)
                    metric_values.append(np.nan)
                    metric_debugs.append({})
            values_content = doc_content + metric_values
            debugs_content = doc_content + metric_debugs
            values.append(values_content)
            debugs.append(debugs_content)

            if self._save_path and self._save_step and (i % (self._save_step) == 0):
                values_temp = pd.DataFrame(values, columns=columns + m_columns)
                debugs_temp = pd.DataFrame(debugs, columns=columns + m_columns)

                self._save(values_temp, self.output_name + f"{self._file_number}_temp")
                if self._debug:
                    self._save(
                        debugs_temp, self.debug_name + f"{self._file_number}_temp"
                    )
        columns = columns + m_columns

        values = pd.DataFrame(values, columns=columns)
        debugs = pd.DataFrame(debugs, columns=columns)

        if self._debug:
            if self._save_path:
                self._save(values, self.output_name + f"{self._file_number}")
                self._save(debugs, self.debug_name + f"{self._file_number}")
            return values, debugs
        else:
            if self._save_path:
                self._save(values)
            return values

    def _save(self, value, base_name):
        file_name = f"{base_name}.csv"
        file_path = os.path.join(self._save_path, file_name)
        value.to_csv(file_path)
        print(f"File saved in location: {file_path}")
        if not file_path.replace(".csv", "").endswith("_temp"):
            Path(file_path.replace(".csv", "_temp.csv")).unlink(missing_ok=True)

    def _determine_number(self):
        number = 1
        for file in os.listdir(self._save_path):
            if file.startswith(self.output_name):
                n = file[len(self.output_name) :].replace(".csv", "")
                if re.findall("\d+", n):
                    n = int(re.findall("\d+", n)[0])
                else:
                    n = 1
                if n >= number:
                    number = n + 1
        return number

    def set_debug(self, debug):
        self._debug = debug

    def set_nlp_customization(self, nlp_customization):
        self._customization = nlp_customization

    def _init_metrics(self, metrics, exceptions, nlp):
        base_metrics = MetricGroup()

        if not metrics:
            base_metrics += self._lang.get_metrics()
        elif not isinstance(metrics, MetricGroup):
            base_metrics += self._list_to_metric_group(metrics)

        else:
            for metric in metrics:
                base_metrics += metric
        if exceptions and not isinstance(exceptions, MetricGroup):
            base_metrics -= self._list_to_metric_group(exceptions)
        elif exceptions and isinstance(exceptions, MetricGroup):
            for exception in exceptions:
                base_metrics -= exception
        for metric in base_metrics:
            metric.set_nlp(nlp)
        self._metrics = base_metrics

    def _set_pipeline(self):
        config = {
            "metrics_ids": self._metrics.to_list(),
            "customization": self._customization,
        }
        self.nlp.add_pipe("stylo_metrix", config=config)

    def _init_nlp(self, lang, nlp):
        lang = Lang.get_language(lang)
        if not nlp:
            nlp = spacy.load(lang.spacy_model)
            nlp.add_pipe("syllables", after="ner")

        self.nlp = nlp
        self._lang = lang

    def _list_to_metric_group(self, metrics):
        defined_metrics = []
        metrics_df = pd.DataFrame(
            {
                "category": [
                    metric.category.__name__
                    for metric in self._lang.get_metrics().metrics
                ],
                "metric_name": [
                    metric.__name__ for metric in self._lang.get_metrics().metrics
                ],
                "metric": list(self._lang.get_metrics().metrics),
            }
        )
        for metric in metrics:
            if metric in metrics_df["category"].values:
                defined_metrics += metrics_df.loc[
                    metrics_df["category"] == metric, "metric"
                ].tolist()
            elif metric in metrics_df["metric_name"].values:
                defined_metrics += metrics_df.loc[
                    metrics_df["metric_name"] == metric, "metric"
                ].tolist()
            elif metric in metrics_df["metric"].values:
                defined_metrics += metrics_df.loc[
                    metrics_df["metric"] == metric, "metric"
                ].tolist()
        return MetricGroup(metrics=defined_metrics)
