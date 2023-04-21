# Copyright (C) 2023  NASK PIB
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

from stylo_metrix.utils import incidence


class WordFormation(Category):
    lang = 'pl'
    name_en = "Word Formation"
    name_local = "Słowotwórcze"


class Affixes:
    @classmethod
    def count(cls, doc):
        affixes = cls.affixes.split(", ")
        data = [token for token in doc if token._.pos == cls.pos] if cls.pos else doc
        search = [token for token in data if
                  any([token.lemma_.startswith(e) if cls.starts else token.lemma_.endswith(e)
                       for e in affixes]) and token.lemma_ not in affixes]
        result = incidence(doc, search)
        return result, {}


class NounsEnd(Affixes):
    starts = False
    pos = 'n'


class WF_NE_OSC(Metric, NounsEnd):
    """ przyrostek bardzo częsty, tworzy pojęcia abstrakcyjne """
    category = WordFormation
    name_en = "Incidence od nouns ending with ość"
    name_local = "Występowanie rzeczowników zakończonych na ość"
    affixes = "ość"


class WF_NE_IK(Metric, NounsEnd):
    """ zdrobnienia - częste w tekstach potocznych, internetowych """
    category = WordFormation
    name_en = "Incidence od nouns ending with ik"
    name_local = "Występowanie rzeczowników zakończonych na ik"
    affixes = "ik"


class WF_NE_EK(Metric, NounsEnd):
    """ zdrobnienia - częste w tekstach potocznych, internetowych """
    category = WordFormation
    name_en = "Incidence od nouns ending with ek"
    name_local = "Występowanie rzeczowników zakończonych na ek"
    affixes = "ek"


class WF_NE_KA(Metric, NounsEnd):
    """ zdrobnienia - częste w tekstach potocznych, internetowych """
    category = WordFormation
    name_en = "Incidence od nouns ending with ka"
    name_local = "Występowanie rzeczowników zakończonych na ka"
    affixes = "ka"


class WF_NE_KO(Metric, NounsEnd):
    """ zdrobnienia - częste w tekstach potocznych, internetowych """
    category = WordFormation
    name_en = "Incidence od nouns ending with ko"
    name_local = "Występowanie rzeczowników zakończonych na ko"
    affixes = "ko"


class WF_NE_IYCIEL(Metric, NounsEnd):
    """ wykonawcy czynności i nosiciele cech """
    category = WordFormation
    name_en = "Incidence od nouns ending with iciel, yciel"
    name_local = "Występowanie rzeczowników zakończonych na iciel, yciel"
    affixes = "iciel, yciel"


class WF_NE_OWIEC(Metric, NounsEnd):
    """ wykonawcy czynności i nosiciele cech """
    category = WordFormation
    name_en = "Incidence od nouns ending with owiec"
    name_local = "Występowanie rzeczowników zakończonych na owiec"
    affixes = "owiec"


class WF_NE_ARZ(Metric, NounsEnd):
    """ wykonawcy czynności i nosiciele cech """
    category = WordFormation
    name_en = "Incidence od nouns ending with arz"
    name_local = "Występowanie rzeczowników zakończonych na arz"
    affixes = "arz"


class WF_NE_OWICZ(Metric, NounsEnd):
    """ wykonawcy czynności i nosiciele cech """
    category = WordFormation
    name_en = "Incidence od nouns ending with owicz"
    name_local = "Występowanie rzeczowników zakończonych na owicz"
    affixes = "owicz"


# -----------------------------------------------------------------

class AdjectivesStart(Affixes):
    starts = True
    pos = 'adj'

# -----------------------------------------------------------------


class AdjectivesEnd(Affixes):
    starts = False
    pos = 'adj'


class WF_ADJE_OWY(Metric, AdjectivesEnd):
    """ najczęstsze przyrostki przymiotnikowe """
    category = WordFormation
    name_en = "Incidence od adjectives ending with owy"
    name_local = "Występowanie przymiotników zakończonych na owy"
    affixes = "owy"


class WF_ADJE_SKI(Metric, AdjectivesEnd):
    """ najczęstsze przyrostki przymiotnikowe """
    category = WordFormation
    name_en = "Incidence od adjectives ending with ski"
    name_local = "Występowanie przymiotników zakończonych na ski"
    affixes = "ski"


class WF_ADJE_LIWY(Metric, AdjectivesEnd):
    """ najczęstsze przyrostki przymiotnikowe """
    category = WordFormation
    name_en = "Incidence od adjectives ending with liwy"
    name_local = "Występowanie przymiotników zakończonych na liwy"
    affixes = "liwy"


# ----------------------------------------------------


# class AllStart(Metric, Affixes):
#     affixes = ""
#     name_en = ""
#     name_local = "Występowanie wyrazów rozpoczynających się na "

#     def count(self, doc):
#         result, debug = self.find_words_affix(doc, affixes=self.__class__.affixes, starts=True, pos=None)
#         return result, debug


# WORD_FORMATION = [
#     WF_NE_OSC,
#     WF_NE_IK,
#     WF_NE_EK,
#     WF_NE_KA,
#     WF_NE_KO,
#     WF_NE_IYCIEL,
#     WF_NE_OWIEC,
#     WF_NE_ARZ,
#     WF_NE_OWICZ,
#     WF_ADJE_OWY,
#     WF_ADJE_SKI,
#     WF_ADJE_LIWY,
# ]

# word_formation_group = MetricsGroup([m() for m in WORD_FORMATION])
