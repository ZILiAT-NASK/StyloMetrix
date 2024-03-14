import re

from spacy.matcher import DependencyMatcher, Matcher

from ...structures import Category, Metric
from ...utils import ratio


class Syntactic(Category):
    lang = "pl"
    name_en = "Syntactic"
    name_local = "Syntaktyka"


class SY_FMWE(Metric):
    category = Syntactic
    name_en = "Flat multiword expressions"
    name_local = "Związki wielowyrazowe"

    def count(doc):
        flat = [[token.head, token] for token in doc if "flat" in token.dep_]
        debug = [token.text for i in flat for token in i]
        result = len(debug)
        return ratio(result, len(doc)), debug


class SY_APPM(Metric):
    category = Syntactic
    name_en = "Appositional modifiers"
    name_local = "Modyfikatory w apozycji"

    def count(doc):
        flat = [[token.head, token] for token in doc if "appos" in token.dep_]
        debug = [token.text for i in flat for token in i]
        result = len(debug)
        return ratio(result, len(doc)), debug


class SY_S_DE(Metric):
    category = Syntactic
    name_en = "Words in declarative sentences"
    name_local = "Wyrazy w zdaniach oznajmujących"

    def count(doc):
        decl = set(
            [sent for sent in doc.sents for token in sent if token.text in ["."]]
        )
        debug = [token.text for i in decl for token in i]
        result = len(debug)
        return ratio(result, len(doc)), debug


class SY_S_EX(Metric):
    category = Syntactic
    name_en = "Words in exclamatory sentences"
    name_local = "Wyrazy w zdaniach wykrzyknikowych"

    def count(doc):
        exl = set([sent for sent in doc.sents for token in sent if token.text == "!"])
        debug = [token.text for i in exl for token in i]
        result = len(debug)
        return ratio(result, len(doc)), debug


class SY_S_IN(Metric):
    category = Syntactic
    name_en = "Words in interrogative sentences"
    name_local = "Wyrazy w zdaniach pytających"

    def count(doc):
        quest = set([sent for sent in doc.sents for token in sent if token.text == "?"])
        debug = [token.text for i in quest for token in i]
        result = len(debug)
        return ratio(result, len(doc)), debug


class SY_S_NEG(Metric):
    category = Syntactic
    name_en = "Words in negative sentences"
    name_local = "Wyrazy w zdaniach przeczących"

    def count(doc):
        neg_sentences = []
        for sent in doc.sents:
            if any(
                token.dep_ in ["ROOT", "ccomp", "cop"] and token.pos_ in ["VERB", "AUX"]
                for token in sent
            ) and any(
                token.dep_ == "advmod:neg" and token.pos_ == "PART" for token in sent
            ):
                neg_sentences.append(sent)
        debug = [token.text for sent in neg_sentences for token in sent]
        result = len(debug)
        return ratio(result, len(doc)), debug


class SY_S_ELL(Metric):
    category = Syntactic
    name_en = "Words in ellipsis-ending sentences"
    name_local = "Wyrazy w zdaniach zakończonych wielokropkiem"

    def count(doc):
        ellipsis_pattern = r"\.\.\."
        ellipsis_matches = re.finditer(ellipsis_pattern, doc.text)
        ellipsis_indices = [match.start() for match in ellipsis_matches]
        ellipsis_sentences = [
            sent
            for sent in doc.sents
            if any(token.idx in ellipsis_indices for token in sent)
        ]
        total_words = len(list(doc))
        debug = [token.text for sent in ellipsis_sentences for token in sent]
        result = len(debug)
        return ratio(result, len(doc)), debug


class SY_S_VOC(Metric):
    category = Syntactic
    name_en = "Words in sentences with a noun in the vocative case"
    name_local = "Wyrazy w zdaniach z rzeczownikiem w wołaczu"

    def count(doc):
        result = 0
        inn7w = []
        for sent in doc.sents:
            if any(
                token.pos_ in ["NOUN", "PROPN"] and "Case=Voc" in token.morph
                for token in sent
            ):
                inn7w.append(sent)
        debug = [token.text for sent in inn7w for token in sent]
        result = len(debug)
        return ratio(result, len(doc)), debug


class SY_S_NOM(Metric):
    category = Syntactic
    name_en = "Words in nominal sentences"
    name_local = "Wyrazy w równoważnikach zdań"

    def count(doc):
        nom = set(
            [
                sent
                for sent in doc.sents
                if all(
                    token.pos_ == "AUX" and "VerbType=Quasi" in token.morph
                    for token in sent
                    if token.pos_ == "AUX"
                )
                and not any(
                    token.text
                    for token in sent
                    if token.pos_ in ["VERB", "AUX"] and token.pos_ != "AUX"
                )
            ]
        )
        debug = [token.text for i in nom for token in i]
        result = len(debug)
        return ratio(result, len(doc)), debug


class SY_S_INF(Metric):
    category = Syntactic
    name_en = "Words in infinitive-only sentences without finite verbs"
    name_local = "Słowa w zdaniach z bezokolicznikami bez czasowników osobowych"

    def count(doc):
        inf = set(
            [
                sent
                for sent in doc.sents
                if not any(
                    token.text for token in sent if "VerbForm=Fin" in token.morph
                )
                and any(token.text for token in sent if "VerbForm=Inf" in token.morph)
            ]
        )
        debug = [token.text for i in inf for token in i]
        result = len(debug)
        return ratio(result, len(doc)), debug


class SY_NPRED(Metric):
    category = Syntactic
    name_en = "Nominal predicates"
    name_local = "Orzeczenia imienne"

    def count(doc):
        result = 0
        nom_pred = []

        for sent in doc.sents:
            for token in sent:
                if (
                    token.dep_ == "cop"
                    and token.head.pos_ in ["NOUN", "ADJ", "PRON"]
                    and token.pos_ == "AUX"
                ):
                    subject = token.head
                    predicate = token
                    result += 1
                    result += 1
                    nom_pred.append((predicate.text, subject.text))

        return ratio(result, len(doc)), nom_pred


class SY_MOD(Metric):
    category = Syntactic
    name_en = "Words within modifiers"
    name_local = "Wyrazy w przydawkach"

    def count(doc):
        mod_tags = ["amod", "nmod", "nmod:arg", "acl", "appos", "det", "det:poss"]
        nouns = [token for token in doc if token.pos_ in ["NOUN", "PROPN"]]
        children_mods = [
            [ch for ch in noun.children if ch.dep_ in mod_tags] for noun in nouns
        ]
        children_mods = sum(children_mods, [])
        mods_extra = [
            [
                item
                for item in list(ch.children)
                if item.dep_ in ["conj", "advmod", "advmod:neg", "case", "obj"]
            ]
            for ch in children_mods
        ]
        mods_extra = sum(mods_extra, [])
        debug = [token.text for token in doc if token in children_mods + mods_extra]
        result = len(debug)
        return ratio(result, len(doc)), debug


class SY_NPHR(Metric):
    category = Syntactic
    name_en = "Words in nominal phrases"
    name_local = "Wyrazy we frazach nominalnych"

    def count(doc):

        mod_tags = [
            "amod",
            "nmod",
            "nmod:arg",
            "acl",
            "appos",
            "det",
            "det:poss",
            "conj",
        ]
        nouns = [token for token in doc if token.pos_ in ["NOUN", "PROPN"]]
        children_mods = [
            [ch for ch in noun.children if ch.dep_ in mod_tags] for noun in nouns
        ]
        children_mods = sum(children_mods, [])
        mods_extra = [
            [
                item
                for item in list(ch.children)
                if item.dep_ in ["conj", "advmod", "advmod:neg", "case", "obj"]
            ]
            for ch in children_mods
        ]
        mods_extra = sum(mods_extra, [])
        extra_heads = [mod.head for mod in mods_extra]
        debug = []
        for mod in children_mods:
            current_item = [mod.head]
            if mod.head in sum(debug, []):
                idx = [mod.head in item for item in debug].index(True)
                current_item = debug[idx]
                debug.pop(idx)

            if mod in extra_heads:
                current_extra = [mod_ for mod_ in mods_extra if mod_.head == mod]
                ccon = [
                    [item for item in token.children if item.dep_ == "cc"]
                    for token in current_extra
                ]
                ccon = sum(ccon, [])
                debug.append(current_item + [mod] + ccon + current_extra)
            else:
                debug.append(current_item + [mod])

        sum_debug = sum(debug, [])
        result = ratio(len(sum_debug), len(doc))
        return result, [[item.text for item in list_] for list_ in debug]


class SY_INV_OBJ(Metric):
    category = Syntactic
    name_en = "OVS word order"
    name_local = "Inwersja zdania, rozpoczęcie od dopełnienia"

    def count(doc):
        nlp = SY_INV_OBJ.get_nlp()
        debug = []
        counter = 0
        matcher = DependencyMatcher(nlp.vocab)
        pattern = [  # anchor token: root
            {"RIGHT_ID": "verb", "RIGHT_ATTRS": {"DEP": {"IN": ["ROOT", "xcomp"]}}},
            # root >-- left child
            {
                "LEFT_ID": "verb",
                "REL_OP": ">--",
                "RIGHT_ID": "left child",
                "RIGHT_ATTRS": {
                    "MORPH": {
                        "INTERSECTS": [
                            "Case=Gen",
                            "Case=Dat",
                            "Case=Acc",
                            "Case=Ins",
                            "Case=Loc",
                        ]
                    }
                },
            },
        ]

        matcher.add("LEFT_CHILD", [pattern])
        matches = matcher(doc)

        for i in range(len(matches)):
            match_id, token_ids = matches[i]
            match = []
            for l in doc[token_ids[1]].lefts:
                match.append(l.text)
            for n in range((token_ids[0] + 1) - token_ids[1]):
                match.append(doc[token_ids[1] + n].text)
            debug.append(match)

        counter = sum([len(listElem) for listElem in debug])

        return ratio(counter, len(doc)), debug


class SY_INV_EPI(Metric):
    category = Syntactic
    name_en = "Inverted epithet"
    name_local = "Inwersja epitetu"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ == "ADJ"
            and token.head.pos_ == "NOUN"
            and token in token.head.rights
        ]

        return ratio(len(debug), len(doc)), debug


class SY_INIT(Metric):
    category = Syntactic
    name_en = "Words being the initial token in a sentence"
    name_local = "Wyrazy będące pierwszym wyrazem zdania"

    def count(doc):
        debug = [sent[0].text for sent in doc.sents if sent]
        result = len(debug)
        return ratio(result, len(doc)), debug


class SY_QUOT(Metric):
    category = Syntactic
    name_en = "Words in quotation marks"
    name_local = "Słowa w cudzysłowie"

    def count(doc):
        quote_positions = [i for i, token in enumerate(doc) if token.text in ['"', "'"]]
        if len(quote_positions) % 2 != 0:
            quote_positions.pop()
        debug = [
            token.text
            for i in range(0, len(quote_positions), 2)
            for token in doc[quote_positions[i] + 1 : quote_positions[i + 1]]
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class SY_SIMILE_ADJ(Metric):
    category = Syntactic
    name_en = "Similes (adjective)"
    name_local = "Porównania (przymiotnik)"

    def count(doc):
        nlp = SY_SIMILE_ADJ.get_nlp()
        matcher = Matcher(nlp.vocab)
        pattern = [
            {"POS": {"IN": ["ADJ"]}},
            {"POS": {"IN": ["SCONJ"]}, "MORPH": {"INTERSECTS": ["ConjType=Cmpr"]}},
            {"POS": {"IN": ["NOUN", "PROPN"]}},
        ]
        matcher.add("nazwa", [pattern])
        matches = matcher(doc)
        debug = [doc[start:end].text for _, start, end in matches]
        tri_gram_count = len(debug) * 3
        result = tri_gram_count
        return ratio(result, len(doc)), debug
