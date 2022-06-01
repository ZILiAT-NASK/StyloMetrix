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


from stylo_metrix.pipeline.en.dictionary_en import TAGS_DICT

""" METRICS FOR THE PRESENT TENSES [PASSIVE & ACTIVE VOICE]"""


def classify_pos(token):
    for pos, tags in TAGS_DICT.items():
        if token.tag_ in tags:
            return pos


def present_simple(doc):
    present_simple = {}

    for token in doc:
        if token.tag_ == "VBP" and [child.pos_ != "AUX" for child in token.children]:
            present_simple[token] = "present_simple"

    for token in doc:
        if token.lemma_ == "do" and (token.tag_ == "VBZ" or token.tag_ == "VBP") and token.head.tag_ == "VB":
            head = token.head
            present_simple[head] = "present_simple"
            present_simple[token] = "present_simple"
            for t in head.subtree:
                if t.tag_ == "VB" and t.dep_ == "conj":
                    present_simple[t] = "present_simple"
    return present_simple


def present_ind_3p(doc):
    present_ind_3p = {}

    for token in doc:
        if token.tag_ == "VBZ" and [child.pos_ != "AUX" for child in token.children]:
            present_ind_3p[token] = "present_ind_3p"

    return present_ind_3p


def present_cont(doc):
    present_cont = {}

    for token in doc:

        if token.lemma_ == "be" and (
                token.tag_ == "VBZ" or token.tag_ == "VBP") and token.dep_ == "aux" and token.head.tag_ == "VBG":
            head = token.head
            present_cont[head] = "present_cont"
            present_cont[token] = "present_cont"

            for t in head.subtree:
                if t.tag_ == "VBG" and t.dep_ == "conj":
                    present_cont[t] = "present_cont"

    return present_cont


def present_perfect_cont(doc):
    present_perfect_cont = {}

    for token in doc:
        if token.dep_ == "auxpass" and (token.text == "'s" or token.text == "’s") and token.head.tag_ == "VBG":
            head = token.head

            for t in head.subtree:
                if t.text == "been" and t.dep_ == "aux":
                    present_perfect_cont[head] = "present_perfect_cont"
                    present_perfect_cont[token] = "present_perfect_cont"
                    present_perfect_cont[t] = "present_perfect_cont"

                for i in head.subtree:
                    if i.tag_ == "VBG" and i.dep_ == "conj":
                        present_perfect_cont[i] = "present_perfect_cont"

        if token.dep_ == "aux" and token.lemma_ == "'ve" and token.head.tag_ == "VBG":
            head = token.head

            for tok in head.subtree:
                if tok.text == "been" and tok.dep_ == "aux":
                    present_perfect_cont[head] = "present_perfect_cont"
                    present_perfect_cont[token] = "present_perfect_cont"
                    present_perfect_cont[tok] = "present_perfect_cont"

            for j in head.subtree:
                if j.tag_ == "VBG" and j.dep_ == "conj":
                    present_perfect_cont[j] = "present_perfect_cont"

        if token.lemma_ == "have" and (token.tag_ == "VBZ" or token.tag_ == "VBP") and token.head.tag_ == "VBG":
            head = token.head

            for tkn in head.subtree:
                if tkn.text == "been" and tkn.dep_ == "aux":
                    present_perfect_cont[head] = "present_perfect_cont"
                    present_perfect_cont[token] = "present_perfect_cont"
                    present_perfect_cont[tkn] = "present_perfect_cont"

            for l in head.subtree:
                if l.tag_ == "VBG" and l.dep_ == "conj":
                    present_perfect_cont[l] = "present_perfect_cont"

    return present_perfect_cont


def present_ind_pas(doc):
    present_ind_pas = {}

    for token in doc:
        if (
                token.tag_ == "VBP" or token.tag_ == "VBZ") and token.dep_ == "auxpass" and token.lemma_ == 'be' and token.head.tag_ == "VBN":
            head = token.head
            present_ind_pas[head] = "present_ind_passive"

            for child in head.subtree:
                if child.text == "been" and child.dep_ == "auxpass":
                    del present_ind_pas[head]
                if child.text == "been" and child.dep_ == "ROOT":
                    del present_ind_pas[head]
            if head in present_ind_pas.keys():
                present_ind_pas[token] = "present_ind_passive"
            for t in head.children:
                if t.tag_ == "VBN" and t.dep_ == "conj" and head in present_ind_pas:
                    present_ind_pas[t] = "present_ind_passive"
    return present_ind_pas


def present_cont_pas(doc):
    present_cont_pas = {}

    for token in doc:
        if (token.tag_ == "VBZ" or token.tag_ == "VBP") and token.lemma_ == "be" and token.dep_ == "aux":
            head = token.head

            for t in head.subtree:
                if t.text == "being" and t.dep_ == "auxpass" and head not in present_cont_pas:
                    present_cont_pas[head] = "present_cont_passive"
                    present_cont_pas[t] = "present_cont_passive"
                    present_cont_pas[token] = "present_cont_passive"

                if t.tag_ == "VBN" and t.dep_ == "conj":
                    present_cont_pas[t] = "present_cont_passive"
    return present_cont_pas


