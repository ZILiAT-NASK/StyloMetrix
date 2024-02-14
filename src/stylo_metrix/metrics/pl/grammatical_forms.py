from ...structures import Category, Metric
from ...utils import ratio


class GrammaticalForms(Category):
    lang = "pl"
    name_en = "Grammatical_Forms"
    name_local = "Czesci_mowy"


class G_N(Metric):
    category = GrammaticalForms
    name_en = "Nouns"
    name_local = "Rzeczowniki"

    def count(doc):
        debug = [token.text for token in doc if token.pos_ in ["NOUN", "PROPN"]]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_V(Metric):
    category = GrammaticalForms
    name_en = "Verbs"
    name_local = "Czasowniki"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ in ["VERB", "AUX"] and "VerbType=Quasi" not in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_ADJ(Metric):
    category = GrammaticalForms
    name_en = "Adjectives"
    name_local = "Przymiotniki"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ == "ADJ"
            and token.is_digit == False
            and "NumForm=Roman" not in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_ADV(Metric):
    category = GrammaticalForms
    name_en = "Adverbs"
    name_local = "Przysłówki"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ == "ADV" and token.is_punct == False
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_PRO(Metric):
    category = GrammaticalForms
    name_en = "Pronouns"
    name_local = "Zaimki"

    def count(doc):
        debug = [token.text for token in doc if token.morph.get("PronType")]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_PRO_PRS(Metric):
    category = GrammaticalForms
    name_en = "Personal pronouns"
    name_local = "Zaimki osobowe"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if "PronType=Prs" in token.morph
            and not any(tag in token.morph for tag in ["Reflex=Yes", "Poss=Yes"])
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_PRO_REL(Metric):
    category = GrammaticalForms
    name_en = "Relative pronouns"
    name_local = "Zaimki względne"

    def count(doc):
        debug = [token.text for token in doc if "PronType=Rel" in token.morph]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_PRO_DEM(Metric):
    category = GrammaticalForms
    name_en = "Demonstrative pronouns"
    name_local = "Zaimki wskazujące"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ in ["PRON", "DET"] and "PronType=Dem" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_PRO_INT(Metric):
    category = GrammaticalForms
    name_en = "Interrogative pronouns"
    name_local = "Zaimki pytajne"

    def count(doc):
        debug = [token.text for token in doc if "PronType=Int" in token.morph]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_PRO_IND(Metric):
    category = GrammaticalForms
    name_en = "Indefinite pronouns"
    name_local = "Zaimki nieokreślone"

    def count(doc):
        debug = [token.text for token in doc if "PronType=Ind" in token.morph]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_PRO_TOT(Metric):
    category = GrammaticalForms
    name_en = "Total pronouns"
    name_local = "Zaimki uogólniające"

    def count(doc):
        debug = [token.text for token in doc if "PronType=Tot" in token.morph]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_PRO_NEG(Metric):
    category = GrammaticalForms
    name_en = "Negative pronouns"
    name_local = "Zaimki przeczące"

    def count(doc):
        debug = [token.text for token in doc if "PronType=Neg" in token.morph]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_PRO_POS(Metric):
    category = GrammaticalForms
    name_en = "Possessive pronouns"
    name_local = "Zaimki dzierżawcze"

    def count(doc):
        list_pronouns = ["jej", "jego", "ich"]
        debug = [
            token.text
            for token in doc
            if "Poss=Yes" in token.morph or token.text in list_pronouns
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_NUM(Metric):
    category = GrammaticalForms
    name_en = "Numerals"
    name_local = "Liczebniki"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.morph.get("NumForm") or token.pos_ == "NUM"
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_CNUM(Metric):
    category = GrammaticalForms
    name_en = "Collective numerals"
    name_local = "Liczebniki zbiorowe"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ == "NUM"
            and [
                "NumType=Sets" in token.morph
                or any("col" in tag_part for tag_part in token.tag_.split(":"))
            ]
            and "NumForm=Digit" not in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_PART(Metric):
    category = GrammaticalForms
    name_en = "Particles"
    name_local = "Partykuły"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if "part" in token.tag_.split(":") and "Reflex=Yes" not in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_ADP(Metric):
    category = GrammaticalForms
    name_en = "Adpositions"
    name_local = "Przyimki"

    def count(doc):
        debug = [token.text for token in doc if token.pos_ == "ADP"]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_INTJ(Metric):
    category = GrammaticalForms
    name_en = "Interjections"
    name_local = "Wykrzykniki"

    def count(doc):
        debug = [token.text for token in doc if token.pos_ == "INTJ"]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_SYM(Metric):
    category = GrammaticalForms
    name_en = "Symbols"
    name_local = "Symbole"

    def count(doc):
        debug = [token.text for token in doc if token.pos_ == "SYM"]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_ABBR(Metric):
    category = GrammaticalForms
    name_en = "Abbreviations"
    name_local = "Skrótowce"

    def count(doc):
        debug = [token.text for token in doc if "brev" in token.tag_.split(":")]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_CONJ(Metric):
    category = GrammaticalForms
    name_en = "Conjunctions"
    name_local = "Spójniki"

    def count(doc):
        debug = [token.text for token in doc if token.pos_ in ["CCONJ", "SCONJ"]]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_CCONJ(Metric):
    category = GrammaticalForms
    name_en = "Coordinating conjunctions"
    name_local = "Łączniki zdan współrzędnie złożonych"

    def count(doc):
        debug = [token.text for token in doc if token.pos_ == "CCONJ"]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_SCONJ(Metric):
    category = GrammaticalForms
    name_en = "Subordinating conjunctions"
    name_local = "Łączniki zdań podrzędnie złożonych"

    def count(doc):
        debug = [token.text for token in doc if token.pos_ == "SCONJ"]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_OTHER(Metric):
    category = GrammaticalForms
    name_en = "Other parts of speech"
    name_local = "Inne części mowy"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ == "X" and "Abbr=Yes" not in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug
