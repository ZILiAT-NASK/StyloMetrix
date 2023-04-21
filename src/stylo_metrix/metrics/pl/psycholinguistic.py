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

from stylo_metrix.utils import incidence


class Psycholinguistic(Category):
    lang = 'pl'
    name_en = "Psycholinguistic"
    name_local = "Psycholingwistyczne"


class AboveMeanCount:
    @classmethod
    def count(cls, doc):
        search = [token for token in doc if token._.affective_norms is not None
                  and token._.affective_norms[cls.param] > doc._.an_means[cls.param]]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug

class BelowMeanCount:
    @classmethod
    def count(cls, doc):
        search = [token for token in doc if token._.affective_norms is not None
                  and token._.affective_norms[cls.param] < doc._.an_means[cls.param]]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class PS_M_VALa(Metric, AboveMeanCount):
    category = Psycholinguistic
    param = 0
    name_en = "Words having more than mean valence"
    name_local = "Wyrazy posiadające więcej niż średni znak emocji (valence)"


class PS_M_VALb(Metric, BelowMeanCount):
    category = Psycholinguistic
    param = 0
    name_en = "Words having less than mean valence"
    name_local = "Wyrazy posiadające mniej niż średni znak emocji (valence)"


class PS_M_AROa(Metric, AboveMeanCount):
    category = Psycholinguistic
    param = 1
    name_en = "Words having more than mean arousal"
    name_local = "Wyrazy posiadające więcej niż średnie pobudzenie (arousal)"


class PS_M_AROb(Metric, BelowMeanCount):
    category = Psycholinguistic
    param = 1
    name_en = "Words having less than mean arousal"
    name_local = "Wyrazy posiadające mniej niż średnie pobudzenie (arousal)"


class PS_M_DOMa(Metric, AboveMeanCount):
    category = Psycholinguistic
    param = 2
    name_en = "Words having more than mean dominance"
    name_local = "Wyrazy posiadające więcej niż średnie opanowanie (dominance)"


class PS_M_DOMb(Metric, BelowMeanCount):
    category = Psycholinguistic
    param = 2
    name_en = "Words having less than mean dominance"
    name_local = "Wyrazy posiadające mniej niż średnie opanowanie (dominance)"


class PS_M_ORIa(Metric, AboveMeanCount):
    category = Psycholinguistic
    param = 3
    name_en = "Words having more than mean origin"
    name_local = "Wyrazy posiadające więcej niż średnie pochodzenie (origin)"


class PS_M_ORIb(Metric, BelowMeanCount):
    category = Psycholinguistic
    param = 3
    name_en = "Words having less than mean origin"
    name_local = "Wyrazy posiadające mniej niż średnie pochodzenie (origin)"


class PS_M_SIGa(Metric, AboveMeanCount):
    category = Psycholinguistic
    param = 4
    name_en = "Words having more than mean significance"
    name_local = "Wyrazy posiadające więcej niż średnie znaczenie (significance)"


class PS_M_SIGb(Metric, BelowMeanCount):
    category = Psycholinguistic
    param = 4
    name_en = "Words having less than mean significance"
    name_local = "Wyrazy posiadające mniej niż średnie znaczenie (significance)"


class PS_M_CONa(Metric, AboveMeanCount):
    category = Psycholinguistic
    param = 5
    name_en = "Words having more than mean concreteness"
    name_local = "Wyrazy posiadające więcej niż średnią konkretność (concreteness)"


class PS_M_CONb(Metric, BelowMeanCount):
    category = Psycholinguistic
    param = 5
    name_en = "Words having less than mean concreteness"
    name_local = "Wyrazy posiadające mniej niż średnią konkretność (concreteness)"


class PS_M_IMGa(Metric, AboveMeanCount):
    category = Psycholinguistic
    param = 6
    name_en = "Words having more than mean imageability"
    name_local = "Wyrazy posiadające więcej niż średnia wyobrażalność (imageability)"


class PS_M_IMGb(Metric, BelowMeanCount):
    category = Psycholinguistic
    param = 6
    name_en = "Words having less than mean imageability"
    name_local = "Wyrazy posiadające mniej niż średnia wyobrażalność (imageability)"


class PS_M_AGEa(Metric, AboveMeanCount):
    category = Psycholinguistic
    param = 7
    name_en = "Words having more than mean age of acquisition"
    name_local = "Wyrazy posiadające więcej niż średni wiek akwizycji (age of acquisition)"


class PS_M_AGEb(Metric, BelowMeanCount):
    category = Psycholinguistic
    param = 7
    name_en = "Words having less than mean age of acquisition"
    name_local = "Wyrazy posiadające mniej niż średni wiek akwizycji (age of acquisition)"


# PSYCHOLINGUISTIC_ABOVE_MEAN = [
#     PS_M_VALa,
#     PS_M_AROa,
#     PS_M_DOMa,
#     PS_M_ORIa,
#     PS_M_SIGa,
#     PS_M_CONa,
#     PS_M_IMGa,
#     PS_M_AGEa,
# ]

# PSYCHOLINGUISTIC_BELOW_MEAN = [
#     PS_M_VALb,
#     PS_M_AROb,
#     PS_M_DOMb,
#     PS_M_ORIb,
#     PS_M_SIGb,
#     PS_M_CONb,
#     PS_M_IMGb,
#     PS_M_AGEb,
# ]

# psycholinguistic_above_mean_group = MetricsGroup([m() for m in PSYCHOLINGUISTIC_ABOVE_MEAN])
# psycholinguistic_below_mean_group = MetricsGroup([m() for m in PSYCHOLINGUISTIC_BELOW_MEAN])
# psycholinguistic_group = psycholinguistic_above_mean_group + psycholinguistic_below_mean_group
