import re
from collections import Counter

from ...structures import Category, Metric
from ...utils import ratio
from .data.dictionaries import (
    adv_dur,
    adv_freq,
    adv_phrases,
    adv_temp,
    errors,
    exceptions,
    intensifiers,
    vulgarisms,
)


class Lexical(Category):
    lang = "pl"
    name_en = "Lexical"
    name_local = "Leksykalne"


class L_NAME(Metric):
    category = Lexical
    name_en = "Proper names"
    name_local = "Nazwy własne"

    def count(doc):
        debug = [token.text for token in doc if token.pos_ == "PROPN"]
        result = len(debug)
        return ratio(result, len(doc)), debug


class L_NAME_M(Metric):
    category = Lexical
    name_en = "Masculine proper nouns"
    name_local = "Nazwy własne w rodzaju męskim"

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
    name_local = "Nazwy własne w rodzaju żeńskim"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ == "PROPN" and "Gender=Fem" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class L_NAME_ENT(Metric):
    category = Lexical
    name_en = "Named entities"
    name_local = "Jednostki nazewnicze"

    def count(doc):
        debug = [token.text for token in doc if token.ent_type_ != ""]
        result = len(debug)
        return ratio(result, len(doc)), debug


class L_PLACEN_GEOG(Metric):
    category = Lexical
    name_en = "Place and geographical names"
    name_local = "Nazwy miejsc i nazwy geograficzne"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.ent_type_ in ["PLACENAME", "GEOGNAME"]
            and token.pos_ == "PROPN"
            and "Animacy=Hum" not in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class L_PERSN(Metric):
    category = Lexical
    name_en = "Person names"
    name_local = "Nazwy osób"

    def count(doc):
        debug = [token.text for token in doc if token.ent_type_ == "PERSNAME"]
        result = len(debug)
        return ratio(result, len(doc)), debug


class L_PERSN_M(Metric):
    category = Lexical
    name_en = "Masculine person names"
    name_local = "Nazwy osób w rodzaju męskim"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.ent_type_ == "PERSNAME" and "Gender=Masc" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class L_PERSN_F(Metric):
    category = Lexical
    name_en = "Feminine person names"
    name_local = "Nazwy osób w rodzaju żeńskim"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.ent_type_ == "PERSNAME" and "Gender=Fem" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class L_ORGN(Metric):
    category = Lexical
    name_en = "Organization names"
    name_local = "Nazwy organizacji"

    def count(doc):
        debug = [token.text for token in doc if token.ent_type_ == "ORGNAME"]
        result = len(debug)
        return ratio(result, len(doc)), debug


class L_ETHN(Metric):
    category = Lexical
    name_en = "Ethnonyms and demonyms"
    name_local = "Etnonimy i demonimy"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.ent_type_ in ["GEOGNAME", "PLACENAME"]
            and "Animacy=Hum" in token.morph
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class L_GEOG_ADJ(Metric):
    category = Lexical
    name_en = "Adjectives derived from geographical names"
    name_local = "Przymiotniki wywodzące się od nazw geograficznych"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ == "ADJ" and token.ent_type_ in ["GEOGNAME", "PLACENAME"]
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class L_DATE(Metric):
    category = Lexical
    name_en = "Dates"
    name_local = "Daty"

    def count(doc):
        debug = [token.text for token in doc if token.ent_type_ == "DATE"]
        result = len(debug)
        return ratio(result, len(doc)), debug


class L_VULG(Metric):
    category = Lexical
    name_en = "Vulgarisms"
    name_local = "Wulgaryzmy"

    def count(doc):
        debug = [
            token.text.lower() for token in doc if token.text.lower() in vulgarisms
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class L_INTENSIF(Metric):
    category = Lexical
    name_en = "Degree modifiers of Greek origin"
    name_local = "Modyfikatory natężenia cechy pochodzenia greckiego"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.lemma_.lower() in intensifiers
            or any(
                prefix
                for prefix in intensifiers
                if token.text.lower().startswith(prefix)
            )
            and not token.lemma_ in exceptions
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class L_ERROR(Metric):
    category = Lexical
    name_en = "Common linguistic errors"
    name_local = "Częste błędy językowe"

    def count(doc):
        words = [token.text.lower() for token in doc]
        debug = []
        total_matched_words = 0
        current_phrase = []

        sorted_phrases = sorted(errors, key=lambda x: len(x.split()), reverse=True)

        for entry in sorted_phrases:
            entry = entry.lower()
            if " " in entry:
                phrase_tokens = entry.split()
                text = doc.text.lower()
                text = re.sub("[!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~]", "", text)
                text = " " + text + " "
                if (
                    entry in text
                    and text[text.find(entry) - 1] == " "
                    and text[text.find(entry) + len(entry)] == " "
                ):
                    if all(token in text for token in phrase_tokens):
                        is_contained = any(phrase in debug for phrase in phrase_tokens)
                        if not is_contained:
                            is_partial_contained = any(
                                phrase in " ".join(debug) for phrase in phrase_tokens
                            )
                            if not is_partial_contained:
                                debug.append(" ".join(phrase_tokens))
                                total_matched_words += len(phrase_tokens)
            elif entry in words:
                debug.append(entry)
                total_matched_words += 1

        return ratio(total_matched_words, len(words)), debug


class L_ADVPHR(Metric):
    category = Lexical
    name_en = "Adverbial phrases"
    name_local = "Frazy przysłówkowe"

    def count(doc):
        words = [token.text.lower() for token in doc]
        debug = []
        total_matched_words = 0
        current_phrase = []

        sorted_phrases = sorted(adv_phrases, key=lambda x: len(x.split()), reverse=True)

        for entry in sorted_phrases:
            entry = entry.lower()
            if " " in entry:
                phrase_tokens = entry.split()
                text = doc.text.lower()
                text = re.sub("[!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~]", "", text)
                text = " " + text + " "
                if (
                    entry in text
                    and text[text.find(entry) - 1] == " "
                    and text[text.find(entry) + len(entry)] == " "
                ):
                    if all(token in text for token in phrase_tokens):
                        is_contained = any(phrase in debug for phrase in phrase_tokens)
                        if not is_contained:
                            is_partial_contained = any(
                                phrase in " ".join(debug) for phrase in phrase_tokens
                            )
                            if not is_partial_contained:
                                debug.append(" ".join(phrase_tokens))
                                total_matched_words += len(phrase_tokens)
            elif entry in words:
                debug.append(entry)
                total_matched_words += 1

        return ratio(total_matched_words, len(words)), debug


class L_ADV_TEMP(Metric):
    category = Lexical
    name_en = "Adverbs of time"
    name_local = "Przysłówki temporalne"

    def count(doc):
        debug = [token.text for token in doc if token.text.lower() in adv_temp]
        result = len(debug)
        return ratio(result, len(doc)), debug


class L_ADV_DUR(Metric):
    category = Lexical
    name_en = "Adverbs of duration"
    name_local = "Przysłówki duratywne"

    def count(doc):
        words = [token.text.lower() for token in doc]
        debug = []
        total_matched_words = 0
        current_phrase = []

        for entry in adv_dur:
            entry = entry.lower()
            if " " in entry:
                phrase_tokens = entry.split()
                text = doc.text.lower()
                text = re.sub("[!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~]", "", text)
                text = " " + text + " "
                if (
                    entry in text
                    and text[text.find(entry) - 1] == " "
                    and text[text.find(entry) + len(entry)] == " "
                ):
                    debug.append(" ".join(phrase_tokens))
                    total_matched_words += len(phrase_tokens)
            elif entry in words:
                debug.append(entry)
                total_matched_words += 1

        return ratio(total_matched_words, len(words)), debug


class L_ADV_FREQ(Metric):
    category = Lexical
    name_en = "Adverbs of frequency"
    name_local = "Przysłówki częstotliwości"

    def count(doc):
        words = [token.text.lower() for token in doc]
        debug = []
        total_matched_words = 0
        current_phrase = []

        for entry in adv_freq:
            entry = entry.lower()
            if " " in entry:
                phrase_tokens = entry.split()
                text = doc.text.lower()
                text = re.sub("[!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~]", "", text)
                text = " " + text + " "
                if (
                    entry in text
                    and text[text.find(entry) - 1] == " "
                    and text[text.find(entry) + len(entry)] == " "
                ):
                    debug.append(" ".join(phrase_tokens))
                    total_matched_words += len(phrase_tokens)
            elif entry in words:
                debug.append(entry)
                total_matched_words += 1

        return ratio(total_matched_words, len(words)), debug


class L_SYL_G1(Metric):
    category = Lexical
    name_en = "One-syllable words"
    name_local = "Wyrazy jednosylabowe"

    def count(doc):
        debug = [token.text for token in doc if token._.syllables_count == 1]
        result = len(debug)
        return ratio(result, len(doc)), debug


class L_SYL_G2(Metric):
    category = Lexical
    name_en = "Two-syllables words"
    name_local = "Wyrazy dwusylabowe"

    def count(doc):
        debug = [token.text for token in doc if token._.syllables_count == 2]
        result = len(debug)
        return ratio(result, len(doc)), debug


class L_SYL_G3(Metric):
    category = Lexical
    name_en = "Three-syllables words"
    name_local = "Wyrazy trójsylabowe"

    def count(doc):
        debug = [token.text for token in doc if token._.syllables_count == 3]
        result = len(debug)
        return ratio(result, len(doc)), debug


class L_SYL_G4(Metric):
    category = Lexical
    name_en = "Words formed of 4 or more syllables"
    name_local = "Wyrazy o liczbie sylab większej niż 3"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token._.syllables_count is not None and token._.syllables_count > 3
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class L_TTR_IA(Metric):
    category = Lexical
    name_en = "Type-token ratio for non-lemmatized tokens"
    name_local = "Type-token ratio dla wyrazów w odmianach"

    def count(doc):
        debug = set([token.text.lower() for token in doc if token.is_punct == False])

        return ratio(len(debug), len(doc)), debug


class L_TTR_LA(Metric):
    category = Lexical
    name_en = "Type-token ratio for lemmatized tokens"
    name_local = "Type-token ratio dla wyrazów zlematyzowanych"

    def count(doc):
        debug = set([token.lemma_.lower() for token in doc if token.is_punct == False])

        return ratio(len(debug), len(doc)), debug


class L_CONT_A(Metric):
    category = Lexical
    name_en = "Incidence of content words"
    name_local = "Wyrazy samodzielne"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if any(
                tag in token.tag_.split(":")
                for tag in [
                    "fin",
                    "bedzie",
                    "praet",
                    "impt",
                    "imps",
                    "inf",
                    "pcon",
                    "pant",
                    "pact",
                    "ppas",
                    "winien",
                    "pred",
                    "subst",
                    "depr",
                    "ger",
                    "adj",
                    "adja",
                    "adjp",
                    "adjc",
                    "adv",
                    "num",
                    "numcol",
                    "ppron12",
                    "ppron3",
                    "siebie",
                ]
            )
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class L_CONT_T(Metric):
    category = Lexical
    name_en = "Content words types"
    name_local = "Typy wyrazów samodzielnych"

    def count(doc):
        debug = set(
            token.text
            for token in doc
            if any(
                tag in token.tag_.split(":")
                for tag in [
                    "fin",
                    "bedzie",
                    "praet",
                    "impt",
                    "imps",
                    "inf",
                    "pcon",
                    "pant",
                    "pact",
                    "ppas",
                    "winien",
                    "pred",
                    "subst",
                    "depr",
                    "ger",
                    "adj",
                    "adja",
                    "adjp",
                    "adjc",
                    "adv",
                    "num",
                    "numcol",
                    "ppron12",
                    "ppron3",
                    "siebie",
                ]
            )
        )
        result = len(debug)
        return ratio(result, len(doc)), debug


class L_CONT_L(Metric):
    category = Lexical
    name_en = "Content words lemma types"
    name_local = "Typy lemm wyrazów samodzielnych"

    def count(doc):
        debug = set(
            token.lemma_
            for token in doc
            if any(
                tag in token.tag_.split(":")
                for tag in [
                    "fin",
                    "bedzie",
                    "praet",
                    "impt",
                    "imps",
                    "inf",
                    "pcon",
                    "pant",
                    "pact",
                    "ppas",
                    "winien",
                    "pred",
                    "subst",
                    "depr",
                    "ger",
                    "adj",
                    "adja",
                    "adjp",
                    "adjc",
                    "adv",
                    "num",
                    "numcol",
                    "ppron12",
                    "ppron3",
                    "siebie",
                ]
            )
        )
        result = len(debug)
        return ratio(result, len(doc)), debug


class L_FUNC_A(Metric):
    category = Lexical
    name_en = "Incidence of function words"
    name_local = "Słowa funkcyjne"

    def count(doc):
        debug = [
            token.text
            for token in doc
            if any(
                tag in token.tag_.split(":")
                for tag in ["part", "brev", "prep", "conj", "comp", "interj"]
            )
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class L_FUNC_T(Metric):
    category = Lexical
    name_en = "Function words types"
    name_local = "Typy wyrazow funkcyjnych"

    def count(doc):
        debug = set(
            token.text
            for token in doc
            if any(
                tag in token.tag_.split(":")
                for tag in ["part", "brev", "prep", "conj", "comp", "interj"]
            )
        )
        result = len(debug)
        return ratio(result, len(doc)), debug


class L_FUNC_L(Metric):
    category = Lexical
    name_en = "Function words lemma types"
    name_local = "Typy lemm wyrazow funkcyjnych"

    def count(doc):
        debug = set(
            token.lemma_
            for token in doc
            if any(
                tag in token.tag_.split(":")
                for tag in ["part", "brev", "prep", "conj", "comp", "interj"]
            )
        )
        result = len(debug)
        return ratio(result, len(doc)), debug


class L_STOP(Metric):
    category = Lexical
    name_en = "Incidence of stop words"
    name_local = "Wyrazy ze stoplisty"

    def count(doc):
        debug = [token.text for token in doc if token.is_stop]
        result = len(debug)
        return ratio(result, len(doc)), debug


class L_TCCT1(Metric):
    category = Lexical
    name_en = "Tokens covering 1% of most common types"
    name_local = "Wyrazy wchodzące w skład 1% najczęstszych typów"

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
    name_local = "Wyrazy wchodzące w skład 5% najczęstszych typów"

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
