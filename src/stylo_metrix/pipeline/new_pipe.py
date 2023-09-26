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

from spacy.language import Language
from spacy.tokens import Doc

from ..structures import Metric
from .pl import pl_components
from .en import en_components
from .en.custom_preprocessing import CustomPreprocessing as CP_en
from .ukr import ukr_components
from .ukr.custom_preprocessing import CustomPreprocessing as CP_ukr
from .ru import ru_components
from .ru.custom_preprocessing import CustomPreprocessing as CP_ru



@Language.factory('stylo_metrix')
def create_sm_component(nlp, name, metrics_ids, customization):
    return SMComponent(nlp, metrics_ids, customization)


class SMComponent:
    def __init__(self, nlp, metrics_ids, customization):
        self.metrics_ids = metrics_ids
        self.customization = customization
        lang = nlp.config["nlp"]["lang"]

        if lang == 'pl':
            components = pl_components
        elif lang == 'en':
            components = en_components
            nlp.tokenizer = CP_en(nlp.tokenizer)
        elif lang == 'uk':
            components = ukr_components
            nlp.tokenizer = CP_ukr(nlp.tokenizer)
        elif lang == 'ru':
            components = ru_components
            nlp.tokenizer = CP_ru(nlp.tokenizer)


        self.components = [component(nlp) for component in components]
        Doc.set_extension("name", default=None, force=True)
        Doc.set_extension("assign_name", method=self._assign_name, force=True)
        Doc.set_extension("metrics", default=dict(), force=True)

    def __call__(self, doc):
        comp_exception = False

        for component in self.components:
            try:
                doc = component(doc)
            except:
                comp_exception = True
        if self.customization:
            doc = self.customization(doc)

        for id in self.metrics_ids:
            metric = Metric.get_by_id(id)
            try:
                if comp_exception or len(doc) == 0:
                    doc._.metrics[metric] = None, []
                else:
                    doc._.metrics[metric] = metric(doc)
            except Exception as e:
                doc._.metrics[metric] = None, []
                print(str(e) + f'\n AT METRIC {metric.code}, TEXT: {doc[:10]}...')
                # raise type(e)(str(e) + f'\n AT METRIC {metric.code}, TEXT: {doc[:10]}...')
        return doc

    def _assign_name(self, doc, name):
        doc._.name = name
        return doc
    