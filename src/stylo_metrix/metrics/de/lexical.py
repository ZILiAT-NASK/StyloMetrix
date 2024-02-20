import re
from collections import Counter

from ...structures import Category, Metric
from ...utils import ratio


class Lexical(Category):
    lang = "de"
    name_en = "Lexical"
    name_local = "Lexikalische"


class L_NAME(Metric):
    category = Lexical
    name_en = "Proper names"
    name_local = "Eigennamen"

    def count(doc):
        debug = [token.text for token in doc if token.pos_ == "PROPN"]
        result = len(debug)
        return ratio(result, len(doc)), debug


class L_NAME_M(Metric):
    category = Lexical
    name_en = "Masculine proper nouns"
    name_local = "Männliche Eigennamen"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ == "PROPN" and "Gender=Masc" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class L_NAME_F(Metric):
    category = Lexical
    name_en = "Feminine proper nouns"
    name_local = "Weibliche Eigennamen"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ == "PROPN" and "Gender=Fem" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class L_GEOG(Metric):
    category = Lexical
    name_en = "Place and geographical names"
    name_local = "Nazwy miejsc i nazwy geograficzne"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.ent_type_ in ["LOC"] and token.pos_ == "PROPN"
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class L_ORG(Metric):
    category = Lexical
    name_en = "Organization names"
    name_local = "Organizationsnamen"

    def count(doc):
        debug = [token.text for token in doc if token.ent_type_ == "ORG"]
        result = len(debug)
        return ratio(result, len(doc)), debug


class L_SYL_G1(Metric):
    category = Lexical
    name_en = "One-syllable words"
    name_local = "Ein-Silben-Wörter"

    def count(doc):
        roman_pattern = r"^[IVXLCDM]+$"
        debug = [
            token.text
            for token in doc
            if token._.syllables_count == 1 and not re.match(roman_pattern, token.text)
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class L_SYL_G2(Metric):
    category = Lexical
    name_en = "Two-syllables words"
    name_local = "Zwei-Silben-Wörter"

    def count(doc):
        roman_pattern = r"^[IVXLCDM]+$"
        debug = [
            token.text
            for token in doc
            if token._.syllables_count == 2 and not re.match(roman_pattern, token.text)
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class L_SYL_G3(Metric):
    category = Lexical
    name_en = "Three-syllables words"
    name_local = "Drei-Silben-Wörter"

    def count(doc):
        roman_pattern = r"^[IVXLCDM]+$"
        debug = [
            token.text
            for token in doc
            if token._.syllables_count == 3 and not re.match(roman_pattern, token.text)
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class L_SYL_G4(Metric):
    category = Lexical
    name_en = "Four-syllables words"
    name_local = "Vier-Silben-Wörter"

    def count(doc):
        roman_pattern = r"^[IVXLCDM]+$"
        debug = [
            token.text
            for token in doc
            if token._.syllables_count == 4 and not re.match(roman_pattern, token.text)
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class L_SYL_G5(Metric):
    category = Lexical
    name_en = "Words formed of 5 or more syllables"
    name_local = "Wörter mit 5 oder mehr Silben"

    def count(doc):
        roman_pattern = r"^[IVXLCDM]+$"
        debug = [
            token.text
            for token in doc
            if token._.syllables_count is not None
            and token._.syllables_count > 4
            and not re.match(roman_pattern, token.text)
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class L_TTR_IA(Metric):
    category = Lexical
    name_en = "Type-token ratio for non-lemmatized tokens"
    name_local = "Type-token ratio für nicht-lemmatisierte Tokens"

    def count(doc):
        debug = set([token.text.lower() for token in doc if token.is_punct == False])
        result = len(debug)
        return ratio(result, len(doc)), debug


class L_TTR_LA(Metric):
    category = Lexical
    name_en = "Type-token ratio for lemmatized tokens"
    name_local = "Type-token ratio für lemmatisierte Tokens"

    def count(doc):
        debug = set([token.lemma_.lower() for token in doc if token.is_punct == False])
        result = len(debug)
        return ratio(result, len(doc)), debug


class L_CONT_A(Metric):
    category = Lexical
    name_en = "Incidence of content words"
    name_local = "Inhaltswörter"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if any(
                tag in token.tag_.split(":")
                for tag in [
                    "ADJA",
                    "ADJD",
                    "ADV",
                    "NN",
                    "NE",
                    "VVFIN",
                    "VVIMP",
                    "VVINF",
                    "VVIZU",
                    "VVPP",
                    "VAFIN",
                    "VAIMP",
                    "VAINF",
                    "VAPP",
                    "VMFIN",
                    "VMINF",
                    "VMPP",
                ]
            )
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class L_CONT_T(Metric):
    category = Lexical
    name_en = "Content words types"
    name_local = "Typen von Inhaltswörtern"

    def count(doc):
        debug = set(
            token.text
            for token in doc
            if any(
                tag in token.tag_.split(":")
                for tag in [
                    "ADJA",
                    "ADJD",
                    "ADV",
                    "NN",
                    "NE",
                    "VVFIN",
                    "VVIMP",
                    "VVINF",
                    "VVIZU",
                    "VVPP",
                    "VAFIN",
                    "VAIMP",
                    "VAINF",
                    "VAPP",
                    "VMFIN",
                    "VMINF",
                    "VMPP",
                ]
            )
        )
        result = len(debug)
        return ratio(result, len(doc)), debug


class L_CONT_L(Metric):
    category = Lexical
    name_en = "Content words lemma types"
    name_local = "Lemmatypen von Inhaltswörtern"

    def count(doc):
        debug = set(
            token.lemma_
            for token in doc
            if any(
                tag in token.tag_.split(":")
                for tag in [
                    "ADJA",
                    "ADJD",
                    "ADV",
                    "NN",
                    "NE",
                    "VVFIN",
                    "VVIMP",
                    "VVINF",
                    "VVIZU",
                    "VVPP",
                    "VAFIN",
                    "VAIMP",
                    "VAINF",
                    "VAPP",
                    "VMFIN",
                    "VMINF",
                    "VMPP",
                ]
            )
        )
        result = len(debug)
        return ratio(result, len(doc)), debug


class L_FUNC_A(Metric):
    category = Lexical
    name_en = "Incidence of function words"
    name_local = "Funktionswörter"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if any(
                tag in token.tag_.split(":")
                for tag in [
                    "APPR",
                    "APPRART",
                    "APPO",
                    "APZR",
                    "ART",
                    "CARD",
                    "ITJ",
                    "KOUI",
                    "KOUS",
                    "KON",
                    "KOKOM",
                    "PDS",
                    "PDAT",
                    "PIS",
                    "PIAT",
                    "PPER",
                    "PPOSS",
                    "PPOSAT",
                    "PAV",
                    "PROAV",
                    "FPTK",
                    "IPTK",
                    "MPTK",
                    "PRELS",
                    "PRF",
                    "PWS",
                    "PWAT",
                    "PROWAV",
                    "PTKZU",
                    "PTKNEG",
                    "PTKVZ",
                    "PTKA",
                    "TRUNC",
                ]
            )
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class L_FUNC_T(Metric):
    category = Lexical
    name_en = "Function words types"
    name_local = "Typen von Funktionswörtern"

    def count(doc):
        debug = set(
            token.text
            for token in doc
            if any(
                tag in token.tag_.split(":")
                for tag in [
                    "APPR",
                    "APPRART",
                    "APPO",
                    "APZR",
                    "ART",
                    "CARD",
                    "ITJ",
                    "KOUI",
                    "KOUS",
                    "KON",
                    "KOKOM",
                    "PDS",
                    "PDAT",
                    "PIS",
                    "PIAT",
                    "PPER",
                    "PPOSS",
                    "PPOSAT",
                    "PAV",
                    "PROAV",
                    "FPTK",
                    "IPTK",
                    "MPTK",
                    "PRELS",
                    "PRF",
                    "PWS",
                    "PWAT",
                    "PROWAV",
                    "PTKZU",
                    "PTKNEG",
                    "PTKVZ",
                    "PTKA",
                    "TRUNC",
                ]
            )
        )
        result = len(debug)
        return ratio(result, len(doc)), debug


class L_FUNC_L(Metric):
    category = Lexical
    name_en = "Function words lemma types"
    name_local = "Lemmatypen von Funktionswörtern"

    def count(doc):
        debug = set(
            token.lemma_
            for token in doc
            if any(
                tag in token.tag_.split(":")
                for tag in [
                    "APPR",
                    "APPRART",
                    "APPO",
                    "APZR",
                    "ART",
                    "CARD",
                    "ITJ",
                    "KOUI",
                    "KOUS",
                    "KON",
                    "KOKOM",
                    "PDS",
                    "PDAT",
                    "PIS",
                    "PIAT",
                    "PPER",
                    "PPOSS",
                    "PPOSAT",
                    "PAV",
                    "PROAV",
                    "FPTK",
                    "IPTK",
                    "MPTK",
                    "PRELS",
                    "PRF",
                    "PWS",
                    "PWAT",
                    "PROWAV",
                    "PTKZU",
                    "PTKNEG",
                    "PTKVZ",
                    "PTKA",
                    "TRUNC",
                ]
            )
        )
        result = len(debug)
        return ratio(result, len(doc)), debug


class L_STOP(Metric):
    category = Lexical
    name_en = "Incidence of stop words"
    name_local = "Stoppwörter"

    def count(doc):
        debug = [token.text for token in doc if token.is_stop]
        result = len(debug)
        return ratio(result, len(doc)), debug


class L_TCCT1(Metric):
    category = Lexical
    name_en = "Tokens covering 1% of most common types"
    name_local = "Tokens, die 1 % der häufigsten Typen abdecken"

    def count(doc):
        counter = Counter([token.lemma_ for token in doc if not token.is_punct])
        avail_types = len(counter)
        n_types = round(avail_types * 0.01)
        if n_types == 0:
            n_types = 1
        inc = sum([n for word, n in counter.most_common(n_types)])
        result = ratio(inc, len(doc))
        debug = [token for token, _ in counter.most_common(n_types)]
        return result, debug


class L_TCCT5(Metric):
    category = Lexical
    name_en = "Tokens covering 5% of most common types"
    name_local = "Tokens, die 5% der häufigsten Typen abdecken"

    def count(doc):
        counter = Counter([token.lemma_ for token in doc if not token.is_punct])
        avail_types = len(counter)
        n_types = round(avail_types * 0.05)
        if n_types == 0:
            n_types = 1
        inc = sum([n for word, n in counter.most_common(n_types)])
        result = ratio(inc, len(doc))
        debug = [token for token, _ in counter.most_common(n_types)]
        return result, debug
