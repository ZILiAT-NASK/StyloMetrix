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
from stylo_metrix.utils import ratio


class GrammaticalForms(Metric, ABC):
    category_en = "Grammatical Forms"

    def incidence(self, doc, attr_name, attr_value, pos_range):
        if pos_range == "all":
            words = [token for token in doc if token.pos_ not in 'PUNCT SPACE']

        else:
            words = [token for token in doc if token._.pos == pos_range]

        search = [getattr(getattr(token, '_'), attr_name) == attr_value for token in words]

        result = ratio(sum(search), len(words))
        return result, {}


class G_V(GrammaticalForms):
    name_en = "Verb incidence"

    def count(self, doc):
        result = self.incidence(doc, attr_name='pos', attr_value='v', pos_range='all')
        return result


class G_PR_S(GrammaticalForms):
    name_en = "Present Simple Tense"

    def count(self, doc):
        result = self.incidence(doc, attr_name='verb_tense', attr_value='present_simple', pos_range='all')
        return result


class G_PR_IND_3(GrammaticalForms):
    name_en = "Present Simple 3rd Person"

    def count(self, doc):
        result = self.incidence(doc, attr_name='verb_tense', attr_value='present_ind_3p', pos_range='all')
        return result


class G_PR_CONT(GrammaticalForms):
    name_en = "Present Continuous Tense"

    def count(self, doc):
        result = self.incidence(doc, attr_name='verb_tense', attr_value='present_cont', pos_range='all')
        return result


class G_PR_P(GrammaticalForms):
    name_en = "Present Perfect Tense"

    def count(self, doc):
        result = self.incidence(doc, attr_name='verb_tense', attr_value='present_perfect', pos_range='all')
        return result


class G_PR_P_CON(GrammaticalForms):
    name_en = "Present Prefect Continuous Tense"

    def count(self, doc):
        result = self.incidence(doc, attr_name='verb_tense', attr_value='present_perfect_cont', pos_range='all')
        return result


class G_PR_S_P(GrammaticalForms):
    name_en = "Present Simple Passive"

    def count(self, doc):
        result = self.incidence(doc, attr_name='verb_tense', attr_value='present_ind_passive', pos_range='all')
        return result


class G_PR_CONT_P(GrammaticalForms):
    name_en = "Present Continuous Passive"

    def count(self, doc):
        result = self.incidence(doc, attr_name='verb_tense', attr_value='present_cont_passive', pos_range='all')
        return result


class G_PR_PRF_P(GrammaticalForms):
    name_en = "Present Perfect Passive"

    def count(self, doc):
        result = self.incidence(doc, attr_name='verb_tense', attr_value='present_perfect_passive', pos_range='all')
        return result


class G_PA_S(GrammaticalForms):
    name_en = "Past Simple Tense"

    def count(self, doc):
        result = self.incidence(doc, attr_name='verb_tense', attr_value='past_simple', pos_range='all')
        return result


class G_PA_S_BE(GrammaticalForms):
    name_en = "Past Simple 'to be'"

    def count(self, doc):
        result = self.incidence(doc, attr_name='verb_tense', attr_value='past_ind_be', pos_range='all')
        return result


class G_PA_CON(GrammaticalForms):
    name_en = "Past Continuous Tense"

    def count(self, doc):
        result = self.incidence(doc, attr_name='verb_tense', attr_value='past_cont', pos_range='all')
        return result


class G_PA_PRF(GrammaticalForms):
    name_en = "Past Perfect Tense"

    def count(self, doc):
        result = self.incidence(doc, attr_name='verb_tense', attr_value='past_perf', pos_range='all')
        return result


class G_PA_PRF_CONT(GrammaticalForms):
    name_en = "Past Perfect Continuous Tense"

    def count(self, doc):
        result = self.incidence(doc, attr_name='verb_tense', attr_value='past_perf_cont', pos_range='all')
        return result


class G_PA_S_P(GrammaticalForms):
    name_en = "Past Simple Passive"

    def count(self, doc):
        result = self.incidence(doc, attr_name='verb_tense', attr_value='past_ind_passive', pos_range='all')
        return result


class G_PA_CON_P(GrammaticalForms):
    name_en = "Past Continuous Passive"

    def count(self, doc):
        result = self.incidence(doc, attr_name='verb_tense', attr_value='past_cont_passive', pos_range='all')
        return result


class G_PA_P_P(GrammaticalForms):
    name_en = "Past Perfect Passive"

    def count(self, doc):
        result = self.incidence(doc, attr_name='verb_tense', attr_value='past_perf_passive', pos_range='all')
        return result


class G_FT_S(GrammaticalForms):
    name_en = "Future Simple Tense"

    def count(self, doc):
        result = self.incidence(doc, attr_name='verb_tense', attr_value='future_simple', pos_range='all')
        return result


class G_FT_CON(GrammaticalForms):
    name_en = "Future Continuous Tense"

    def count(self, doc):
        result = self.incidence(doc, attr_name='verb_tense', attr_value='future_progr', pos_range='all')
        return result


class G_FT_P(GrammaticalForms):
    name_en = "Future Perfect Tense"

    def count(self, doc):
        result = self.incidence(doc, attr_name='verb_tense', attr_value='future_perfect', pos_range='all')
        return result


class G_FT_P_CON(GrammaticalForms):
    name_en = "Future Perfect Continuous"

    def count(self, doc):
        result = self.incidence(doc, attr_name='verb_tense', attr_value='future_perfect_cont', pos_range='all')
        return result


class G_FT_S_P(GrammaticalForms):
    name_en = "Future Simple Passive"

    def count(self, doc):
        result = self.incidence(doc, attr_name='verb_tense', attr_value='future_simple_passive', pos_range='all')
        return result


class G_FT_PR_P(GrammaticalForms):
    name_en = "Future Continuous Passive"

    def count(self, doc):
        result = self.incidence(doc, attr_name='verb_tense', attr_value='future_progr_passive', pos_range='all')
        return result


class G_FT_P_P(GrammaticalForms):
    name_en = "Present Perfect Passive"

    def count(self, doc):
        result = self.incidence(doc, attr_name='verb_tense', attr_value='future_perf_passive', pos_range='all')
        return result



class G_WLD(GrammaticalForms):
    name_en = "Would Simple"

    def count(self, doc):
        result = self.incidence(doc, attr_name='modal_verbs', attr_value='would_ind_active', pos_range='all')
        return result


class G_WLD_P(GrammaticalForms):
    name_en = "Would Passive"

    def count(self, doc):
        result = self.incidence(doc, attr_name='modal_verbs', attr_value='would_ind_passive', pos_range='all')
        return result


class G_WLD_CON(GrammaticalForms):
    name_en = "Would Continuous"

    def count(self, doc):
        result = self.incidence(doc, attr_name='modal_verbs', attr_value='would_cont', pos_range='all')
        return result


class G_WLD_PRF(GrammaticalForms):
    name_en = "Would Perfect"

    def count(self, doc):
        result = self.incidence(doc, attr_name='modal_verbs', attr_value='would_perf_active', pos_range='all')
        return result


class G_WLD_P_P(GrammaticalForms):
    name_en = "Would Perfect Passive"

    def count(self, doc):
        result = self.incidence(doc, attr_name='modal_verbs', attr_value='would_perf_passive', pos_range='all')
        return result


class G_SHLD(GrammaticalForms):
    name_en = "Should Simple"

    def count(self, doc):
        result = self.incidence(doc, attr_name='modal_verbs', attr_value='should_ind_active', pos_range='all')
        return result


class G_SHLD_P(GrammaticalForms):
    name_en = "Should Simple Passive"

    def count(self, doc):
        result = self.incidence(doc, attr_name='modal_verbs', attr_value='should_ind_passive', pos_range='all')
        return result


class G_SHLL(GrammaticalForms):
    name_en = "Shall Simple"

    def count(self, doc):
        result = self.incidence(doc, attr_name='modal_verbs', attr_value='shall_ind_active', pos_range='all')
        return result


class G_SHLL_P(GrammaticalForms):
    name_en = "Shall Simple Passive"

    def count(self, doc):
        result = self.incidence(doc, attr_name='modal_verbs', attr_value='shall_ind_passive', pos_range='all')
        return result


class G_SHLD_CON(GrammaticalForms):
    name_en = "Should Continuous"

    def count(self, doc):
        result = self.incidence(doc, attr_name='modal_verbs', attr_value='should_cont', pos_range='all')
        return result


class G_SHLD_PRF(GrammaticalForms):
    name_en = "Should Perfect"

    def count(self, doc):
        result = self.incidence(doc, attr_name='modal_verbs', attr_value='should_perf_active', pos_range='all')
        return result


class G_SHLD_P_P(GrammaticalForms):
    name_en = "Should Perfect Passive"

    def count(self, doc):
        result = self.incidence(doc, attr_name='modal_verbs', attr_value='should_perf_passive', pos_range='all')
        return result


class G_MST(GrammaticalForms):
    name_en = "Must Simple"

    def count(self, doc):
        result = self.incidence(doc, attr_name='modal_verbs', attr_value='must_ind_active', pos_range='all')
        return result


class G_MST_P(GrammaticalForms):
    name_en = "Must Simple Passive"

    def count(self, doc):
        result = self.incidence(doc, attr_name='modal_verbs', attr_value='must_ind_passive', pos_range='all')
        return result


class G_MST_CON(GrammaticalForms):
    name_en = "Must Continuous"

    def count(self, doc):
        result = self.incidence(doc, attr_name='modal_verbs', attr_value='must_cont', pos_range='all')
        return result


class G_MST_PRF(GrammaticalForms):
    name_en = "Must Perfect"

    def count(self, doc):
        result = self.incidence(doc, attr_name='modal_verbs', attr_value='must_perf_active', pos_range='all')
        return result


class G_MST_P_P(GrammaticalForms):
    name_en = "Must Perfect Passive"

    def count(self, doc):
        result = self.incidence(doc, attr_name='modal_verbs', attr_value='must_perf_passive', pos_range='all')
        return result


class G_CAN(GrammaticalForms):
    name_en = "Can Simple"

    def count(self, doc):
        result = self.incidence(doc, attr_name='modal_verbs', attr_value='can_ind', pos_range='all')
        return result


class G_CAN_P(GrammaticalForms):
    name_en = "Can Simple Passive"

    def count(self, doc):
        result = self.incidence(doc, attr_name='modal_verbs', attr_value='can_ind_passive', pos_range='all')
        return result


class G_CLD(GrammaticalForms):
    name_en = "Could Simple"

    def count(self, doc):
        result = self.incidence(doc, attr_name='modal_verbs', attr_value='could_ind', pos_range='all')
        return result


class G_CLD_P(GrammaticalForms):
    name_en = "Could Simple Passive"

    def count(self, doc):
        result = self.incidence(doc, attr_name='modal_verbs', attr_value='could_ind_passive', pos_range='all')
        return result


class G_CAN_CON(GrammaticalForms):
    name_en = "Can Continuous"

    def count(self, doc):
        result = self.incidence(doc, attr_name='modal_verbs', attr_value='can_cont', pos_range='all')
        return result


class G_CLD_CON(GrammaticalForms):
    name_en = "Could Continuous"

    def count(self, doc):
        result = self.incidence(doc, attr_name='modal_verbs', attr_value='could_cont', pos_range='all')
        return result


class G_CLD_PRF(GrammaticalForms):
    name_en = "Could Perfect"

    def count(self, doc):
        result = self.incidence(doc, attr_name='modal_verbs', attr_value='could_perf', pos_range='all')
        return result


class G_CLD_P_P(GrammaticalForms):
    name_en = "Could Perfect Passive"

    def count(self, doc):
        result = self.incidence(doc, attr_name='modal_verbs', attr_value='could_perf_passive', pos_range='all')
        return result


class G_MAY(GrammaticalForms):
    name_en = "May Simple"

    def count(self, doc):
        result = self.incidence(doc, attr_name='modal_verbs', attr_value='may_ind', pos_range='all')
        return result


class G_MAY_P(GrammaticalForms):
    name_en = "May Simple Passive"

    def count(self, doc):
        result = self.incidence(doc, attr_name='modal_verbs', attr_value='may_ind_passive', pos_range='all')
        return result


class G_MGHT(GrammaticalForms):
    name_en = "Might Simple"

    def count(self, doc):
        result = self.incidence(doc, attr_name='modal_verbs', attr_value='might_ind', pos_range='all')
        return result


class G_MGHT_P(GrammaticalForms):
    name_en = "Might Simple Passive"

    def count(self, doc):
        result = self.incidence(doc, attr_name='modal_verbs', attr_value='might_ind_passive', pos_range='all')
        return result


class G_MAY_CON(GrammaticalForms):
    name_en = "May Continuous"

    def count(self, doc):
        result = self.incidence(doc, attr_name='modal_verbs', attr_value='may_cont', pos_range='all')
        return result


class G_MGTH_PRF(GrammaticalForms):
    name_en = "Might Perfect"

    def count(self, doc):
        result = self.incidence(doc, attr_name='modal_verbs', attr_value='might_perf', pos_range='all')
        return result


#
class G_MGHT_PRF_P(GrammaticalForms):
    name_en = "Might Perfect Passive"

    def count(self, doc):
        result = self.incidence(doc, attr_name='modal_verbs', attr_value='might_perf_passive', pos_range='all')
        return result


class G_MAY_PRF_P(GrammaticalForms):
    name_en = "May Perfect Passive"

    def count(self, doc):
        result = self.incidence(doc, attr_name='modal_verbs', attr_value='may_perf_passive', pos_range='all')
        return result


class G_ADJ_POS(GrammaticalForms):
    name_en = "Adjectives Positive Degree"

    def count(self, doc):
        result = self.incidence(doc, attr_name='adjectives', attr_value="positive_adjective", pos_range='all')
        return result


class G_ADJ_COMP(GrammaticalForms):
    name_en = "Adjectives Comparative Degree"

    def count(self, doc):
        result = self.incidence(doc, attr_name='adjectives', attr_value="comparative_adjective", pos_range='all')
        return result


class G_ADJ_SUP(GrammaticalForms):
    name_en = "Adjectives Superlative Degree"

    def count(self, doc):
        result = self.incidence(doc, attr_name='adjectives', attr_value="superlative_adjective", pos_range='all')
        return result


GRAMMATICAL_FORMS = [
    G_V,
    G_PR_S,
    G_PR_IND_3,
    G_PR_CONT,
    G_PR_P,
    G_PR_P_CON,
    G_PR_S_P,
    G_PR_CONT_P,
    G_PR_PRF_P,
    G_PA_S,
    G_PA_S_BE,
    G_PA_CON,
    G_PA_PRF,
    G_PA_PRF_CONT,
    G_PA_S_P,
    G_PA_CON_P,
    G_PA_P_P,
    G_FT_S,
    G_FT_CON,
    G_FT_P,
    G_FT_P_CON,
    G_FT_S_P,
    G_FT_PR_P,
    G_FT_P_P,
    G_WLD,
    G_WLD_P,
    G_WLD_CON,
    G_WLD_PRF,
    G_WLD_P_P,
    G_SHLD,
    G_SHLD_P,
    G_SHLL,
    G_SHLL_P,
    G_SHLD_CON,
    G_SHLD_PRF,
    G_SHLD_P_P,
    G_MST,
    G_MST_P,
    G_MST_CON,
    G_MST_PRF,
    G_MST_P_P,
    G_CAN,
    G_CAN_P,
    G_CLD,
    G_CLD_P,
    G_CAN_CON,
    G_CLD_CON,
    G_CLD_PRF,
    G_CLD_P_P,
    G_MAY,
    G_MAY_P,
    G_MGHT,
    G_MGHT_P,
    G_MAY_CON,
    G_MGTH_PRF,
    G_MGHT_PRF_P,
    G_MAY_PRF_P,
    G_ADJ_POS,
    G_ADJ_COMP,
    G_ADJ_SUP,
]

grammatical_forms_group = MetricsGroup([m() for m in GRAMMATICAL_FORMS])