def present_perfect_passive(doc):
    present_perfect_passive = {}

    for token in doc:
        if token.lemma_ == "have" and (token.tag_ == "VBZ" or token.tag_ == "VBP") and token.head.tag_ == "VBN":
            head = token.head

            for t in head.subtree:
                if t.text == "been" and t.dep_ == "auxpass" and head not in present_perfect_passive:
                    present_perfect_passive[head] = "present_perfect_passive"
                    present_perfect_passive[token] = "present_perfect_passive"
                    present_perfect_passive[t] = "present_perfect_passive"

            for tok in head.children:
                if tok.tag_ == "VBN" and tok.dep_ == "conj" and head in present_perfect_passive:
                    present_perfect_passive[tok] = "present_perfect_passive"

        if (token.tag_ == "VBZ" or token.tag_ == "VBP") and token.head.tag_ == "VBN":
            head = token.head

            for j in head.subtree:
                if j.text == "been" and j.dep_ == "auxpass" and head not in present_perfect_passive:
                    present_perfect_passive[head] = "present_perfect_passive"
                    present_perfect_passive[token] = "present_perfect_passive"
                    present_perfect_passive[j] = "present_perfect_passive"

            for tkn in head.children:
                if tkn.tag_ == "VBN" and tkn.dep_ == "conj" and head in present_perfect_passive:
                    present_perfect_passive[tkn] = "present_perfect_passive"

    return present_perfect_passive


def present_perfect(doc):
    verbs = []
    aux = {}

    verbs_perfect_passive = present_perfect_passive(doc)
    verbs_ind_pas = present_ind_pas(doc)
    verbs_cont_pas = present_cont_pas(doc)

    for token in doc:

        if token.lemma_ == "have" and (token.tag_ == "VBZ" or token.tag_ == "VBP") and token.head.tag_ == "VBN":
            head = token.head

            if head not in verbs:
                verbs.append(head)
                verbs.append(token)

            for key in verbs_perfect_passive:
                for verb in verbs:
                    if key == verb:
                        verbs.remove(head)
                        verbs.remove(token)

            for tok in head.children:
                if tok.tag_ == "VBN" and tok.dep_ == "conj" and head in verbs and tok not in verbs:
                    verbs.append(tok)

        if (token.tag_ == "VBZ" or token.tag_ == "VBP") and token.head.tag_ == "VBN":
            head = token.head

            if head not in verbs:
                verbs.append(head)

            for key in verbs_perfect_passive:
                for verb in verbs:
                    if key == verb:
                        verbs.remove(head)

            for key in verbs_ind_pas:
                for verb in verbs:
                    if key == verb:
                        verbs.remove(head)

            for key in verbs_cont_pas:
                for verb in verbs:
                    if key == verb:
                        verbs.remove(head)

            for tok in head.subtree:
                if tok.tag_ == "VBN" and tok.dep_ == "conj" and head in verbs and tok not in verbs:
                    verbs.append(tok)

            if head in verbs:
                aux[token] = "present_perfect"

    present_perfect = {}

    for verb in verbs:
        present_perfect[verb] = "present_perfect"

    present_perfect_ = present_perfect | aux

    return present_perfect_


""" METRICS FOR THE PAST TENSES [PASSIVE & ACTIVE VOICE]"""


def past_simple_passive(doc):
    past_ind_passive = {}

    for token in doc:

        if token.lemma_ == "be" and token.tag_ == "VBD" and token.dep_ == "auxpass" and token.head.tag_ == "VBN":
            head = token.head
            past_ind_passive[head] = "past_ind_passive"

            for child in head.children:
                if child.text == "been" and child.dep_ == "auxpass":
                    del past_ind_passive[head]

            for tok in head.subtree:
                if tok.tag_ == "VBN" and tok.dep_ == "conj":
                    past_ind_passive[tok] = "past_ind_passive"

            if head in past_ind_passive.keys():
                past_ind_passive[token] = "past_ind_passive"

    return past_ind_passive


def past_simple(doc):
    past_ind = {}

    for token in doc:
        if token.lemma_ == "be":
            continue
        if token.lemma_ == "have" and [child.tag_ == "VBN" for child in token.children]:
            continue
        if token.pos_ != "AUX" and token.tag_ == "VBD":
            past_ind[token] = "past_simple"

        if token.lemma_ == "do" and token.tag_ == "VBD" and token.head.tag_ == "VB":
            head = token.head
            past_ind[head] = "past_simple"
            past_ind[token] = "past_simple"
            for t in head.subtree:
                if t.tag_ == "VB" and t.dep_ == "conj":
                    past_ind[t] = "past_simple"

    return past_ind


def past_simple_be(doc):
    past_ind_be = {}

    for token in doc:
        for child in token.children:
            if token.lemma_ == "be" and token.tag_ == "VBD" and child.tag_ != "VBG" and token not in past_ind_be:
                past_ind_be[token] = "past_ind_be"

    return past_ind_be


