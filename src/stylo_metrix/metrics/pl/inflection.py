# Copyright (C) 2022  NASK PIB
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from stylo_metrix.structures import Metric, Category

from stylo_metrix.utils import incidence, select, ratio


class Inflection(Category):
    lang = 'pl'
    name_en = "Inflection"
    name_local = "Fleksja"


class IN_V_INF(Metric):
    category = Inflection
    name_en = "Infinitives"
    name_local = "Czasowniki w bezokoliczniku"

    def count(doc):
        selection = select(doc, {'pos': 'v', 'verb_inflection': 'inf'})
        result = incidence(doc, selection)
        debug = {'TOKENS': selection}
        return result, debug


class IN_V_INFL(Metric):
    category = Inflection
    name_en = "Inflected verbs"
    name_local = "Czasowniki w formie osobowej"

    def count(doc):
        selection = select(doc, {'pos': 'v', 'verb_inflection': 'infl'})
        result = incidence(doc, selection)
        debug = {'TOKENS': selection}
        return result, debug
    

class IN_V_QUASI(Metric):
    category = Inflection
    name_en = "Quasi-verbs"
    name_local = "Quasi-czasowniki"

    def count(doc):
        quasi = list(token.text for token in doc if str(token.morph.get('VerbType')) =='[\'Quasi\']')
        result = ratio(len(quasi), doc._.n_tokens)
        debug = {'TOKENS': quasi}
        return result, debug


# VERBS_INFLECTION = [
#     IN_V_INF,
#     IN_V_INFL,
#     IN_V_QUASI,
# ]


class IN_V_1S(Metric):
    category = Inflection
    name_en = "First person singular verbs"
    name_local = "Czasowniki w 1. os. l. poj."

    def count(doc):
        selection = select(doc, {'pos': 'v', 'verb_person': 's1'})
        result = incidence(doc, selection)
        debug = {'TOKENS': selection}
        return result, debug


class IN_V_1P(Metric):
    category = Inflection
    name_en = "First person plural verbs"
    name_local = "Czasowniki w 1. os. l. mn."

    def count(doc):
        selection = select(doc, {'pos': 'v', 'verb_person': 'p1'})
        result = incidence(doc, selection)
        debug = {'TOKENS': selection}
        return result, debug


class IN_V_2S(Metric):
    category = Inflection
    name_en = "Second person singular verbs"
    name_local = "Czasowniki w 2. os. l. poj."

    def count(doc):
        selection = select(doc, {'pos': 'v', 'verb_person': 's2'})
        result = incidence(doc, selection)
        debug = {'TOKENS': selection}
        return result, debug


class IN_V_2P(Metric):
    category = Inflection
    name_en = "Second person plural verbs"
    name_local = "Czasowniki w 2. os. l. mn."

    def count(doc):
        selection = select(doc, {'pos': 'v', 'verb_person': 'p2'})
        result = incidence(doc, selection)
        debug = {'TOKENS': selection}
        return result, debug


class IN_V_3S(Metric):
    category = Inflection
    name_en = "Third person singular verbs"
    name_local = "Czasowniki w 3. os. l. poj."

    def count(doc):
        selection = select(doc, {'pos': 'v', 'verb_person': 's3'})
        result = incidence(doc, selection)
        debug = {'TOKENS': selection}
        return result, debug


class IN_V_3P(Metric):
    category = Inflection
    name_en = "Third person plural verbs"
    name_local = "Czasowniki w 3. os. l. mn."

    def count(doc):
        selection = select(doc, {'pos': 'v', 'verb_person': 'p3'})
        result = incidence(doc, selection)
        debug = {'TOKENS': selection}
        return result, debug


# VERBS_PERSONS = [
#     IN_V_1S,
#     IN_V_1P,
#     IN_V_2S,
#     IN_V_2P,
#     IN_V_3S,
#     IN_V_3P,
# ]


class IN_V_PAST(Metric):
    category = Inflection
    name_en = "Verbs in past tense"
    name_local = "Czasowniki w czasie przeszłym"

    def count(doc):
        selection = select(doc, {'pos': 'v', 'verb_tense': 'past'})
        result = incidence(doc, selection)
        debug = {'TOKENS': selection}
        return result, debug


class IN_V_PRES(Metric):
    category = Inflection
    name_en = "Verbs in present tense"
    name_local = "Czasowniki w czasie teraźniejszym"

    def count(doc):
        selection = select(doc, {'pos': 'v', 'verb_tense': 'pres'})
        result = incidence(doc, selection)
        debug = {'TOKENS': selection}
        return result, debug


class IN_V_FUT(Metric):
    category = Inflection
    name_en = "Verbs in future tense"
    name_local = "Czasowniki w czasie przyszłym"

    def count(doc):
        selection = select(doc, {'pos': 'v', 'verb_tense': 'fut'})
        result = incidence(doc, selection)
        debug = {'TOKENS': selection}
        return result, debug


class IN_V_FUTS(Metric):
    category = Inflection
    name_en = "Verbs in future simple tense"
    name_local = "Czasowniki w czasie przyszłym prostym"

    def count(doc):
        selection = select(doc, {'pos': 'v', 'verb_future': 'futs'})
        result = incidence(doc, selection)
        debug = {'TOKENS': selection}
        return result, debug


class IN_V_FUTC(Metric):
    category = Inflection
    name_en = "Verbs in future complex tense"
    name_local = "Czasowniki w czasie przyszłym złożonym"

    def count(doc):
        selection = select(doc, {'pos': 'v', 'verb_future': 'futc'})
        result = incidence(doc, selection)
        debug = {'TOKENS': selection}
        return result, debug


# VERBS_TENSES = [
#     IN_V_PAST,
#     IN_V_PRES,
#     IN_V_FUT,
#     IN_V_FUTS,
#     IN_V_FUTC,
# ]


class IN_V_PERF(Metric):
    category = Inflection
    name_en = "Verbs in perfective aspect"
    name_local = "Czasowniki w aspekcie dokonanym"

    def count(doc):
        selection = select(doc, {'pos': 'v', 'verb_aspect': 'perf'})
        result = incidence(doc, selection)
        debug = {'TOKENS': selection}
        return result, debug


class IN_V_IMPERF(Metric):
    category = Inflection
    name_en = "Verbs in imperfective aspect"
    name_local = "Czasowniki w aspekcie niedokonanym"

    def count(doc):
        selection = select(doc, {'pos': 'v', 'verb_aspect': 'imperf'})
        result = incidence(doc, selection)
        debug = {'TOKENS': selection}
        return result, debug


VERBS_ASPECTS = [
    IN_V_PERF,
    IN_V_IMPERF,
]


class IN_V_IMP(Metric):
    category = Inflection
    name_en = "Verbs in imperative mood"
    name_local = "Czasowniki w trybie rozkazującym"

    def count(doc):
        selection = select(doc, {'pos': 'v', 'verb_voice': 'impt'})
        result = incidence(doc, selection)
        debug = {'TOKENS': selection}
        return result, debug


class IN_V_COND(Metric):
    category = Inflection
    name_en = "Verbs in conditional mood"
    name_local = "Czasowniki w trybie przypuszczającym"

    def count(doc):
        selection = select(doc, {'pos': 'v', 'verb_voice': 'cond'})
        result = incidence(doc, selection)
        debug = {'TOKENS': selection}
        return result, debug


# VERBS_MOODS = [
#     IN_V_IMP,
#     IN_V_COND,
# ]

class IN_V_ACT(Metric):
    category = Inflection
    name_en = "Verbs in active voice"
    name_local = "Czasowniki w stronie czynnej"

    def count(doc):
        actives = list(token.text for token in doc if str(token.morph.get('Voice'))=='[\'Act\']')
        debug = {"VALUES": actives}
        return ratio(len(actives), doc._.n_tokens), debug

class IN_V_PASS(Metric):
    category = Inflection
    name_en = "Verbs in passive voice"
    name_local = "Czasowniki w stronie biernej"

    def count(doc):
        passives = list(token.text for token in doc if str(token.morph.get('Voice'))=='[\'Pass\']')
        debug = {"VALUES": passives}
        return ratio(len(passives), doc._.n_tokens), debug

# VERBS_VOICES = [
#     IN_V_ACT,
#     IN_V_PASS,
# ]

