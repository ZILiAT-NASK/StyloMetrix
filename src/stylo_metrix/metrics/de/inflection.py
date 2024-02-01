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
            and str(token.morph.get("Number")) == "['Sing']"
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
            if token.pos_ in ["NOUN", "PROPN"]
            and str(token.morph.get("Number")) == "['Plur']"
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
            and str(token.morph.get("Gender")) == "['Masc']"
            and str(token.morph.get("Number")) == "['Sing']"
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
            and str(token.morph.get("Gender")) == "['Fem']"
            and str(token.morph.get("Number")) == "['Sing']"
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
            and str(token.morph.get("Gender")) == "['Neut']"
            and str(token.morph.get("Number")) == "['Sing']"
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
            and str(token.morph.get("Gender")) == "['Masc']"
            and str(token.morph.get("Number")) == "['Plur']"
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
            and str(token.morph.get("Gender")) == "['Fem']"
            and str(token.morph.get("Number")) == "['Plur']"
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
            and str(token.morph.get("Gender")) == "['Neut']"
            and str(token.morph.get("Number")) == "['Plur']"
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
            if token.pos_ in ["NOUN", "PROPN"]
            and str(token.morph.get("Case")) == "['Nom']"
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
            if token.pos_ in ["NOUN", "PROPN"]
            and str(token.morph.get("Case")) == "['Gen']"
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
            if token.pos_ in ["NOUN", "PROPN"]
            and str(token.morph.get("Case")) == "['Dat']"
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
            if token.pos_ in ["NOUN", "PROPN"]
            and str(token.morph.get("Case")) == "['Acc']"
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
            and str(token.morph.get("Degree")) == "['Pos']"
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
            if token.pos_ in ["ADJ"] and str(token.morph.get("Degree")) == "['Cmp']"
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
            if token.pos_ in ["ADJ"] and str(token.morph.get("Degree")) == "['Sup']"
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
            if token.pos_ in ["ADV"] and str(token.morph.get("Degree")) == "['Pos']"
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
            if token.pos_ in ["ADV"] and str(token.morph.get("Degree")) == "['Cmp']"
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
            if token.pos_ in ["ADV"] and str(token.morph.get("Degree")) == "['Sup']"
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
            and str(token.morph.get("Number")) == "['Sing']"
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
            and str(token.morph.get("Number")) == "['Plur']"
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
            and str(token.morph.get("Case")) == "['Nom']"
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
            and str(token.morph.get("Case")) == "['Gen']"
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
            and str(token.morph.get("Case")) == "['Dat']"
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
            and str(token.morph.get("Case")) == "['Acc']"
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
            and str(token.morph.get("Person")) == "['1']"
            and str(token.morph.get("Number")) == "['Sing']"
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
            and str(token.morph.get("Person")) == "['2']"
            and str(token.morph.get("Number")) == "['Sing']"
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
            and str(token.morph.get("Person")) == "['3']"
            and str(token.morph.get("Number")) == "['Sing']"
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
            and str(token.morph.get("Person")) == "['1']"
            and str(token.morph.get("Number")) == "['Plur']"
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
            and str(token.morph.get("Person")) == "['2']"
            and str(token.morph.get("Number")) == "['Plur']"
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
            and str(token.morph.get("Person")) == "['3']"
            and str(token.morph.get("Number")) == "['Plur']"
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
            if "ART" in token.tag_.split(":")
            and str(token.morph.get("Number")) == "['Sing']"
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
            if "ART" in token.tag_.split(":")
            and str(token.morph.get("Number")) == "['Plur']"
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
            if str(token.morph.get("Definite")) == "['Def']"
            and str(token.morph.get("Number")) == "['Sing']"
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
            if str(token.morph.get("Definite")) == "['Def']"
            and str(token.morph.get("Number")) == "['Plur']"
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
            if str(token.morph.get("Definite")) == "['Ind']"
            and str(token.morph.get("Number")) == "['Sing']"
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
            if "ART" in token.tag_.split(":")
            and str(token.morph.get("Gender")) == "['Masc']"
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
            if "ART" in token.tag_.split(":")
            and str(token.morph.get("Gender")) == "['Fem']"
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
            if "ART" in token.tag_.split(":")
            and str(token.morph.get("Gender")) == "['Neut']"
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
            if "ART" in token.tag_.split(":")
            and str(token.morph.get("Case")) == "['Nom']"
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
            if "ART" in token.tag_.split(":")
            and str(token.morph.get("Case")) == "['Gen']"
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
            if "ART" in token.tag_.split(":")
            and str(token.morph.get("Case")) == "['Dat']"
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
            if "ART" in token.tag_.split(":")
            and str(token.morph.get("Case")) == "['Acc']"
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
            if str(token.morph.get("Definite")) == "['Def']"
            and str(token.morph.get("Case")) == "['Nom']"
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
            if str(token.morph.get("Definite")) == "['Def']"
            and str(token.morph.get("Case")) == "['Gen']"
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
            if str(token.morph.get("Definite")) == "['Def']"
            and str(token.morph.get("Case")) == "['Dat']"
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
            if str(token.morph.get("Definite")) == "['Def']"
            and str(token.morph.get("Case")) == "['Acc']"
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
            if str(token.morph.get("Definite")) == "['Ind']"
            and str(token.morph.get("Case")) == "['Nom']"
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
            if str(token.morph.get("Definite")) == "['Ind']"
            and str(token.morph.get("Case")) == "['Gen']"
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
            if str(token.morph.get("Definite")) == "['Ind']"
            and str(token.morph.get("Case")) == "['Dat']"
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
            if str(token.morph.get("Definite")) == "['Ind']"
            and str(token.morph.get("Case")) == "['Acc']"
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_FIN(Metric):
    category = Inflection
    name_en = "Finite verbs"
    name_local = "Finite Verben"

    def count(doc):
        debug = [
            token.text for token in doc if str(token.morph.get("VerbForm")) == "['Fin']"
        ]
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
    name_local = "Infinite Verbformen"

    def count(doc):
        debug = [
            token.text for token in doc if str(token.morph.get("VerbForm")) == "['Inf']"
        ]
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
        debug = [
            token.text for token in doc if str(token.morph.get("Tense")) == "['Pres']"
        ]
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
            and str(token.morph.get("Person")) == "['1']"
            and str(token.morph.get("Number")) == "['Sing']"
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
            and str(token.morph.get("Person")) == "['2']"
            and str(token.morph.get("Number")) == "['Sing']"
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
            and str(token.morph.get("Person")) == "['3']"
            and str(token.morph.get("Number")) == "['Sing']"
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
            and str(token.morph.get("Person")) == "['1']"
            and str(token.morph.get("Number")) == "['Plur']"
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
            and str(token.morph.get("Person")) == "['2']"
            and str(token.morph.get("Number")) == "['Plur']"
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
            and str(token.morph.get("Person")) == "['3']"
            and str(token.morph.get("Number")) == "['Plur']"
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_PAST(Metric):
    category = Inflection
    name_en = "Verbs in past tense"
    name_local = "Verben in der Vergangenheitsform"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if (
                str(token.morph.get("Tense")) == "['Past']"
                and str(token.morph.get("Mood")) != "['Sub']"
            )
            or "VVPP" in token.tag_.split(":")
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
            and str(token.morph.get("Tense")) == "['Past']"
            and str(token.morph.get("Mood")) != "['Sub']"
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
            and str(token.morph.get("Tense")) == "['Past']"
            and str(token.morph.get("Mood")) != "['Sub']"
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
            and str(token.morph.get("Mood")) != "['Sub']"
            and str(token.morph.get("Tense")) == "['Past']"
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
            if str(token.morph.get("Tense")) == "['Past']"
            and "VMFIN" in token.tag_.split(":")
        ]
        result = len(debug)
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
                and str(token.morph.get("Tense")) == "['Past']"
                and token.lemma_ in ["haben", "sein"]
            ]

            partizip = [
                token.text
                for token in sent
                if token.pos_ in ["VERB", "AUX"]
                and str(token.morph.get("VerbForm")) == "['Part']"
                and token.dep_ == "oc"
            ]

            if aux and partizip:
                debug.append((aux, partizip))
                result += len(aux) + len(partizip)

        return ratio(result, len(doc)), debug


