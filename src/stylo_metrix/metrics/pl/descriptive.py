from spacy.matcher import Matcher

from ...structures import Metric, Category
from ...utils import ratio


class Deskryptywne(Category):
  lang='pl'
  name_en='Descriptive'
  name_local='Deskryptywne'


	
class G_ADJ_CP(Metric):
    category = Deskryptywne
    name_en = "Compound adjectives"
    name_local = "Przymiotniki złożone"

    def count(doc):
        nlp = G_ADJ_CP.get_nlp()
        matcher = Matcher(nlp.vocab)
        double_pattern = [{"POS": {"IN": ["ADJ"]}}, {"MORPH": {"INTERSECTS": ["PunctType=Hyph"]}}, {"POS": {"IN": ["ADJ"]}}]
        triple_pattern = [{"POS": {"IN": ["ADJ"]}}, {"MORPH": {"INTERSECTS": ["PunctType=Hyph"]}},
                        {"POS": {"IN": ["ADJ"]}, "OP": "*"}, {"MORPH": {"INTERSECTS": ["PunctType=Hyph"]}},
                        {"POS": {"IN": ["ADJ"]}}]

        matcher.add("triple", [triple_pattern])
        matcher.add("double", [double_pattern])

        matches = matcher(doc)

        triple_debug = []
        double_debug = []

        for match_id, start, end in matches:
            match_text = doc[start:end].text
            if match_id == nlp.vocab.strings["triple"]:
                triple_debug.append(match_text)
            elif match_id == nlp.vocab.strings["double"]:
                double_debug.append(match_text)

        filtered_double_debug = [double for double in double_debug if all(double not in triple for triple in triple_debug)]

        bi_gram_count = len(filtered_double_debug) * 3
        tri_gram_count = len(triple_debug) * 5
        result = bi_gram_count + tri_gram_count
        return ratio(result, len(doc)), filtered_double_debug + triple_debug

class DESC_ADJ(Metric):
    category = Deskryptywne
    name_en = "Adjectival description of properties"
    name_local = "Opis właściwości przymiotnikowy"

    def count(doc):
        nlp = DESC_ADJ.get_nlp()
        matcher = Matcher(nlp.vocab)
        pattern = [{"POS": "ADJ", "IS_DIGIT": False}, {"ORTH": {"IN": ['-',',',';','/']}, "OP":"?"}, {"POS":"CCONJ", "OP": "?"},{"ORTH": {"IN": ['-',',',';','/']}, "OP":"?"},{"POS": "ADJ", "IS_DIGIT": False}]
        matcher.add("nazwa", [pattern])
        matches = matcher(doc)
        debug = [token for match in matches for _, start, end in [match] for token in doc[start:end]]
        result = len(debug)
        return ratio(result, len(doc)), debug

class DESC_ADV(Metric):
    category = Deskryptywne
    name_en = "Adverbial description of properties"
    name_local = "Opis właściwości przysłówkowy"

    def count(doc):
        nlp = DESC_ADV.get_nlp()
        matcher = Matcher(nlp.vocab)
        pattern = [{"POS": "ADV", "IS_DIGIT": False}, {"ORTH": {"IN": ['-',',',';','/']}, "OP":"?"}, {"POS":"CCONJ", "OP": "?"},{"ORTH": {"IN": ['-',',',';','/']}, "OP":"?"},{"POS": "ADV", "IS_DIGIT": False}]
        matcher.add("nazwa", [pattern])
        matches = matcher(doc)
        debug = [token for match in matches for _, start, end in [match] for token in doc[start:end]]
        result = len(debug)
        return ratio(result, len(doc)), debug
	
class DESC_APOS_NPHR(Metric):
    category = Deskryptywne
    name_en = "Descriptive apostrophe with a nominal phrase"
    name_local = "Rozbudowana apostrofa z frazą nominalną"

    def count(doc):
        result = 0
        dets = ["det", "amod"]
        debug = []

        for sent in doc.sents:
            inn7w = list(
                token.text
                for token in sent
                if (token.pos_ in ["NOUN", "PROPN"] and str(token.morph.get("Case")) == "['Voc']") or
                  (token.pos_ in ["NOUN", "PROPN"] and token.dep_ == "vocative")
            )

            pron = [
                token.text
                for token in sent
                if token.dep_ in dets and token.head.text in inn7w
            ]
            
            nmod = [
                token.text
                for token in sent
                if token.dep_ == "nmod:arg" and token.head.text in inn7w   
            ]
            
            amod = [
                token.text
                for token in sent
                if token.dep_ == "amod" and token.head.text in nmod
            ]
            
            if inn7w and pron and nmod or (inn7w and pron and nmod and amod):
                debug.append((pron, nmod, amod, inn7w))
                result = result + len(inn7w) + len(pron) + len(nmod) + len(amod)

        return ratio(result, len(doc)), debug
		
