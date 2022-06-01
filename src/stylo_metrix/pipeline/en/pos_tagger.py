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

import stylo_metrix.pipeline.en.grammar as grammar
from spacy.tokens import Token


class POSTagger():

    def __init__(self, nlp):
        self.nlp = nlp

        Token.set_extension("pos", default=None, force=True)
        Token.set_extension("verb_tense", default=None, force=True)
        Token.set_extension("modal_verbs", default=None, force=True)
        Token.set_extension("adjectives", default=None, force=True)

    def __call__(self, doc):
        for token in doc:
            token._.set("pos", grammar.classify_pos(token))

        pr_s = grammar.present_simple(doc)
        for t, lable in pr_s.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", lable)

        pr_ind_3 = grammar.present_ind_3p(doc)
        for t, lable in pr_ind_3.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", lable)

        pr_cont = grammar.present_cont(doc)
        for t, lable in pr_cont.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", lable)

        pr_perf = grammar.present_perfect(doc)
        for t, lable in pr_perf.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", lable)

        pr_perf_cont = grammar.present_perfect_cont(doc)
        for t, lable in pr_perf_cont.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", lable)

        pr_s_p = grammar.present_ind_pas(doc)
        for t, lable in pr_s_p.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", lable)

        pr_cont_p = grammar.present_cont_pas(doc)
        for t, lable in pr_cont_p.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", lable)

        pr_p_p = grammar.present_perfect_passive(doc)
        for t, lable in pr_p_p.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", lable)

        past_s = grammar.past_simple(doc)
        for t, lable in past_s.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", lable)

        past_s_be = grammar.past_simple_be(doc)
        for t, lable in past_s_be.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", lable)

        past_cont = grammar.past_cont(doc)
        for t, lable in past_cont.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", lable)

        past_p = grammar.past_perfect(doc)
        for t, lable in past_p.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", lable)

        past_p_cont = grammar.past_perfect_cont(doc)
        for t, lable in past_p_cont.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", lable)

        past_smp_p = grammar.past_simple_passive(doc)
        for t, lable in past_smp_p.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", lable)

        past_cont_p = grammar.past_cont_passive(doc)
        for t, lable in past_cont_p.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", lable)

        past_p_p = grammar.past_perf_passive(doc)
        for t, lable in past_p_p.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", lable)

        ft_s = grammar.future_simple(doc)
        for t, lable in ft_s.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", lable)

        ft_c = grammar.future_cont(doc)
        for t, lable in ft_c.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", lable)

        ft_p = grammar.future_perfect(doc)
        for t, lable in ft_p.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", lable)

        ft_p_c = grammar.future_perf_cont(doc)
        for t, lable in ft_p_c.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", lable)

        ft_s_p = grammar.future_simple_passive(doc)
        for t, lable in ft_s_p.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", lable)

        ft_cont_p = grammar.future_progr_passive(doc)
        for t, lable in ft_cont_p.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", lable)

        ft_p_p = grammar.future_perfect_passive(doc)
        for t, lable in ft_p_p.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", lable)

        would = grammar.would_ind_active(doc)
        for t, lable in would.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", lable)

        wld_pa = grammar.would_ind_passive(doc)
        for t, lable in wld_pa.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", lable)

        wld_c = grammar.would_cont_active(doc)
        for t, lable in wld_c.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", lable)

        wld_prf = grammar.would_perf_active(doc)
        for t, lable in wld_prf.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", lable)

        wld_prf_p = grammar.would_perf_passive(doc)
        for t, lable in wld_prf_p.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", lable)

        shld = grammar.should_ind_active(doc)
        for t, lable in shld.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", lable)

        shld_pa = grammar.should_ind_passive(doc)
        for t, lable in shld_pa.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", lable)

        shl = grammar.shall_ind_active(doc)
        for t, lable in shl.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", lable)

        shl_pa = grammar.shall_ind_passive(doc)
        for t, lable in shl_pa.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", lable)

        shl_c = grammar.should_cont(doc)
        for t, lable in shl_c.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", lable)

        shld_prf = grammar.should_perf_active(doc)
        for t, lable in shld_prf.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", lable)

        shld_prf_pa = grammar.should_perf_passive(doc)
        for t, lable in shld_prf_pa.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", lable)

        must = grammar.must_ind_active(doc)
        for t, lable in must.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", lable)

        must_pa = grammar.must_ind_passive(doc)
        for t, lable in must_pa.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", lable)

        must_cont = grammar.must_cont(doc)
        for t, lable in must_cont.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", lable)

        must_prf = grammar.must_perf_active(doc)
        for t, lable in must_prf.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", lable)

        must_prf_p = grammar.must_perf_passive(doc)
        for t, lable in must_prf_p.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", lable)

        can = grammar.can_ind(doc)
        for t, lable in can.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", lable)

        can_p = grammar.can_ind_passive(doc)
        for t, lable in can_p.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", lable)

        could = grammar.could_ind_active(doc)
        for t, lable in could.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", lable)

        could_p = grammar.could_ind_passive(doc)
        for t, lable in could_p.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", lable)

        can_c = grammar.can_cont(doc)
        for t, lable in can_c.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", lable)

        could_c = grammar.could_cont(doc)
        for t, lable in could_c.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", lable)

        could_prf = grammar.could_perf_active(doc)
        for t, lable in could_prf.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", lable)

        could_prf_p = grammar.could_perf_passive(doc)
        for t, lable in could_prf_p.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", lable)

        may = grammar.may_ind_active(doc)
        for t, lable in may.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", lable)

        may_p = grammar.may_ind_passive(doc)
        for t, lable in may_p.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", lable)

        might = grammar.might_ind_active(doc)
        for t, lable in might.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", lable)

        might_p = grammar.might_ind_passive(doc)
        for t, lable in might_p.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", lable)

        may_c = grammar.may_cont(doc)
        for t, lable in may_c.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", lable)

        might_prf = grammar.might_perf_active(doc)
        for t, lable in might_prf.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", lable)

        might_prf_p = grammar.might_perf_passive(doc)
        for t, lable in might_prf_p.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", lable)

        may_prf = grammar.may_perf_passive(doc)
        for t, lable in may_prf.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", lable)

        adj = grammar.adjectives(doc)
        for t, lable in adj.items():
            for token in doc:
                if t == token:
                    token._.set("adjectives", lable)
        return doc