class IN_V_SUB(Metric):
    category = Inflection
    name_en = "Verb forms in the subjunctive"
    name_local = "Verbformen im Konjunktiv"

    def count(doc):
        debug = [
            token.text for token in doc if str(token.morph.get("Mood")) == "['Sub']"
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_PRES_SUB(Metric):
    category = Inflection
    name_en = "Verb forms in the present subjunctive"
    name_local = "Verbformen im Konjunktiv I"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if str(token.morph.get("Mood")) == "['Sub']"
            and str(token.morph.get("Tense")) == "['Pres']"
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class IN_V_PAST_SUB(Metric):
    category = Inflection
    name_en = "Verb forms in the past subjunctive"
    name_local = "Verbformen im Konjunktiv II"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if str(token.morph.get("Mood")) == "['Sub']"
            and str(token.morph.get("Tense")) == "['Past']"
        ]
        result = len(debug)
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
                token.text
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
            ]

            partizip = [
                token.text
                for token in sent
                if token.pos_ in ["VERB", "AUX"]
                and str(token.morph.get("VerbForm")) == "['Part']"
                and token.dep_ == "oc"
            ]

            inf = [
                token.text
                for token in sent
                if str(token.morph.get("VerbForm")) == "['Inf']"
            ]

            mod = [
                token.text
                for token in sent
                if token.pos_ == "AUX" and "VMFIN" in token.tag_.split(":")
            ]

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
                token.text
                for token in sent
                if token.text.lower()
                in ["würde", "würdest", "würden", "würdet", "würden"]
            ]

            inf = [
                token.text
                for token in sent
                if str(token.morph.get("VerbForm")) == "['Inf']"
            ]

        if aux and inf:
            debug.append((aux + inf))
            result += len(aux) + len(inf)
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
                and str(token.morph.get("VerbForm")) == "['Part']"
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
                if str(token.morph.get("Tense")) == "['Pres']"
                and token.lemma_ == "werden"
            ]

            inf = [
                token.text
                for token in sent
                if token.pos_ == "VERB"
                and str(token.morph.get("VerbForm")) == "['Inf']"
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
                if str(token.morph.get("Tense")) == "['Pres']"
                and token.lemma_ == "werden"
            ]

            inf = [
                token.text
                for token in sent
                if token.pos_ == "VERB"
                and str(token.morph.get("VerbForm")) == "['Part']"
                and token.dep_ in ["oc", "cj"]
            ]

            aux2 = [
                token.text for token in sent if token.text.lower() in ["haben", "sein"]
            ]

            if aux and inf and aux2:
                debug.append((aux, inf, aux2))
                result += len(aux) + len(inf) + len(aux2)

        return ratio(result, len(doc)), debug


class IN_V_PASS(Metric):
    category = Inflection
    name_en = "Procesual passive verb forms"
    name_local = "Verbformen im Vorgangspassiv"

    def count(doc):
        result = 0
        debug = []

        for sent in doc.sents:
            aux = [
                token.text
                for token in sent
                if str(token.morph.get("Tense")) in ["['Past']", "['Pres']"]
                and token.lemma_ == "werden"
            ]

            aux_perfekt = [
                token.text
                for token in sent
                if str(token.morph.get("Tense")) == "['Pres']"
                and token.lemma_ == "sein"
            ]

            aux_plusq = [
                token.text
                for token in sent
                if str(token.morph.get("Tense")) == "['Past']"
                and token.lemma_ == "sein"
            ]

            partizip = [
                token.text
                for token in sent
                if token.pos_ == "VERB"
                and str(token.morph.get("VerbForm")) == "['Part']"
                and token.dep_ in ["oc", "cj"]
            ]

            worden = [token.text for token in sent if token.text.lower() == "worden"]

            futur_ii = any(
                any(
                    (str(partizip_token.morph.get("VerbForm")) == "['Part']")
                    and (token.text.lower() in ["haben", "sein"])
                    for partizip_token in sent
                    if partizip_token.i == token.i - 1
                )
                for token in sent
            )

            if (
                (aux and partizip and not futur_ii)
                or (aux_perfekt and partizip and worden and not futur_ii)
                or (aux_plusq and partizip and worden and not futur_ii)
            ):
                debug.append((aux + aux_perfekt + aux_plusq, partizip, worden))
                result += (
                    len(aux)
                    + len(aux_perfekt)
                    + len(aux_plusq)
                    + len(partizip)
                    + len(worden)
                )

        return ratio(result, len(doc)), debug


class IN_V_SPASS(Metric):
    category = Inflection
    name_en = "Stative passive verb forms"
    name_local = "Verbformen im Zustandspassiv"

    def count(doc):
        result = 0
        debug = []

        for sent in doc.sents:
            aux = [
                token.text
                for token in sent
                if str(token.morph.get("Tense")) == "['Pres']"
                and token.lemma_ == "sein"
            ]

            partizip = [
                token.text
                for token in sent
                if token.pos_ == "VERB"
                and str(token.morph.get("VerbForm")) == "['Part']"
                and token.dep_ in ["oc", "pd"]
            ]

            if aux and partizip:
                debug.append((aux, partizip))
                result += len(aux) + len(partizip)

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
                if token.lemma_ == "haben"
                and str(token.morph.get("Tense")) == "['Pres']"
            ]

            aux = [
                token.text
                for token in sent
                if str(token.morph.get("Tense")) in ["['Pres']", "['Past']"]
                and token.lemma_
                in [
                    "müssen",
                    "mussen",
                    "muss" "dürfen",
                    "sollen",
                    "wollen",
                    "möchten",
                    "können",
                ]
            ]

            partizip = [
                token.text
                for token in sent
                if token.pos_ == "VERB"
                and str(token.morph.get("VerbForm")) == "['Part']"
                and token.dep_ in ["oc", "cj"]
            ]

            werden = [token.text for token in sent if token.text.lower() == "werden"]

            if (aux and partizip and werden) or (
                aux_perfekt and aux and partizip and werden
            ):
                debug.append((aux + aux_perfekt, partizip, werden))
                result += len(aux) + len(aux_perfekt) + len(partizip) + len(werden)

        return ratio(result, len(doc)), debug