class IN_V_PCON(Metric):
    category = Inflection
    name_en = "Present adverbial participles"
    name_local = "Imiesłowy przysłówkowe współczesne"

    def count(doc):
        selection = select(doc, {'pos': 'v', 'participle_type': 'pcon'})
        result = incidence(doc, selection)
        debug = {'TOKENS': selection}
        return result, debug


class IN_V_PANT(Metric):
    category = Inflection
    name_en = "Perfect adverbial participles"
    name_local = "Imiesłowy przysłówkowe uprzednie"

    def count(doc):
        selection = select(doc, {'pos': 'v', 'participle_type': 'pant'})
        result = incidence(doc, selection)
        debug = {'TOKENS': selection}
        return result, debug


class IN_V_PACT(Metric):
    category = Inflection
    name_en = "Active adjectival participles"
    name_local = "Imiesłowy przymiotnikowe czynne"

    def count(doc):
        selection = select(doc, {'pos': 'v', 'participle_type': 'pact'})
        result = incidence(doc, selection)
        debug = {'TOKENS': selection}
        return result, debug


class IN_V_PPAS(Metric):
    category = Inflection
    name_en = "Passive adjectival participles"
    name_local = "Imiesłowy przymiotnikowe bierne (przeszłe)"

    def count(doc):
        selection = select(doc, {'pos': 'v', 'participle_type': 'ppas'})
        result = incidence(doc, selection)
        debug = {'TOKENS': selection}
        return result, debug


# VERBS_PARTICIPLES = [
#     IN_V_PCON,
#     IN_V_PANT,
#     IN_V_PACT,
#     IN_V_PPAS,
# ]


class IN_V_GER(Metric):
    category = Inflection
    name_en = "Gerunds"
    name_local = "Rzeczowniki odczasownikowe"


    def count(doc):
        selection = select(doc, {'pos': 'n', 'noun_type': 'ger'})
        result = incidence(doc, selection)
        debug = {'TOKENS': selection}
        return result, debug


# VERBS_DERIVATION = [
#     IN_V_GER,
# ]


class Nouns:
    @classmethod
    def count(cls, doc):
        selection = select(doc, {'pos': 'n', 'case': cls.case})
        result = incidence(doc, selection)
        debug = {'TOKENS': selection}
        return result, debug


class IN_N_1M(Metric, Nouns):
    category = Inflection
    case = "nom"
    name_en = "Nouns in nominative case"
    name_local = "Rzeczowniki w mianowniku"


class IN_N_2D(Metric, Nouns):
    category = Inflection
    case = "gen"
    name_en = "Nouns in genitive case"
    name_local = "Rzeczowniki w dopełniaczu"


class IN_N_3C(Metric, Nouns):
    category = Inflection
    case = "dat"
    name_en = "Nouns in dative case"
    name_local = "Rzeczowniki w celowniku"


class IN_N_4B(Metric, Nouns):
    category = Inflection
    case = "acc"
    name_en = "Nouns in accusative case"
    name_local = "Rzeczowniki w bierniku"


class IN_N_5MSC(Metric, Nouns):
    category = Inflection
    case = "inst"
    name_en = "Nouns in instrumental case"
    name_local = "Rzeczowniki w narzędniku"


class IN_N_6N(Metric, Nouns):
    category = Inflection
    case = "loc"
    name_en = "Nouns in locative case"
    name_local = "Rzeczowniki w miejscowniku"


class IN_N_7W(Metric, Nouns):
    category = Inflection
    case = "voc"
    name_en = "Nouns in vocative case"
    name_local = "Rzeczowniki w wołaczu"


# NOUNS_CASES = [
#     IN_N_1M,
#     IN_N_2D,
#     IN_N_3C,
#     IN_N_4B,
#     IN_N_5MSC,
#     IN_N_6N,
#     IN_N_7W,
# ]


class Pronouns:
    @classmethod
    def count(cls, doc):
        selection = select(doc, {'pos': 'pro', 'case': cls.case})
        result = incidence(doc, selection)
        debug = {'TOKENS': selection}
        return result, debug


