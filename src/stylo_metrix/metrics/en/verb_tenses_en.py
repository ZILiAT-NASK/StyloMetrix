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


class VerbTenses(Category):
    lang = 'en'
    name_en = "Verbs Tenses"


class VT_PRESENT_ACTIVE(Metric):
    category = VerbTenses
    name_en = "Present tenses active"

    def count(doc):
        label_list = ["present_simple", "present_ind_3p",
                      "present_cont", "present_perfect",
                      "present_perfect_cont"]
        search = [token for token in doc if token._.verb_tense in label_list]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class VT_PRESENT_PASSIVE(Metric):
    category = VerbTenses
    name_en = "Present tenses passive"

    def count(doc):
        label_list = ["present_ind_passive", "present_cont_passive",
                      "present_perfect_passive"]
        search = [token for token in doc if token._.verb_tense in label_list]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class VT_PAST_ACTIVE(Metric):
    category = VerbTenses
    name_en = "Past tenses active"

    def count(doc):
        label_list = ["past_simple", "past_ind_be",
                      "past_cont", "past_perf", "past_perf_cont"]
        search = [token for token in doc if token._.verb_tense in label_list]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class VT_PAST_PASSIVE(Metric):
    category = VerbTenses
    name_en = "Past tenses passive"

    def count(doc):
        label_list = ["past_ind_passive", "past_cont_passive", "past_perf_passive"]
        search = [token for token in doc if token._.verb_tense in label_list]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class VT_FUTURE_ACTIVE(Metric):
    category = VerbTenses
    name_en = "Future tenses active"

    def count(doc):
        label_list = ["future_simple", "future_progr", "future_perfect", "future_perfect_cont"]
        search = [token for token in doc if token._.verb_tense in label_list]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class VT_FUTURE_PASSIVE(Metric):
    category = VerbTenses
    name_en = "Future tenses passive"

    def count(doc):
        label_list = ["future_simple_passive", "future_progr_passive", "future_perf_passive"]
        search = [token for token in doc if token._.verb_tense in label_list]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class VT_MODALS_ACTIVE(Metric):
    category = VerbTenses
    name_en = "Modal verbs active"

    def count(doc):
        label_list = ["would_ind_active", "would_cont", "would_perf_active",
                      "should_ind_active", "shall_ind_active", "should_cont", "should_perf_active",
                      "must_ind_active", "must_cont", "must_perf_active", "can_ind", "could_ind",
                      "can_cont", "could_cont", "could_perf", "may_ind", "might_ind", "may_cont",
                      "might_perf"]
        search = [token for token in doc if token._.modal_verbs in label_list]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class VT_MODALS_PASSIVE(Metric):
    category = VerbTenses
    name_en = "Modal verbs active"

    def count(doc):
        label_list = ["would_ind_passive", "would_perf_passive", "should_ind_passive",
                      "shall_ind_passive", "should_perf_passive", "must_ind_passive",
                      "must_perf_passive", "can_ind_passive", "could_ind_passive", "could_perf_passive",
                      "may_ind_passive", "might_ind_passive", "might_perf_passive", "may_perf_passive"]
        search = [token for token in doc if token._.modal_verbs in label_list]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class VT_PRESENT_SIMPLE(Metric):
    category = VerbTenses
    name_en = "Present Simple tense"

    def count(doc):
        search = [token for token in doc if token._.verb_tense == "present_simple"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class VT_PRESENT_PROGRESSIVE(Metric):
    category = VerbTenses
    name_en = "Present Continuous tense"

    def count(doc):
        search = [token for token in doc if token._.verb_tense == "present_cont"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class VT_PRESENT_PERFECT(Metric):
    category = VerbTenses
    name_en = "Present Perfect tense"

    def count(doc):
        search = [token for token in doc if token._.verb_tense == "present_perfect"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class VT_PRESENT_PERFECT_PROGR(Metric):
    category = VerbTenses
    name_en = "Present Prefect Continuous tense"

    def count(doc):
        search = [token for token in doc if token._.verb_tense == "present_perfect_cont"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class VT_PRESENT_SIMPLE_PASSIVE(Metric):
    category = VerbTenses
    name_en = "Present Simple passive"

    def count(doc):
        search = [token for token in doc if token._.verb_tense == "present_ind_passive"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class VT_PRESENT_PROGR_PASSIVE(Metric):
    category = VerbTenses
    name_en = "Present Continuous passive"

    def count(doc):
        search = [token for token in doc if token._.verb_tense == "present_cont_passive"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class VT_PRESENT_PERFECT_PASSIVE(Metric):
    category = VerbTenses
    name_en = "Present Perfect passive"

    def count(doc):
        search = [token for token in doc if token._.verb_tense == "present_perfect_passive"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class VT_PAST_SIMPLE(Metric):
    category = VerbTenses
    name_en = "Past Simple tense"

    def count(doc):
        search = [token for token in doc if token._.verb_tense == "past_simple"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class VT_PAST_SIMPLE_BE(Metric):
    category = VerbTenses
    name_en = "Past Simple 'to be' verb"

    def count(doc):
        search = [token for token in doc if token._.verb_tense == "past_ind_be"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class VT_PAST_PROGR(Metric):
    category = VerbTenses
    name_en = "Past Continuous tense"

    def count(doc):
        search = [token for token in doc if token._.verb_tense == "past_cont"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class VT_PAST_PERFECT(Metric):
    category = VerbTenses
    name_en = "Past Perfect tense"

    def count(doc):
        search = [token for token in doc if token._.verb_tense == "past_perf"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class VT_PAST_PERFECT_PROGR(Metric):
    category = VerbTenses
    name_en = "Past Perfect Continuous tense"

    def count(doc):
        search = [token for token in doc if token._.verb_tense == "past_perf_cont"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class VT_PAST_SIMPLE_PASSIVE(Metric):
    category = VerbTenses
    name_en = "Past Simple passive"

    def count(doc):
        search = [token for token in doc if token._.verb_tense == "past_ind_passive"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class VT_PAST_POGR_PASSIVE(Metric):
    category = VerbTenses
    name_en = "Past Continuous passive"

    def count(doc):
        search = [token for token in doc if token._.verb_tense == "past_cont_passive"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class VT_PAST_PERFECT_PASSIVE(Metric):
    category = VerbTenses
    name_en = "Past Perfect passive"

    def count(doc):
        search = [token for token in doc if token._.verb_tense == "past_perf_passive"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class VT_FUTURE_SIMPLE(Metric):
    category = VerbTenses
    name_en = "Future Simple tense"

    def count(doc):
        search = [token for token in doc if token._.verb_tense == "future_simple"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class VT_FUTURE_PROGRESSIVE(Metric):
    category = VerbTenses
    name_en = "Future Continuous tense"

    def count(doc):
        search = [token for token in doc if token._.verb_tense == "future_progr"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class VT_FUTURE_PERFECT(Metric):
    category = VerbTenses
    name_en = "Future Perfect tense"

    def count(doc):
        search = [token for token in doc if token._.verb_tense == "future_perfect"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class VT_FUTURE_PERFECT_PROGR(Metric):
    category = VerbTenses
    name_en = "Future Perfect Continuous tense"

    def count(doc):
        search = [token for token in doc if token._.verb_tense == "future_perfect_cont"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class VT_FUTURE_SIMPLE_PASSIVE(Metric):
    category = VerbTenses
    name_en = "Future Simple passive"

    def count(doc):
        search = [token for token in doc if token._.verb_tense == "future_simple_passive"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class VT_FUTURE_PROGR_PASSIVE(Metric):
    category = VerbTenses
    name_en = "Future Continuous passive"

    def count(doc):
        search = [token for token in doc if token._.verb_tense == "future_progr_passive"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class VT_FUTURE_PERFECT_PASSIVE(Metric):
    category = VerbTenses
    name_en = "Present Perfect passive"

    def count(doc):
        search = [token for token in doc if token._.verb_tense == "future_perf_passive"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug
