from spacy.matcher import Matcher

from ...structures import Category, Metric
from ...utils import ratio


class Descriptive(Category):
    lang = "pl"
    name_en = "Descriptive"
    name_local = "Deskryptywne"


class DESC_ADJ_CP(Metric):
    category = Descriptive
    name_en = "Compound adjectives"
    name_local = "Przymiotniki złożone"

    def count(doc):
        nlp = DESC_ADJ_CP.get_nlp()
        matcher = Matcher(nlp.vocab)
        double_pattern = [
            {"POS": {"IN": ["ADJ"]}},
            {"MORPH": {"INTERSECTS": ["PunctType=Hyph"]}},
            {"POS": {"IN": ["ADJ"]}},
        ]
        triple_pattern = [
            {"POS": {"IN": ["ADJ"]}},
            {"MORPH": {"INTERSECTS": ["PunctType=Hyph"]}},
            {"POS": {"IN": ["ADJ"]}, "OP": "*"},
            {"MORPH": {"INTERSECTS": ["PunctType=Hyph"]}},
            {"POS": {"IN": ["ADJ"]}},
        ]

        matcher.add("triple", [triple_pattern])
        matcher.add("double", [double_pattern])

        matches = matcher(doc)

        triple_debug = []
        double_debug = []

        for match_id, start, end in matches:
            match_text = doc[start:end]
            if match_id == nlp.vocab.strings["triple"]:
                triple_debug.append(match_text)
            elif match_id == nlp.vocab.strings["double"]:
                double_debug.append(match_text)

        filtered_double_debug = [
            double
            for double in double_debug
            if all(double.text not in triple.text for triple in triple_debug)
        ]

        filtered = filtered_double_debug + triple_debug
        morph_cases = [
            [
                token.morph.get("Case")[0]
                for token in item
                if token.morph.get("Case") != []
            ]
            for item in filtered
        ]
        same_cases = [len(set(item)) == 1 for item in morph_cases]

        filtered = [filtered[i] for i in range(len(filtered)) if same_cases[i]]
        debug = [item.text for item in filtered]
        result = sum([len([token for token in item]) for item in filtered])
        return ratio(result, len(doc)), debug


class DESC_ADJ(Metric):
    category = Descriptive
    name_en = "Adjectival description of properties"
    name_local = "Opis właściwości przymiotnikowy"

    def count(doc):
        nlp = DESC_ADJ.get_nlp()
        matcher = Matcher(nlp.vocab)
        pattern = [
            {"POS": "ADJ", "IS_DIGIT": False},
            {"ORTH": {"IN": [",", "/"]}, "OP": "?"},
            {"POS": "CCONJ", "OP": "?"},
            {"ORTH": {"IN": [",", "/"]}, "OP": "?"},
            {"POS": "ADJ", "IS_DIGIT": False},
        ]
        matcher.add("nazwa", [pattern])
        matches = matcher(doc)
        filtered = [[token for token in doc[start:end]] for _, start, end in matches]
        morph_cases = [
            [
                token.morph.get("Case")[0]
                for token in item
                if token.morph.get("Case") != []
            ]
            for item in filtered
        ]
        same_cases = [len(set(item)) == 1 for item in morph_cases]
        filtered = [filtered[i] for i in range(len(filtered)) if same_cases[i]]
        debug = sum(filtered, [])  # flat list
        result = len(debug)
        return ratio(result, len(doc)), [token.text for token in debug]


class DESC_ADV(Metric):
    category = Descriptive
    name_en = "Adverbial description of properties"
    name_local = "Opis właściwości przysłówkowy"

    def count(doc):
        nlp = DESC_ADV.get_nlp()
        matcher = Matcher(nlp.vocab)
        pattern = [
            {"POS": "ADV", "IS_DIGIT": False},
            {"ORTH": {"IN": [",", "/"]}, "OP": "?"},
            {"POS": "CCONJ", "OP": "?"},
            {"ORTH": {"IN": [",", "/"]}, "OP": "?"},
            {"POS": "ADV", "IS_DIGIT": False},
        ]
        matcher.add("nazwa", [pattern])
        matches = matcher(doc)
        debug = [
            token.text
            for match in matches
            for _, start, end in [match]
            for token in doc[start:end]
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class DESC_APOS_NPHR(Metric):
    category = Descriptive
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
                if (token.pos_ in ["NOUN", "PROPN"] and "Case=Voc" in token.morph)
                or (token.pos_ in ["NOUN", "PROPN"] and token.dep_ == "vocative")
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
    category = Descriptive
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
                if token.pos_ in ["NOUN", "PROPN"] and "Case=Voc" in token.morph
            )
            pron = [
                token.text
                for token in sent
                if token.pos_ == "VERB" and "Person=2" in token.morph
            ]
            if inn7w and pron:
                debug.append((inn7w, pron))
                result = result + len(inn7w) + len(pron)
        return ratio(result, len(doc)), debug


