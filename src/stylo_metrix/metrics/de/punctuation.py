from spacy.matcher import Matcher

from ...structures import Category, Metric
from ...utils import ratio


class Punctuation(Category):
    lang = "de"
    name_en = "Punctuation"
    name_local = "Interpunktion"


class PUNCT_TOTAL(Metric):
    category = Punctuation
    name_en = "Total punctuation"
    name_local = "Interpunktion"

    def count(doc):
        debug = [token.text for token in doc if token.pos_ == "PUNCT"]
        result = len(debug)
        return ratio(result, len(doc)), debug


class PUNCT_BI_NOUN(Metric):
    category = Punctuation
    name_en = "Punctuation following a noun"
    name_local = "Interpunktion nach einem Nomen"

    def count(doc):
        nlp = PUNCT_BI_NOUN.get_nlp()
        matcher = Matcher(nlp.vocab)
        pattern = [{"POS": "NOUN"}, {"TEXT": {"in": [",", ";", ":", "-", "–", "—"]}}]
        matcher.add("punct_noun", [pattern])
        matches = matcher(doc)
        debug = [doc[start:end].text for _, start, end in matches]
        result = len(debug) * 2
        return ratio(result, len(doc)), debug


class PUNCT_BI_VERB(Metric):
    category = Punctuation
    name_en = "Punctuation following a verb"
    name_local = "Interpunktion nach einem Verb"

    def count(doc):
        nlp = PUNCT_BI_VERB.get_nlp()
        matcher = Matcher(nlp.vocab)
        patterns = [
            [{"POS": {"IN": ["VERB", "AUX"]}}, {"IS_PUNCT": True}],
            [{"POS": {"IN": ["VERB", "AUX"]}}, {"POS": "PRON"}, {"IS_PUNCT": True}],
        ]
        matcher.add("punct_bi_verb3", patterns)
        matches = matcher(doc)
        debug = [doc[start:end].text for _, start, end in matches]
        bi_gram_count = len(debug) * 2
        return ratio(bi_gram_count, len(doc)), debug