def past_cont_passive(doc):
    past_cont_passive = {}

    for token in doc:
        if token.lemma_ == "be" and token.tag_ == "VBD" and token.head.tag_ == "VBN":
            head = token.head

            for child in head.children:
                if child.text == "being" and child.tag_ == "VBG":
                    past_cont_passive[head] = "past_cont_passive"
                    past_cont_passive[child] = "past_cont_passive"
                    past_cont_passive[token] = "past_cont_passive"

            for t in head.subtree:
                if t.tag_ == "VBN" and t.dep_ == "conj" and head in past_cont_passive and t not in past_cont_passive:
                    past_cont_passive[t] = "past_cont_passive"

    return past_cont_passive


def past_cont(doc):
    past_cont = {}

    for token in doc:
        if token.lemma_ == "be" and token.tag_ == "VBD" and token.head.tag_ == "VBG":
            head = token.head
            past_cont[head] = "past_cont"
            past_cont[token] = "past_cont"
            for t in head.subtree:
                if t.tag_ == "VBG" and t.dep_ == "conj" and t not in past_cont:
                    past_cont[t] = "past_cont"

    return past_cont


def past_perfect(doc):
    past_perf = {}

    for token in doc:
        if token.tag_ == "VBD" and token.dep_ == "aux" and token.lemma_ == "have" and token.head.tag_ == "VBN":
            head = token.head
            past_perf[head] = "past_perf"

            for child in head.children:
                if child.text == "been" and child.dep_ == "auxpass":
                    del past_perf[head]

            for t in head.subtree:
                if t.tag_ == "VBN" and t.dep_ == "conj" and head in past_perf and t not in past_perf:
                    past_perf[t] = "past_perf"

        if (token.text == "'d" or token.text == "’d") and (token.head.tag_ == "VBN" or token.head.tag_ == "VBD"):
            head = token.head
            past_perf[head] = "past_perf"

            for child in head.children:
                if child.lemma_ == "be" and child.dep_ == "auxpass" and head in past_perf:
                    del past_perf[head]

            for tok in head.subtree:
                if tok.tag_ == "VBN" and tok.dep_ == "conj" and head in past_perf and tok not in past_perf:
                    past_perf[tok] = "past_perf"

            if head in past_perf.keys():
                past_perf[token] = "past_perf"

    return past_perf


def past_perf_passive(doc):
    past_perf_passive = {}

    for token in doc:
        if token.tag_ == "VBD" and token.lemma_ == "have" and token.head.tag_ == "VBN":
            head = token.head

            for child in head.children:
                if child.text == "been" and child.dep_ == "auxpass":
                    past_perf_passive[head] = "past_perf_passive"
                    past_perf_passive[token] = "past_perf_passive"
                    past_perf_passive[child] = "past_perf_passive"

            for t in head.subtree:
                if t.tag_ == "VBN" and t.dep_ == "conj" and head in past_perf_passive and t not in past_perf_passive:
                    past_perf_passive[t] = "past_perf_passive"

                    # make sure that no past simple passive verbs are regarded as
                    # synonyms of the past perfect passive
                    for ch in t.children:
                        if ch.lemma_ == "be" and (ch.tag_ == "VBD" or ch.tag_ == "VBG") and t in past_perf_passive:
                            del past_perf_passive[t]

        if (token.text == "'d" or token.text == "’d") and token.head.tag_ == "VBN":
            head = token.head

            for child in head.children:
                if child.lemma_ == "be" and child.dep_ == "auxpass":
                    past_perf_passive[head] = "past_perf_passive"
                    past_perf_passive[token] = "past_perf_passive"
                    past_perf_passive[child] = "past_perf_passive"

            for tok in head.subtree:
                if tok.tag_ == "VBN" and tok.dep_ == "conj" and head in past_perf_passive:
                    past_perf_passive[tok] = "past_perf_passive"

                    for chld in tok.children:
                        if chld.lemma_ == "be" and (chld.tag_ == "VBD" or chld.tag_ == "VBG"):
                            del past_perf_passive[tok]

    return past_perf_passive


def past_perfect_cont(doc):
    past_perfect_cont = {}

    for token in doc:
        if token.tag_ == "VBD" and token.lemma_ == "have" and token.head.tag_ == "VBG":
            head = token.head
            past_perfect_cont[head] = "past_perf_cont"
            past_perfect_cont[token] = "past_perf_cont"

            for j in head.children:
                if j.text == "been":
                    past_perfect_cont[j] = "past_perf_cont"

            for t in head.subtree:
                if t.tag_ == "VBG" and t.dep_ == "conj" and t not in past_perfect_cont:
                    past_perfect_cont[t] = "past_perf_cont"

    return past_perfect_cont


""" METRICS FOR THE FUTURE TENSES [PASSIVE & ACTIVE VOICE]"""


def future_simple(doc):
    future_simple = {}

    for token in doc:
        if (str(token)[len(str(token)) - 2:] == "ll" or token.lemma_ == "will") \
                and token.head.tag_ == "VB" and token.head not in future_simple:
            head = token.head

            for t in head.subtree:
                if t.tag_ == "VB" and t.dep_ != "xcomp":
                    future_simple[t] = "future_simple"
                    future_simple[token] = "future_simple"

    return future_simple


