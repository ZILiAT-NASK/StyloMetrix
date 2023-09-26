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


from .dictionary_en import FUNCTION_WORDS
import itertools



def is_function_word(token):
    if token.lemma_ in FUNCTION_WORDS:
        return True


def is_content_word(token):
    if not token._.is_function_word:
        return True


"""GRAMMATICAL TENSES"""

""" METRICS FOR THE PRESENT TENSES [PASSIVE & ACTIVE VOICE]"""


def present_simple(doc):
    label = "present_simple"
    ext = "verb_tense"

    negative = list(itertools.chain.from_iterable([[token, token.head] for token in doc if token.dep_ == "aux" and token.lemma_ == "do" and "Tense=Pres" in token.morph
                                                   and "VerbForm=Inf" in token.head.morph]))
    tokens = [token for token in doc if (token.tag_ == "VBZ" or token.tag_ == "VBP") and "Tense=Pres" in token.morph and "VerbForm=Fin" and token.dep_ != "aux" and token.dep_ != "auxpass"]
    general = tokens + negative
    return general, ext, label


def present_cont(doc):

    label = "present_cont"
    ext = "verb_tense"
    tokens = list(itertools.chain.from_iterable([[token, token.head] for token in doc if token.dep_ == "aux" and token.lemma_ == "be" and "Tense=Pres" in token.morph and
              token.head.tag_ == "VBG" and not [child for child in token.head.children if child.text == "have"]]))
    conj = [token for token in doc if token.dep_ == "conj" and token.tag_ == "VBG" and token.head in tokens]
    general = tokens + conj
    return general, ext, label


def present_perfect_cont(doc):
    label = "present_perfect_cont"
    ext = "verb_tense"
    aux_have = ["have", "'s", "'ve", "’s", "’ve"]
    aux_been = []
    tokens = list(itertools.chain.from_iterable([[token, token.head] for token in doc if token.dep_ == "aux" and token.lemma_ in aux_have and "Tense=Pres" in token.morph and 
              token.head.tag_ == "VBG" and [aux_been.append(child) for child in token.head.lefts if child.text == "been" and child.dep_ == "aux"]]))
    conj = [token for token in doc if token.dep_ == "conj" and token.head in tokens]
    general = tokens + aux_been + conj

    return general, ext, label


def present_simple_passive(doc):
    label = "present_ind_passive"
    ext = "verb_tense"
    aux = ["is", "am", "are", "'re", "'m", "'s", "’re", "’m", "’s"]

    roots = [token for token in doc if "Aspect=Perf" in token.morph  and "Tense=Past" in token.morph  and "VerbForm=Part" in token.morph and\
             [child for child in token.lefts if child.dep_ == "auxpass" and child.text in aux]]
    aux = [token for token in doc if token in [*token.head.lefts] and token.head in roots and token.text in aux]
    conj = [token for token in doc if token.tag_ == "VBN" and token.dep_ == "conj" and token.head in roots]
    general = roots + aux + conj
    return general, ext, label


def present_progressive_passive(doc):
    label = "present_cont_passive"
    ext = "verb_tense"
    aux = ["is", "am", "are", "'re", "'m", "'s", "’re", "’m", "’s"]
    
    roots = [token for token in doc if "Aspect=Perf" in token.morph and "Tense=Past" in token.morph and "VerbForm=Part" in token.morph and\
             [child for child in token.lefts if child.dep_ == "aux" and child.text in aux] and [t for t in token.lefts if t.dep_ == "auxpass" and t.text == "being"]]
    aux = [token for token in doc if token in [*token.head.lefts] and token.head in roots and token.text in aux]
    auxpass = [token for token in doc if token in [*token.head.lefts] and token.head in roots and token.text == "being"]
    conj = [token for token in doc if token.tag_ == "VBN" and token.dep_ == "conj" and token.head in roots]
    general = roots + aux + auxpass + conj
    return general, ext, label


def present_perfect_passive(doc):
    label = "present_perfect_passive"
    ext = "verb_tense"
    aux = ["have", "'s", "'ve", "’s", "’ve"]
    auxpass = []

    tokens = list(itertools.chain.from_iterable([[token, token.head] for token in doc if token.dep_ == "aux" and token.lemma_ in aux and "Tense=Pres" in token.morph
                                                 and token.head.tag_ == "VBN" and [auxpass.append(child) for child in token.head.lefts if child.dep_ == "auxpass" and child.text == "been"]]))
    conj = [token for token in doc if token in [*token.head.rights] and token.dep_ == "conj" and token.head in tokens]
    general = tokens + conj + auxpass
    return general, ext, label


def present_perfect(doc):
    label = "present_perfect"
    ext = "verb_tense"

    aux = ["have", "'ve", "'s", "’ve", "’s"]
    tokens = list(itertools.chain.from_iterable([[token, token.head] for token in doc if token.dep_ == "aux" and token.lemma_ in aux and "Tense=Pres" in token.morph
                                                 and token.head.tag_ == "VBN" and not any(child for child in token.head.lefts if child.dep_ == "auxpass" or child.dep_ == "nsubjpass")]))
    conj = [token for token in doc if token in [*token.head.rights] and token.dep_ == "conj" and token.head in tokens]
    general = tokens + conj 
    return general, ext, label


""" METRICS FOR THE PAST TENSES [PASSIVE & ACTIVE VOICE]"""


def past_simple_passive(doc):
    label = "past_ind_passive"
    ext = "verb_tense"

    tokens = list(itertools.chain.from_iterable([[token, token.head]for token in doc if "Tense=Past" in token.morph and "VerbForm=Fin" in token.morph and token.dep_ == "auxpass" 
              and "Aspect=Perf" in token.head.morph and "Tense=Past" in token.head.morph and "VerbForm=Part" in token.head.morph]))
    conj = [token for token in doc if token.tag_ == "VBN" and token.dep_ == "conj" and token.head in tokens]
    general = tokens + conj
    return general, ext, label


def past_simple(doc):
    label = "past_simple"
    ext = "verb_tense"

    indicative = [token for token in doc if "Tense=Past" in token.morph and "VerbForm=Fin" in token.morph and token.text != "was" and token.text != "were"
                  and [child for child in token.lefts if child.dep_ == "nsubj"]]
    did_sentences = list(itertools.chain.from_iterable([[token, token.head] for token in doc if "Tense=Past" in token.morph 
                                                        and "VerbForm=Fin" in token.morph and token.dep_ == "aux" and "VerbForm=Inf" in token.head.morph]))
    conj = [token for token in doc if token.pos_ == "VERB" and token.dep_ == "conj" and token.head in indicative]
    conj_neg_inter = [token for token in doc if "VerbForm=Inf" in token.morph and token.dep_ == "conj" and [i for i in token.head.lefts if "Tense=Past" in i.morph 
                    and "VerbForm=Fin" in i.morph and i.dep_ == "aux"]]

    general = indicative + did_sentences + conj + conj_neg_inter

    return general, ext, label


def past_simple_be(doc):
    label = "past_ind_be"
    ext = "verb_tense"

    tokens = [token for token in doc if token.lemma_ == "be" and token.tag_ == "VBD" and [child for child in token.children if child.tag_ != "VBG"]]
    return tokens, ext, label


def past_cont_passive(doc):
    label = "past_cont_passive"
    ext = "verb_tense"

    aux = []
    tokens = list(itertools.chain.from_iterable([[token, token.head] for token in doc if token.text == "being" and "Tense=Past" in token.head.morph and
                                                 "VerbForm=Part" in token.head.morph and token.head.tag_ == "VBN" and 
                                                 [aux.append(child) for child in token.head.lefts if child.dep_ == "aux" and child.lemma_ == "be" and "Tense=Past" in child.morph and "VerbForm=Fin" in child.morph]]))
    conj = [token for token in doc if token.tag_ == "VBN" and token.dep_ == "conj" and token.head in tokens]
    general = aux + tokens + conj
    return general, ext, label


def past_cont(doc):
    label = "past_cont"
    ext = "verb_tense"

    tokens = list(itertools.chain.from_iterable([[token, token.head] for token in doc if token.lemma_ == "be" and token.tag_ == "VBD" and token.head.tag_ == "VBG" and 
                                                 not [t for t in token.head.lefts if t.dep_ == "aux" and t.text == "had"]]))
    conj = [token for token in doc if token.tag_ == "VBG" and token.dep_ == "conj" and token.head in tokens]
    general = tokens + conj

    return general, ext, label


def past_perfect(doc):
    label = "past_perf"
    ext = "verb_tense"

    tokens = list(itertools.chain.from_iterable([[token, token.head] for token in doc if token.dep_ == "aux" and "Tense=Past" in token.morph and token.lemma_ != "be"
              and"Aspect=Perf" in token.head.morph and "Tense=Past" in token.head.morph and
              not [child for child in token.head.lefts if child.dep_ == "auxpass" and child.lemma_ == "be"]]))
    conj = [token for token in doc if token.dep_ == "conj" and token.pos_ == "VERB" and token.head in tokens]
    general = tokens + conj

    return general, ext, label


def past_perf_passive(doc):
    label = "past_perf_passive"
    ext = "verb_tense"

    auxpass = []
    tokens = list(itertools.chain.from_iterable([[token, token.head] for token in doc if token.dep_ == "aux" and "Tense=Past" in token.morph and token.lemma_ != "be"
              and"Aspect=Perf" in token.head.morph and "Tense=Past" in token.head.morph and [auxpass.append(child) for child in token.head.lefts if child.dep_ == "auxpass" and child.lemma_ == "be"]]))
    conj = [token for token in doc if token.dep_ == "conj" and token.pos_ == "VERB" and token.head in tokens]
    general =  tokens + conj + auxpass

    return general, ext, label


def past_perfect_cont(doc):
    label = "past_perf_cont"
    ext = "verb_tense"

    aux_been = []
    aux_have = ["had", "'d", "’d", "Had"]
    tokens = list(itertools.chain.from_iterable([[token, token.head] for token in doc if token.dep_ == "aux" and token.text in aux_have and 
              token.head.tag_ == "VBG" and [aux_been.append(child) for child in token.head.lefts if child.text == "been" and child.dep_ == "aux"]]))
    conj = [token for token in doc if token.dep_ == "conj" and token.tag_ == "VBG" and token.head in tokens]
    general = tokens + conj + aux_been
    return general, ext, label


""" METRICS FOR THE FUTURE TENSES [PASSIVE & ACTIVE VOICE]"""


def future_simple(doc):
    label = "future_simple"
    ext = "verb_tense"

    tokens = list(itertools.chain.from_iterable([[token, token.head] for token in doc if (token.lemma_ =="will" or token.lemma_ == "'ll" or token.lemma_ == "’ll")
              and "VerbForm=Inf" in token.head.morph]))
    conj = [token for token in doc if "VerbForm=Inf" in token.morph and token.dep_ == "conj" and token.head in tokens]
    general = tokens + conj

    return general, ext, label


def future_simple_passive(doc):
    label = "future_simple_passive"
    ext = "verb_tense"

    aux = []
    tokens = list(itertools.chain.from_iterable([[token, token.head] for token in doc if (token.lemma_ =="will" or token.lemma_ == "'ll" or token.lemma_ == "’ll")
              and "Tense=Past" in token.head.morph and "VerbForm=Part" in token.head.morph and [aux.append(child) for child in token.head.lefts if child.dep_ == "auxpass" and child.text == "be"]
              and not [t for t in token.head.lefts if t.text == "being"]]))
    conj = [token for token in doc if token.dep_ == "conj" and token.pos_ == "VERB" and "Tense=Past" in token.morph and "VerbForm=Part" in token.morph and token.head in tokens]
    general = tokens + aux + conj

    return general, ext, label


def future_cont(doc):
    label = "future_progr"
    ext = "verb_tense"

    aux = []
    heads = list(itertools.chain.from_iterable([[token, token.head] for token in doc if (token.lemma_ =="will" or token.lemma_ == "'ll" or token.lemma_ == "’ll") and
             "Tense=Pres" in token.head.morph and "VerbForm=Part" in token.head.morph and [aux.append(child) for child in token.head.lefts if "VerbForm=Inf" in child.morph and child.lemma_ == "be"]]))
    conj = [token for token in doc if token.dep_ == "conj" and token.pos_ == "VERB" and "Tense=Pres" in token.morph and "VerbForm=Part" in token.morph and token.head in heads]
    general = aux + heads + conj
    return general, ext, label


def future_progr_passive(doc):
    label = "future_progr_passive"
    ext = "verb_tense"

    aux = []
    tokens = list(itertools.chain.from_iterable([[token, token.head] for token in doc if (token.lemma_ =="will" or token.lemma_ == "'ll" or token.lemma_ == "’ll")
              and "Tense=Past" in token.head.morph and "VerbForm=Part" in token.head.morph and [aux.append(child) for child in token.head.lefts if child.dep_ == "aux" and child.text == "be"]
              and [aux.append(t) for t in token.head.lefts if t.text == "being" and t.dep_ == "auxpass"]]))
    conj = [token for token in doc if token.dep_ == "conj" and token.pos_ == "VERB" and "Tense=Past" in token.morph and "VerbForm=Part" in token.morph and token.head in tokens]
    general = tokens + aux + conj
    return general, ext, label


def future_perfect(doc):
    label = "future_perfect"
    ext = "verb_tense"

    aux = []
    tokens = list(itertools.chain.from_iterable([[token, token.head] for token in doc if (token.lemma_ =="will" or token.lemma_ == "'ll" or token.lemma_ == "’ll")
              and "Tense=Past" in token.head.morph and "VerbForm=Part" in token.head.morph and not [t for t in token.head.lefts if t.text == "been" and t.dep_ == "auxpass"]
              and [aux.append(child) for child in token.head.lefts if child.dep_ == "aux" and child.text == "have"]]))
    conj = [token for token in doc if token.dep_ == "conj" and "Tense=Past" in token.morph and "VerbForm=Part" in token.morph and token.head in tokens]
    general = tokens + aux + conj

    return general, ext, label


def future_perfect_passive(doc):
    label = "future_perf_passive"
    ext = "verb_tense"

    aux = []
    tokens = list(itertools.chain.from_iterable([[token, token.head] for token in doc if (token.lemma_ =="will" or token.lemma_ == "'ll" or token.lemma_ == "’ll")
              and "Tense=Past" in token.head.morph and "VerbForm=Part" in token.head.morph and [aux.append(t) for t in token.head.lefts if t.text == "been" and t.dep_ == "auxpass"]
              and [aux.append(child) for child in token.head.lefts if child.dep_ == "aux" and child.text == "have"]]))
    conj = [token for token in doc if token.dep_ == "conj" and "Tense=Past" in token.morph and "VerbForm=Part" in token.morph and token.head in tokens]
    general = tokens + aux + conj

    return general, ext, label


def future_perf_cont(doc):
    label = "future_perfect_cont"
    ext = "verb_tense"

    aux = []
    tokens = list(itertools.chain.from_iterable([[token, token.head] for token in doc if (token.lemma_ =="will" or token.lemma_ == "'ll" or token.lemma_ == "’ll")
                                                 and "Tense=Pres" in token.head.morph and "VerbForm=Part" in token.head.morph and [aux.append(child) for child in token.head.lefts if child.dep_ == "aux" and child.text == "have"]
                                                 and [aux.append(t) for t in token.head.lefts if t.text == "been" and t.dep_ == "aux"]]))
    conj = [token for token in doc if token.dep_ == "conj" and "Tense=Pres" in token.morph and "VerbForm=Part" in token.morph and token.head in tokens]
    general = tokens + aux + conj
    return general, ext, label


""" METRICS FOR MODAL VERBS [PASSIVE & ACTIVE VOICE]"""


def would_ind_active(doc):
    would_ind_active = set()
    label = "would_ind_active"
    ext = "modal_verbs"

    for token in doc:
        if token.lemma_ == "would" and token.head.tag_ == "VB":
            head = token.head
            would_ind_active.add(head)
            would_ind_active.add(token)

            for t in head.subtree:
                if t.tag_ == "VB" and t.dep_ == "conj":
                    would_ind_active.add(t)
    return would_ind_active, ext, label


def would_ind_passive(doc):
    would_ind_passive = []
    label = "would_ind_passive"
    ext = "modal_verbs"

    for token in doc:
        if token.lemma_ == "would" and token.head.tag_ == "VBN":
            head = token.head

            for tkn in head.children:
                if tkn.text == "be" and tkn.dep_ == "auxpass":
                    would_ind_passive.append(head)
                    would_ind_passive.append(token)
                    would_ind_passive.append(tkn)

            for t in head.subtree:
                if t.tag_ == "VBN" and t.dep_ == "conj" and head in would_ind_passive:
                    would_ind_passive.append(t)

    return would_ind_passive, ext, label


def would_cont_active(doc):
    would_cont_active = set()
    ext = "modal_verbs"
    label = "would_cont"

    for token in doc:

        if token.lemma_ == "would" and token.head.tag_ == "VBG":
            head = token.head

            for t in head.subtree:
                if t.text == "be":
                    would_cont_active.add(head)
                    would_cont_active.add(t)
                    would_cont_active.add(token)

                    for j in head.subtree:
                        if j.tag_ == "VBG" and j.dep_ == "conj":
                            would_cont_active.add(j)
    return would_cont_active, ext, label


def would_perf_active(doc):
    would_perf_active = []
    label = "would_perf_active"
    ext = "modal_verbs"

    for token in doc:
        if (token.lemma_ == "would" or token.lemma_ == "'d" or token.lemma_ == "’d") and token.head.tag_ == "VBN":
            head = token.head

            for t in head.children:
                if t.lemma_ == "have":
                    would_perf_active.append(head)

            for k in head.children:
                if k.lemma_ == "be" and head in would_perf_active:
                    would_perf_active.remove(head)

            if head in would_perf_active:
                would_perf_active.append(token)
                for tkn in head.children:
                    if tkn.lemma_ == "have":
                        would_perf_active.append(tkn)

            for j in head.subtree:
                if (j.tag_ == "VBN" or j.tag_ == "VBD") and j.dep_ == "conj" and head in would_perf_active:
                    would_perf_active.append(j)

    return would_perf_active, ext, label


def would_perf_passive(doc):
    would_perf_passive = set()
    label = "would_perf_passive"
    ext = "modal_verbs"

    for token in doc:

        if (token.lemma_ == "would" or token.lemma_ == "'d" or token.lemma_ == "’d") and token.head.tag_ == "VBN":
            would_perf_passive.add(token)
            head = token.head

            for k in head.children:
                if k.text == "been" and k.dep_ == "auxpass":
                    would_perf_passive.add(head)
                    would_perf_passive.add(k)

            for j in head.subtree:
                if (j.tag_ == "VBN" or j.tag_ == "VBD") and j.dep_ == "conj" and head in would_perf_passive:
                    would_perf_passive.add(j)

    return would_perf_passive, ext, label


def should_ind_active(doc):
    should_ind_active = set()
    label = "should_ind_active"
    ext = "modal_verbs"

    for token in doc:

        if token.lemma_ == "should" and token.head.tag_ == "VB":
            head = token.head
            should_ind_active.add(head)
            should_ind_active.add(token)
            for t in head.subtree:
                if t.tag_ == "VB" and t.dep_ == "conj":
                    should_ind_active.add(t)
    return should_ind_active, ext, label


def should_ind_passive(doc):
    should_ind_passive = set()
    label = "should_ind_passive"
    ext = "modal_verbs"

    for token in doc:

        if token.lemma_ == "should" and token.head.tag_ == "VBN":
            head = token.head

            for tkn in head.children:
                if tkn.text == "be" and tkn.dep_ == "auxpass":
                    should_ind_passive.add(head)
                    should_ind_passive.add(tkn)
                    should_ind_passive.add(token)

            for t in head.subtree:
                if t.tag_ == "VBN" and t.dep_ == "conj" and head in should_ind_passive:
                    should_ind_passive.add(t)
    return should_ind_passive, ext, label