class IN_PRO_1M(Metric, Pronouns):
    category = Inflection
    case = "nom"
    name_en = "Pronouns in nominative case"
    name_local = "Zaimki w mianowniku"


class IN_PRO_2D(Metric, Pronouns):
    category = Inflection
    case = "gen"
    name_en = "Pronouns in genitive case"
    name_local = "Zaimki w dopełniaczu"


class IN_PRO_3C(Metric, Pronouns):
    category = Inflection
    case = "dat"
    name_en = "Pronouns in dative case"
    name_local = "Zaimki w celowniku"


class IN_PRO_4B(Metric, Pronouns):
    category = Inflection
    case = "acc"
    name_en = "Pronouns in accusative case"
    name_local = "Zaimki w bierniku"


class IN_PRO_5MSC(Metric, Pronouns):
    category = Inflection
    case = "inst"
    name_en = "Pronouns in instrumental case"
    name_local = "Zaimki w narzędniku"


class IN_PRO_6N(Metric, Pronouns):
    category = Inflection
    case = "loc"
    name_en = "Pronouns in locative case"
    name_local = "Zaimki w miejscowniku"


class IN_PRO_7W(Metric, Pronouns):
    category = Inflection
    case = "voc"
    name_en = "Pronouns in vocative case"
    name_local = "Zaimki w wołaczu"


# PRONOUNS_CASES = [
#     IN_PRO_1M,
#     IN_PRO_2D,
#     IN_PRO_3C,
#     IN_PRO_4B,
#     IN_PRO_5MSC,
#     IN_PRO_6N,
#     IN_PRO_7W,
# ]


class IN_PRO_1S(Metric):
    category = Inflection
    name_en = "First person singular pronouns"
    name_local = "Zaimki w 1 os. l. poj."

    def count(doc):
        selection = select(doc, {'pos': 'pro', 'pronoun_type': 's1'})
        result = incidence(doc, selection)
        debug = {'TOKENS': selection}
        return result, debug


class IN_PRO_1P(Metric):
    category = Inflection
    name_en = "First person plural pronouns"
    name_local = "Zaimki w 1 os. l. mn."

    def count(doc):
        selection = select(doc, {'pos': 'pro', 'pronoun_type': 'p1'})
        result = incidence(doc, selection)
        debug = {'TOKENS': selection}
        return result, debug


class IN_PRO_2S(Metric):
    category = Inflection
    name_en = "Second person singular pronouns"
    name_local = "Zaimki w 2 os. l. poj."

    def count(doc):
        selection = select(doc, {'pos': 'pro', 'pronoun_type': 's2'})
        result = incidence(doc, selection)
        debug = {'TOKENS': selection}
        return result, debug


class IN_PRO_2P(Metric):
    category = Inflection
    name_en = "Second person plural pronouns"
    name_local = "Zaimki w 2 os. l. mn."

    def count(doc):
        selection = select(doc, {'pos': 'pro', 'pronoun_type': 'p2'})
        result = incidence(doc, selection)
        debug = {'TOKENS': selection}
        return result, debug


class IN_PRO_3S(Metric):
    category = Inflection
    name_en = "Third person singular pronouns"
    name_local = "Zaimki w 3 os. l. poj."

    def count(doc):
        selection = select(doc, {'pos': 'pro', 'pronoun_type': 's3'})
        result = incidence(doc, selection)
        debug = {'TOKENS': selection}
        return result, debug


class IN_PRO_3P(Metric):
    category = Inflection
    name_en = "Third person plural pronouns"
    name_local = "Zaimki w 3 os. l. mn."

    def count(doc):
        selection = select(doc, {'pos': 'pro', 'pronoun_type': 'p3'})
        result = incidence(doc, selection)
        debug = {'TOKENS': selection}
        return result, debug


# PRONOUNS_PERSONS = [
#     IN_PRO_1S,
#     IN_PRO_1P,
#     IN_PRO_2S,
#     IN_PRO_2P,
#     IN_PRO_3S,
#     IN_PRO_3P,
# ]


class IN_ADJ_POS(Metric):
    category = Inflection
    name_en = "Adjectives in positive degree"
    name_local = "Przymiotniki w stopniu równym"

    def count(doc):
        selection = select(doc, {'pos': 'adj', 'adjective_degree': 'pos'})
        result = incidence(doc, selection)
        debug = {'TOKENS': selection}
        return result, debug


class IN_ADJ_COM(Metric):
    category = Inflection
    name_en = "Adjectives in comparative degree"
    name_local = "Przymiotniki w stopniu wyższym"

    def count(doc):
        selection = select(doc, {'pos': 'adj', 'adjective_degree': 'com'})
        result = incidence(doc, selection)
        debug = {'TOKENS': selection}
        return result, debug


class IN_ADJ_SUP(Metric):
    category = Inflection
    name_en = "Adjectives in superlative degree"
    name_local = "Przymiotniki w stopniu najwyższym"

    def count(doc):
        selection = select(doc, {'pos': 'adj', 'adjective_degree': 'sup'})
        result = incidence(doc, selection)
        debug = {'TOKENS': selection}
        return result, debug


# ADJECTIVES_DEGREES = [
#     IN_ADJ_POS,
#     IN_ADJ_COM,
#     IN_ADJ_SUP,
# ]


class IN_ADV_POS(Metric):
    category = Inflection
    name_en = "Adverbs in positive degree"
    name_local = "Przysłówki w stopniu równym"

    def count(doc):
        selection = select(doc, {'pos': 'adv', 'adverb_degree': 'pos'})
        result = incidence(doc, selection)
        debug = {'TOKENS': selection}
        return result, debug


class IN_ADV_COM(Metric):
    category = Inflection
    name_en = "Adverbs in comparative degree"
    name_local = "Przysłówki w stopniu wyższym"

    def count(doc):
        selection = select(doc, {'pos': 'adv', 'adverb_degree': 'com'})
        result = incidence(doc, selection)
        debug = {'TOKENS': selection}
        return result, debug


class IN_ADV_SUP(Metric):
    category = Inflection
    name_en = "Adverbs in superlative degree"
    name_local = "Przysłówki w stopniu najwyższym"

    def count(doc):
        selection = select(doc, {'pos': 'adv', 'adverb_degree': 'sup'})
        result = incidence(doc, selection)
        debug = {'TOKENS': selection}
        return result, debug


# ADVERBS_DEGREES = [
#     IN_ADV_POS,
#     IN_ADV_COM,
#     IN_ADV_SUP,
# ]

# verbs_inflection_group = MetricsGroup([m() for m in VERBS_INFLECTION])
# verbs_persons_group = MetricsGroup([m() for m in VERBS_PERSONS])
# verbs_tenses_group = MetricsGroup([m() for m in VERBS_TENSES])
# verbs_aspects_group = MetricsGroup([m() for m in VERBS_ASPECTS])
# verbs_moods_group = MetricsGroup([m() for m in VERBS_MOODS])
# verbs_voices_group = MetricsGroup([m() for m in VERBS_VOICES])
# verbs_participles_group = MetricsGroup([m() for m in VERBS_PARTICIPLES])
# verbs_derivation_group = MetricsGroup([m() for m in VERBS_DERIVATION])
# nouns_cases_group = MetricsGroup([m() for m in NOUNS_CASES])
# pronouns_cases_group = MetricsGroup([m() for m in PRONOUNS_CASES])
# pronouns_persons_group = MetricsGroup([m() for m in PRONOUNS_PERSONS])
# adjectives_degrees_group = MetricsGroup([m() for m in ADJECTIVES_DEGREES])
# adverbs_degrees_group = MetricsGroup([m() for m in ADVERBS_DEGREES])

# verbs_group = verbs_inflection_group + \
#               verbs_persons_group + \
#               verbs_tenses_group + \
#               verbs_aspects_group + \
#               verbs_moods_group + \
#               verbs_voices_group + \
#               verbs_participles_group + \
#               verbs_derivation_group
# nouns_group = nouns_cases_group
# pronouns_group = pronouns_cases_group + \
#                  pronouns_persons_group
# adjectives_group = adjectives_degrees_group
# adverbs_group = adverbs_degrees_group
# inflection_group = verbs_group + \
#                    nouns_group + \
#                    pronouns_group + \
#                    adjectives_group + \
#                    adverbs_group