def future_simple_passive(doc):
    future_simple_passive = {}

    for token in doc:
        if (str(token)[
            len(str(token)) - 2:] == "ll" or token.lemma_ == "will") and \
                token.head.tag_ == "VBN" and token.head not in future_simple_passive:
            head = token.head

            for t in head.children:
                if t.text == "be" and t.dep_ == "auxpass":
                    future_simple_passive[head] = "future_simple_passive"
                    future_simple_passive[token] = "future_simple_passive"
                    future_simple_passive[t] = "future_simple_passive"

            for child in head.subtree:
                if child.tag_ == "VBN" and child.dep_ == "conj" and head in future_simple_passive:
                    future_simple_passive[child] = "future_simple_passive"

                    for ch in child.children:
                        if (
                                ch.text == "being" or ch.text == "been") and ch.dep_ == "auxpass" and child in future_simple_passive:
                            del future_simple_passive[child]

    return future_simple_passive


def future_cont(doc):
    future_progr = {}
    for token in doc:
        if (str(token)[len(str(token)) - 2:] == "ll" or token.lemma_ == "will") \
                and token.head.tag_ == "VBG" and token.head not in future_progr:
            head = token.head
            future_progr[head] = "future_progr"

            for t in head.subtree:
                if t.lemma_ == "have":
                    del future_progr[head]

                if t.tag_ == "VBG" and t.dep_ == "conj":
                    future_progr[t] = "future_progr"

            if head in future_cont.keys():
                future_progr[token] = "future_progr"

            for j in head.children:
                if j.text == "be":
                    future_progr[j] = "future_progr"
    return future_progr


def future_progr_passive(doc):
    future_progr_passive = {}

    for token in doc:
        if (str(token)[len(str(token)) - 2:] == "ll" or token.lemma_ == "will") \
                and token.head.tag_ == "VBN" and token.head not in future_progr_passive:
            head = token.head

            for t in head.children:
                if t.text == "being" and t.dep_ == "auxpass":
                    future_progr_passive[head] = "future_progr_passive"
                    future_progr_passive[t] = "future_progr_passive"
                    future_progr_passive[token] = "future_progr_passive"

                if t.text == "be" and head in future_progr_passive.keys():
                    future_progr_passive[t] = "future_progr_passive"

                if t.tag_ == "VBN" and t.dep_ == "conj" and head in future_progr_passive:
                    future_progr_passive[t] = "future_progr_passive"

                    for chld in t.children:
                        if chld.text == "be" or chld.text == "been" and chld.dep_ == "auxpass" and t in future_progr_passive:
                            del future_progr_passive[t]

    return future_progr_passive


def future_perfect(doc):
    future_perfect = {}

    for token in doc:
        if (str(token)[len(str(token)) - 2:] == "ll" or token.lemma_ == "will") \
                and token.head.tag_ == "VBN" and token.head not in future_perfect:
            head = token.head

            for t in head.children:
                if t.lemma_ == "have" and t.dep_ == "aux":
                    future_perfect[head] = "future_perfect"
                if t.text == "been" and t.dep_ == "auxpass":
                    del future_perfect[head]

            for tok in head.subtree:
                if tok.tag_ == "VBN" and tok.dep_ == "conj" and head in future_perfect:
                    future_perfect[tok] = "future_perfect"

                for chld in tok.children:
                    if (chld.text == "being" or chld.text == "be") and tok in future_perfect:
                        del future_perfect[tok]

            if head in future_perfect.keys():
                for j, k in head.children:
                    if j.text == "been" and k.text == "have":
                        future_perfect[j] = "future_perfect"
                        future_perfect[k] = "future_perfect"

    return future_perfect


def future_perfect_passive(doc):
    future_perf_passive = {}

    for token in doc:
        if (str(token)[len(str(token)) - 2:] == "ll" or token.lemma_ == "will") \
                and token.head.tag_ == "VBN" and token.head not in future_perf_passive:
            head = token.head

            for child in head.children:
                if child.text == "been" and child.dep_ == "auxpass":
                    future_perf_passive[head] = "future_perf_passive"
                    future_perf_passive[token] = "future_perf_passive"
                    future_perf_passive[child] = "future_perf_passive"

            for chld in head.subtree:
                if chld.tag_ == "VBN" and chld.dep_ == "conj" and head in future_perf_passive:
                    future_perf_passive[chld] = "future_perf_passive"

                for t in chld.children:
                    if (t.text == "be" or t.text == "being") and t.dep_ == "auxpass" and chld in future_perf_passive:
                        del future_perf_passive[chld]

    return future_perf_passive


def future_perf_cont(doc):
    future_perfect_cont = {}
    for token in doc:
        if (str(token)[len(str(token)) - 2:] == "ll" or token.lemma_ == "will") \
                and token.head.tag_ == "VBG" and token.head not in future_perfect_cont:
            head = token.head

            for t in head.children:
                if t.tag_ == "VBN" and t.lemma_ == "be":
                    future_perfect_cont[head] = "future_perfect_cont"
                    future_perfect_cont[t] = "future_perfect_cont"
                    future_perfect_cont[token] = "future_perfect_cont"
    return future_perfect_cont


""" METRICS FOR MODAL VERBS [PASSIVE & ACTIVE VOICE]"""