def shall_ind_active(doc):
    shall_ind_active = set()
    label = "shall_ind_active"
    ext = "modal_verbs"

    for token in doc:

        if token.lemma_ == "shall" and token.head.tag_ == "VB":
            head = token.head
            shall_ind_active.add(head)
            shall_ind_active.add(token)
            for t in head.subtree:
                if t.tag_ == "VB" and t.dep_ == "conj":
                    shall_ind_active.add(t)
    return shall_ind_active, ext, label


def shall_ind_passive(doc):
    shall_ind_passive = set()
    label = "shall_ind_passive"
    ext = "modal_verbs"

    for token in doc:

        if token.lemma_ == "shall" and token.head.tag_ == "VBN":
            head = token.head

            for tkn in head.children:
                if tkn.text == "be" and tkn.dep_ == "auxpass":
                    shall_ind_passive.add(head)
                    shall_ind_passive.add(tkn)
                    shall_ind_passive.add(token)

            for t in head.subtree:
                if t.tag_ == "VBN" and t.dep_ == "conj" and head in shall_ind_passive:
                    shall_ind_passive.add(t)
    return shall_ind_passive, ext, label


def should_cont(doc):
    should_cont = set()
    label = "should_cont"
    ext = "modal_verbs"

    for token in doc:

        if token.lemma_ == "should" and token.head.tag_ == "VBG":
            head = token.head

            for t in head.subtree:
                if t.text == "be":
                    should_cont.add(head)
                    should_cont.add(t)
                    should_cont.add(token)

                    for j in head.subtree:
                        if j.tag_ == "VBG" and j.dep_ == "conj":
                            should_cont.add(j)
    return should_cont, ext, label


def should_perf_active(doc):
    should_perf_active = set()
    label = "should_perf_active"
    ext = "modal_verbs"

    for token in doc:

        if token.lemma_ == "should" and token.head.tag_ == "VBN":
            head = token.head

            for t in head.children:
                if t.text == "have":
                    should_perf_active.add(head)
                    should_perf_active.add(t)

                    for k in head.children:
                        if k.text == "been" and k.dep_ != "ROOT" and (head in should_perf_active):
                            should_perf_active.remove(head)
                            should_perf_active.remove(t)

            if head in should_perf_active:
                should_perf_active.add(token)

            for k in head.subtree:
                if (k.tag_ == "VBN" or k.tag_ == "VBD") and k.dep_ == "conj" and head in should_perf_active:
                    should_perf_active.add(k)
    return should_perf_active, ext, label


def should_perf_passive(doc):
    should_perf_passive = set()
    label = "should_perf_passive"
    ext = "modal_verbs"

    for token in doc:

        if token.lemma_ == "should" and token.head.tag_ == "VBN":
            head = token.head

            for t in head.children:
                if t.text == "been" and t.dep_ == "auxpass":
                    should_perf_passive.add(head)
                    should_perf_passive.add(t)
                    should_perf_passive.add(token)

            for j in head.subtree:
                if (j.tag_ == "VBN" or j.tag_ == "VBD") and j.dep_ == "conj" and head in should_perf_passive:
                    should_perf_passive.add(j)
    return should_perf_passive, ext, label


def must_ind_active(doc):
    must_ind_active = set()
    label = "must_ind_active"
    ext = "modal_verbs"

    for token in doc:

        if token.lemma_ == "must" and token.head.tag_ == "VB":
            head = token.head
            must_ind_active.add(head)
            must_ind_active.add(token)
            for t in head.subtree:
                if t.tag_ == "VB" and t.dep_ == "conj":
                    must_ind_active.add(t)
    return must_ind_active, ext, label


def must_ind_passive(doc):
    must_ind_passive = set()
    label = "must_ind_passive"
    ext = "modal_verbs"

    for token in doc:

        if token.lemma_ == "must" and token.head.tag_ == "VBN":
            head = token.head

            for tkn in head.children:
                if tkn.text == "be" and tkn.dep_ == "auxpass":
                    must_ind_passive.add(head)
                    must_ind_passive.add(token)
                    must_ind_passive.add(tkn)

            for t in head.subtree:
                if t.tag_ == "VBN" and t.dep_ == "conj" and head in must_ind_passive:
                    must_ind_passive.add(t)
    return must_ind_passive, ext, label


def must_cont(doc):
    must_cont = set()
    label = "must_cont"
    ext = "modal_verbs"

    for token in doc:

        if token.lemma_ == "must" and token.head.tag_ == "VBG":
            head = token.head

            for t in head.subtree:
                if t.text == "be":
                    must_cont.add(head)
                    must_cont.add(token)
                    must_cont.add(t)

                    for j in head.subtree:
                        if j.tag_ == "VBG" and j.dep_ == "conj":
                            must_cont.add(j)
    return must_cont, ext, label


def must_perf_active(doc):
    must_perf_active = set()
    label = "must_perf_active"
    ext = "modal_verbs"

    for token in doc:

        if token.lemma_ == "must" and token.head.tag_ == "VBN":
            head = token.head

            for t in head.subtree:
                if t.text == "have":
                    must_perf_active.add(head)
                    must_perf_active.add(t)

                    for tkn in head.children:
                        if tkn.text == "been" and tkn.dep_ != "ROOT":
                            must_perf_active.remove(head)
                            must_perf_active.remove(t)

            if head in must_perf_active:
                must_perf_active.add(token)

            for j in head.subtree:
                if (j.tag_ == "VBN" or j.tag_ == "VBD") and j.dep_ == "conj":
                    must_perf_active.add(j)
    return must_perf_active, ext, label


def must_perf_passive(doc):
    must_perf_passive = set()
    label = "must_perf_passive"
    ext = "modal_verbs"

    for token in doc:

        if token.lemma_ == "must" and token.head.tag_ == "VBN":
            head = token.head

            for tkn in head.children:
                if tkn.text == "been" and tkn.dep_ == "auxpass":
                    must_perf_passive.add(head)
                    must_perf_passive.add(token)
                    must_perf_passive.add(tkn)

                    for tkn in head.children:
                        if tkn.lemma_ == "have":
                            must_perf_passive.add(tkn)

            for j in head.subtree:
                if (j.tag_ == "VBN" or j.tag_ == "VBD") and j.dep_ == "conj" and head in must_perf_passive:
                    must_perf_passive.add(j)
    return must_perf_passive, ext, label


def can_ind(doc):
    can_ind = set()
    label = "can_ind"
    ext = "modal_verbs"

    for token in doc:

        if token.lemma_ == "can" and token.head.tag_ == "VB":
            head = token.head
            can_ind.add(head)
            can_ind.add(token)
            for t in head.subtree:
                if t.tag_ == "VB" and t.dep_ == "conj":
                    can_ind.add(t)
    return can_ind, ext, label


def can_ind_passive(doc):
    can_present_ind_passive = set()
    label = "can_ind_passive"
    ext = "modal_verbs"

    for token in doc:

        if token.lemma_ == "can" and token.head.tag_ == "VBN":
            head = token.head

            for tkn in head.children:
                if tkn.text == "be" and tkn.dep_ == "auxpass":
                    can_present_ind_passive.add(head)
                    can_present_ind_passive.add(tkn)
                    can_present_ind_passive.add(token)

            for t in head.subtree:
                if t.tag_ == "VBN" and t.dep_ == "conj" and head in can_present_ind_passive:
                    can_present_ind_passive.add(t)

    return can_present_ind_passive, ext, label


def could_ind_active(doc):
    could_ind_active = set()
    label = "could_ind"
    ext = "modal_verbs"

    for token in doc:

        if token.lemma_ == "could" and token.head.tag_ == "VB":
            head = token.head
            could_ind_active.add(head)
            could_ind_active.add(token)
            for t in head.subtree:
                if t.tag_ == "VB" and t.dep_ == "conj":
                    could_ind_active.add(t)
    return could_ind_active, ext, label


def could_ind_passive(doc):
    could_ind_passive = set()
    label = "could_ind_passive"
    ext = "modal_verbs"

    for token in doc:

        if token.lemma_ == "could" and token.head.tag_ == "VBN":
            head = token.head

            for tkn in head.children:
                if tkn.text == "be" and tkn.dep_ == "auxpass":
                    could_ind_passive.add(head)
                    could_ind_passive.add(token)
                    could_ind_passive.add(tkn)

            for t in head.subtree:
                if t.tag_ == "VBN" and t.dep_ == "conj" and head in could_ind_passive:
                    could_ind_passive.add(t)
    return could_ind_passive, ext, label


def can_cont(doc):
    can_cont = set()
    label = "can_cont"
    ext = "modal_verbs"

    for token in doc:

        if token.lemma_ == "can" and token.head.tag_ == "VBG":
            head = token.head

            for t in head.subtree:
                if t.text == "be":
                    can_cont.add(head)
                    can_cont.add(t)
                    can_cont.add(token)

                    for j in head.subtree:
                        if j.tag_ == "VBG" and j.dep_ == "conj":
                            can_cont.add(j)
    return can_cont, ext, label


def could_cont(doc):
    could_cont = set()
    label = "could_cont"
    ext = "modal_verbs"

    for token in doc:

        if token.lemma_ == "could" and token.head.tag_ == "VBG":
            head = token.head

            for t in head.subtree:
                if t.text == "be":
                    could_cont.add(head)
                    could_cont.add(token)
                    could_cont.add(t)

                    for j in head.subtree:
                        if j.tag_ == "VBG" and j.dep_ == "conj":
                            could_cont.add(j)
    return could_cont, ext, label


def could_perf_active(doc):

    label = "could_perf"
    ext = "modal_verbs"
    sentences = list(itertools.chain.from_iterable([[sent for token in sent if token.dep_ == "ROOT" and doc[token.i-1].text == "have" 
                  and doc[token.i-1].dep_ == "aux" and [child for child in token.lefts if child.text == "could" and child.dep_ == "aux"]]
                  for sent in doc.sents]))
    search = list(itertools.chain.from_iterable([[[token.head, doc[token.head.i-1], token] for 
                                                  token in sent if token.dep_ == "aux" and token.text == "could"] for sent in sentences]))
    result = list(itertools.chain.from_iterable(search))
    return result, ext, label


def could_perf_passive(doc):
    could_perf_passive = set()
    label = "could_perf_passive"
    ext = "modal_verbs"

    for token in doc:

        if token.lemma_ == "could" and token.head.tag_ == "VBN":
            head = token.head

            for t in head.children:
                if t.text == "been":
                    could_perf_passive.add(head)
                    could_perf_passive.add(t)
                    could_perf_passive.add(token)

                    for k in head.children:
                        if k.lemma_ == "have":
                            could_perf_passive.add(k)

            for i in head.subtree:
                if i.tag_ == "VBN" and i.dep_ == "conj" and head in could_perf_passive:
                    could_perf_passive.add(i)
    return could_perf_passive, ext, label


def may_ind_active(doc):
    may_ind_active = set()
    label = "may_ind"
    ext = "modal_verbs"

    for token in doc:

        if token.lemma_ == "may" and token.head.tag_ == "VB":
            head = token.head
            may_ind_active.add(head)
            may_ind_active.add(token)
            for t in head.subtree:
                if t.tag_ == "VB" and t.dep_ == "conj":
                    may_ind_active.add(t)
    return may_ind_active, ext, label


def may_ind_passive(doc):
    may_ind_passive = set()
    label = "may_ind_passive"
    ext = "modal_verbs"

    for token in doc:

        if token.lemma_ == "may" and token.head.tag_ == "VBN":
            head = token.head

            for tkn in head.children:
                if tkn.text == "be" and tkn.dep_ == "auxpass":
                    may_ind_passive.add(head)
                    may_ind_passive.add(tkn)
                    may_ind_passive.add(token)

            for t in head.subtree:
                if t.tag_ == "VBN" and t.dep_ == "conj" and head in may_ind_passive:
                    may_ind_passive.add(t)
    return may_ind_passive, ext, label


def might_ind_active(doc):
    might_ind_active = set()
    label = "might_ind"
    ext = "modal_verbs"

    for token in doc:

        if token.lemma_ == "might" and token.head.tag_ == "VB":
            head = token.head
            might_ind_active.add(head)
            might_ind_active.add(token)
            for t in head.subtree:
                if t.tag_ == "VB" and t.dep_ == "conj":
                    might_ind_active.add(t)
    return might_ind_active, ext, label


def might_ind_passive(doc):
    might_ind_passive = set()
    label = "might_ind_passive"
    ext = "modal_verbs"

    for token in doc:

        if token.lemma_ == "might" and token.head.tag_ == "VBN":
            head = token.head

            for tkn in head.children:
                if tkn.text == "be" and tkn.dep_ == "auxpass":
                    might_ind_passive.add(head)
                    might_ind_passive.add(token)
                    might_ind_passive.add(tkn)

            for t in head.subtree:
                if t.tag_ == "VBN" and t.dep_ == "conj" and head in might_ind_passive:
                    might_ind_passive.add(t)
    return might_ind_passive, ext, label


def may_cont(doc):
    may_cont = set()
    label = "may_cont"
    ext = "modal_verbs"

    for token in doc:

        if token.lemma_ == "may" and token.head.tag_ == "VBG":
            head = token.head

            for t in head.subtree:
                if t.text == "be":
                    may_cont.add(head)
                    may_cont.add(token)
                    may_cont.add(t)

                    for j in head.subtree:
                        if j.tag_ == "VBG" and j.dep_ == "conj":
                            may_cont.add(j)
    return may_cont, ext, label


def might_perf_active(doc):
    might_perf_active = set()
    label = "might_perf"
    ext = "modal_verbs"

    for token in doc:
        if token.lemma_ == "might" and token.head.tag_ == "VBN":
            head = token.head

            for t in head.subtree:
                if t.text == "have":
                    might_perf_active.add(head)
                    might_perf_active.add(t)

                    for k in head.children:
                        if k.text == "been" and k.dep_ != "ROOT" and (head in might_perf_active):
                            might_perf_active.remove(head)
                            might_perf_active.remove(t)

            if head in might_perf_active:
                might_perf_active.add(token)

            for j in head.subtree:
                if (j.tag_ == "VBN" or j.tag_ == "VBD") and j.dep_ == "conj":
                    might_perf_active.add(j)
    return might_perf_active, ext, label


def might_perf_passive(doc):
    might_perf_passive = set()
    label = "might_perf_passive"
    ext = "modal_verbs"

    for token in doc:

        if token.lemma_ == "might" and token.head.tag_ == "VBN":
            head = token.head

            for t in head.children:
                if t.text == "been" and t.dep_ == "auxpass":
                    might_perf_passive.add(head)
                    might_perf_passive.add(token)
                    might_perf_passive.add(t)

                    for k in head.children:
                        if k.lemma_ == "have":
                            might_perf_passive.add(k)

            for k in head.subtree:
                if k.tag_ == "VBN" and k.dep_ == "conj" and head in might_perf_passive:
                    might_perf_passive.add(k)
    return might_perf_passive, ext, label


def may_perf_passive(doc):
    may_perf_passive = set()
    label = "may_perf_passive"
    ext = "modal_verbs"

    for token in doc:

        if token.lemma_ == "may" and token.head.tag_ == "VBN":
            head = token.head

            for t in head.children:
                if t.text == "been" and t.dep_ == "auxpass":
                    may_perf_passive.add(head)
                    may_perf_passive.add(token)
                    may_perf_passive.add(t)
                if t.lemma_ == "have":
                    may_perf_passive.add(t)

            for k in head.subtree:
                if k.tag_ == "VBN" and k.dep_ == "conj" and head in may_perf_passive:
                    may_perf_passive.add(k)
    return may_perf_passive, ext, label