class DESC_APOS_ADJ(Metric):
    category = Descriptive
    name_en = "Descriptive apostrophe with an adjective"
    name_local = "Apostrofa opisowa z przymiotnikiem"

    def count(doc):
        result = 0
        dets = ["det", "amod"]
        debug = []

        for sent in doc.sents:
            inn7w = [
                token.text
                for token in sent
                if (token.pos_ in ["NOUN", "PROPN"] and "Case=Voc" in token.morph)
                or (token.pos_ in ["NOUN", "PROPN"] and token.dep_ == "vocative")
            ]

            pron = [
                token.text
                for token in sent
                if token.dep_ in dets and token.head.text in inn7w
            ]
            if inn7w and pron:
                debug.append((pron, inn7w))
                result = result + len(inn7w) + len(pron)

        return ratio(result, len(doc)), debug


class DESC_ADV_ADJ(Metric):
    category = Descriptive
    name_en = "Adverbs followed by adjectives"
    name_local = "Przymiotniki występujące po przysłówkach"

    def count(doc):
        nlp = DESC_ADV_ADJ.get_nlp()
        matcher = Matcher(nlp.vocab)
        pattern = [{"POS": "ADV", "IS_DIGIT": False}, {"POS": "ADJ", "IS_DIGIT": False}]
        matcher.add("nazwa", [pattern])
        matches = matcher(doc)
        debug = [doc[start:end].text for _, start, end in matches]
        bi_gram_count = len(debug) * 2
        return ratio(bi_gram_count, len(doc)), debug


class DESC_ADV_ADV(Metric):
    category = Descriptive
    name_en = "Adverb pairs incidence"
    name_local = "Występowanie par przysłówków"

    def count(doc):
        nlp = DESC_ADV_ADV.get_nlp()
        matcher = Matcher(nlp.vocab)
        pattern = [{"POS": "ADV", "IS_DIGIT": False}, {"POS": "ADV", "IS_DIGIT": False}]
        matcher.add("nazwa", [pattern])
        matches = matcher(doc)
        debug = [doc[start:end].text for _, start, end in matches]
        bi_gram_count = len(debug) * 2
        return ratio(bi_gram_count, len(doc)), debug


class DESC_PRON_VOC(Metric):
    category = Descriptive
    name_en = "Personal pronoun followed by a noun in the vocative case"
    name_local = "Rzeczownik w wołaczu po zaimku osobowym"

    def count(doc):
        nlp = DESC_PRON_VOC.get_nlp()
        matcher = Matcher(nlp.vocab)
        noun_voc = [
            token
            for token in doc
            if token.pos_ in ["NOUN", "PROPN"] and "Case=Voc" in token.morph
        ]
        noun_nom = [
            token
            for token in doc
            if token.pos_ in ["NOUN", "PROPN"] and "Case=Nom" in token.morph
        ]
        pattern1 = [
            {"LOWER": {"IN": ["ty"]}},
            {"TEXT": {"IN": [token.text for token in noun_voc]}},
        ]
        pattern2 = [
            {"LOWER": {"IN": ["wy"]}},
            {"TEXT": {"IN": [token.text for token in noun_nom]}},
        ]
        matcher.add("nazwa", [pattern1, pattern2])
        matches = matcher(doc)

        debug = [doc[start:end].text for _, start, end in matches]
        bi_gram_count = len(debug) * 2
        return ratio(bi_gram_count, len(doc)), debug


class DESC_PRON_ADJ_VOC(Metric):
    category = Descriptive
    name_en = (
        "Personal pronoun followed by an adjective and a noun in the vocative case"
    )
    name_local = "Rzeczownik w wołaczu po zaimku osobowym i przymiotniku"

    def count(doc):
        nlp = DESC_PRON_ADJ_VOC.get_nlp()
        matcher = Matcher(nlp.vocab)
        noun_voc = [
            token
            for token in doc
            if token.pos_ in ["NOUN", "PROPN"] and "Case=Voc" in token.morph
        ]
        noun_nom = [
            token
            for token in doc
            if token.pos_ in ["NOUN", "PROPN"] and "Case=Nom" in token.morph
        ]
        pattern1 = [
            {"LOWER": {"IN": ["ty"]}},
            {"POS": "ADJ"},
            {"TEXT": {"IN": [token.text for token in noun_voc]}},
        ]
        pattern2 = [
            {"LOWER": {"IN": ["wy"]}},
            {"POS": "ADJ"},
            {"TEXT": {"IN": [token.text for token in noun_nom]}},
        ]
        matcher.add("nazwa", [pattern1, pattern2])
        matches = matcher(doc)

        debug = [doc[start:end].text for _, start, end in matches]
        bi_gram_count = len(debug) * 3
        return ratio(bi_gram_count, len(doc)), debug
