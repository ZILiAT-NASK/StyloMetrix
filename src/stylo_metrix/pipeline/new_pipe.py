from spacy.language import Language
from spacy.tokens import Doc

from ..structures import Metric
from .en import en_components
from .en.custom_preprocessing import CustomPreprocessing as CP_en
from .pl import pl_components
from .ukr import ukr_components
from .ukr.custom_preprocessing import CustomPreprocessing as CP_ukr


@Language.factory('stylo_metrix')
def create_sm_component(nlp, name, metrics_ids):
    return SMComponent(nlp, metrics_ids)


class SMComponent:
    def __init__(self, nlp, metrics_ids):
        self.metrics_ids = metrics_ids
        lang = nlp.config["nlp"]["lang"]

        if lang == 'pl':
            components = pl_components
        elif lang == 'en':
            components = en_components
            nlp.tokenizer = CP_en(nlp.tokenizer)
        elif lang == 'uk':
            components = ukr_components
            nlp.tokenizer = CP_ukr(nlp.tokenizer)

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

        for id in self.metrics_ids:
            metric = Metric.get_by_id(id)
            if comp_exception:
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
    