"""ADJECTIVES AND ADVERBS: DEGREES OF COMPARISON"""


def adjectives(doc):
    adj = {}

    for token in doc:
        if "Degree=Pos" in token.morph and token.pos_ == "ADJ":
            adj[token] = "positive_adjective"

        if "Degree=Pos" in token.morph and token.pos_ == "ADJ":
            head = token
            for child in head.children:
                if "Degree=Cmp" in child.morph:
                    adj[head] = "comparative_adjective"
                    adj[child] = "comparative_adjective"

        if "Degree=Cmp" in token.morph and (token not in adj) and token.pos_ == "ADJ":
            adj[token] = "comparative_adjective"

        if "Degree=Pos" in token.morph and token.pos_ == "ADJ":
            head = token
            for child in head.children:
                if "Degree=Sup" in child.morph:
                    adj[head] = "superlative_adjective"
                    adj[child] = "superlative_adjective"

        if "Degree=Sup" in token.morph and token.tag_ == "JJS" and token.head.pos_ != "ADV":
            adj[token] = "superlative_adjective"

        if "Degree=Pos" in token.morph and token.pos_ == "ADJ":
            head = token
            for child in head.children:
                if "PunctType=Dash" in child.morph:
                    for t in head.children:
                        if t.pos_ == "ADJ":
                            adj[t] = "positive_adjective"
                        if t.dep_ == "advmod":
                            adj[t] = "positive_adjective"

        if token.dep_ == "acomp":
            for child in token.children:
                if "PunctType=Dash" in child.morph:
                    for t in token.children:
                        if t.pos_ == "ADV" or child.pos_ == "ADJ":
                            adj[token] = "positive_adjective"
                            adj[t] = "positive_adjective"

        if token.pos_ == "ADJ" and (token.head.pos_ == "VERB" or token.head.pos_ == "AUX") and token in adj:
            del adj[token]

        if token.pos_ == "ADJ" and (token.dep_ == "npadvmod" or token.dep_ == "advmod") and token in adj:
            del adj[token]

    return adj


def adverbs(doc):
    adv = {}

    for token in doc:
        if token.tag_ == "RB":
            adv[token] = "positive_adverb"

        if token.tag_ == "RB":
            head = token
            for child in head.children:
                if "Degree=Cmp" in child.morph and child.tag_ == "RBR":
                    adv[head] = "comparative_adverb"
                    adv[child] = "comparative_adverb"

        if "Degree=Cmp" in token.morph and (token not in adv) and token.tag_ == "RBR" and token.head.pos_ == "ADV":
            adv[token] = "comparative_adverb"

        if token.tag_ == "RB" and token.dep_ == "advmod":
            head = token
            for child in head.children:
                if "Degree=Sup" in child.morph and child.tag_ == "RBS":
                    adv[head] = "superlative_adverb"
                    adv[child] = "superlative_adverb"

        if "Degree=Sup" in token.morph and token.tag_ == "JJS" and token.head.pos_ == "ADV":
            adv[token] = "superlative_adjective"

        if "Degree=Sup" in token.morph and token.pos_ == "ADV":
            adv[token] = "superlative_adverb"

        if token.pos_ == "ADV":
            head = token
            for child in head.children:
                if "PunctType=Dash" in child.morph:
                    for t in head.children:
                        if t.pos_ == "ADV":
                            adv[t] = "positive_adverb"
                        if t.dep_ == "advmod":
                            adv[t] = "positive_adverb"

        if (token.pos_ == "ADJ" and "Degree=Sup" in token.morph) \
                and (token.dep_ == "npadvmod" or token.dep_ == "advmod"):
            adv[token] = "superlative_adverb"

    return adv


FUNCTION_LIST = [
    present_simple,
    present_cont,
    present_perfect_cont,
    present_simple_passive,
    present_progressive_passive,
    present_perfect_passive,
    present_perfect,
    past_simple_passive,
    past_simple,
    past_simple_be,
    past_cont_passive,
    past_cont,
    past_perfect,
    past_perf_passive,
    past_perfect_cont,
    future_simple,
    future_simple_passive,
    future_cont,
    future_progr_passive,
    future_perfect,
    future_perfect_passive,
    future_perf_cont,
    would_ind_active,
    would_ind_passive,
    would_cont_active,
    would_perf_active,
    would_perf_passive,
    should_ind_active,
    should_ind_passive,
    shall_ind_active,
    shall_ind_passive,
    should_cont,
    should_perf_active,
    should_perf_passive,
    must_ind_active,
    must_cont,
    must_perf_active,
    must_perf_passive,
    can_ind,
    can_ind_passive,
    could_ind_active,
    could_ind_passive,
    can_cont,
    could_cont,
    could_perf_active,
    could_perf_passive,
    may_ind_active,
    may_ind_passive,
    might_ind_active,
    might_ind_passive,
    may_cont,
    might_perf_active,
    might_perf_passive,
    may_perf_passive,
]