class DESC_APOS_VERB(Metric):
    category = Deskryptywne
    name_en = "Apostrophe containing a verb"
    name_local = "Apostrofa wraz z czasownikiem"

    def count(doc):
        result = 0
        debug = []
        dets = ["det", "amod"]
        for sent in doc.sents:
            inn7w = list(
                token.text
                for token in sent
                if token.pos_ in ["NOUN", "PROPN"] and str(token.morph.get("Case")) == "['Voc']"
            )
            pron = [
                token.text
                for token in sent
                if token.pos_ == "VERB" and str(token.morph.get("Person")) == "['2']"
            ]
            if inn7w and pron:
                debug.append((inn7w, pron))
                result = result + len(inn7w) + len(pron)
        return ratio(result, len(doc)), debug
		
class DESC_APOS_NPHR(Metric):
    category = Deskryptywne
    name_en = "Descriptive apostrophe with a nominal phrase"
    name_local = "Rozbudowana apostrofa z frazą nominalną"

    def count(doc):
        result = 0
        dets = ["det", "amod"]
        debug = []

        for sent in doc.sents:
            inn7w = [
                token.text
                for token in sent
                if (token.pos_ in ["NOUN", "PROPN"] and str(token.morph.get("Case")) == "['Voc']") or
                  (token.pos_ in ["NOUN", "PROPN"] and token.dep_ == "vocative")
            ]

            pron = [
                token.text
                for token in sent
                if token.dep_ in dets and token.head.text in inn7w
            ]

            nmod = [
                token.text
                for token in sent
                if token.dep_ == "nmod:arg" and token.head.text in inn7w
            ]

            amod = [
                token.text
                for token in sent
                if token.dep_ == "amod" and token.head.text in nmod
            ]

            if inn7w and pron and nmod and amod:
                debug.append((inn7w, pron, nmod, amod))
                result + len(inn7w) + len(pron) + len(nmod) + len(amod)

            elif inn7w and pron and nmod:
                debug.append((inn7w, pron, nmod))
                result += len(inn7w) + len(pron) + len(nmod)

        return ratio(result, len(doc)), debug
		
class DESC_ADV_ADJ(Metric):
    category = Deskryptywne
    name_en = "Adverbs followed by adjectives"
    name_local = "Przymiotniki występujące po przysłówkach"

    def count(doc):
        nlp = DESC_ADV_ADJ.get_nlp()
        matcher = Matcher(nlp.vocab)
        pattern = [{"POS": "ADV", "IS_DIGIT": False}, {"POS": "ADJ", "IS_DIGIT": False}]
        matcher.add("nazwa", [pattern])
        matches = matcher(doc)
        debug = [doc[start:end].text for _, start, end in matches]
        bi_gram_count = len(debug)*2
        return ratio(bi_gram_count, len(doc)), debug

class DESC_ADV_ADV(Metric):
    category = Deskryptywne
    name_en = "Adverb pairs incidence"
    name_local = "Występowanie par przysłówków"

    def count(doc):    
        nlp = DESC_ADV_ADV.get_nlp()
        matcher = Matcher(nlp.vocab)
        pattern = [{"POS": "ADV", "IS_DIGIT": False}, {"POS": "ADV", "IS_DIGIT": False}]
        matcher.add("nazwa", [pattern])
        matches = matcher(doc)
        debug = [doc[start:end].text for _, start, end in matches]
        bi_gram_count = len(debug)*2
        return ratio(bi_gram_count, len(doc)), debug

class DESC_PRON_VOC(Metric):
    category = Deskryptywne
    name_en = "Personal pronoun followed by a noun in the vocative case"
    name_local = "Rzeczownik w wołaczu po zaimku osobowym"

    def count(doc):
        nlp = DESC_PRON_VOC.get_nlp()  
        matcher = Matcher(nlp.vocab)
        pattern = [{"MORPH": {"INTERSECTS": ["PronType=Prs"]}}, {"MORPH": {"INTERSECTS": ["Case=Voc"]}}]
        matcher.add("nazwa", [pattern])
        matches = matcher(doc)
        
        debug = [doc[start:end].text for _, start, end in matches]
        bi_gram_count = len(debug)*2
        return ratio(bi_gram_count, len(doc)), debug