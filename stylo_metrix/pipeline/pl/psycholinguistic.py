from spacy.tokens import Doc, Token

from stylo_metrix.pipeline.pl.resources.experimental_data import MEANS, PSYCHOLINGUISTIC_DATA


class Psycholinguistic():

    def __init__(self, nlp):
        self.nlp = nlp
        Token.set_extension("affective_norms", default=None, force=True)  # type dict
        Doc.set_extension("an_means", default=MEANS, force=True)

    def __call__(self, doc):
        for token in doc:
            if token.lemma_ in PSYCHOLINGUISTIC_DATA.keys():
                token._.set("affective_norms", PSYCHOLINGUISTIC_DATA[token.lemma_])
        return doc
