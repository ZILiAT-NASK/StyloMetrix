from ...structures import Category, Metric
from ...utils import ratio


class Descriptive(Category):
    lang = "de"
    name_en = "Descriptive"
    name_local = "Deskriptive"


class DESC_PRON_VOC(Metric):
    category = Descriptive
    name_en = "Direct address phrases with a pronoun"
    name_local = "Direkte Anredephrasen mit einem Pronomen"

    def count(doc):
        result = 0
        debug = []

        for sent in doc.sents:
            pron = [
                token.text
                for token in sent
                if token.text.lower() in ["du", "ihr"]
                and str(token.morph.get("Poss")) != "['Yes']"
                and token.dep_ != "sb"
            ]

            adjs = [
                token.text
                for token in sent
                if token.pos_ == "ADJ" and token.dep_ == "nk"
            ]

            noun = [
                token.text
                for token in sent
                if token.pos_ in ["NOUN", "PROPN"]
                and str(token.morph.get("Case")) == "['Nom']"
                and token.dep_ == "ROOT"
            ]

            if (pron and adjs and noun) or (pron and noun):
                debug.append((pron + adjs, noun))
                result += len(pron) + len(adjs) + len(noun)

        return ratio(result, len(doc)), debug
