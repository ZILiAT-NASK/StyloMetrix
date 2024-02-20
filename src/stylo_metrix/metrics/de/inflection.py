from ...structures import Category, Metric
from ...utils import ratio


class Inflection(Category):
    lang = "de"
    name_en = "Inflection"
    name_local = "Flexion"


class IN_N_SG(Metric):
    category = Inflection
    name_en = "Singular nouns"
    name_local = "Substantive im Singular"

    def count(doc):
        numerals = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        debug = [
            token.text
            for token in doc
            if token.pos_ in ["NOUN", "PROPN"]
            and "Number=Sing" in token.morph
            and not any(char in numerals for char in token.text)
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_N_PL(Metric):
    category = Inflection
    name_en = "Plural nouns"
    name_local = "Substantive im Plural"

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
    name_local = "Maskuline Substantive im Singular"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ in ["NOUN", "PROPN"]
            and "Gender=Masc" in token.morph
            and "Number=Sing" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_N_FS(Metric):
    category = Inflection
    name_en = "Singular feminine nouns"
    name_local = "Feminine Substantive im Singular"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ in ["NOUN", "PROPN"]
            and "Gender=Fem" in token.morph
            and "Number=Sing" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_N_NS(Metric):
    category = Inflection
    name_en = "Singular neutral nouns"
    name_local = "Neutrale Substantive im Singular"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ in ["NOUN", "PROPN"]
            and "Gender=Neut" in token.morph
            and "Number=Sing" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_N_MP(Metric):
    category = Inflection
    name_en = "Plural masculine nouns"
    name_local = "Maskuline Substantive im Plural"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ in ["NOUN", "PROPN"]
            and "Gender=Masc" in token.morph
            and "Number=Plur" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_N_FP(Metric):
    category = Inflection
    name_en = "Feminine masculine nouns"
    name_local = "Feminine Substantive im Plural"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ in ["NOUN", "PROPN"]
            and "Gender=Fem" in token.morph
            and "Number=Plur" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_N_NP(Metric):
    category = Inflection
    name_en = "Neutral masculine nouns"
    name_local = "Neutrale Substantive im Plural"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ in ["NOUN", "PROPN"]
            and "Gender=Neut" in token.morph
            and "Number=Plur" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_N_1NOM(Metric):
    category = Inflection
    name_en = "Nouns in the nominative case"
    name_local = "Nomen im Nominativ"

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
    name_local = "Nomen im Genitiv"

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
    name_local = "Nomen im Dativ"

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
    name_local = "Nomen im Accusativ"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ in ["NOUN", "PROPN"] and "Case=Acc" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_ADJ_POS(Metric):
    category = Inflection
    name_en = "Adjectives in positive degree"
    name_local = "Adjektive im Positiv"

    def count(doc):
        numerals = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        debug = [
            token.text
            for token in doc
            if token.pos_ == "ADJ"
            and not any(char in numerals for char in token.text)
            and "Degree=Pos" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_ADJ_CMP(Metric):
    category = Inflection
    name_en = "Adjectives in comparative degree"
    name_local = "Adjektive im Komparativ"

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
    name_local = "Adjektive im Superlativ"

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
    name_local = "Adverben im Positiv"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ == "ADV" and "Degree=Pos" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_ADV_CMP(Metric):
    category = Inflection
    name_en = "Adverbs in comparative degree"
    name_local = "Adverben im Komparativ"

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
    name_local = "Adverben im Superlativ"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ == "ADV" and "Degree=Sup" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_PRO_SG(Metric):
    category = Inflection
    name_en = "Singular pronouns"
    name_local = "Pronomen im Singular"

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
            and "Number=Sing" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_PRO_PL(Metric):
    category = Inflection
    name_en = "Plural pronouns"
    name_local = "Pronomen im Plural"

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
            and "Number=Plur" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_PRO_1NOM(Metric):
    category = Inflection
    name_en = "Pronouns in the nominative case"
    name_local = "Pronomen im Nominativ"

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
            and "Case=Nom" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_PRO_2GEN(Metric):
    category = Inflection
    name_en = "Pronouns in the genitive case"
    name_local = "Pronomen im Genitiv"

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
            and "Case=Gen" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_PRO_3DAT(Metric):
    category = Inflection
    name_en = "Pronouns in the dative case"
    name_local = "Pronomen im Dativ"

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
            and "Case=Dat" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_PRO_4ACC(Metric):
    category = Inflection
    name_en = "Pronouns in the accusative case"
    name_local = "Pronomen im Accusativ"

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
            and "Case=Acc" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_PRO_1SG(Metric):
    category = Inflection
    name_en = "Personal pronouns in 1st person singular"
    name_local = "Personalpronomen in der ersten Person Singular"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if "PPER" in token.tag_.split(":")
            and "Person=1" in token.morph
            and "Number=Sing" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_PRO_2SG(Metric):
    category = Inflection
    name_en = "Personal pronouns in 2nd person singular"
    name_local = "Personalpronomen in der zweiten Person Singular"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if "PPER" in token.tag_.split(":")
            and "Person=2" in token.morph
            and "Number=Sing" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_PRO_3SG(Metric):
    category = Inflection
    name_en = "Personal pronouns in 3rd person singular"
    name_local = "Personalpronomen in der dritten Person Singular"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if "PPER" in token.tag_.split(":")
            and "Person=3" in token.morph
            and "Number=Sing" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_PRO_1PL(Metric):
    category = Inflection
    name_en = "Personal pronouns in 1st person plural"
    name_local = "Personalpronomen in der ersten Person Plural"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if "PPER" in token.tag_.split(":")
            and "Person=1" in token.morph
            and "Number=Plur" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_PRO_2PL(Metric):
    category = Inflection
    name_en = "Personal pronouns in 2nd person plural"
    name_local = "Personalpronomen in der zweiten Person Plural"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if "PPER" in token.tag_.split(":")
            and "Person=2" in token.morph
            and "Number=Plur" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_PRO_3PL(Metric):
    category = Inflection
    name_en = "Personal pronouns in 3rd person plural"
    name_local = "Personalpronomen in der dritten Person Plural"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if "PPER" in token.tag_.split(":")
            and "Person=3" in token.morph
            and "Number=Plur" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_POSS_1SG(Metric):
    category = Inflection
    name_en = "Possessive pronouns in 1st person singular"
    name_local = "Possesivpronomen in der ersten Person Singular"

    def count(doc):
        poss = ["mein", "meine", "meiner", "meines", "meinen", "meinem"]
        debug = [token.text for token in doc if token.text.lower() in poss]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_POSS_2SG(Metric):
    category = Inflection
    name_en = "Possessive pronouns in 2nd person singular"
    name_local = "Possesivpronomen in der zweiten Person Singular"

    def count(doc):
        poss = ["dein", "deine", "deiner", "deines", "deinen", "deinem"]
        debug = [token.text for token in doc if token.text.lower() in poss]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_POSS_3SG(Metric):
    category = Inflection
    name_en = "Possessive pronouns in 3rd person singular"
    name_local = "Possesivpronomen in der dritten Person Singular"

    def count(doc):
        poss = [
            "sein",
            "seine",
            "seiner",
            "seines",
            "seinen",
            "seinem",
            "ihr",
            "ihrem",
            "ihren",
            "ihre",
            "ihrer",
            "ihres",
        ]
        debug = [
            token.text
            for token in doc
            if token.text.lower() in poss and "Poss=Yes" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_POSS_1PL(Metric):
    category = Inflection
    name_en = "Possessive pronouns in 1st person plural"
    name_local = "Possesivpronomen in der ersten Person Plural"

    def count(doc):
        poss = ["unser", "unsere", "unserer", "unseres", "unseren", "unserem"]
        debug = [token.text for token in doc if token.text.lower() in poss]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_POSS_2PL(Metric):
    category = Inflection
    name_en = "Possessive pronouns in 2nd person plural"
    name_local = "Possesivpronomen in der zweiten Person Plural"

    def count(doc):
        poss = ["euer", "eure", "eurer", "eures", "euren", "eurem"]
        debug = [token.text for token in doc if token.text.lower() in poss]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_POSS_3PL(Metric):
    category = Inflection
    name_en = "Possessive pronouns in 3rd person plural"
    name_local = "Possesivpronomen in der dritten Person Plural"

    def count(doc):
        poss = ["ihr", "ihrem", "ihren", "ihre", "ihrer", "ihres"]
        debug = [
            token.text
            for token in doc
            if token.text.lower() in poss and "Poss=Yes" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_ART_SG(Metric):
    category = Inflection
    name_en = "Singular determiners"
    name_local = "Artikel im Singular"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if "ART" in token.tag_.split(":") and "Number=Sing" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_ART_PL(Metric):
    category = Inflection
    name_en = "Plural determiners"
    name_local = "Artikel im Plural"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if "ART" in token.tag_.split(":") and "Number=Plur" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_ART_DEF_SG(Metric):
    category = Inflection
    name_en = "Singular definite articles"
    name_local = "Bestimmte Artikel im Singular"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if "Definite=Def" in token.morph and "Number=Sing" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_ART_DEF_PL(Metric):
    category = Inflection
    name_en = "Plural definite articles"
    name_local = "Bestimmte Artikel im Plural"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if "Definite=Def" in token.morph and "Number=Plur" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_ART_IND_SG(Metric):
    category = Inflection
    name_en = "Singular indefinite articles"
    name_local = "Unbestimmte Artikel im Singular"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if "Definite=Ind" in token.morph and "Number=Sing" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_ART_M(Metric):
    category = Inflection
    name_en = "Masculine determiners"
    name_local = "Maskuline Artikel"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if "ART" in token.tag_.split(":") and "Gender=Masc" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_ART_F(Metric):
    category = Inflection
    name_en = "Feminine determiners"
    name_local = "Feminine Artikel"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if "ART" in token.tag_.split(":") and "Gender=Fem" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_ART_N(Metric):
    category = Inflection
    name_en = "Neutral determiners"
    name_local = "Neutrale Artikel"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if "ART" in token.tag_.split(":") and "Gender=Neut" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_ART_1NOM(Metric):
    category = Inflection
    name_en = "Articles in the nominative case"
    name_local = "Artikel im Nominativ"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if "ART" in token.tag_.split(":") and "Case=Nom" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_ART_2GEN(Metric):
    category = Inflection
    name_en = "Articles in the genitive case"
    name_local = "Artikel im Genitiv"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if "ART" in token.tag_.split(":") and "Case=Gen" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_ART_3DAT(Metric):
    category = Inflection
    name_en = "Articles in the dative case"
    name_local = "Artikel im Dativ"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if "ART" in token.tag_.split(":") and "Case=Dat" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_ART_4ACC(Metric):
    category = Inflection
    name_en = "Articles in the accusative case"
    name_local = "Artikel im Accusativ"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if "ART" in token.tag_.split(":") and "Case=Acc" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_ART_DEF_1NOM(Metric):
    category = Inflection
    name_en = "Definite articles in the nominative case"
    name_local = "Bestimmte Artikel im Nominativ"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if "Definite=Def" in token.morph and "Case=Nom" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_ART_DEF_2GEN(Metric):
    category = Inflection
    name_en = "Definite articles in the genitive case"
    name_local = "Bestimmte Artikel im Genitiv"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if "Definite=Def" in token.morph and "Case=Gen" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_ART_DEF_3DAT(Metric):
    category = Inflection
    name_en = "Definite articles in the dative case"
    name_local = "Bestimmte Artikel im Dativ"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if "Definite=Def" in token.morph and "Case=Dat" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_ART_DEF_4ACC(Metric):
    category = Inflection
    name_en = "Definite articles in the accusative case"
    name_local = "Bestimmte Artikel im Accusativ"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if "Definite=Def" in token.morph and "Case=Acc" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_ART_IND_1NOM(Metric):
    category = Inflection
    name_en = "Indefinite articles in the nominative case"
    name_local = "Unbestimmte Artikel im Nominativ"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if "Definite=Ind" in token.morph and "Case=Nom" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_ART_IND_2GEN(Metric):
    category = Inflection
    name_en = "Indefinite articles in the genitive case"
    name_local = "Unbestimmte Artikel im Genitiv"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if "Definite=Ind" in token.morph and "Case=Gen" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_ART_IND_3DAT(Metric):
    category = Inflection
    name_en = "Indefinite articles in the nominative case"
    name_local = "Unbestimmte Artikel im Nominativ"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if "Definite=Ind" in token.morph and "Case=Dat" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_ART_IND_4ACC(Metric):
    category = Inflection
    name_en = "Indefinite articles in the accusative case"
    name_local = "Unbestimmte Artikel im Accusativ"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if "Definite=Ind" in token.morph and "Case=Acc" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_FIN(Metric):
    category = Inflection
    name_en = "Finite verbs"
    name_local = "Finite Verben"

    def count(doc):
        debug = [token.text for token in doc if "VerbForm=Fin" in token.morph]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_AUX_FIN(Metric):
    category = Inflection
    name_en = "Finite auxiliary verbs"
    name_local = "Finite auxiliare Verben"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if any(tag in token.tag_.split(":") for tag in ["VAFIN", "VMFIN"])
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_AUX2_FIN(Metric):
    category = Inflection
    name_en = "Finite auxiliary verbs"
    name_local = "Finite Hilfsverben"

    def count(doc):
        debug = [token.text for token in doc if "VAFIN" in token.tag_.split(":")]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_AUX_MOD_FIN(Metric):
    category = Inflection
    name_en = "Finite modal verbs"
    name_local = "Finite Modalverben"

    def count(doc):
        debug = [token.text for token in doc if "VMFIN" in token.tag_.split(":")]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_INF(Metric):
    category = Inflection
    name_en = "Infinitive verbs"
    name_local = "Infinitive Verbformen"

    def count(doc):
        debug = [token.text for token in doc if "VerbForm=Inf" in token.morph]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_VVIZU(Metric):
    category = Inflection
    name_en = "Infinitive verbs with 'zu'"
    name_local = "Infinitiv mit 'zu'"

    def count(doc):
        debug = [token.text for token in doc if "VVIZU" in token.tag_.split(":")]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_PRES(Metric):
    category = Inflection
    name_en = "Verbs in present tense"
    name_local = "Verben im Präsens"

    def count(doc):
        debug = [token.text for token in doc if "Tense=Pres" in token.morph]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_1SG(Metric):
    category = Inflection
    name_en = "First person singular verbs"
    name_local = "Verben in der ersten Person Singular"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ in ["VERB", "AUX"]
            and "Person=1" in token.morph
            and "Number=Sing" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_2SG(Metric):
    category = Inflection
    name_en = "Second person singular verbs"
    name_local = "Verben in der zweiten Person Singular"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ in ["VERB", "AUX"]
            and "Person=2" in token.morph
            and "Number=Sing" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_3SG(Metric):
    category = Inflection
    name_en = "Third person singular verbs"
    name_local = "Verben in der dritten Person Singular"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ in ["VERB", "AUX"]
            and "Person=3" in token.morph
            and "Number=Sing" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_1PL(Metric):
    category = Inflection
    name_en = "First person plural verbs"
    name_local = "Verben in der ersten Person Plural"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ in ["VERB", "AUX"]
            and "Person=1" in token.morph
            and "Number=Plur" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_2PL(Metric):
    category = Inflection
    name_en = "Second person plural verbs"
    name_local = "Verben in der zweiten Person Plural"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ in ["VERB", "AUX"]
            and "Person=2" in token.morph
            and "Number=Plur" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_3PL(Metric):
    category = Inflection
    name_en = "Third person plural verbs"
    name_local = "Verben in der dritten Person Plural"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ in ["VERB", "AUX"]
            and "Person=3" in token.morph
            and "Number=Plur" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_PP(Metric):
    category = Inflection
    name_en = "Participle Perfect Verbs"
    name_local = "Partizip Perfekt Vollverben"

    def count(doc):
        debug = [token.text for token in doc if "VVPP" in token.tag_.split(":")]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_PAST_IMP(Metric):
    category = Inflection
    name_en = "Imperfect verbs"
    name_local = "Imperfekt Verben"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ in ["AUX", "VERB"]
            and "Tense=Past" in token.morph
            and "Mood=Sub" not in token.morph
            and not any(
                child for child in token.children if "VerbForm=Part" in child.morph
            )
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_PAST_IMP2(Metric):
    category = Inflection
    name_en = "Imperfect Verbs excluding Modals and Auxiliaries"
    name_local = "Imperfekt Verben ohne Modale und Hilfsverben"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ == "VERB"
            and "Tense=Past" in token.morph
            and "Mood=Sub" not in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_PAST_IMP_AUX(Metric):
    category = Inflection
    name_en = "Imperfect Modals and Auxiliaries"
    name_local = "Imperfekt Modale und Hilfsverben"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ == "AUX"
            and "Tense=Past" in token.morph
            and "Mood=Sub" not in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_PAST_IMP_MOD(Metric):
    category = Inflection
    name_en = "Participle Perfect Verbs"
    name_local = "Imperfekt Modalverben"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if "Tense=Past" in token.morph
            and "VMFIN" in token.tag_.split(":")
            and "Mood=Sub" not in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_PERFEKT(Metric):
    category = Inflection
    name_en = "Present perfect tense verb forms"
    name_local = "Verben im Perfekt"

    def count(doc):
        result = 0
        debug = []

        for sent in doc.sents:
            aux_candidates = [
                token
                for token in sent
                if token.text.lower()
                in [
                    "bin",
                    "bist",
                    "ist",
                    "sind",
                    "seid",
                    "habe",
                    "hast",
                    "hat",
                    "haben",
                    "habt",
                ]
                and any(
                    child for child in token.children if "VerbForm=Part" in child.morph
                )
            ]

            partizip_candidates = [
                token
                for token in sent
                if "VVPP" in token.tag_.split(":") and token.dep_ == "oc"
            ]

            aux = [token.text for token in aux_candidates]

            for aux_token in aux_candidates:
                partizip_tokens = []

                for token in aux_token.children:
                    if token in partizip_candidates and "werden" not in [
                        child.lemma_ for child in token.children
                    ]:
                        partizip_tokens.append(token.text)

            if aux and partizip_tokens:
                debug.append((aux, partizip_tokens))
                result += len(aux) + len(partizip_tokens)

        return ratio(result, len(doc)), debug


class IN_V_PLUSQUAM(Metric):
    category = Inflection
    name_en = "Past perfect tense verb forms"
    name_local = "Verben im Plusquamperfekt"

    def count(doc):
        result = 0
        debug = []

        for sent in doc.sents:
            aux = [
                token.text
                for token in sent
                if token.dep_ == "ROOT"
                and "Tense=Past" in token.morph
                and "Mood=Sub" not in token.morph
                and token.lemma_ in ["haben", "sein"]
                and any(
                    child for child in token.children if "VerbForm=Part" in child.morph
                )
            ]

            partizip = [
                token.text
                for token in sent
                if "VerbForm=Part" in token.morph and token.dep_ == "oc"
            ]

            if aux and partizip:
                debug.append((aux, partizip))
                result += len(aux) + len(partizip)

        return ratio(result, len(doc)), debug


class IN_V_PAST(Metric):
    category = Inflection
    name_en = "Verbs in past tense"
    name_local = "Vergangenheitszeitformen"

    def count(doc):
        result1, debug1 = IN_V_PAST_IMP.count(doc)
        result2, debug2 = IN_V_PERFEKT.count(doc)
        result3, debug3 = IN_V_PLUSQUAM.count(doc)
        combined_result = result1 + result2 + result3
        combined_debug = debug1 + debug2 + debug3
        return combined_result, combined_debug


class IN_V_SUB(Metric):
    category = Inflection
    name_en = "Verb forms in the subjunctive"
    name_local = "Verbformen im Konjunktiv"

    def count(doc):
        debug = [token.text for token in doc if "Mood=Sub" in token.morph]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_PRES_SUB(Metric):
    category = Inflection
    name_en = "Verb forms in the present subjunctive"
    name_local = "Verbformen im Konjunktiv Präsens"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if "Mood=Sub" in token.morph and "Tense=Pres" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_PAST_SUB(Metric):
    category = Inflection
    name_en = "Verb forms in the past subjunctive"
    name_local = "Verbformen im Konjunktiv Imperfekt"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if "Mood=Sub" in token.morph and "Tense=Past" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_PERF_SUB(Metric):
    category = Inflection
    name_en = "Verb forms in the perfective subjunctive"
    name_local = "Verbformen im Konjunktiv Perfekt"

    def count(doc):
        result = 0
        debug = []

        for sent in doc.sents:
            aux = [
                token.text
                for token in sent
                if "Mood=Sub" in token.morph
                and "Tense=Pres" in token.morph
                and any(
                    child for child in token.children if "VerbForm=Part" in child.morph
                )
            ]

            partizip = [
                token.text
                for token in sent
                if token.pos_ in ["VERB", "AUX"]
                and "VerbForm=Part" in token.morph
                and token.dep_ == "oc"
            ]
            if aux and partizip:
                debug.append(aux + partizip)
                result += len(aux) + len(partizip)

        return ratio(result, len(doc)), debug


class IN_V_PAST_SUB_PLUSQ(Metric):
    category = Inflection
    name_en = "Verb forms in the past subjunctive (Plusquamperfekt)"
    name_local = "Verbformen im Konjunktiv Plusquamperfekt"

    def count(doc):
        result = 0
        debug = []

        for sent in doc.sents:
            aux = [
                token
                for token in sent
                if token.text.lower()
                in [
                    "hätte",
                    "hättest",
                    "hätten",
                    "hättet",
                    "hätten",
                    "wäre",
                    "wärest",
                    "wären",
                    "wäret",
                    "wären",
                ]
                and any(
                    child
                    for child in token.children
                    if "VerbForm=Part" in child.morph or "VerbForm=Inf" in child.morph
                )
            ]

            partizip = [
                token.text
                for token in sent
                if "VerbForm=Part" in token.morph and token.dep_ == "oc"
            ]

            mod = [
                token
                for token in sent
                if token.text.lower()
                in ["müssen", "dürfen", "können", "wollen", "mögen", "sollen"]
                and any(
                    child.text == token.text
                    for aux_token in aux
                    for child in aux_token.children
                )
            ]

            inf = [
                token.text
                for token in sent
                if "VVINF" in token.tag_.split(":")
                and any(
                    child.text == token.text
                    for mod_token in mod
                    for child in mod_token.children
                )
            ]

            aux = [token.text for token in aux]
            mod = [token.text for token in mod]

            if (aux and partizip) or (aux and inf and mod):
                debug.append((aux + partizip + inf + mod))
                result += len(aux) + len(partizip) + len(inf) + len(mod)

        return ratio(result, len(doc)), debug


class IN_V_KOND1(Metric):
    category = Inflection
    name_en = "Verb forms in the conditional clause"
    name_local = "Verbformen im Konditional I"

    def count(doc):
        result = 0
        debug = []

        for sent in doc.sents:
            aux = [
                token
                for token in sent
                if token.text.lower()
                in ["würde", "würdest", "würden", "würdet", "würden"]
            ]

            inf_children_list = []  # Use a list to store all occurrences
            for aux_token in aux:
                inf_children_list.extend(
                    child.text
                    for child in aux_token.children
                    if "VerbForm=Inf" in child.morph
                )
            aux = [token.text for token in aux]
            if aux and inf_children_list:
                debug.append((aux, inf_children_list))
                result += len(aux) + len(inf_children_list)
        return ratio(result, len(doc)), debug


class IN_V_KOND2(Metric):
    category = Inflection
    name_en = "Verb forms in the conditional clause"
    name_local = "Verbformen im Konditional II"

    def count(doc):
        result = 0
        debug = []

        for sent in doc.sents:
            aux = [
                token.text
                for token in sent
                if token.text.lower()
                in ["würde", "würdest", "würden", "würdet", "würden"]
            ]

            partizip = [
                token.text
                for token in sent
                if token.pos_ in ["VERB", "AUX"]
                and "VerbForm=Part" in token.morph
                and token.dep_ == "oc"
            ]

            aux2 = [
                token.text for token in sent if token.text.lower() in ["haben", "sein"]
            ]

        if aux and partizip and aux2:
            debug.append((aux + partizip + aux2))
            result += len(aux) + len(partizip) + len(aux2)
        return ratio(result, len(doc)), debug


class IN_V_FUT1(Metric):
    category = Inflection
    name_en = "Verbs in future simple tense"
    name_local = "Verbformen im Futur I"

    def count(doc):
        result = 0
        debug = []

        for sent in doc.sents:
            aux = [
                token.text
                for token in sent
                if "Tense=Pres" in token.morph
                and token.text.lower() in ["werden", "werde", "wirst", "wird", "werdet"]
                and not any(
                    child for child in token.children if "VerbForm=Part" in child.morph
                )
            ]

            inf = [
                token.text
                for token in sent
                if token.pos_ == "VERB"
                and "VerbForm=Inf" in token.morph
                and token.dep_ in ["oc", "cj"]
            ]

            if aux and inf:
                debug.append((aux, inf))
                result += len(aux) + len(inf)

        return ratio(result, len(doc)), debug


class IN_V_FUT2(Metric):
    category = Inflection
    name_en = "Verbs in future perfect tense"
    name_local = "Verbformen im Futur II"

    def count(doc):
        result = 0
        debug = []

        for sent in doc.sents:
            aux = [
                token.text
                for token in sent
                if "Tense=Pres" in token.morph
                and token.text.lower() in ["werden", "werde", "wirst", "wird", "werdet"]
                and any(
                    child
                    for child in token.children
                    if child.text.lower() in ["haben", "sein"]
                )
            ]

            partizip = [
                token.text
                for token in sent
                if token.pos_ == "VERB"
                and "VerbForm=Part" in token.morph
                and token.dep_ in ["oc", "cj"]
            ]

            aux2 = [
                token.text
                for token in sent
                if token.text.lower() in ["haben", "sein"] and token.dep_ == "oc"
            ]

            if aux and partizip and aux2:
                debug.append((aux, partizip, aux2))
                result += len(aux) + len(partizip) + len(aux2)

        return ratio(result, len(doc)), debug


class IN_V_FUT(Metric):
    category = Inflection
    name_en = "Verbs in future tense"
    name_local = "Verbformen im Futur"

    def count(doc):
        result1, debug1 = IN_V_FUT1.count(doc)
        result2, debug2 = IN_V_FUT2.count(doc)
        combined_result = result1 + result2
        combined_debug = debug1 + debug2
        return combined_result, combined_debug


class IN_V_PASS(Metric):
    category = Inflection
    name_en = "Procesual passive verb forms"
    name_local = "Verbformen im Vorgangspassiv"

    def count(doc):
        result = 0
        debug = []

        for sent in doc.sents:
            aux_pres = [
                token.text
                for token in sent
                if "Tense=Pres" in token.morph and token.lemma_ == "werden"
            ]

            aux_past = [
                token.text
                for token in sent
                if "Tense=Past" in token.morph and token.lemma_ == "werden"
            ]

            aux_perfekt = [
                token.text
                for token in sent
                if "Tense=Pres" in token.morph and token.lemma_ == "sein"
            ]

            aux_plusq = [
                token.text
                for token in sent
                if "Tense=Past" in token.morph and token.lemma_ == "sein"
            ]

            partizip = [
                token.text
                for token in sent
                if token.pos_ == "VERB"
                and "VerbForm=Part" in token.morph
                and token.dep_ in ["oc", "cj"]
            ]

            worden = [token.text for token in sent if token.text.lower() == "worden"]

            futur_ii = any(
                any(
                    ("VerbForm=Part" in token.morph)
                    and (token.text.lower() in ["haben", "sein"])
                    for partizip_token in sent
                    if partizip_token.i == token.i - 1
                )
                for token in sent
            )

            if aux_pres and partizip and not futur_ii:
                debug.append((aux_pres, partizip))
                result += len(aux_pres) + len(partizip)
            elif aux_past and partizip and not futur_ii:
                debug.append((aux_past, partizip))
                result += len(aux_past) + len(partizip)
            elif aux_perfekt and partizip and worden and not futur_ii:
                debug.append((aux_perfekt, partizip, worden))
                result += len(aux_perfekt) + len(partizip) + len(worden)
            elif aux_plusq and partizip and worden and not futur_ii:
                debug.append((aux_plusq, partizip, worden))
                result += len(aux_plusq) + len(partizip) + len(worden)

        return ratio(result, len(doc)), debug


class IN_V_PASS_MOD(Metric):
    category = Inflection
    name_en = "Passive voice with modal verbs"
    name_local = "Passiv mit Modalverben"

    def count(doc):
        result = 0
        debug = []

        for sent in doc.sents:

            aux_perfekt = [
                token.text
                for token in sent
                if "Tense=Pres" in token.morph and token.lemma_ == "haben"
            ]

            aux_pres = [
                token.text
                for token in sent
                if "Tense=Pres" in token.morph
                and token.lemma_
                in [
                    "müssen",
                    "mussen",
                    "muss",
                    "musste",
                    "dürfen",
                    "sollen",
                    "wollen",
                    "möchten",
                    "können",
                    "mögen",
                ]
                and not any(
                    child
                    for child in token.children
                    if child.pos_ == "VERB" and "VerbForm=Inf" in child.morph
                )
            ]

            aux_past = [
                token.text
                for token in sent
                if "Tense=Past" in token.morph
                and token.lemma_
                in [
                    "müssen",
                    "mussen",
                    "muss",
                    "musste",
                    "dürfen",
                    "sollen",
                    "wollen",
                    "möchten",
                    "können",
                    "mögen",
                ]
                and not any(
                    child
                    for child in token.children
                    if child.pos_ == "VERB" and "VerbForm=Inf" in child.morph
                )
            ]

            aux_inf = [
                token.text
                for token in sent
                if "VerbForm=Inf" in token.morph
                and token.lemma_
                in [
                    "müssen",
                    "dürfen",
                    "mussen",
                    "muss",
                    "sollen",
                    "wollen",
                    "möchten",
                    "können",
                    "mögen",
                ]
            ]

            partizip = [
                token.text
                for token in sent
                if token.pos_ == "VERB"
                and "VerbForm=Part" in token.morph
                and token.dep_ in ["oc", "cj"]
            ]

            werden = [
                token.text
                for token in sent
                if token.text.lower() == "werden"
                # and token.head.text in aux_pres
            ]

            if aux_pres and partizip and werden:
                debug.append((aux_pres, partizip, werden))
                result += len(aux_pres) + len(partizip) + len(werden)
            elif aux_past and partizip and werden:
                debug.append((aux_past, partizip, werden))
                result += len(aux_past) + len(partizip) + len(werden)
            elif aux_perfekt and aux_inf and partizip and werden:
                debug.append((aux_perfekt, aux_inf, partizip, werden))
                result += len(aux_perfekt) + len(aux_inf) + len(partizip) + len(werden)

        return ratio(result, len(doc)), debug