def would_ind_active(doc):
    would_ind_active = {}

    for token in doc:
        if token.lemma_ == "would" and token.head.tag_ == "VB":
            head = token.head
            would_ind_active[head] = "would_ind_active"
            would_ind_active[token] = "would_ind_active"

            for t in head.subtree:
                if t.tag_ == "VB" and t.dep_ == "conj":
                    would_ind_active[t] = "would_ind_active"
    return would_ind_active


def would_ind_passive(doc):
    would_ind_passive = {}

    for token in doc:
        if token.lemma_ == "would" and token.head.tag_ == "VBN":
            head = token.head

            for tkn in head.children:
                if tkn.text == "be" and tkn.dep_ == "auxpass":
                    would_ind_passive[head] = "would_ind_passive"
                    would_ind_passive[token] = "would_ind_passive"
                    would_ind_passive[tkn] = "would_ind_passive"

            for t in head.subtree:
                if t.tag_ == "VBN" and t.dep_ == "conj" and head in would_ind_passive:
                    would_ind_passive[t] = "would_ind_passive"

    return would_ind_passive


def would_cont_active(doc):
    would_cont_active = {}

    for token in doc:

        if token.lemma_ == "would" and token.head.tag_ == "VBG":
            head = token.head

            for t in head.subtree:
                if t.text == "be":
                    would_cont_active[head] = "would_cont"
                    would_cont_active[t] = "would_cont"
                    would_cont_active[token] = "would_cont"

                    for j in head.subtree:
                        if j.tag_ == "VBG" and j.dep_ == "conj":
                            would_cont_active[j] = "would_cont"
    return would_cont_active


def would_perf_active(doc):
    would_perf_active = {}

    for token in doc:
        if (token.lemma_ == "would" or token.lemma_ == "'d" or token.lemma_ == "’d") and token.head.tag_ == "VBN":
            head = token.head

            for t in head.children:
                if t.lemma_ == "have":
                    would_perf_active[head] = "would_perf_active"

            for k in head.children:
                if k.lemma_ == "be" and head in would_perf_active:
                    del would_perf_active[head]

            if head in would_perf_active.keys():
                would_perf_active[token] = "would_perf_active"
                for tkn in head.children:
                    if tkn.lemma_ == "have":
                        would_perf_active[tkn] = "would_perf_active"

            for j in head.subtree:
                if (j.tag_ == "VBN" or j.tag_ == "VBD") and j.dep_ == "conj" and head in would_perf_active:
                    would_perf_active[j] = "would_perf_active"

    return would_perf_active


def would_perf_passive(doc):
    would_perf_passive = {}

    for token in doc:

        if (token.lemma_ == "would" or token.lemma_ == "'d" or token.lemma_ == "’d") and token.head.tag_ == "VBN":
            head = token.head

            for k in head.children:
                if k.text == "been" and k.dep_ == "auxpass":
                    would_perf_passive[head] = "would_perf_passive"

            for j in head.subtree:
                if (j.tag_ == "VBN" or j.tag_ == "VBD") and j.dep_ == "conj" and head in would_perf_passive:
                    would_perf_passive[j] = "would_perf_passive"

    return would_perf_passive


def should_ind_active(doc):
    should_ind_active = {}

    for token in doc:

        if token.lemma_ == "should" and token.head.tag_ == "VB":
            head = token.head
            should_ind_active[head] = "should_ind_active"
            should_ind_active[token] = "should_ind_active"
            for t in head.subtree:
                if t.tag_ == "VB" and t.dep_ == "conj":
                    should_ind_active[t] = "should_ind_active"
    return should_ind_active


def should_ind_passive(doc):
    should_ind_passive = {}

    for token in doc:

        if token.lemma_ == "should" and token.head.tag_ == "VBN":
            head = token.head

            for tkn in head.children:
                if tkn.text == "be" and tkn.dep_ == "auxpass":
                    should_ind_passive[head] = "should_ind_passive"
                    should_ind_passive[tkn] = "should_ind_passive"
                    should_ind_passive[token] = "should_ind_passive"

            for t in head.subtree:
                if t.tag_ == "VBN" and t.dep_ == "conj" and head in should_ind_passive:
                    should_ind_passive[t] = "should_ind_passive"
    return should_ind_passive


def shall_ind_active(doc):
    shall_ind_active = {}

    for token in doc:

        if token.lemma_ == "shall" and token.head.tag_ == "VB":
            head = token.head
            shall_ind_active[head] = "shall_ind_active"
            shall_ind_active[token] = "shall_ind_active"
            for t in head.subtree:
                if t.tag_ == "VB" and t.dep_ == "conj":
                    shall_ind_active[t] = "shall_ind_active"
    return shall_ind_active


def shall_ind_passive(doc):
    shall_ind_passive = {}

    for token in doc:

        if token.lemma_ == "shall" and token.head.tag_ == "VBN":
            head = token.head

            for tkn in head.children:
                if tkn.text == "be" and tkn.dep_ == "auxpass":
                    shall_ind_passive[head] = "shall_ind_passive"
                    shall_ind_passive[tkn] = "aux_shall_ind_passive"
                    shall_ind_passive[token] = "shall_ind_passive"

            for t in head.subtree:
                if t.tag_ == "VBN" and t.dep_ == "conj" and head in shall_ind_passive:
                    shall_ind_passive[t] = "shall_ind_passive"
    return shall_ind_passive


def should_cont(doc):
    should_cont = {}

    for token in doc:

        if token.lemma_ == "should" and token.head.tag_ == "VBG":
            head = token.head

            for t in head.subtree:
                if t.text == "be":
                    should_cont[head] = "should_cont"
                    should_cont[t] = "aux_should_cont"
                    should_cont[token] = "should_cont"

                    for j in head.subtree:
                        if j.tag_ == "VBG" and j.dep_ == "conj":
                            should_cont[j] = "should_cont"
    return should_cont


def should_perf_active(doc):
    should_perf_active = {}

    for token in doc:

        if token.lemma_ == "should" and token.head.tag_ == "VBN":
            head = token.head

            for t in head.children:
                if t.text == "have":
                    should_perf_active[head] = "should_perf_active"
                    should_perf_active[t] = "should_perf_active"

            for j in head.children:
                if j.lemma_ == "be" and head in should_perf_active:
                    del should_perf_active[head]
                    del should_perf_active[t]

            if head in should_perf_active.keys():
                should_perf_active[token] = "should_perf_active"

            for k in head.subtree:
                if (k.tag_ == "VBN" or k.tag_ == "VBD") and k.dep_ == "conj" and head in should_perf_active:
                    should_perf_active[k] = "should_perf_active"
    return should_perf_active


def should_perf_passive(doc):
    should_perf_passive = {}

    for token in doc:

        if token.lemma_ == "should" and token.head.tag_ == "VBN":
            head = token.head

            for t in head.children:
                if t.text == "been" and t.dep_ == "auxpass":
                    should_perf_passive[head] = "should_perf_passive"
                    should_perf_passive[t] = "should_perf_passive"
                    should_perf_passive[token] = "should_perf_passive"
                if t.lemma_ == "have":
                    should_perf_passive[t] = "should_perf_passive"

            for j in head.subtree:
                if (j.tag_ == "VBN" or j.tag_ == "VBD") and j.dep_ == "conj" and head in should_perf_passive:
                    should_perf_passive[j] = "should_perf_passive"
    return should_perf_passive


def must_ind_active(doc):
    must_ind_active = {}

    for token in doc:

        if token.lemma_ == "must" and token.head.tag_ == "VB":
            head = token.head
            must_ind_active[head] = "must_ind_active"
            must_ind_active[token] = "must_ind_active"
            for t in head.subtree:
                if t.tag_ == "VB" and t.dep_ == "conj":
                    must_ind_active[t] = "must_ind_active"
    return must_ind_active


def must_ind_passive(doc):
    must_ind_passive = {}

    for token in doc:

        if token.lemma_ == "must" and token.head.tag_ == "VBN":
            head = token.head

            for tkn in head.children:
                if tkn.text == "be" and tkn.dep_ == "auxpass":
                    must_ind_passive[head] = "must_ind_passive"
                    must_ind_passive[token] = "must_ind_passive"
                    must_ind_passive[tkn] = "must_ind_passive"

            for t in head.subtree:
                if t.tag_ == "VBN" and t.dep_ == "conj" and head in must_ind_passive:
                    must_ind_passive[t] = "must_ind_passive"
    return must_ind_passive


def must_cont(doc):
    must_cont = {}

    for token in doc:

        if token.lemma_ == "must" and token.head.tag_ == "VBG":
            head = token.head

            for t in head.subtree:
                if t.text == "be":
                    must_cont[head] = "must_cont"
                    must_cont[token] = "must_cont"
                    must_cont[t] = "must_cont"

                    for j in head.subtree:
                        if j.tag_ == "VBG" and j.dep_ == "conj":
                            must_cont[j] = "must_cont"
    return must_cont


def must_perf_active(doc):
    must_perf_active = {}

    for token in doc:

        if token.lemma_ == "must" and token.head.tag_ == "VBN":
            head = token.head

            for t in head.subtree:
                if t.text == "have":
                    must_perf_active[head] = "must_perf_active"
                    must_perf_active[t] = "must_perf_active"

            for tkn in head.children:
                if tkn.lemma_ == "be" and head in must_perf_active:
                    del must_perf_active[head]
                    del must_perf_active[t]

            if head in must_perf_active.keys():
                must_perf_active[token] = "must_perf_active"

            for j in head.subtree:
                if (j.tag_ == "VBN" or j.tag_ == "VBD") and j.dep_ == "conj":
                    must_perf_active[j] = "must_perf_active"
    return must_perf_active


def must_perf_passive(doc):
    must_perf_passive = {}

    for token in doc:

        if token.lemma_ == "must" and token.head.tag_ == "VBN":
            head = token.head

            for tkn in head.children:
                if tkn.text == "been" and tkn.dep_ == "auxpass":
                    must_perf_passive[head] = "could_perf_passive"
                    must_perf_passive[token] = "could_perf_passive"
                    must_perf_passive[tkn] = "could_perf_passive"
                if tkn.lemma_ == "have":
                    must_perf_passive[tkn] = "could_perf_passive"

            for j in head.subtree:
                if (j.tag_ == "VBN" or j.tag_ == "VBD") and j.dep_ == "conj" and head in must_perf_passive:
                    must_perf_passive[j] = "must_perf_active"
    return must_perf_passive


