from spacy.matcher import Matcher

from ...structures import Metric, Category
from ...utils import ratio

class Interpunkcja(Category):
    lang='pl'
    name_en='Punctuation'
    name_local='Interpunkcja'

class PUNCT_TOTAL(Metric):
    category = Interpunkcja
    name_en = "Total punctuation"
    name_local = "Interpunkcja"

    def count(doc):
        debug = [token.text for token in doc if token.pos_ == 'PUNCT']
        result = len(debug)
        return ratio(result, len(doc)), debug
		
class PUNCT_BI_NOUN(Metric):
    category = Interpunkcja
    name_en = "Punctuation following a noun"
    name_local = "Interpunkcja po rzeczowniku"

    def count(doc):
        nlp = PUNCT_BI_NOUN.get_nlp()
        matcher = Matcher(nlp.vocab)
        pattern = [{"POS": "NOUN"}, {"TEXT": {"in": [",", ";", ":", "-", "–", "—"]}}]
        matcher.add("punct_noun", [pattern])
        matches = matcher(doc)
        debug = [doc[start:end].text for _, start, end in matches]
        result = len(debug)*2
        return ratio(result, len(doc)), debug
		
class PUNCT_BI_VERB(Metric):
    category = Interpunkcja
    name_en = "Punctuation following a verb"
    name_local = "Interpunkcja po czasowniku"

    def count(doc):
        nlp = PUNCT_BI_VERB.get_nlp()
        matcher = Matcher(nlp.vocab)
        pattern = [[{"POS": {"IN": ["VERB", "AUX"]}}, {"LOWER": {"in": ["się"]}, "POS": "PRON", "OP": "?"}, {"TEXT": {"in": [",", ";", ":", "-", "–", "—"]}}]]
        matcher.add("punct_bi_verb", pattern)
        matches = matcher(doc)
        debug = [token for match in matches for _, start, end in [match] for token in doc[start:end]]
        result = len(debug)
        return ratio(result, len(doc)), debug
		