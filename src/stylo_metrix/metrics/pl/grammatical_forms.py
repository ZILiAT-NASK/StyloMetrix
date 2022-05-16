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


class GrammaticalForms(Metric, ABC):
    category_pl = "Grammatical Forms"
    category_en = "Formy gramatyczne"


class G_V(GrammaticalForms):
    name_en = "Verb incidence"
    name_pl = "Występowanie czasowników"

    def count(self, doc):
        result = incidence(doc, select(doc, {'pos': 'v'}))
        return result, {}


class G_N(GrammaticalForms):
    name_en = "Noun incidence"
    name_pl = "Występowanie rzeczowników"

    def count(self, doc):
        result = incidence(doc, select(doc, {'pos': 'n'}))
        return result, {}


class G_ADJ(GrammaticalForms):
    name_en = "Adjective incidence"
    name_pl = "Występowanie przymiotników"

    def count(self, doc):
        result = incidence(doc, select(doc, {'pos': 'adj'}))
        return result, {}


class G_ADV(GrammaticalForms):
    name_en = "Adverb incidence"
    name_pl = "Występowanie przysłówków"

    def count(self, doc):
        result = incidence(doc, select(doc, {'pos': 'adv'}))
        return result, {}


class G_PRO(GrammaticalForms):
    name_en = "Pronoun incidence"
    name_pl = "Występowanie zaimków"

    def count(self, doc):
        result = incidence(doc, select(doc, {'pos': 'pro'}))
        return result, {}


class G_PRO_DEM(GrammaticalForms):
    name_en = "Demonstrative pronouns incidence"
    name_pl = "Występowanie zaimków wskazujących"

    def count(self, doc):
        result = incidence(doc, select(doc, {'pos': 'pro', 'pronoun_type': 'dem'}))
        return result, {}


GRAMMATICAL_FORMS = [
    G_V,
    G_N,
    G_ADJ,
    G_ADV,
    G_PRO,
    G_PRO_DEM,
]

grammatical_forms_group = MetricsGroup([m() for m in GRAMMATICAL_FORMS])
