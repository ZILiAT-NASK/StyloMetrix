from spacy.tokens import Doc
from stylo_metrix.structures.stylo_metrix_vector import StyloMetrixVector
from stylo_metrix.metrics.pl import original_group


class Metrics:

    def __init__(self, nlp):
        self.nlp = nlp
        Doc.set_extension("sm", default=None, force=True)
        nlp.metrics_group = original_group

    def __call__(self, doc):
        doc._.set("sm", StyloMetrixVector(doc, self.nlp.metrics_group))
        return doc

    def add_metrics(self, metric): pass
    def set_metrics(self, metrics_group): pass
    def remove_metrics(self, id): pass
