from spacy.language import Language

from stylo_metrix.pipeline.en import COMPONENTS_EN
from stylo_metrix.pipeline.pl import COMPONENTS_PL


@Language.factory("stylo_metrix")
class StyloMetrixPipe():

    def __init__(self, nlp, name):
        lang = nlp.config["nlp"]["lang"]
        if lang == "pl":
            self.components = [component(nlp) for component in COMPONENTS_PL]
        elif lang == "en":
            self.components = [component(nlp) for component in COMPONENTS_EN]
        else:
            print(f"The language code [{lang}] is not supported by StyloMetrix.")

    def __call__(self, doc):
        for component in self.components:
            doc = component(doc)
        return doc
