from ...structures import Category, Metric
from ...utils import ratio


class GrammaticalForms(Category):
    lang = "de"
    name_en = "Parts of Speech"
    name_local = "GrammatischeFormen"


class G_N(Metric):
    category = GrammaticalForms
    name_en = "Nouns"
    name_local = "Substantive"

    def count(doc):
        numerals = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        debug = [
            token.text
            for token in doc
            if token.pos_ in ["NOUN", "PROPN"]
            and not any(char in numerals for char in token.text)
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_ADJ(Metric):
    category = GrammaticalForms
    name_en = "Adjectives"
    name_local = "Adjektive"

    def count(doc):
        numerals = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        debug = [
            token.text
            for token in doc
            if token.pos_ == "ADJ" and not any(char in numerals for char in token.text)
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_ADV(Metric):
    category = GrammaticalForms
    name_en = "Adverbs"
    name_local = "Adverbien"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ == "ADV" and token.is_punct == False
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_V(Metric):
    category = GrammaticalForms
    name_en = "Verbs"
    name_local = "Verben"

    def count(doc):
        debug = [token.text for token in doc if token.pos_ in ["VERB", "AUX"]]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_VMOD(Metric):
    category = GrammaticalForms
    name_en = "Modal verbs"
    name_local = "Modalverben"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if any(tag in token.tag_.split(":") for tag in ["VMFIN", "VMINF"])
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_NUM(Metric):
    category = GrammaticalForms
    name_en = "Numerals"
    name_local = "Numerale"

    def count(doc):
        debug = [token.text for token in doc if token.pos_ == "NUM"]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_PART(Metric):
    category = GrammaticalForms
    name_en = "Particles"
    name_local = "Partikeln"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if any(
                tag in token.tag_.split(":")
                for tag in ["FPTK", "IPTK", "MPTK", "PTKNEG", "PTKZU", "PTKVZ", "PTKA"]
            )
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_ADP(Metric):
    category = GrammaticalForms
    name_en = "Adpositions"
    name_local = "Präpositionen"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if any(
                tag in token.tag_.split(":")
                for tag in ["APPR", "APPRART", "APPO", "APZR"]
            )
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_CONJ(Metric):
    category = GrammaticalForms
    name_en = "Conjunctions"
    name_local = "Konjunktionen"

    def count(doc):
        debug = [token.text for token in doc if token.pos_ in ["CCONJ", "SCONJ"]]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_CCONJ(Metric):
    category = GrammaticalForms
    name_en = "Coordinating conjunctions"
    name_local = "Koordinierende Konjunktionen"

    def count(doc):
        debug = [token.text for token in doc if token.pos_ == "CCONJ"]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_SCONJ(Metric):
    category = GrammaticalForms
    name_en = "Conjunctions"
    name_local = "Subordinierende Konjunktionen"

    def count(doc):
        debug = [token.text for token in doc if token.pos_ == "SCONJ"]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_PRO(Metric):
    category = GrammaticalForms
    name_en = "Pronouns"
    name_local = "Pronomen"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if any(
                tag in token.tag_.split(":")
                for tag in [
                    "PDS",
                    "PIS",
                    "PIAT",
                    "PDAT",
                    "PPER",
                    "PPOSS",
                    "PPOSAT",
                    "PROAV",
                    "PRELS",
                    "PRF",
                    "PWS",
                    "PWAT",
                    "PROWAV",
                    "PWAV",
                ]
            )
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_PRO_PRS(Metric):
    category = GrammaticalForms
    name_en = "Personal pronouns"
    name_local = "Personalpronomen"

    def count(doc):
        debug = [token.text for token in doc if "PPER" in token.tag_.split(":")]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_PRO_DEM(Metric):
    category = GrammaticalForms
    name_en = "Demonstrative pronouns"
    name_local = "Demonstrativpronomen"

    def count(doc):
        debug = [token.text for token in doc if "PronType=Dem" in token.morph]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_PRO_IND(Metric):
    category = GrammaticalForms
    name_en = "Indefinite pronouns"
    name_local = "Indefinitpronomen"

    def count(doc):
        debug = [token.text for token in doc if "PronType=Ind" in token.morph]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_PRO_PIS(Metric):
    category = GrammaticalForms
    name_en = "Substitutive indefinite pronouns"
    name_local = "Ersetzende Indefinitpronomen"

    def count(doc):
        debug = [token.text for token in doc if "PIS" in token.tag_.split(":")]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_PRO_PIAT(Metric):
    category = GrammaticalForms
    name_en = "Attributive indefinite pronouns"
    name_local = "Attributive Indefinitpronomen"

    def count(doc):
        debug = [token.text for token in doc if "PIAT" in token.tag_.split(":")]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_PRO_POS(Metric):
    category = GrammaticalForms
    name_en = "Possessive pronouns"
    name_local = "Possessivpronomen"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if any(tag in token.tag_.split(":") for tag in ["PPOSAT", "PPOS"])
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_PRO_INT(Metric):
    category = GrammaticalForms
    name_en = "Interrogative pronouns"
    name_local = "Interrogativpronomen"

    def count(doc):
        debug = [token.text for token in doc if "PronType=Int" in token.morph]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_PRO_REL(Metric):
    category = GrammaticalForms
    name_en = "Relative pronouns"
    name_local = "Relativpronomen"

    def count(doc):
        debug = [token.text for token in doc if "PronType=Rel" in token.morph]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_PRO_REFL(Metric):
    category = GrammaticalForms
    name_en = "Reflexive pronouns"
    name_local = "Reflexivpronomen"

    def count(doc):
        debug = [token.text for token in doc if "PRF" in token.tag_.split(":")]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_PRO_REZ(Metric):
    category = GrammaticalForms
    name_en = "Reciprocal pronouns"
    name_local = "Reziprokpronomen"

    def count(doc):
        reziprok = [
            "einander",
            "miteinander",
            "voneinander",
            "gegeneinander",
            "umeinander",
            "ineinander",
            "füreinander",
            "übereinander",
        ]
        debug = [token.text for token in doc if token.text.lower() in reziprok]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_PRO_UNPERS(Metric):
    category = GrammaticalForms
    name_en = "Impersonal pronouns"
    name_local = "Unpersönliche Pronomen"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.text.lower() == "es" and token.dep_ in ["sb", "ph", "ep"]
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_PRO_ADV(Metric):
    category = GrammaticalForms
    name_en = "Pronominal adverbs"
    name_local = "Pronominaladverbien"

    def count(doc):
        debug = [token.text for token in doc if "PROAV" in token.tag_.split(":")]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_ART(Metric):
    category = GrammaticalForms
    name_en = "Determiners"
    name_local = "Artikel"

    def count(doc):
        debug = [token.text for token in doc if "ART" in token.tag_.split(":")]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_ART_DEF(Metric):
    category = GrammaticalForms
    name_en = "Definite articles"
    name_local = "Bestimmte Artikel"

    def count(doc):
        debug = [token.text for token in doc if "Definite=Def" in token.morph]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_ART_IND(Metric):
    category = GrammaticalForms
    name_en = "Indefinite articles"
    name_local = "Unbestimmte Artikel"

    def count(doc):
        debug = [token.text for token in doc if "Definite=Ind" in token.morph]
        result = len(debug)
        return ratio(result, len(doc)), debug


class G_OTHER(Metric):
    category = GrammaticalForms
    name_en = "Other parts of speech"
    name_local = "Andere Wortarten"

    def count(doc):
        debug = [token.text for token in doc if token.pos_ == "X"]
        result = len(debug)
        return ratio(result, len(doc)), debug