def can_ind(doc):
    can_ind = {}

    for token in doc:

        if token.lemma_ == "can" and token.head.tag_ == "VB":
            head = token.head
            can_ind[head] = "can_ind"
            can_ind[token] = "can_ind"
            for t in head.subtree:
                if t.tag_ == "VB" and t.dep_ == "conj":
                    can_ind[t] = "can_ind"
    return can_ind


def can_ind_passive(doc):
    can_present_ind_passive = {}

    for token in doc:

        if token.lemma_ == "can" and token.head.tag_ == "VBN":
            head = token.head

            for tkn in head.children:
                if tkn.text == "be" and tkn.dep_ == "auxpass":
                    can_present_ind_passive[head] = "can_ind_passive"
                    can_present_ind_passive[tkn] = "can_ind_passive"
                    can_present_ind_passive[token] = "can_ind_passive"

            for t in head.subtree:
                if t.tag_ == "VBN" and t.dep_ == "conj" and head in can_present_ind_passive:
                    can_present_ind_passive[t] = "can_ind_passive"

    return can_present_ind_passive


def could_ind_active(doc):
    could_ind_active = {}

    for token in doc:

        if token.lemma_ == "could" and token.head.tag_ == "VB":
            head = token.head
            could_ind_active[head] = "could_ind"
            could_ind_active[token] = "could_ind"
            for t in head.subtree:
                if t.tag_ == "VB" and t.dep_ == "conj":
                    could_ind_active[t] = "could_ind"
    return could_ind_active


def could_ind_passive(doc):
    could_ind_passive = {}

    for token in doc:

        if token.lemma_ == "could" and token.head.tag_ == "VBN":
            head = token.head

            for tkn in head.children:
                if tkn.text == "be" and tkn.dep_ == "auxpass":
                    could_ind_passive[head] = "could_ind_passive"
                    could_ind_passive[token] = "could_ind_passive"
                    could_ind_passive[tkn] = "could_ind_passive"

            for t in head.subtree:
                if t.tag_ == "VBN" and t.dep_ == "conj" and head in could_ind_passive:
                    could_ind_passive[t] = "could_ind_passive"
    return could_ind_passive


def can_cont(doc):
    can_cont = {}

    for token in doc:

        if token.lemma_ == "can" and token.head.tag_ == "VBG":
            head = token.head

            for t in head.subtree:
                if t.text == "be":
                    can_cont[head] = "can_cont"
                    can_cont[t] = "can_cont"
                    can_cont[token] = "can_cont"

                    for j in head.subtree:
                        if j.tag_ == "VBG" and j.dep_ == "conj":
                            can_cont[j] = "can_cont"
    return can_cont


def could_cont(doc):
    could_cont = {}

    for token in doc:

        if token.lemma_ == "could" and token.head.tag_ == "VBG":
            head = token.head

            for t in head.subtree:
                if t.text == "be":
                    could_cont[head] = "could_cont"
                    could_cont[token] = "could_cont"
                    could_cont[t] = "could_cont"

                    for j in head.subtree:
                        if j.tag_ == "VBG" and j.dep_ == "conj":
                            could_cont[j] = "could_cont"
    return could_cont


def could_perf_active(doc):
    could_perf_active = {}

    for token in doc:

        if token.lemma_ == "could" and token.head.tag_ == "VBN":
            head = token.head

            for t in head.subtree:
                if t.lemma_ == "have":
                    could_perf_active[head] = "could_perf"
                    could_perf_active[t] = "could_perf"

            for j in head.children:
                if j.lemma_ == "be" and head in could_perf_active:
                    del could_perf_active[head]
                    del could_perf_active[t]

            if head in could_perf_active.keys():
                could_perf_active[token] = "could_perf"

            for k in head.subtree:
                if k.tag_ == "VBN" and k.dep_ == "conj" and head in could_perf_active:
                    could_perf_active[k] = "could_perf"
    return could_perf_active


def could_perf_passive(doc):
    could_perf_passive = {}

    for token in doc:

        if token.lemma_ == "could" and token.head.tag_ == "VBN":
            head = token.head

            for t in head.children:
                if t.text == "been":
                    could_perf_passive[head] = "could_perf_passive"
                    could_perf_passive[t] = "could_perf_passive"
                    could_perf_passive[token] = "could_perf_passive"
                if t.lemma_ == "have":
                    could_perf_passive[t] = "could_perf_passive"

            for k in head.subtree:
                if k.tag_ == "VBN" and k.dep_ == "conj" and head in could_perf_passive:
                    could_perf_passive[k] = "could_perf_passive"
    return could_perf_passive


def may_ind_active(doc):
    may_ind_active = {}

    for token in doc:

        if token.lemma_ == "may" and token.head.tag_ == "VB":
            head = token.head
            may_ind_active[head] = "may_ind"
            may_ind_active[token] = "may_ind"
            for t in head.subtree:
                if t.tag_ == "VB" and t.dep_ == "conj":
                    may_ind_active[t] = "may_ind"
    return may_ind_active


def may_ind_passive(doc):
    may_ind_passive = {}

    for token in doc:

        if token.lemma_ == "may" and token.head.tag_ == "VBN":
            head = token.head

            for tkn in head.children:
                if tkn.text == "be" and tkn.dep_ == "auxpass":
                    may_ind_passive[head] = "may_ind_passive"
                    may_ind_passive[tkn] = "may_ind_passive"
                    may_ind_passive[token] = "may_ind_passive"

            for t in head.subtree:
                if t.tag_ == "VBN" and t.dep_ == "conj" and head in may_ind_passive:
                    may_ind_passive[t] = "may_ind_passive"
    return may_ind_passive


def might_ind_active(doc):
    might_ind_active = {}

    for token in doc:

        if token.lemma_ == "might" and token.head.tag_ == "VB":
            head = token.head
            might_ind_active[head] = "might_ind"
            might_ind_active[token] = "might_ind"
            for t in head.subtree:
                if t.tag_ == "VB" and t.dep_ == "conj":
                    might_ind_active[t] = "might_ind"
    return might_ind_active


def might_ind_passive(doc):
    might_ind_passive = {}

    for token in doc:

        if token.lemma_ == "might" and token.head.tag_ == "VBN":
            head = token.head

            for tkn in head.children:
                if tkn.text == "be" and tkn.dep_ == "auxpass":
                    might_ind_passive[head] = "might_ind_passive"
                    might_ind_passive[token] = "might_ind_passive"
                    might_ind_passive[tkn] = "might_ind_passive"

            for t in head.subtree:
                if t.tag_ == "VBN" and t.dep_ == "conj" and head in might_ind_passive:
                    might_ind_passive[t] = "might_ind_passive"
    return might_ind_passive


def may_cont(doc):
    may_cont = {}

    for token in doc:

        if token.lemma_ == "may" and token.head.tag_ == "VBG":
            head = token.head

            for t in head.subtree:
                if t.text == "be":
                    may_cont[head] = "may_cont"
                    may_cont[token] = "may_cont"
                    may_cont[t] = "may_cont"

                    for j in head.subtree:
                        if j.tag_ == "VBG" and j.dep_ == "conj":
                            may_cont[j] = "may_cont"
    return may_cont


def might_perf_active(doc):
    might_perf_active = {}

    for token in doc:

        if token.lemma_ == "might" and token.head.tag_ == "VBN":
            head = token.head

            for t in head.subtree:
                if t.text == "have":
                    might_perf_active[head] = "might_perf"
                    might_perf_active[t] = "might_perf"

            for tkn in head.children:
                if tkn.lemma_ == "be" and head in might_perf_active:
                    del might_perf_active[head]
                    del might_perf_active[t]

            if head in might_perf_active.keys():
                might_perf_active[token] = "might_perf"

            for j in head.subtree:
                if (j.tag_ == "VBN" or j.tag_ == "VBD") and j.dep_ == "conj":
                    might_perf_active[j] = "might_perf"
    return might_perf_active


def might_perf_passive(doc):
    might_perf_passive = {}

    for token in doc:

        if token.lemma_ == "might" and token.head.tag_ == "VBN":
            head = token.head

            for t in head.children:
                if t.text == "been" and t.dep_ == "auxpass":
                    might_perf_passive[head] = "might_perf_passive"
                    might_perf_passive[token] = "might_perf_passive"
                    might_perf_passive[t] = "might_perf_passive"
                if t.lemma_ == "have":
                    might_perf_passive[t] = "might_perf_passive"

            for k in head.subtree:
                if k.tag_ == "VBN" and k.dep_ == "conj" and head in might_perf_passive:
                    might_perf_passive[k] = "might_perf_passive"
    return might_perf_passive


def may_perf_passive(doc):
    may_perf_passive = {}

    for token in doc:

        if token.lemma_ == "may" and token.head.tag_ == "VBN":
            head = token.head

            for t in head.children:
                if t.text == "been" and t.dep_ == "auxpass":
                    may_perf_passive[head] = "may_perf_passive"
                    may_perf_passive[token] = "may_perf_passive"
                    may_perf_passive[t] = "may_perf_passive"
                if t.lemma_ == "have":
                    may_perf_passive[t] = "may_perf_passive"

            for k in head.subtree:
                if k.tag_ == "VBN" and k.dep_ == "conj" and head in may_perf_passive:
                    may_perf_passive[k] = "may_perf_passive"
    return may_perf_passive


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

        if "Degree=Sup" in token.morph and token.pos_ != "ADV":
            adj[token] = "superlative_adjective"

        if "Degree=Pos" in token.morph and token.pos_ == "ADJ":
            head = token
            for child in token.subtree:
                if "PunctType=Dash" in child.morph:
                    for t in token.children:
                        if "PunctType=Dash" not in t.morph:
                            adj[head] = "positive_adjective"
                            adj[t] = "positive_adjective"

        if token.pos_ == "ADJ" and (token.dep_ == "npadvmod" or token.dep_ == "advmod"):
            del adj[token]
    return adj
