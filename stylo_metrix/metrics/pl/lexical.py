from abc import ABC
from collections import Counter
from stylo_metrix.structures import Metric, MetricsGroup
from stylo_metrix.utils import incidence, ratio


class Lexical(Metric, ABC):
    category_pl = "Lexical"
    category_en = "Leksykalne"


# class L_TTR_LC(Lexical):
#     descript_on_en = "Lexical diversity, type-token ratio, content word lemmas"
#     description_pl = "Type-token ratio dla lemm wyrazów samodzielnych"
#
#     def count(self, doc):
#         types = set(token.lemma_ for token in doc._.content_words)
#         result = ratio(len(types), doc._.n_content_words)
#         return result, {}


class L_TTR_LA(Lexical):
    name_en = "Lexical diversity, type-token ratio, all words"
    name_pl = "Type-token ratio dla lemm"
    
    def count(self, doc):
        types = set(token.lemma_ for token in doc._.words)
        result = incidence(doc, types)
        return result, {}


# class L_TTR_IC(Lexical):
#     description_en = "Lexical diversity, type-token ratio, content words, inflected"
#     description_pl = "Type-token ratio dla odmienionych wyrazów samodzielnych"
#
#     def count(self, doc):
#         types = set(token.norm_ for token in doc._.content_words)
#         result = ratio(len(types), doc._.n_content_words)
#         return result, {}


class L_TTR_IA(Lexical):
    name_en = "Lexical diversity, type-token ratio, all words, inflected"
    name_pl = "Type-token ratio dla odmienionych"
    
    def count(self, doc):
        types = set(token.norm_ for token in doc._.words)
        result = incidence(doc, types)
        return result, {}


class L_CONT_A(Lexical):
    name_en = ""
    name_pl = "Występowanie wyrazów samodzielnych wśród"
    
    def count(self, doc):
        search = [token.text for token in doc._.words if token._.is_content_word]
        result = incidence(doc, search)
        return result, {}


class L_NCONT_A(Lexical):
    name_en = ""
    name_pl = "Występowanie wyrazów niesamodzielnych wśród"
    
    def count(self, doc):
        search = [token.text for token in doc._.words if not token._.is_content_word]
        result = incidence(doc, search)
        return result, {}


class L_CONT_T(Lexical):
    name_en = ""
    name_pl = "Występowanie typów wyrazów samodzielnych wśród"

    def count(self, doc):
        search = set(token.text for token in doc._.words if token._.is_content_word)
        result = incidence(doc, search)
        return result, {}


class L_NCONT_T(Lexical):
    name_en = ""
    name_pl = "Występowanie typów wyrazów niesamodzielnych wśród"

    def count(self, doc):
        search = set(token.text for token in doc._.words if not token._.is_content_word)
        result = incidence(doc, search)
        return result, {}


class L_CONT_L(Lexical):
    name_en = ""
    name_pl = "Występowanie lemm wyrazów samodzielnych wśród"

    def count(self, doc):
        search = set(token.lemma_ for token in doc._.words if token._.is_content_word)
        result = incidence(doc, search)
        return result, {}


# class L_REP_M(Lexical):
#     description_en = ""
#     description_pl = "Średnia liczba powtórzeń lemm"
#
#     def count(self, doc):
#         lemmas = [token.lemma_ for token in doc._.words]
#         counter = Counter(lemmas)
#         result = mean(counter.values())
#         return result, {}
#
#
# class L_REP_MC(Lexical):
#     description_en = ""
#     description_pl = "Średnia liczba powtórzeń lemm wyrazów samodzielnych"
#
#     def count(self, doc):
#         lemmas = [token.lemma_ for token in doc._.words if token._.is_content_word]
#         counter = Counter(lemmas)
#         result = mean(counter.values())
#         return result, {}
#
#
# class L_REP_MS(Lexical):
#     description_en = ""
#     description_pl = "Średnia liczba powtórzeń lemm wyrazów wyłączając stop words"
#
#     def count(self, doc):
#         lemmas = [token.lemma_ for token in doc._.words if not token.is_stop]
#         counter = Counter(lemmas)
#         result = mean(counter.values())
#         return result, {}
#
#
# class L_REP_SD(Lexical):
#     description_en = ""
#     description_pl = "Odchylenie standardowe liczb powtórzeń lemm"
#
#     def count(self, doc):
#         lemmas = [token.lemma_ for token in doc._.words]
#         counter = Counter(lemmas)
#         result = stdev(counter.values())
#         return result, {}
#
#
# class L_REP_SDC(Lexical):
#     description_en = ""
#     description_pl = "Odchylenie standardowe liczb powtórzeń lemm wyrazów samodzielnych"
#
#     def count(self, doc):
#         lemmas = [token.lemma_ for token in doc._.words if token._.is_content_word]
#         counter = Counter(lemmas)
#         result = stdev(counter.values())
#         return result, {}
#
#
# class L_REP_SDS(Lexical):
#     description_en = ""
#     description_pl = "Odchylenie standardowe liczb powtórzeń lemm wyrazów wyłączając stop words"
#
#     def count(self, doc):
#         lemmas = [token.lemma_ for token in doc._.words if not token.is_stop]
#         counter = Counter(lemmas)
#         result = stdev(counter.values())
#         return result, {}


class L_NAME(Lexical):
    name_en = ""
    name_pl = "Występowanie nazw własnych (liczba słów) wśród wszystkich słów"
    
    def count(self, doc):
        ents = [list(ent) for ent in doc.ents]
        sum_ents = sum(ents, [])
        result = incidence(doc, sum_ents)
        return result, {}


class L_PERSN(Lexical):
    name_en = ""
    name_pl = "Występowanie nazw osób wśród"
    
    def count(self, doc):
        ents = [list(ent) for ent in doc.ents if ent.label_ == 'persName']
        sum_ents = sum(ents, [])
        result = incidence(doc, sum_ents)
        return result, {}


class L_TCCT1(Lexical):
    name_en = "Percentage of tokens covering 1% of most common types"
    name_pl = "Procent wyrazów wchodzących w skład 1% najczęstszych typów (min. 1 typ)"

    def count(self, doc):
        counter = Counter([token.lemma_ for token in doc])
        ile_typow = len(counter)
        proc_typow = round(ile_typow * 0.01)
        if proc_typow == 0:
            proc_typow = 1
        suma_wystapien = sum([n for word, n in counter.most_common(proc_typow)])
        result = ratio(suma_wystapien, doc._.n_tokens)
        return result, {
            "[MOST COMMON TYPES]": counter.most_common(proc_typow)
        }


class L_TCCT5(Lexical):
    name_en = "Percentage of tokens covering 5% of most common types"
    name_pl = "Procent wyrazów wchodzących w skład 5% najczęstszych typów (min. 1 typ)"

    def count(self, doc):
        counter = Counter([token.lemma_ for token in doc])
        ile_typow = len(counter)
        proc_typow = round(ile_typow * 0.05)
        if proc_typow == 0:
            proc_typow = 1
        suma_wystapien = sum([n for word, n in counter.most_common(proc_typow)])
        result = ratio(suma_wystapien, doc._.n_tokens)
        return result, {
            "[MOST COMMON TYPES]": counter.most_common(proc_typow)
        }


class L_SYL_G3(Lexical):
    name_en = "Words formed of more than 3 syllables incidence"
    name_pl = "Procent wyrazów o liczbie sylab większej niż 3"

    def count(self, doc):
        lengths = [token._.syllables_count for token in doc if token._.syllables_count is not None]
        selected = [length for length in lengths if length > 3]
        result = incidence(doc, selected)
        return result, {}


# LEXICAL = [
#     L_TTR_LC,
#     L_TTR_LA,
#     L_TTR_IC,
#     L_TTR_IA,
#     L_CONT_A,
#     L_NCONT_A,
#     L_CONT_T,
#     L_NCONT_T,
#     L_CONT_L,
#     L_REP_M,
#     L_REP_MC,
#     L_REP_MS,
#     L_REP_SD,
#     L_REP_SDC,
#     L_REP_SDS,
#     L_NAME,
#     L_PERSN,
#     L_TCCT1,
#     L_TCCT5,
#     L_SYL_G3,
# ]

LEXICAL = [
    L_TTR_LA,
    L_TTR_IA,
    L_CONT_A,
    L_NCONT_A,
    L_CONT_T,
    L_NCONT_T,
    L_CONT_L,
    L_NAME,
    L_PERSN,
    L_TCCT1,
    L_TCCT5,
    L_SYL_G3,
]

lexical_group = MetricsGroup([m() for m in LEXICAL])
