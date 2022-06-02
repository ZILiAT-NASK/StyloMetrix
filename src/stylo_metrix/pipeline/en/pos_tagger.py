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
        """
        pos: adj adv v det intj conj n pro part num prep
        verb_tense:
        modal_verbs:
        adjectives:
        is_word: True False
        is_content_word: cont noncont None
        """
        self.nlp = nlp

        Token.set_extension("pos", default=None, force=True)
        Token.set_extension("verb_tense", default=None, force=True)
        Token.set_extension("modal_verbs", default=None, force=True)
        Token.set_extension("adjectives", default=None, force=True)
        Token.set_extension("is_word", default=False, force=True)
        Token.set_extension("is_function_word", default=False, force=True)
        Token.set_extension("is_content_word", default=False, force=True)

    def __call__(self, doc):
        for token in doc:
            token._.set("pos", grammar.classify_pos(token))
            token._.set("is_word", grammar.is_word(token))
            token._.set("is_function_word", grammar.is_function_word(token))
            token._.set("is_content_word", grammar.is_content_word(token))

        pr_s = grammar.present_simple(doc)
        for t, label in pr_s.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", label)

        pr_ind_3 = grammar.present_ind_3p(doc)
        for t, label in pr_ind_3.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", label)

        pr_cont = grammar.present_cont(doc)
        for t, label in pr_cont.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", label)

        pr_perf = grammar.present_perfect(doc)
        for t, label in pr_perf.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", label)

        pr_perf_cont = grammar.present_perfect_cont(doc)
        for t, label in pr_perf_cont.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", label)

        pr_s_p = grammar.present_ind_pas(doc)
        for t, label in pr_s_p.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", label)

        pr_cont_p = grammar.present_cont_pas(doc)
        for t, label in pr_cont_p.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", label)

        pr_p_p = grammar.present_perfect_passive(doc)
        for t, label in pr_p_p.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", label)

        past_s = grammar.past_simple(doc)
        for t, label in past_s.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", label)

        past_s_be = grammar.past_simple_be(doc)
        for t, label in past_s_be.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", label)

        past_cont = grammar.past_cont(doc)
        for t, label in past_cont.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", label)

        past_p = grammar.past_perfect(doc)
        for t, label in past_p.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", label)

        past_p_cont = grammar.past_perfect_cont(doc)
        for t, label in past_p_cont.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", label)

        past_smp_p = grammar.past_simple_passive(doc)
        for t, label in past_smp_p.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", label)

        past_cont_p = grammar.past_cont_passive(doc)
        for t, label in past_cont_p.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", label)

        past_p_p = grammar.past_perf_passive(doc)
        for t, label in past_p_p.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", label)

        ft_s = grammar.future_simple(doc)
        for t, label in ft_s.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", label)

        ft_c = grammar.future_cont(doc)
        for t, label in ft_c.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", label)

        ft_p = grammar.future_perfect(doc)
        for t, label in ft_p.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", label)

        ft_p_c = grammar.future_perf_cont(doc)
        for t, label in ft_p_c.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", label)

        ft_s_p = grammar.future_simple_passive(doc)
        for t, label in ft_s_p.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", label)

        ft_cont_p = grammar.future_progr_passive(doc)
        for t, label in ft_cont_p.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", label)

        ft_p_p = grammar.future_perfect_passive(doc)
        for t, label in ft_p_p.items():
            for token in doc:
                if t == token:
                    token._.set("verb_tense", label)

        would = grammar.would_ind_active(doc)
        for t, label in would.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", label)

        wld_pa = grammar.would_ind_passive(doc)
        for t, label in wld_pa.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", label)

        wld_c = grammar.would_cont_active(doc)
        for t, label in wld_c.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", label)

        wld_prf = grammar.would_perf_active(doc)
        for t, label in wld_prf.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", label)

        wld_prf_p = grammar.would_perf_passive(doc)
        for t, label in wld_prf_p.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", label)

        shld = grammar.should_ind_active(doc)
        for t, label in shld.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", label)

        shld_pa = grammar.should_ind_passive(doc)
        for t, label in shld_pa.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", label)

        shl = grammar.shall_ind_active(doc)
        for t, label in shl.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", label)

        shl_pa = grammar.shall_ind_passive(doc)
        for t, label in shl_pa.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", label)

        shl_c = grammar.should_cont(doc)
        for t, label in shl_c.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", label)

        shld_prf = grammar.should_perf_active(doc)
        for t, label in shld_prf.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", label)

        shld_prf_pa = grammar.should_perf_passive(doc)
        for t, label in shld_prf_pa.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", label)

        must = grammar.must_ind_active(doc)
        for t, label in must.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", label)

        must_pa = grammar.must_ind_passive(doc)
        for t, label in must_pa.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", label)

        must_cont = grammar.must_cont(doc)
        for t, label in must_cont.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", label)

        must_prf = grammar.must_perf_active(doc)
        for t, label in must_prf.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", label)

        must_prf_p = grammar.must_perf_passive(doc)
        for t, label in must_prf_p.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", label)

        can = grammar.can_ind(doc)
        for t, label in can.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", label)

        can_p = grammar.can_ind_passive(doc)
        for t, label in can_p.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", label)

        could = grammar.could_ind_active(doc)
        for t, label in could.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", label)

        could_p = grammar.could_ind_passive(doc)
        for t, label in could_p.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", label)

        can_c = grammar.can_cont(doc)
        for t, label in can_c.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", label)

        could_c = grammar.could_cont(doc)
        for t, label in could_c.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", label)

        could_prf = grammar.could_perf_active(doc)
        for t, label in could_prf.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", label)

        could_prf_p = grammar.could_perf_passive(doc)
        for t, label in could_prf_p.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", label)

        may = grammar.may_ind_active(doc)
        for t, label in may.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", label)

        may_p = grammar.may_ind_passive(doc)
        for t, label in may_p.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", label)

        might = grammar.might_ind_active(doc)
        for t, label in might.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", label)

        might_p = grammar.might_ind_passive(doc)
        for t, label in might_p.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", label)

        may_c = grammar.may_cont(doc)
        for t, label in may_c.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", label)

        might_prf = grammar.might_perf_active(doc)
        for t, label in might_prf.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", label)

        might_prf_p = grammar.might_perf_passive(doc)
        for t, label in might_prf_p.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", label)

        may_prf = grammar.may_perf_passive(doc)
        for t, label in may_prf.items():
            for token in doc:
                if t == token:
                    token._.set("modal_verbs", label)

        adj = grammar.adjectives(doc)
        for t, label in adj.items():
            for token in doc:
                if t == token:
                    token._.set("adjectives", label)
        return doc
