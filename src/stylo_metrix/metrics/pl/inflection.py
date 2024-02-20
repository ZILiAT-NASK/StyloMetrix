from spacy.matcher import Matcher

from ...structures import Category, Metric
from ...utils import ratio


class Inflection(Category):
    lang = "pl"
    name_en = "Inflection"
    name_local = "Odmiana"


class IN_ADJ_POS(Metric):
    category = Inflection
    name_en = "Adjectives in positive degree"
    name_local = "Przymiotniki w stopniu równym"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ == "ADJ"
            and token.is_digit == False
            and "NumForm=Roman" not in token.morph
            and token.is_punct == False
            and "Degree=Pos" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_ADJ_COM(Metric):
    category = Inflection
    name_en = "Adjectives in comparative degree"
    name_local = "Przymiotniki w stopniu wyższym"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ == "ADJ" and "Degree=Cmp" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_ADJ_SUP(Metric):
    category = Inflection
    name_en = "Adjectives in superlative degree"
    name_local = "Przymiotniki w stopniu najwyższym"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ == "ADJ" and "Degree=Sup" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_ADV_POS(Metric):
    category = Inflection
    name_en = "Adverbs in positive degree"
    name_local = "Przysłówki w stopniu równym"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ == "ADV" and "Degree=Pos" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_ADV_COM(Metric):
    category = Inflection
    name_en = "Adverbs in comparative degree"
    name_local = "Przysłówki w stopniu wyższym"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ == "ADV" and "Degree=Cmp" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_ADV_SUP(Metric):
    category = Inflection
    name_en = "Adverbs in superlative degree"
    name_local = "Przysłówki w stopniu najwyższym"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ == "ADV" and "Degree=Sup" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_N_1NOM(Metric):
    category = Inflection
    name_en = "Nouns in the nominative case"
    name_local = "Rzeczowniki w mianowniku"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ in ["NOUN", "PROPN"] and "Case=Nom" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_N_2GEN(Metric):
    category = Inflection
    name_en = "Nouns in the genitive case"
    name_local = "Rzeczowniki w dopełniaczu"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ in ["NOUN", "PROPN"] and "Case=Gen" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_N_3DAT(Metric):
    category = Inflection
    name_en = "Nouns in the dative case"
    name_local = "Rzeczowniki w celowniku"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ in ["NOUN", "PROPN"] and "Case=Dat" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_N_4ACC(Metric):
    category = Inflection
    name_en = "Nouns in the accusative case"
    name_local = "Rzeczowniki w bierniku"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ in ["NOUN", "PROPN"] and "Case=Acc" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_N_5INS(Metric):
    category = Inflection
    name_en = "Nouns in the instrumental case"
    name_local = "Rzeczowniki w narzędniku"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ in ["NOUN", "PROPN"] and "Case=Ins" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_N_6LOC(Metric):
    category = Inflection
    name_en = "Nouns in the locative case"
    name_local = "Rzeczowniki w miejscowniku"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ in ["NOUN", "PROPN"] and "Case=Loc" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_N_7VOC(Metric):
    category = Inflection
    name_en = "Nouns in the vocative case"
    name_local = "Rzeczowniki w wołaczu"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ in ["NOUN", "PROPN"] and "Case=Voc" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_N_SG(Metric):
    category = Inflection
    name_en = "Singular nouns"
    name_local = "Rzeczowniki w liczbie pojedynczej"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ in ["NOUN", "PROPN"] and "Number=Sing" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_N_PL(Metric):
    category = Inflection
    name_en = "Plural nouns"
    name_local = "Rzeczowniki w liczbie mnogiej"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ in ["NOUN", "PROPN"] and "Number=Plur" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_N_MS(Metric):
    category = Inflection
    name_en = "Singular masculine nouns"
    name_local = "Rzeczowniki w liczbie pojedynczej w rodzaju męskim"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ in ["NOUN", "PROPN"]
            and all(tag in token.morph for tag in ["Gender=Masc", "Number=Sing"])
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_N_MP(Metric):
    category = Inflection
    name_en = "Nouns in masculine personal gender (plural)"
    name_local = "Rzeczowniki w liczbie mnogiej w rodzaju męskoosobowym"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ in ["NOUN", "PROPN"]
            and all(
                tag in token.morph
                for tag in ["Animacy=Hum", "Gender=Masc", "Number=Plur"]
            )
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_N_FS(Metric):
    category = Inflection
    name_en = "Singular feminine nouns"
    name_local = "Rzeczowniki w liczbie pojedynczej w rodzaju żeńskim"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ in ["NOUN", "PROPN"]
            and all(tag in token.morph for tag in ["Gender=Fem", "Number=Sing"])
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_N_NMP(Metric):
    category = Inflection
    name_en = "Nouns in non-masculine personal gender (plural)"
    name_local = "Rzeczowniki w liczbie mnogiej w rodzaju niemęskoosobowym"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ in ["NOUN", "PROPN"]
            and "Number=Plur" in token.morph
            and (
                "Gender=Masc" in token.morph
                and "Animacy=Hum" not in token.morph
                or "Gender=Masc" not in token.morph
            )
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_N_NS(Metric):
    category = Inflection
    name_en = "Singular neutral nouns"
    name_local = "Rzeczowniki w liczbie pojedynczej w rodzaju nijakim"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ in ["NOUN", "PROPN"]
            and all(tag in token.morph for tag in ["Gender=Neut", "Number=Sing"])
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_PRO_1NOM(Metric):
    category = Inflection
    name_en = "Pronouns in the nominative case"
    name_local = "Zaimki w mianowniku"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.morph.get("PronType") and "Case=Nom" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_PRO_2GEN(Metric):
    category = Inflection
    name_en = "Pronouns in the genitive case"
    name_local = "Zaimki w dopełniaczu"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.morph.get("PronType") and "Case=Gen" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_PRO_3DAT(Metric):
    category = Inflection
    name_en = "Pronouns in the dative case"
    name_local = "Zaimki w celowniku"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.morph.get("PronType") and "Case=Dat" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_PRO_4ACC(Metric):
    category = Inflection
    name_en = "Pronouns in the accusative case"
    name_local = "Zaimki w bierniku"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.morph.get("PronType") and "Case=Acc" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_PRO_5INS(Metric):
    category = Inflection
    name_en = "Pronouns in the instrumental case"
    name_local = "Zaimki w narzędniku"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.morph.get("PronType") and "Case=Ins" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_PRO_6LOC(Metric):
    category = Inflection
    name_en = "Pronouns in the locative case"
    name_local = "Zaimki w miejscowniku"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.morph.get("PronType") and "Case=Loc" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_PRO_7VOC(Metric):
    category = Inflection
    name_en = "Pronouns in the vocative case"
    name_local = "Zaimki w wołaczu"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.morph.get("PronType") and "Case=Voc" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_PRO_1S(Metric):
    category = Inflection
    name_en = "First person singular pronouns"
    name_local = "Zaimki w 1 os. l. poj."

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.morph.get("PronType")
            and all(tag in token.morph for tag in ["Number=Sing", "Person=1"])
            and "Number[psor]=Plur" not in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_PRO_2S(Metric):
    category = Inflection
    name_en = "First person singular pronouns"
    name_local = "Zaimki w 1 os. l. poj."

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.morph.get("PronType")
            and all(tag in token.morph for tag in ["Number=Sing", "Person=2"])
            and "Number[psor]=Plur" not in token.morph
            or token.lemma_ == "twój"
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_PRO_3S(Metric):
    category = Inflection
    name_en = "Third person singular pronouns"
    name_local = "Zaimki w 3 os. l. poj."

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.morph.get("PronType")
            and all(tag in token.morph for tag in ["Number=Sing", "Person=3"])
            and "Number[psor]=Plur" not in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_PRO_1P(Metric):
    category = Inflection
    name_en = "First person plural pronouns"
    name_local = "Zaimki w 1 os. l. mn."

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.morph.get("PronType")
            and (
                all(tag in token.morph for tag in ["Number=Plur", "Person=1"])
                or token.lemma_ == "nasz"
            )
            and not ("Number[psor]=Sing" in token.morph or token.lemma_ == "wasz")
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_PRO_2P(Metric):
    category = Inflection
    name_en = "Second person plural pronouns"
    name_local = "Zaimki w 2 os. l. mn."

    def count(doc):
        debug = [
            token.text
            for token in doc
            if (
                (
                    token.morph.get("PronType")
                    and all(tag in token.morph for tag in ["Number=Plur", "Person=2"])
                )
                and token.lemma_ not in ["nasz", "twój"]
            )
            or (token.lemma_ == "wasz" and "Number[psor]=Sing" not in token.morph)
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_PRO_3P(Metric):
    category = Inflection
    name_en = "Third person plural pronouns"
    name_local = "Zaimki w 3 os. l. mn."

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.morph.get("PronType")
            and all(tag in token.morph for tag in ["Number=Plur", "Person=3"])
            and "Number[psor]=Sing" not in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_1S(Metric):
    category = Inflection
    name_en = "Verbs in 1 person singular"
    name_local = "Czasowniki w pierwszej osobie liczby pojedynczej"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ in ["VERB", "AUX"]
            and all(tag in token.morph for tag in ["Person=1", "Number=Sing"])
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_2S(Metric):
    category = Inflection
    name_en = "Verbs in 2 person singular"
    name_local = "Czasowniki w drugiej osobie liczby pojedynczej"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ in ["VERB", "AUX"]
            and all(tag in token.morph for tag in ["Person=2", "Number=Sing"])
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_3S(Metric):
    category = Inflection
    name_en = "Verbs in 3 person singular"
    name_local = "Czasowniki w trzeciej osobie liczby pojedynczej"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ in ["VERB", "AUX"]
            and all(tag in token.morph for tag in ["Person=3", "Number=Sing"])
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_1P(Metric):
    category = Inflection
    name_en = "Verbs in 3 person plural"
    name_local = "Czasowniki w pierwszej osobie liczby mnogiej"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ in ["VERB", "AUX"]
            and all(tag in token.morph for tag in ["Person=1", "Number=Plur"])
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_2P(Metric):
    category = Inflection
    name_en = "Verbs in 2 person plural"
    name_local = "Czasowniki w drugiej osobie liczby mnogiej"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ in ["VERB", "AUX"]
            and all(tag in token.morph for tag in ["Person=2", "Number=Plur"])
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_3P(Metric):
    category = Inflection
    name_en = "Verbs in 3 person plural"
    name_local = "Czasowniki w trzeciej osobie liczby mnogiej"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ in ["VERB", "AUX"]
            and all(tag in token.morph for tag in ["Person=3", "Number=Plur"])
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_FIN(Metric):
    category = Inflection
    name_en = "Finite verbs"
    name_local = "Czasowniki w formie osobowej"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ in ["VERB", "AUX"]
            and not any(
                tag in token.morph
                for tag in [
                    "VerbType=Quasi",
                    "VerbForm=Inf",
                    "VerbForm=Conv",
                    "Person=0",
                ]
            )
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_INF(Metric):
    category = Inflection
    name_en = "Infinitive verbs"
    name_local = "Bezokoliczniki"

    def count(doc):
        debug = [token.text for token in doc if "VerbForm=Inf" in token.morph]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_QUASI(Metric):
    category = Inflection
    name_en = "Quasi-verbs"
    name_local = "Quasi-czasowniki"

    def count(doc):
        debug = [token.text for token in doc if "VerbType=Quasi" in token.morph]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_IMPERS(Metric):
    category = Inflection
    name_en = "Impersonal verb forms"
    name_local = "Bezosobniki"

    def count(doc):
        debug = [token.text for token in doc if "Person=0" in token.morph]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_IMPERS_PERF(Metric):
    category = Inflection
    name_en = "Impersonal verb forms in perfective aspect"
    name_local = "Bezosobniki w aspekcie dokonanym"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if all(tag in token.morph for tag in ["Person=0", "Aspect=Perf"])
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_IMPERS_IMPERF(Metric):
    category = Inflection
    name_en = "Impersonal verb forms in imperfective aspect"
    name_local = "Bezosobniki w aspekcie niedokonanym"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if all(tag in token.morph for tag in ["Person=0", "Aspect=Imp"])
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_MOD(Metric):
    category = Inflection
    name_en = "Modal verbs"
    name_local = "Czasowniki modalne"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.lemma_
            in ["chcieć", "musieć", "móc", "umieć", "potrafić", "powinien"]
            or "VerbType=Mod" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_PACT(Metric):
    category = Inflection
    name_en = "Active adjectival participles"
    name_local = "Imiesłowy przymiotnikowe czynne"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if all(tag in token.morph for tag in ["VerbForm=Part", "Voice=Act"])
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_PPAS(Metric):
    category = Inflection
    name_en = "Passive adjectival participles"
    name_local = "Imiesłowy przymiotnikowe bierne"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if all(tag in token.morph for tag in ["VerbForm=Part", "Voice=Pass"])
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_PPAS_PERF(Metric):
    category = Inflection
    name_en = "Passive adjectival participles in perfective aspect"
    name_local = "Imiesłowy przymiotnikowe bierne w aspekcie dokonanym"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if all(
                tag in token.morph
                for tag in ["VerbForm=Part", "Voice=Pass", "Aspect=Perf"]
            )
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_PPAS_IMPERF(Metric):
    category = Inflection
    name_en = "Passive adjectival participles in imperfective aspect"
    name_local = "Imiesłowy przymiotnikowe bierne w aspekcie niedokonanym"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if all(
                tag in token.morph
                for tag in ["VerbForm=Part", "Voice=Pass", "Aspect=Imp"]
            )
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_PCON(Metric):
    category = Inflection
    name_en = "Present adverbial participles"
    name_local = "Imiesłowy przysłówkowe współczesne"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if all(
                tag in token.morph
                for tag in ["VerbForm=Conv", "Tense=Pres", "Aspect=Imp"]
            )
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_PANT(Metric):
    category = Inflection
    name_en = "Perfect adverbial participles"
    name_local = "Imiesłowy przysłówkowe uprzednie"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if all(
                tag in token.morph
                for tag in ["VerbForm=Conv", "Tense=Past", "Aspect=Perf"]
            )
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_PERF(Metric):
    category = Inflection
    name_en = "Verbs in perfect aspect"
    name_local = "Czasowniki w aspekcie dokonanym"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ == "VERB"
            and "Aspect=Perf" in token.morph
            and "VerbForm=Conv" not in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_IMPERF(Metric):
    category = Inflection
    name_en = "Verbs in imperfect aspect"
    name_local = "Czasowniki w aspekcie niedokonanym"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ == "VERB"
            and "Aspect=Imp" in token.morph
            and "VerbForm=Conv" not in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_ACT(Metric):
    category = Inflection
    name_en = "Verbs in active voice"
    name_local = "Czasowniki w stronie czynnej"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ in ["VERB", "AUX"]
            and "Voice=Act" in token.morph
            and not any(tag in token.morph for tag in ["VerbForm=Inf", "VerbForm=Conv"])
            and token.dep_ != "aux:pass"
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_PASS(Metric):
    category = Inflection
    name_en = "Verbs in passive voice"
    name_local = "Czasowniki w stronie biernej"

    def count(doc):
        nlp = IN_V_PASS.get_nlp()
        matcher = Matcher(nlp.vocab)
        adjs = [
            token
            for token in doc
            if token.pos_ == "ADJ" and "VerbForm=Part" in token.morph
        ]
        pattern = [
            {"POS": "AUX"},
            {"OP": "?"},
            {"TEXT": {"IN": [token.text for token in adjs]}},
        ]
        matcher.add("verb_pass", [pattern])
        matches = matcher(doc)
        debug = [(doc[start].text, doc[end - 1].text) for _, start, end in matches]
        bi_gram_count = len(matches) * 2
        return ratio(bi_gram_count, len(doc)), debug


class IN_V_GER(Metric):
    category = Inflection
    name_en = "Gerunds"
    name_local = "Rzeczowniki odczasownikowe"

    def count(doc):
        debug = [token.text for token in doc if "VerbForm=Vnoun" in token.morph]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_PRES(Metric):
    category = Inflection
    name_en = "Verbs in present tense"
    name_local = "Czasowniki w czasie teraźniejszym"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if "Tense=Pres" in token.morph and "VerbForm=Conv" not in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_PAST(Metric):
    category = Inflection
    name_en = "Verbs in past tense"
    name_local = "Czasowniki w czasie przeszłym"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if "Tense=Past" in token.morph
            and not any(tag in token.morph for tag in ["VerbForm=Conv", "Mood=Cnd"])
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_FUTS(Metric):
    category = Inflection
    name_en = "Verbs in simple future tense"
    name_local = "Czasowniki w czasie przyszłym prostym"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if ("fin" in token.tag_.split(":") and "perf" in token.tag_.split(":"))
            or ("bedzie" in token.tag_.split(":") and token.dep_ not in "aux".split())
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_FUTC(Metric):
    category = Inflection
    name_en = "Verbs in future complex tense"
    name_local = "Czasowniki w czasie przyszłym złożonym"

    def count(doc):
        result = 0
        debug = []

        for sent in doc.sents:
            aux = [
                token.text
                for token in sent
                if token.dep_ == "aux"
                and "Tense=Fut" in token.morph
                and token.lemma_ == "być"
            ]

            root = [
                token.text
                for token in sent
                if token.pos_ == "VERB"
                and token.dep_ in ["ROOT"]
                and "Aspect=Imp" in token.morph
                and ("Tense=Past" in token.morph or "VerbForm=Inf" in token.morph)
            ]

            conj = [
                token.text
                for token in sent
                if token.dep_ == "conj" and token.head.text in root
            ]

            if aux and root and conj:
                debug.append((aux, root, conj))
                result += len(aux) + len(root) + len(conj)
            elif aux and root:
                debug.append((aux, root))
                result += len(aux) + len(root)

        return ratio(result, len(doc)), debug


class IN_V_FUT(Metric):
    category = Inflection
    name_en = "Verbs in future tense"
    name_local = "Czasowniki w czasie przyszłym"

    def count(doc):
        result1, debug1 = IN_V_FUTS.count(doc)
        result2, debug2 = IN_V_FUTC.count(doc)
        combined_result = result1 + result2
        combined_debug = debug1 + debug2
        return combined_result, combined_debug


class IN_V_IMP(Metric):
    category = Inflection
    name_en = "Verbs in imperative mood"
    name_local = "Czasowniki w trybie rozkazującym"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if "impt" in token.tag_.split(":")
            or (any(ch.dep_ == "aux:imp" for ch in token.children))
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_COND(Metric):
    category = Inflection
    name_en = "Verbs in conditional"
    name_local = "Czasowniki w trybie przypuszczającym"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if (token.pos_ in ["VERB", "AUX"] and "Mood=Cnd" in token.morph)
            or "praet" in token.tag_.split(":")
            and any(
                any(w == t.text.lower() for t in token.children)
                for w in "bym byś by byśmy byście".split()
            )
            or any(
                word in (t.text.lower() for t in token.children)
                for word in "gdyby gdybym gdybyś gdybyśmy gdybyście jakby jakbym jakbyś jakbyśmy jakbyście jeżeliby jeżelibym jeżelibyś jeżelibyśmy jeżelibyście jeśliby jeślibyś jeślibyśmy jeślibyście".split()
            )
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug
