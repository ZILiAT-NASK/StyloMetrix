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


from ...structures import Category, Metric
from ...utils import ratio


class General(Category):
    lang = "en"
    name_en = "General verb metrics"
    name_local = name_en


class VF_INFINITIVE(Metric):
    category = General
    name_en = "Incidence of verbs in infinitive"
    name_local = name_en

    def count(doc):
        debug = [token.text for token in doc if "VerbForm=Inf" in token.morph]
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug


class G_PASSIVE(Metric):
    category = General
    name_en = "Passive voice"
    name_local = name_en

    def count(doc):
        label_list = [
            "present_ind_passive",
            "present_cont_passive",
            "present_perfect_passive",
            "past_ind_passive",
            "past_cont_passive",
            "past_perf_passive",
            "future_simple_passive",
            "future_progr_passive",
            "future_perf_passive",
        ]
        debug = [token.text for token in doc if token._.verb_tense in label_list]
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug


class G_ACTIVE(Metric):
    category = General
    name_en = "Active voice"
    name_local = name_en

    def count(doc):
        label_list = [
            "present_simple",
            "present_ind_3p",
            "present_cont",
            "present_perfect",
            "present_perfect_cont",
            "past_simple",
            "past_ind_be",
            "past_cont",
            "past_perf",
            "past_perf_cont",
            "future_simple",
            "future_progr",
            "future_perfect",
            "future_perfect_cont",
        ]
        debug = [token.text for token in doc if token._.verb_tense in label_list]
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug


class G_PRESENT(Metric):
    category = General
    name_en = "Present tenses"
    name_local = name_en

    def count(doc):
        label_list = [
            "present_simple",
            "present_ind_3p",
            "present_cont",
            "present_perfect",
            "present_perfect_cont",
            "present_ind_passive",
            "present_cont_passive",
            "present_perfect_passive",
        ]
        debug = [token.text for token in doc if token._.verb_tense in label_list]
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug


class G_PAST(Metric):
    category = General
    name_en = "Past tenses"
    name_local = name_en

    def count(doc):
        label_list = [
            "past_simple",
            "past_ind_be",
            "past_cont",
            "past_perf",
            "past_perf_cont",
            "past_ind_passive",
            "past_cont_passive",
            "past_perf_passive",
        ]
        debug = [token.text for token in doc if token._.verb_tense in label_list]
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug


class G_FUTURE(Metric):
    category = General
    name_en = "Future tenses active"
    name_local = name_en

    def count(doc):
        label_list = [
            "future_simple",
            "future_progr",
            "future_perfect",
            "future_perfect_cont",
            "future_simple_passive",
            "future_progr_passive",
            "future_perf_passive",
        ]
        debug = [token.text for token in doc if token._.verb_tense in label_list]
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug


class G_MODALS_SIMPLE(Metric):
    category = General
    name_en = "Modal verbs active"
    name_local = name_en

    def count(doc):
        label_list = [
            "would_ind_active",
            "should_ind_active",
            "shall_ind_active",
            "must_ind_active",
            "can_ind",
            "could_ind",
            "may_ind",
            "might_ind",
            "would_ind_passive",
            "should_ind_passive",
            "shall_ind_passive",
            "must_ind_passive",
            "can_ind_passive",
            "could_ind_passive",
            "may_ind_passive",
            "might_ind_passive",
        ]
        debug = [token.text for token in doc if token._.modal_verbs in label_list]
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug


class G_MODALS_CONT(Metric):
    category = General
    name_en = "Modal verbs active"
    name_local = name_en

    def count(doc):
        label_list = [
            "would_cont",
            "should_cont",
            "must_cont",
            "can_cont",
            "could_cont",
            "may_cont",
        ]
        debug = [token.text for token in doc if token._.modal_verbs in label_list]
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug


class G_MODALS_PERFECT(Metric):
    category = General
    name_en = "Modal verbs active"
    name_local = name_en

    def count(doc):
        label_list = [
            "would_perf_active",
            "would_perf_passive",
            "should_perf_active",
            "should_perf_passive",
            "must_perf_passive",
            "could_perf_passive",
            "could_perf",
            "might_perf",
            "might_perf_passive",
            "must_perf_active",
            "must_perf_passive",
            "may_perf_passive",
        ]
        debug = [token.text for token in doc if token._.modal_verbs in label_list]
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug
