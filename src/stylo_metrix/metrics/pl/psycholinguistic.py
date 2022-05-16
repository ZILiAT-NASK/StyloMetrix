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


class Psycholinguistic(Metric, ABC):
    category_pl = "Psycholinguistic"
    category_en = "Psycholingwistyczne"

    def get_above_mean(self, doc, nr_param):
        values = [token._.affective_norms[nr_param] for token in doc if token._.affective_norms is not None]
        search = [value for value in values if value > doc._.an_means[nr_param]]
        result = incidence(doc, search)
        return result

    def get_below_mean(self, doc, nr_param):
        values = [token._.affective_norms[nr_param] for token in doc if token._.affective_norms is not None]
        search = [value for value in values if value < doc._.an_means[nr_param]]
        result = incidence(doc, search)
        return result


class PS_M_VALa(Psycholinguistic):
    name_en = "Incidence of words with more than mean valence"
    name_pl = "Występowanie wyrazów posiadających więcej niż średni znak emocji (valence)"

    def count(self, document):
        result = self.get_above_mean(document, 0)
        return result, {}


class PS_M_VALb(Psycholinguistic):
    name_en = "Incidence of words with less than mean valence"
    name_pl = "Występowanie wyrazów posiadających mniej niż średni znak emocji (valence)"

    def count(self, document):
        result = self.get_below_mean(document, 0)
        return result, {}


class PS_M_AROa(Psycholinguistic):
    name_en = "Incidence of words with more than mean arousal"
    name_pl = "Występowanie wyrazów posiadających więcej niż średnie pobudzenie (arousal)"

    def count(self, document):
        result = self.get_above_mean(document, 1)
        return result, {}


class PS_M_AROb(Psycholinguistic):
    name_en = "Incidence of words with less than mean arousal"
    name_pl = "Występowanie wyrazów posiadających mniej niż średnie pobudzenie (arousal)"

    def count(self, document):
        result = self.get_below_mean(document, 1)
        return result, {}


class PS_M_DOMa(Psycholinguistic):
    name_en = "Incidence of words with more than mean dominance"
    name_pl = "Występowanie wyrazów posiadających więcej niż średnie opanowanie (dominance)"

    def count(self, document):
        result = self.get_above_mean(document, 2)
        return result, {}


class PS_M_DOMb(Psycholinguistic):
    name_en = "Incidence of words with less than mean dominance"
    name_pl = "Występowanie wyrazów posiadających mniej niż średnie opanowanie (dominance)"

    def count(self, document):
        result = self.get_below_mean(document, 2)
        return result, {}


class PS_M_ORIa(Psycholinguistic):
    name_en = "Incidence of words with more than mean origin"
    name_pl = "Występowanie wyrazów posiadających więcej niż średnie pochodzenie (origin)"

    def count(self, document):
        result = self.get_above_mean(document, 3)
        return result, {}


class PS_M_ORIb(Psycholinguistic):
    name_en = "Incidence of words with less than mean origin"
    name_pl = "Występowanie wyrazów posiadających mniej niż średnie pochodzenie (origin)"

    def count(self, document):
        result = self.get_below_mean(document, 3)
        return result, {}


class PS_M_SIGa(Psycholinguistic):
    name_en = "Incidence of words with more than mean significance"
    name_pl = "Występowanie wyrazów posiadających więcej niż średnie znaczenie (significance)"

    def count(self, document):
        result = self.get_above_mean(document, 4)
        return result, {}


class PS_M_SIGb(Psycholinguistic):
    name_en = "Incidence of words with less than mean significance"
    name_pl = "Występowanie wyrazów posiadających mniej niż średnie znaczenie (significance)"

    def count(self, document):
        result = self.get_below_mean(document, 4)
        return result, {}


class PS_M_CONa(Psycholinguistic):
    name_en = "Incidence of words with more than mean concreteness"
    name_pl = "Występowanie wyrazów posiadających więcej niż średnią konkretność (concreteness)"

    def count(self, document):
        result = self.get_above_mean(document, 5)
        return result, {}


class PS_M_CONb(Psycholinguistic):
    name_en = "Incidence of words with less than mean concreteness"
    name_pl = "Występowanie wyrazów posiadających mniej niż średnią konkretność (concreteness)"

    def count(self, document):
        result = self.get_below_mean(document, 5)
        return result, {}


class PS_M_IMGa(Psycholinguistic):
    name_en = "Incidence of words with more than mean imageability"
    name_pl = "Występowanie wyrazów posiadających więcej niż średnia wyobrażalność (imageability)"

    def count(self, document):
        result = self.get_above_mean(document, 6)
        return result, {}


class PS_M_IMGb(Psycholinguistic):
    name_en = "Incidence of words with less than mean imageability"
    name_pl = "Występowanie wyrazów posiadających mniej niż średnia wyobrażalność (imageability)"

    def count(self, document):
        result = self.get_below_mean(document, 6)
        return result, {}


class PS_M_AGEa(Psycholinguistic):
    name_en = "Incidence of words with more than mean age of acquisition"
    name_pl = "Występowanie wyrazów posiadających więcej niż średni wiek akwizycji (age of acquisition)"

    def count(self, document):
        result = self.get_above_mean(document, 7)
        return result, {}


class PS_M_AGEb(Psycholinguistic):
    name_en = "Incidence of words with less than mean age of acquisition"
    name_pl = "Występowanie wyrazów posiadających mniej niż średni wiek akwizycji (age of acquisition)"

    def count(self, document):
        result = self.get_below_mean(document, 7)
        return result, {}


PSYCHOLINGUISTIC_ABOVE_MEAN = [
    PS_M_VALa,
    PS_M_AROa,
    PS_M_DOMa,
    PS_M_ORIa,
    PS_M_SIGa,
    PS_M_CONa,
    PS_M_IMGa,
    PS_M_AGEa,
]

PSYCHOLINGUISTIC_BELOW_MEAN = [
    PS_M_VALb,
    PS_M_AROb,
    PS_M_DOMb,
    PS_M_ORIb,
    PS_M_SIGb,
    PS_M_CONb,
    PS_M_IMGb,
    PS_M_AGEb,
]

psycholinguistic_above_mean_group = MetricsGroup([m() for m in PSYCHOLINGUISTIC_ABOVE_MEAN])
psycholinguistic_below_mean_group = MetricsGroup([m() for m in PSYCHOLINGUISTIC_BELOW_MEAN])
psycholinguistic_group = psycholinguistic_above_mean_group + psycholinguistic_below_mean_group
