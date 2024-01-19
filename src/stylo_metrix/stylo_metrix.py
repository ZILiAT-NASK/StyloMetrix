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
    def __init__(
        self,
        lang,
        nlp=None,
        metrics=None,
        exceptions=None,
        debug=False,
        save_path=None,
        nlp_customization=None,
    ):
        super().__init__()
        self._debug = debug
        self._customization = nlp_customization
        self._init_nlp(lang, nlp)
        self._init_metrics(metrics, exceptions, self.nlp)
        self._set_pipeline()
        if save_path:
            if not os.path.exists(save_path):
                raise Exception(f"Path {save_path} is not exists")
        self._save_path = save_path

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
        columns = columns + m_columns

        values = pd.DataFrame(values, columns=columns)
        debugs = pd.DataFrame(debugs, columns=columns)

        output_name = "sm_output"
        debug_name = "sm_debug"

        if self._debug:
            if self._save_path:
                deb_num = self._save(values, self._save_path, output_name)
                self._save(values, self._save_path, debug_name, deb_num)
            return values, debugs
        else:
            if self._save_path:
                self._save(values, self._save_path, output_name)
            return values

    def _save(self, value, path, base_name, number=None):
        if not number:
            number = 1
            for file in os.listdir(path):
                if file.startswith(base_name):
                    n = int(file[len(base_name) :].replace(".csv", ""))
                    if n >= number:
                        number = n + 1
        file_name = f"{base_name}{number}.csv"
        file_path = os.path.join(path, file_name)
        value.to_csv(file_path)
        print(f"File saved in location: {file_path}")
        return number

    def set_debug(self, debug):
        self._debug = debug

    def set_nlp_customization(self, nlp_customization):
        self._customization = nlp_customization

    def _init_metrics(self, metrics, exceptions, nlp):
        base_metrics = MetricGroup()
        if not metrics:
            base_metrics += self._lang.get_metrics()
        else:
            for metric in metrics:
                base_metrics += metric
        if exceptions:
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
