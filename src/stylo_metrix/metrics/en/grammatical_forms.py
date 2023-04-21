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


class GrammaticalForms(Category):
    lang = 'en'
    name_en = "Grammatical Forms"

class G_WOULD(Metric):
    category = GrammaticalForms
    name_en = "Would verb simple"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "would_ind_active"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class G_WOULD_PASSIVE(Metric):
    category = GrammaticalForms
    name_en = "Would verb passive"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "would_ind_passive"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class G_WOULD_PROGRESSIVE(Metric):
    category = GrammaticalForms
    name_en = "Would verb continuous"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "would_cont"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class G_WOULD_PERFECT(Metric):
    category = GrammaticalForms
    name_en = "Would verb perfect"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "would_perf_active"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class G_WOULD_PERFECT_PASSIVE(Metric):
    category = GrammaticalForms
    name_en = "Would verb perfect passive"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "would_perf_passive"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class G_SHOULD(Metric):
    category = GrammaticalForms
    name_en = "Should verb simple"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "should_ind_active"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class G_SHOULD_PASSIVE(Metric):
    category = GrammaticalForms
    name_en = "Should verb simple passive"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "should_ind_passive"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class G_SHALL(Metric):
    category = GrammaticalForms
    name_en = "Shall verb simple"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "shall_ind_active"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class G_SHALL_PASSIVE(Metric):
    category = GrammaticalForms
    name_en = "Shall verb simple passive"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "shall_ind_passive"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class G_SHOULD_PROGRESSIVE(Metric):
    category = GrammaticalForms
    name_en = "Should verb continuous"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "should_cont"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class G_SHOULD_PERFECT(Metric):
    category = GrammaticalForms
    name_en = "Should verb perfect"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "should_perf_active"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class G_SHOULD_PERFECT_PASSIVE(Metric):
    category = GrammaticalForms
    name_en = "Should verb perfect passive"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "should_perf_passive"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class G_MUST(Metric):
    category = GrammaticalForms
    name_en = "Must verb simple"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "must_ind_active"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class G_MUST_PASSIVE(Metric):
    category = GrammaticalForms
    name_en = "Must verb simple passive"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "must_ind_passive"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class G_MUST_PROGRESSIVE(Metric):
    category = GrammaticalForms
    name_en = "Must verb continuous"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "must_cont"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class G_MUST_PERFECT(Metric):
    category = GrammaticalForms
    name_en = "Must verb perfect"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "must_perf_active"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class G_MST_PERFECT_PASSIVE(Metric):
    category = GrammaticalForms
    name_en = "Must verb perfect passive"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "must_perf_passive"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class G_CAN(Metric):
    category = GrammaticalForms
    name_en = "Can verb simple"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "can_ind"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class G_CAN_PASSIVE(Metric):
    category = GrammaticalForms
    name_en = "Can verb simple passive"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "can_ind_passive"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class G_COULD(Metric):
    category = GrammaticalForms
    name_en = "Could verb simple"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "could_ind"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class G_COULD_PASSIVE(Metric):
    category = GrammaticalForms
    name_en = "Could verb simple passive"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "could_ind_passive"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class G_CAN_PROGRESSIVE(Metric):
    category = GrammaticalForms
    name_en = "Can verb continuous"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "can_cont"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class G_COULD_PROGRESSIVE(Metric):
    category = GrammaticalForms
    name_en = "Could verb continuous"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "could_cont"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class G_COULD_PERFECT(Metric):
    category = GrammaticalForms
    name_en = "Could verb perfect"

    def count(doc):
        search = [token.text for token in doc if token._.modal_verbs == "could_perf"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class G_COULD_PERFECT_PASSIVE(Metric):
    category = GrammaticalForms
    name_en = "Could verb perfect passive"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "could_perf_passive"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class G_MAY(Metric):
    category = GrammaticalForms
    name_en = "May verb simple"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "may_ind"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class G_MAY_PASSIVE(Metric):
    category = GrammaticalForms
    name_en = "May verb simple passive"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "may_ind_passive"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class G_MIGHT(Metric):
    category = GrammaticalForms
    name_en = "Might verb simple"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "might_ind"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class G_MIGHT_PASSIVE(Metric):
    category = GrammaticalForms
    name_en = "Might verb simple passive"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "might_ind_passive"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class G_MAY_PROGRESSIVE(Metric):
    category = GrammaticalForms
    name_en = "May verb continuous"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "may_cont"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class G_MIGTH_PERFECT(Metric):
    category = GrammaticalForms
    name_en = "Might verb perfect"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "might_perf"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class G_MIGHT_PERFECT_PASSIVE(Metric):
    category = GrammaticalForms
    name_en = "Might verb perfect passive"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "might_perf_passive"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class G_MAY_PERFECT_PASSIVE(Metric):
    category = GrammaticalForms
    name_en = "May verb perfect passive"

    def count(doc):
        search = [token for token in doc if token._.modal_verbs == "may_perf_passive"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class G_ADJ_POSITIVE(Metric):
    category = GrammaticalForms
    name_en = "Adjectives in positive degree"

    def count(doc):
        search = [token for token in doc if token._.adjectives == "positive_adjective"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class G_ADJ_COMPARATIVE(Metric):
    category = GrammaticalForms
    name_en = "Adjectives in comparative degree"

    def count(doc):
        search = [token for token in doc if token._.adjectives == "comparative_adjective"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class G_ADJ_SUPERLATIVE(Metric):
    category = GrammaticalForms
    name_en = "Adjectives in superlative degree"

    def count(doc):
        search = [token for token in doc if token._.adjectives == "superlative_adjective"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class G_ADV_POSITIVE(Metric):
    category = GrammaticalForms
    name_en = "Adverbs in positive degree"

    def count(doc):
        search = [token for token in doc if token._.adverbs == "positive_adverb"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class G_ADV_COMPARATIVE(Metric):
    category = GrammaticalForms
    name_en = "Adverbs in comparative degree"

    def count(doc):
        search = [token for token in doc if token._.adverbs == "comparative_adverb"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class G_ADV_SUPERLATIVE(Metric):
    category = GrammaticalForms
    name_en = "Adverbs in superlative degree"

    def count(doc):
        search = [token for token in doc if token._.adverbs == "superlative_adverb"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug
