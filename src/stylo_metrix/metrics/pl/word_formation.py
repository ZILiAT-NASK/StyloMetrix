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
from stylo_metrix.utils import incidence


class WordFormation(Metric, ABC):
    category_pl = "Word Formation"
    category_en = "Słowotwórcze"
    affixes = ""

    def find_words_affix(self, doc, affixes, starts, pos):
        affixes = affixes.split(", ")
        data = [token for token in doc if token._.pos == pos] if pos else doc
        search = [token for token in data if
                  any([token.lemma_.startswith(e) if starts else token.lemma_.endswith(e)
                       for e in affixes]) and token.lemma_ not in affixes]
        result = incidence(doc, search)
        return result, {}


class NounsEnd(WordFormation, ABC):
    affixes = ""

    def count(self, doc):
        result, debug = self.find_words_affix(doc, affixes=self.__class__.affixes, starts=False, pos='n')
        return result, debug


class WF_NE_OSC(NounsEnd):
    """ przyrostek bardzo częsty, tworzy pojęcia abstrakcyjne """
    name_en = "Incidence od nouns ending with ość"
    name_pl = "Występowanie rzeczowników zakończonych na ość"
    affixes = "ość"


class WF_NE_IK(NounsEnd):
    """ zdrobnienia - częste w tekstach potocznych, internetowych """
    name_en = "Incidence od nouns ending with ik"
    name_pl = "Występowanie rzeczowników zakończonych na ik"
    affixes = "ik"


class WF_NE_EK(NounsEnd):
    """ zdrobnienia - częste w tekstach potocznych, internetowych """
    name_en = "Incidence od nouns ending with ek"
    name_pl = "Występowanie rzeczowników zakończonych na ek"
    affixes = "ek"


class WF_NE_KA(NounsEnd):
    """ zdrobnienia - częste w tekstach potocznych, internetowych """
    name_en = "Incidence od nouns ending with ka"
    name_pl = "Występowanie rzeczowników zakończonych na ka"
    affixes = "ka"


class WF_NE_KO(NounsEnd):
    """ zdrobnienia - częste w tekstach potocznych, internetowych """
    name_en = "Incidence od nouns ending with ko"
    name_pl = "Występowanie rzeczowników zakończonych na ko"
    affixes = "ko"


class WF_NE_IYCIEL(NounsEnd):
    """ wykonawcy czynności i nosiciele cech """
    name_en = "Incidence od nouns ending with iciel, yciel"
    name_pl = "Występowanie rzeczowników zakończonych na iciel, yciel"
    affixes = "iciel, yciel"


class WF_NE_OWIEC(NounsEnd):
    """ wykonawcy czynności i nosiciele cech """
    name_en = "Incidence od nouns ending with owiec"
    name_pl = "Występowanie rzeczowników zakończonych na owiec"
    affixes = "owiec"


class WF_NE_ARZ(NounsEnd):
    """ wykonawcy czynności i nosiciele cech """
    name_en = "Incidence od nouns ending with arz"
    name_pl = "Występowanie rzeczowników zakończonych na arz"
    affixes = "arz"


class WF_NE_OWICZ(NounsEnd):
    """ wykonawcy czynności i nosiciele cech """
    name_en = "Incidence od nouns ending with owicz"
    name_pl = "Występowanie rzeczowników zakończonych na owicz"
    affixes = "owicz"


# -----------------------------------------------------------------

class AdjectivesStart(WordFormation, ABC):
    affixes = ""
    name_en = ""
    name_pl = "Występowanie przymiotników rozpoczynających się na "
    languages = "pl" + affixes

    def count(self, doc):
        result, debug = self.find_words_affix(doc, affixes=self.__class__.affixes, starts=True, pos='adj')
        return result, debug


# -----------------------------------------------------------------


class AdjectivesEnd(WordFormation, ABC):
    affixes = ""
    name_en = ""
    name_pl = "Występowanie przymiotników zakończonych na "
    languages = "pl" + affixes

    def count(self, doc):
        result, debug = self.find_words_affix(doc, affixes=self.__class__.affixes, starts=False, pos='adj')
        return result, debug


class WF_ADJE_OWY(AdjectivesEnd):
    """ najczęstsze przyrostki przymiotnikowe """
    name_en = "Incidence od adjectives ending with owy"
    name_pl = "Występowanie przymiotników zakończonych na owy"
    affixes = "owy"


class WF_ADJE_SKI(AdjectivesEnd):
    """ najczęstsze przyrostki przymiotnikowe """
    name_en = "Incidence od adjectives ending with ski"
    name_pl = "Występowanie przymiotników zakończonych na ski"
    affixes = "ski"


class WF_ADJE_LIWY(AdjectivesEnd):
    """ najczęstsze przyrostki przymiotnikowe """
    name_en = "Incidence od adjectives ending with liwy"
    name_pl = "Występowanie przymiotników zakończonych na liwy"
    affixes = "liwy"


# ----------------------------------------------------


class AllStart(WordFormation, ABC):
    affixes = ""
    name_en = ""
    name_pl = "Występowanie wyrazów rozpoczynających się na "
    languages = "pl" + affixes

    def count(self, doc):
        result, debug = self.find_words_affix(doc, affixes=self.__class__.affixes, starts=True, pos=None)
        return result, debug


WORD_FORMATION = [
    WF_NE_OSC,
    WF_NE_IK,
    WF_NE_EK,
    WF_NE_KA,
    WF_NE_KO,
    WF_NE_IYCIEL,
    WF_NE_OWIEC,
    WF_NE_ARZ,
    WF_NE_OWICZ,
    WF_ADJE_OWY,
    WF_ADJE_SKI,
    WF_ADJE_LIWY,
]

word_formation_group = MetricsGroup([m() for m in WORD_FORMATION])
