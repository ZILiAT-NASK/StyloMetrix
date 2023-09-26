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


from ...structures import Metric, Category
from ...utils import ratio


class VerbTenses(Category):
    lang = 'en'
    name_en = "Verbs Tenses"


class VT_PRESENT_SIMPLE(Metric):
    category = VerbTenses
    name_en = "Present Simple tense"

    def count(doc):
        search = [token for token in doc if token._.verb_tense == "present_simple"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_PRESENT_PROGRESSIVE(Metric):
    category = VerbTenses
    name_en = "Present Continuous tense"

    def count(doc):
        search = [token for token in doc if token._.verb_tense == "present_cont"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_PRESENT_PERFECT(Metric):
    category = VerbTenses
    name_en = "Present Perfect tense"

    def count(doc):
        search = [token for token in doc if token._.verb_tense == "present_perfect"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_PRESENT_PERFECT_PROGR(Metric):
    category = VerbTenses
    name_en = "Present Prefect Continuous tense"

    def count(doc):
        search = [token for token in doc if token._.verb_tense == "present_perfect_cont"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_PRESENT_SIMPLE_PASSIVE(Metric):
    category = VerbTenses
    name_en = "Present Simple passive"

    def count(doc):
        search = [token for token in doc if token._.verb_tense == "present_ind_passive"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_PRESENT_PROGR_PASSIVE(Metric):
    category = VerbTenses
    name_en = "Present Continuous passive"

    def count(doc):
        search = [token for token in doc if token._.verb_tense == "present_cont_passive"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_PRESENT_PERFECT_PASSIVE(Metric):
    category = VerbTenses
    name_en = "Present Perfect passive"

    def count(doc):
        search = [token for token in doc if token._.verb_tense == "present_perfect_passive"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_PAST_SIMPLE(Metric):
    category = VerbTenses
    name_en = "Past Simple tense"

    def count(doc):
        search = [token for token in doc if token._.verb_tense == "past_simple"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_PAST_SIMPLE_BE(Metric):
    category = VerbTenses
    name_en = "Past Simple 'to be' verb"

    def count(doc):
        search = [token for token in doc if token._.verb_tense == "past_ind_be"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_PAST_PROGR(Metric):
    category = VerbTenses
    name_en = "Past Continuous tense"

    def count(doc):
        search = [token for token in doc if token._.verb_tense == "past_cont"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_PAST_PERFECT(Metric):
    category = VerbTenses
    name_en = "Past Perfect tense"

    def count(doc):
        search = [token for token in doc if token._.verb_tense == "past_perf"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_PAST_PERFECT_PROGR(Metric):
    category = VerbTenses
    name_en = "Past Perfect Continuous tense"

    def count(doc):
        search = [token for token in doc if token._.verb_tense == "past_perf_cont"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_PAST_SIMPLE_PASSIVE(Metric):
    category = VerbTenses
    name_en = "Past Simple passive"

    def count(doc):
        search = [token for token in doc if token._.verb_tense == "past_ind_passive"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_PAST_POGR_PASSIVE(Metric):
    category = VerbTenses
    name_en = "Past Continuous passive"

    def count(doc):
        search = [token for token in doc if token._.verb_tense == "past_cont_passive"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_PAST_PERFECT_PASSIVE(Metric):
    category = VerbTenses
    name_en = "Past Perfect passive"

    def count(doc):
        search = [token for token in doc if token._.verb_tense == "past_perf_passive"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_FUTURE_SIMPLE(Metric):
    category = VerbTenses
    name_en = "Future Simple tense"

    def count(doc):
        search = [token for token in doc if token._.verb_tense == "future_simple"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_FUTURE_PROGRESSIVE(Metric):
    category = VerbTenses
    name_en = "Future Continuous tense"

    def count(doc):
        search = [token for token in doc if token._.verb_tense == "future_progr"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_FUTURE_PERFECT(Metric):
    category = VerbTenses
    name_en = "Future Perfect tense"

    def count(doc):
        search = [token for token in doc if token._.verb_tense == "future_perfect"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_FUTURE_PERFECT_PROGR(Metric):
    category = VerbTenses
    name_en = "Future Perfect Continuous tense"

    def count(doc):
        search = [token for token in doc if token._.verb_tense == "future_perfect_cont"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_FUTURE_SIMPLE_PASSIVE(Metric):
    category = VerbTenses
    name_en = "Future Simple passive"

    def count(doc):
        search = [token for token in doc if token._.verb_tense == "future_simple_passive"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_FUTURE_PROGR_PASSIVE(Metric):
    category = VerbTenses
    name_en = "Future Continuous passive"

    def count(doc):
        search = [token for token in doc if token._.verb_tense == "future_progr_passive"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_FUTURE_PERFECT_PASSIVE(Metric):
    category = VerbTenses
    name_en = "Present Perfect passive"

    def count(doc):
        search = [token for token in doc if token._.verb_tense == "future_perf_passive"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug

"""
MODAL VERBS
"""

class VT_WOULD(Metric):
    category = VerbTenses
    name_en = "Would verb simple"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "would_ind_active"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_WOULD_PASSIVE(Metric):
    category = VerbTenses
    name_en = "Would verb passive"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "would_ind_passive"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_WOULD_PROGRESSIVE(Metric):
    category = VerbTenses
    name_en = "Would verb continuous"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "would_cont"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_WOULD_PERFECT(Metric):
    category = VerbTenses
    name_en = "Would verb perfect"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "would_perf_active"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_WOULD_PERFECT_PASSIVE(Metric):
    category = VerbTenses
    name_en = "Would verb perfect passive"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "would_perf_passive"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_SHOULD(Metric):
    category = VerbTenses
    name_en = "Should verb simple"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "should_ind_active"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_SHOULD_PASSIVE(Metric):
    category = VerbTenses
    name_en = "Should verb simple passive"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "should_ind_passive"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_SHALL(Metric):
    category = VerbTenses
    name_en = "Shall verb simple"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "shall_ind_active"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_SHALL_PASSIVE(Metric):
    category = VerbTenses
    name_en = "Shall verb simple passive"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "shall_ind_passive"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_SHOULD_PROGRESSIVE(Metric):
    category = VerbTenses
    name_en = "Should verb continuous"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "should_cont"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_SHOULD_PERFECT(Metric):
    category = VerbTenses
    name_en = "Should verb perfect"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "should_perf_active"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_SHOULD_PERFECT_PASSIVE(Metric):
    category = VerbTenses
    name_en = "Should verb perfect passive"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "should_perf_passive"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_MUST(Metric):
    category = VerbTenses
    name_en = "Must verb simple"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "must_ind_active"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_MUST_PASSIVE(Metric):
    category = VerbTenses
    name_en = "Must verb simple passive"

    def count(doc):
        search = []
        for token in doc:
            if token.lemma_ == "must" and token.head.tag_ == "VBN":
                head = token.head

                for tkn in head.children:
                    if tkn.text == "be" and tkn.dep_ == "auxpass":
                        search.append(head)
                        search.append(token)
                        search.append(tkn)

                for t in head.subtree:
                    if t.tag_ == "VBN" and t.dep_ == "conj" and head in search:
                        search.append(t)
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_MUST_PROGRESSIVE(Metric):
    category = VerbTenses
    name_en = "Must verb continuous"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "must_cont"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_MUST_PERFECT(Metric):
    category = VerbTenses
    name_en = "Must verb perfect"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "must_perf_active"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_MST_PERFECT_PASSIVE(Metric):
    category = VerbTenses
    name_en = "Must verb perfect passive"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "must_perf_passive"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_CAN(Metric):
    category = VerbTenses
    name_en = "Can verb simple"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "can_ind"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_CAN_PASSIVE(Metric):
    category = VerbTenses
    name_en = "Can verb simple passive"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "can_ind_passive"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_COULD(Metric):
    category = VerbTenses
    name_en = "Could verb simple"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "could_ind"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_COULD_PASSIVE(Metric):
    category = VerbTenses
    name_en = "Could verb simple passive"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "could_ind_passive"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_CAN_PROGRESSIVE(Metric):
    category = VerbTenses
    name_en = "Can verb continuous"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "can_cont"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_COULD_PROGRESSIVE(Metric):
    category = VerbTenses
    name_en = "Could verb continuous"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "could_cont"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_COULD_PERFECT(Metric):
    category = VerbTenses
    name_en = "Could + perfect infinitive"

    def count(doc):
        search = [token.text for token in doc if token._.modal_verbs == "could_perf"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_COULD_PERFECT_PASSIVE(Metric):
    category = VerbTenses
    name_en = "Could verb perfect passive"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "could_perf_passive"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_MAY(Metric):
    category = VerbTenses
    name_en = "May verb simple"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "may_ind"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_MAY_PASSIVE(Metric):
    category = VerbTenses
    name_en = "May verb simple passive"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "may_ind_passive"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_MIGHT(Metric):
    category = VerbTenses
    name_en = "Might verb simple"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "might_ind"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_MIGHT_PASSIVE(Metric):
    category = VerbTenses
    name_en = "Might verb simple passive"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "might_ind_passive"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_MAY_PROGRESSIVE(Metric):
    category = VerbTenses
    name_en = "May verb continuous"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "may_cont"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_MIGTH_PERFECT(Metric):
    category = VerbTenses
    name_en = "Might verb perfect"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "might_perf"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_MIGHT_PERFECT_PASSIVE(Metric):
    category = VerbTenses
    name_en = "Might verb perfect passive"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "might_perf_passive"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class VT_MAY_PERFECT_PASSIVE(Metric):
    category = VerbTenses
    name_en = "May verb perfect passive"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "may_perf_passive"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug

