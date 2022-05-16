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


from abc import ABC

from stylo_metrix.structures import Metric, MetricsGroup
from stylo_metrix.utils import incidence, select


class Inflection(Metric, ABC):
    category_pl = "Inflection"
    category_en = "Fleksja"


class IN_V_INF(Inflection):
    name_en = "Infinitives incidence"
    name_pl = "Występowanie czasowników w bezokoliczniku"

    def count(self, doc):
        result = incidence(doc, select(doc, {'pos': 'v', 'verb_inflection': 'inf'}))
        return result, {}


class IN_V_INFL(Inflection):
    name_en = "Inflected verb incidence"
    name_pl = "Występowanie czasowników w formie osobowej"

    def count(self, doc):
        result = incidence(doc, select(doc, {'pos': 'v', 'verb_inflection': 'infl'}))
        return result, {}


VERBS_INFLECTION = [
    IN_V_INF,
    IN_V_INFL,
]


class IN_V_1S(Inflection):
    name_en = "First person singular verb incidence"
    name_pl = "Występowanie czasowników w 1. os. l. poj."

    def count(self, doc):
        result = incidence(doc, select(doc, {'pos': 'v', 'verb_person': 's1'}))
        return result, {}


class IN_V_1P(Inflection):
    name_en = "First person plural verb incidence"
    name_pl = "Występowanie czasowników w 1. os. l. mn."

    def count(self, doc):
        result = incidence(doc, select(doc, {'pos': 'v', 'verb_person': 'p1'}))
        return result, {}


class IN_V_2S(Inflection):
    name_en = "Second person singular verb incidence"
    name_pl = "Występowanie czasowników w 2. os. l. poj."

    def count(self, doc):
        result = incidence(doc, select(doc, {'pos': 'v', 'verb_person': 's2'}))
        return result, {}


class IN_V_2P(Inflection):
    name_en = "Second person plural verb incidence"
    name_pl = "Występowanie czasowników w 2. os. l. mn."

    def count(self, doc):
        result = incidence(doc, select(doc, {'pos': 'v', 'verb_person': 'p2'}))
        return result, {}


class IN_V_3S(Inflection):
    name_en = "Third person singular verb incidence"
    name_pl = "Występowanie czasowników w 3. os. l. poj."

    def count(self, doc):
        result = incidence(doc, select(doc, {'pos': 'v', 'verb_person': 's3'}))
        return result, {}


class IN_V_3P(Inflection):
    name_en = "Third person plural verb incidence"
    name_pl = "Występowanie czasowników w 3. os. l. mn."

    def count(self, doc):
        result = incidence(doc, select(doc, {'pos': 'v', 'verb_person': 'p3'}))
        return result, {}


VERBS_PERSONS = [
    IN_V_1S,
    IN_V_1P,
    IN_V_2S,
    IN_V_2P,
    IN_V_3S,
    IN_V_3P,
]


class IN_V_PAST(Inflection):
    name_en = "Verbs in past tense incidence"
    name_pl = "Występowanie czasowników w czasie przeszłym"

    def count(self, doc):
        result = incidence(doc, select(doc, {'pos': 'v', 'verb_tense': 'past'}))
        return result, {}


class IN_V_PRES(Inflection):
    name_en = "Verbs in present tense incidence"
    name_pl = "Występowanie czasowników w czasie teraźniejszym"

    def count(self, doc):
        result = incidence(doc, select(doc, {'pos': 'v', 'verb_tense': 'pres'}))
        return result, {}


class IN_V_FUT(Inflection):
    name_en = "Verbs in future tense incidence"
    name_pl = "Występowanie czasowników w czasie przyszłym"

    def count(self, doc):
        result = incidence(doc, select(doc, {'pos': 'v', 'verb_tense': 'fut'}))
        return result, {}


class IN_V_FUTS(Inflection):
    name_en = "Verbs in future simple tense incidence"
    name_pl = "Występowanie czasowników w czasie przyszłym prostym"

    def count(self, doc):
        result = incidence(doc, select(doc, {'pos': 'v', 'verb_future': 'futs'}))
        return result, {}


class IN_V_FUTC(Inflection):
    name_en = "Verbs in future complex tense incidence"
    name_pl = "Występowanie czasowników w czasie przyszłym złożonym"

    def count(self, doc):
        result = incidence(doc, select(doc, {'pos': 'v', 'verb_future': 'futc'}))
        return result, {}


VERBS_TENSES = [
    IN_V_PAST,
    IN_V_PRES,
    IN_V_FUT,
    IN_V_FUTS,
    IN_V_FUTC,
]


class IN_V_PERF(Inflection):
    name_en = "Verbs in perfective aspect incidence"
    name_pl = "Występowanie czasowników w aspekcie dokonanym"

    def count(self, doc):
        result = incidence(doc, select(doc, {'pos': 'v', 'verb_aspect': 'perf'}))
        return result, {}


class IN_V_IMPERF(Inflection):
    name_en = "Verbs in imperfective aspect incidence"
    name_pl = "Występowanie czasowników w aspekcie niedokonanym"

    def count(self, doc):
        result = incidence(doc, select(doc, {'pos': 'v', 'verb_aspect': 'imperf'}))
        return result, {}


VERBS_ASPECTS = [
    IN_V_PERF,
    IN_V_IMPERF,
]


class IN_V_IMP(Inflection):
    name_en = "Verbs in imperative mood incidence"
    name_pl = "Występowanie czasowników w trybie rozkazującym"

    def count(self, doc):
        result = incidence(doc, select(doc, {'pos': 'v', 'verb_voice': 'impt'}))
        return result, {}


class IN_V_COND(Inflection):
    name_en = "Verbs in conditional mood incidence"
    name_pl = "Występowanie czasowników w trybie przypuszczającym"

    def count(self, doc):
        result = incidence(doc, select(doc, {'pos': 'v', 'verb_voice': 'cond'}))
        return result, {}


VERBS_MOODS = [
    IN_V_IMP,
    IN_V_COND,
]


class IN_V_PCON(Inflection):
    name_en = "Present adverbial participles incidence"
    name_pl = "Występowanie imiesłowów przysłówkowych współczesnych"

    def count(self, doc):
        result = incidence(doc, select(doc, {'pos': 'v', 'participle_type': 'pcon'}))
        return result, {}


class IN_V_PANT(Inflection):
    name_en = "Perfect adverbial participles incidence"
    name_pl = "Występowanie imiesłowów przysłówkowych uprzednich"

    def count(self, doc):
        result = incidence(doc, select(doc, {'pos': 'v', 'participle_type': 'pant'}))
        return result, {}


class IN_V_PACT(Inflection):
    name_en = "Active adjectival participles incidence"
    name_pl = "Występowanie imiesłowów przymiotnikowych czynnych"

    def count(self, doc):
        result = incidence(doc, select(doc, {'pos': 'v', 'participle_type': 'pact'}))
        return result, {}


class IN_V_PPAS(Inflection):
    name_en = "Passive adjectival participles incidence"
    name_pl = "Występowanie imiesłowów przymiotnikowych biernych (przeszłych)"

    def count(self, doc):
        result = incidence(doc, select(doc, {'pos': 'v', 'participle_type': 'ppas'}))
        return result, {}


VERBS_PARTICIPLES = [
    IN_V_PCON,
    IN_V_PANT,
    IN_V_PACT,
    IN_V_PPAS,
]


class IN_V_GER(Inflection):
    name_en = "Gerunds incidence"
    name_pl = "Występowanie rzeczowników odczasownikowych"

    def count(self, doc):
        result = incidence(doc, select(doc, {'pos': 'n', 'noun_type': 'ger'}))
        return result, {}


VERBS_DERIVATION = [
    IN_V_GER,
]


class Nouns(Inflection, ABC):
    case = ""

    def count(self, doc):
        result = incidence(doc, select(doc, {'pos': 'n', 'case': self.__class__.case}))
        return result, {}


class IN_N_1M(Nouns):
    case = "nom"
    name_en = "Nouns in nominative case incidence"
    name_pl = "Występowanie rzeczowników w mianowniku"


class IN_N_2D(Nouns):
    case = "gen"
    name_en = "Nouns in genitive case incidence"
    name_pl = "Występowanie rzeczowników w dopełniaczu"


class IN_N_3C(Nouns):
    case = "dat"
    name_en = "Nouns in dative case incidence"
    name_pl = "Występowanie rzeczowników w celowniku"


class IN_N_4B(Nouns):
    case = "acc"
    name_en = "Nouns in accusative case incidence"
    name_pl = "Występowanie rzeczowników w bierniku"


class IN_N_5MSC(Nouns):
    case = "inst"
    name_en = "Nouns in instrumental case incidence"
    name_pl = "Występowanie rzeczowników w narzędniku"


class IN_N_6N(Nouns):
    case = "loc"
    name_en = "Nouns in locative case incidence"
    name_pl = "Występowanie rzeczowników w miejscowniku"


class IN_N_7W(Nouns):
    case = "voc"
    name_en = "Nouns in vocative case incidence"
    name_pl = "Występowanie rzeczowników w wołaczu"


NOUNS_CASES = [
    IN_N_1M,
    IN_N_2D,
    IN_N_3C,
    IN_N_4B,
    IN_N_5MSC,
    IN_N_6N,
    IN_N_7W,
]


class Pronouns(Inflection, ABC):
    case = ""
    name_en = ""
    name_pl = "Zaimki w przypadku " + case

    def count(self, doc):
        result = incidence(doc, select(doc, {'pos': 'pro', 'case': self.__class__.case}))
        return result, {}


class IN_PRO_1M(Pronouns):
    case = "nom"
    name_en = "Pronouns in nominative case incidence"
    name_pl = "Występowanie zaimków w mianowniku"


class IN_PRO_2D(Pronouns):
    case = "gen"
    name_en = "Pronouns in genitive case incidence"
    name_pl = "Występowanie zaimków w dopełniaczu"


class IN_PRO_3C(Pronouns):
    case = "dat"
    name_en = "Pronouns in dative case incidence"
    name_pl = "Występowanie zaimków w celowniku"


class IN_PRO_4B(Pronouns):
    case = "acc"
    name_en = "Pronouns in accusative case incidence"
    name_pl = "Występowanie zaimków w bierniku"


class IN_PRO_5MSC(Pronouns):
    case = "inst"
    name_en = "Pronouns in instrumental case incidence"
    name_pl = "Występowanie zaimków w narzędniku"


class IN_PRO_6N(Pronouns):
    case = "loc"
    name_en = "Pronouns in locative case incidence"
    name_pl = "Występowanie zaimków w miejscowniku"


class IN_PRO_7W(Pronouns):
    case = "voc"
    name_en = "Pronouns in vocative case incidence"
    name_pl = "Występowanie zaimków w wołaczu"


PRONOUNS_CASES = [
    IN_PRO_1M,
    IN_PRO_2D,
    IN_PRO_3C,
    IN_PRO_4B,
    IN_PRO_5MSC,
    IN_PRO_6N,
    IN_PRO_7W,
]


class IN_PRO_1S(Inflection):
    name_en = "First person singular pronoun incidence"
    name_pl = "Występowanie zaimków w 1 os. l. poj."

    def count(self, doc):
        result = incidence(doc, select(doc, {'pos': 'pro', 'pronoun_type': 's1'}))
        return result, {}


class IN_PRO_1P(Inflection):
    name_en = "First person plural pronoun incidence"
    name_pl = "Występowanie zaimków w 1 os. l. mn."

    def count(self, doc):
        result = incidence(doc, select(doc, {'pos': 'pro', 'pronoun_type': 'p1'}))
        return result, {}


class IN_PRO_2S(Inflection):
    name_en = "Second person singular pronoun incidence"
    name_pl = "Występowanie zaimków w 2 os. l. poj."

    def count(self, doc):
        result = incidence(doc, select(doc, {'pos': 'pro', 'pronoun_type': 's2'}))
        return result, {}


class IN_PRO_2P(Inflection):
    name_en = "Second person plural pronoun incidence"
    name_pl = "Występowanie zaimków w 2 os. l. mn."

    def count(self, doc):
        result = incidence(doc, select(doc, {'pos': 'pro', 'pronoun_type': 'p2'}))
        return result, {}


class IN_PRO_3S(Inflection):
    name_en = "Third person singular pronoun incidence"
    name_pl = "Występowanie zaimków w 3 os. l. poj."

    def count(self, doc):
        result = incidence(doc, select(doc, {'pos': 'pro', 'pronoun_type': 's3'}))
        return result, {}


class IN_PRO_3P(Inflection):
    name_en = "Third person plural pronoun incidence"
    name_pl = "Występowanie zaimków w 3 os. l. mn."

    def count(self, doc):
        result = incidence(doc, select(doc, {'pos': 'pro', 'pronoun_type': 'p3'}))
        return result, {}


PRONOUNS_PERSONS = [
    IN_PRO_1S,
    IN_PRO_1P,
    IN_PRO_2S,
    IN_PRO_2P,
    IN_PRO_3S,
    IN_PRO_3P,
]


class IN_ADJ_POS(Inflection):
    name_en = "Adjectives in positive degree incidence"
    name_pl = "Występowanie przymiotników w stopniu równym"

    def count(self, doc):
        result = incidence(doc, select(doc, {'pos': 'adj', 'adjective_degree': 'pos'}))
        return result, {}


class IN_ADJ_COM(Inflection):
    name_en = "Adjectives in comparative degree incidence"
    name_pl = "Występowanie przymiotników w stopniu wyższym"

    def count(self, doc):
        result = incidence(doc, select(doc, {'pos': 'adj', 'adjective_degree': 'com'}))
        return result, {}


class IN_ADJ_SUP(Inflection):
    name_en = "Adjectives in superlative degree incidence"
    name_pl = "Występowanie przymiotników w stopniu najwyższym"

    def count(self, doc):
        result = incidence(doc, select(doc, {'pos': 'adj', 'adjective_degree': 'sup'}))
        return result, {}


ADJECTIVES_DEGREES = [
    IN_ADJ_POS,
    IN_ADJ_COM,
    IN_ADJ_SUP,
]


class IN_ADV_POS(Inflection):
    name_en = "Adverbs in positive degree incidence"
    name_pl = "Występowanie przysłówków w stopniu równym"

    def count(self, doc):
        result = incidence(doc, select(doc, {'pos': 'adv', 'adverb_degree': 'pos'}))
        return result, {}


class IN_ADV_COM(Inflection):
    name_en = "Adverbs in comparative degree incidence"
    name_pl = "Występowanie przysłówków w stopniu wyższym"

    def count(self, doc):
        result = incidence(doc, select(doc, {'pos': 'adv', 'adverb_degree': 'com'}))
        return result, {}


class IN_ADV_SUP(Inflection):
    name_en = "Adverbs in superlative degree incidence"
    name_pl = "Występowanie przysłówków w stopniu najwyższym"

    def count(self, doc):
        result = incidence(doc, select(doc, {'pos': 'adv', 'adverb_degree': 'sup'}))
        return result, {}


ADVERBS_DEGREES = [
    IN_ADV_POS,
    IN_ADV_COM,
    IN_ADV_SUP,
]

verbs_inflection_group = MetricsGroup([m() for m in VERBS_INFLECTION])
verbs_persons_group = MetricsGroup([m() for m in VERBS_PERSONS])
verbs_tenses_group = MetricsGroup([m() for m in VERBS_TENSES])
verbs_aspects_group = MetricsGroup([m() for m in VERBS_ASPECTS])
verbs_moods_group = MetricsGroup([m() for m in VERBS_MOODS])
verbs_participles_group = MetricsGroup([m() for m in VERBS_PARTICIPLES])
verbs_derivation_group = MetricsGroup([m() for m in VERBS_DERIVATION])
nouns_cases_group = MetricsGroup([m() for m in NOUNS_CASES])
pronouns_cases_group = MetricsGroup([m() for m in PRONOUNS_CASES])
pronouns_persons_group = MetricsGroup([m() for m in PRONOUNS_PERSONS])
adjectives_degrees_group = MetricsGroup([m() for m in ADJECTIVES_DEGREES])
adverbs_degrees_group = MetricsGroup([m() for m in ADVERBS_DEGREES])

verbs_group = verbs_inflection_group + \
              verbs_persons_group + \
              verbs_tenses_group + \
              verbs_aspects_group + \
              verbs_moods_group + \
              verbs_participles_group + \
              verbs_derivation_group
nouns_group = nouns_cases_group
pronouns_group = pronouns_cases_group + \
                 pronouns_persons_group
adjectives_group = adjectives_degrees_group
adverbs_group = adverbs_degrees_group
inflection_group = verbs_group + \
                   nouns_group + \
                   pronouns_group + \
                   adjectives_group + \
                   adverbs_group
