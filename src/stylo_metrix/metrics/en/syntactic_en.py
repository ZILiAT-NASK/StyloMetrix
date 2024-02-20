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


import itertools

from ...structures import Category, Metric
from ...utils import ratio


class Syntactic(Category):
    lang = "en"
    name_en = "Syntactic"
    name_local = name_en


class SY_QUESTION(Metric):
    category = Syntactic
    name_en = "Number of words in interrogative sentences"
    name_local = name_en

    def count(doc):
        sentences = [sent.text.split() for sent in doc.sents if sent.text.endswith("?")]
        debug = list(itertools.chain.from_iterable(sentences))
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class SY_NARRATIVE(Metric):
    category = Syntactic
    name_en = "Number of words in narrative sentences"
    name_local = name_en

    def count(doc):
        sents = [sent.text.split() for sent in doc.sents if sent.text.endswith(".")]
        debug = list(itertools.chain.from_iterable(sents))
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class SY_NEGATIVE_QUESTIONS(Metric):
    category = Syntactic
    name_en = "Words in negative questions"
    name_local = name_en

    def count(doc):
        general_question = []
        for sent in doc.sents:
            if any(token for token in sent if token.dep_ == "neg"):
                broad_case = [
                    sent.text.split()
                    for token in sent
                    if token.is_sent_start
                    and token.head == token
                    and token.pos_ == "AUX"
                    and sent.text.endswith("?")
                ]
                # case_one = list(itertools.chain(*broad_case))
                general_question.append(broad_case)

                root = [
                    sent.text.split()
                    for token in sent
                    if token.head == token
                    and any(
                        child
                        for child in token.lefts
                        if child.dep_ == "aux" and child.is_sent_start
                    )
                    and sent not in broad_case
                    and sent.text.endswith("?")
                ]
                general_question.append(root)

                middle = [
                    sent.text.split()
                    for token in sent
                    if token.head == token
                    and any(child for child in token.lefts if child.dep_ == "aux")
                    and any(c for c in token.lefts if c.is_punct)
                    and sent.text.endswith("?")
                ]
                general_question.append(middle)

        debug = list(itertools.chain(*general_question))
        debug = list(itertools.chain(*debug))
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class SY_SPECIAL_QUESTIONS(Metric):
    category = Syntactic
    name_en = "Words in special questions"
    name_local = name_en

    def count(doc):
        QUESTION_WORDS = [
            "what",
            "which",
            "who",
            "whom",
            "whose",
            "where",
            "when",
            "why",
            "how",
        ]
        root = [
            [
                sent.text.split()
                for token in sent
                if token.head == token
                and any(
                    child
                    for child in token.lefts
                    if child.text.lower() in QUESTION_WORDS
                )
            ]
            for sent in doc.sents
        ]
        nested = list(itertools.chain(*root))
        debug = list(itertools.chain(*nested))
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class SY_TAG_QUESTIONS(Metric):
    category = Syntactic
    name_en = "Words in tag questions"
    name_local = name_en

    def count(doc):
        QUESTION_WORDS = [
            "what",
            "which",
            "who",
            "whom",
            "whose",
            "where",
            "when",
            "why",
            "how",
        ]
        tag_question = [
            sent.text.split()
            for sent in doc.sents
            if sent.text.endswith("?")
            and not any(
                token
                for token in sent
                if token.dep_ == "ROOT"
                and any(child for child in token.lefts if child.dep_ == "aux")
            )
            and not any(token for token in sent if token.text.lower() in QUESTION_WORDS)
            and any(token for token in sent if token.dep_ == "aux")
        ]
        debug = list(itertools.chain(*tag_question))
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class SY_GENERAL_QUESTIONS(Metric):
    category = Syntactic
    name_en = "Words in general questions"
    name_local = name_en

    def count(doc):
        general_question = []

        for sent in doc.sents:
            if any(token for token in sent if token.dep_ == "neg"):
                continue
            else:
                broad_case = [
                    sent.text.split()
                    for token in sent
                    if token.dep_ == "aux"
                    and token.is_sent_start
                    and sent.text.endswith("?")
                ]
                general_question.append(broad_case)

                root = [
                    sent.text.split()
                    for token in sent
                    if token.head == token
                    and any(
                        child
                        for child in token.lefts
                        if child.dep_ == "aux" and child.is_sent_start
                    )
                    and sent.text.endswith("?")
                ]
                general_question.append(root)

                middle = [
                    sent.text.split()
                    for token in sent
                    if token.head == token
                    and any(child for child in token.lefts if child.dep_ == "aux")
                    and any(c for c in token.lefts if c.is_punct)
                    and sent.text.endswith("?")
                ]
                general_question.append(middle)

        debug = list(itertools.chain(*general_question))
        debug = set(itertools.chain(*debug))
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class SY_EXCLAMATION(Metric):
    category = Syntactic
    name_en = "Number of words in exclamatory sentences"
    name_local = name_en

    def count(doc):
        sent = [
            sent.text.split()
            for sent in doc.sents
            for token in sent
            if sent.text.endswith("!")
        ]
        debug = set(itertools.chain.from_iterable(sent))
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class SY_IMPERATIVE(Metric):
    category = Syntactic
    name_en = "Words in imperative sentences"
    name_local = name_en

    def count(doc):
        sentence_tokens = [
            [token.text for token in sent if token.is_alpha]
            for sent in doc.sents
            if "VerbForm=Inf" in sent[0].morph and sent[0].tag_ == "VB"
        ]
        debug = set(itertools.chain.from_iterable(sentence_tokens))
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class SY_SUBORD_SENT(Metric):
    category = Syntactic
    name_en = "Words in subordinate sentences"
    name_local = name_en

    def count(doc):
        subord_sentences = [
            sent.text.split()
            for sent in doc.sents
            if any(token.pos_ == "SCONJ" or token.tag_ == "WDT" for token in sent)
        ]
        debug = [*itertools.chain(*subord_sentences)]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class SY_SUBORD_SENT_PUNCT(Metric):
    category = Syntactic
    name_en = "Punctuation in subordinate sentences"
    name_local = name_en

    def count(doc):
        sub_sent_punct = [
            sent for sent in doc.sents if any(token.pos_ == "SCONJ" for token in sent)
        ]
        debug = itertools.chain(*sub_sent_punct)
        debug = [tkn.text for tkn in debug if tkn.pos_ in "PUNCT"]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class SY_COORD_SENT(Metric):
    category = Syntactic
    name_en = "Words in coordinate sentences"
    name_local = name_en

    def count(doc):
        coord_sentences = [
            sent.text.split()
            for sent in doc.sents
            if any("ConjType=Cmp" in token.morph for token in sent)
        ]
        debug = [*itertools.chain(*coord_sentences)]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class SY_COORD_SENT_PUNCT(Metric):
    category = Syntactic
    name_en = "Punctuation in coordinate sentences"
    name_local = name_en

    def count(doc):
        coord_sent_punct = [
            sent for sent in doc.sents if any(token.pos_ == "CCONJ" for token in sent)
        ]
        debug = itertools.chain(*coord_sent_punct)
        debug = [tkn.text for tkn in debug if tkn.pos_ in "PUNCT"]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class SY_SIMPLE_SENT(Metric):
    category = Syntactic
    name_en = "Tokens in simple sentences"
    name_local = name_en

    def count(doc):
        simple_sent = [
            sent.text.split()
            for sent in doc.sents
            if not any(
                token
                for token in sent
                if (token.pos_ == "SCONJ" or token.pos_ == "CCONJ")
            )
        ]
        debug = [*itertools.chain(*simple_sent)]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class SY_INVERSE_PATTERNS(Metric):
    category = Syntactic
    name_en = "Incidents of inverse patterns"
    name_local = name_en

    def count(doc):
        # if token is npadvmod and goes before the ROOT verb
        pattern_1 = [
            sent.text.split()
            for sent in doc.sents
            for token in sent
            if token.dep_ == "npadvmod" and token.i < token.head.i
        ]
        # if token is dep and goes before the ROOT verb
        pattern_2 = [
            sent.text.split()
            for sent in doc.sents
            for token in sent
            if token.dep_ == "dep"
            and token.i < token.head.i
            and (token.text != "\n" or token.text != "\n\n")
        ]
        # if token is dobj and goes before the ROOT verb
        pattern_3 = [
            sent.text.split()
            for sent in doc.sents
            for token in sent
            if token.dep_ == "dobj" and token.i < token.head.i
        ]
        # if token determines a relative clause and goes before the ROOT
        pattern_4 = [
            sent.text.split()
            for sent in doc.sents
            for token in sent
            if token.dep_ == "relcl" and token.i < token.head.i
        ]
        # if token is the ROOT in the Past Tense and the token is sentence start
        pattern_5 = [
            sent.text.split()
            for sent in doc.sents
            for token in sent
            if token.dep_ == "ROOT"
            and "Tense=Past" in token.morph
            and token.is_sent_start
        ]

        patterns = pattern_1 + pattern_2 + pattern_3 + pattern_4 + pattern_5
        debug = [*itertools.chain(*patterns)]
        result = len(debug) / len(doc.text.split())

        return result, debug


class SY_SIMILE(Metric):
    category = Syntactic
    name_en = "Simile"
    name_local = name_en

    def count(doc):
        head_pos = ["AUX", "VERB"]
        prep_tokens = [
            sent.text.split()
            for sent in doc.sents
            for token in sent
            if token.pos_ == "ADP"
            and token.text == "like"
            and token.head.pos_ in head_pos
        ]
        # check = [[child for child in token.children if child.dep_ == "pobj" or child.dep_ == "pcomp"] for token in prep_tokens]
        as_as = [
            sent.text.split()
            for sent in doc.sents
            for token in sent
            if token.text == "as"
            and token.dep_ == "prep"
            and token.head.pos_ in ["ADJ", "NOUN"]
        ]
        tokens = prep_tokens + as_as
        debug = list(itertools.chain(*tokens))
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class SY_FRONTING(Metric):
    category = Syntactic
    name_en = "Fronting"
    name_local = name_en

    def count(doc):
        debug = []
        heads = ["nsubj", "aux", "ROOT", "nsubjpass", "auxpass"]
        tags = ["prep", "pobj", "amod", "dobj"]

        for sent in doc.sents:
            tokens = []
            for token in sent:
                if token.dep_ not in heads:
                    tokens.append(token.dep_)
                else:
                    break
            debug.append(
                sent.text.split() if any(tag in tokens for tag in tags) else []
            )

        debug = list(itertools.chain(*debug))
        result = len(debug) / len(doc.text.split())

        return result, debug


class SY_IRRITATION(Metric):
    category = Syntactic
    name_en = "Incidents of continuous tenses as irritation markers"
    name_local = name_en

    def count(doc):
        words = ["constantly", "continuously", "always", "all the time", "every time"]
        sents = []

        for sent in doc.sents:
            if any(
                token
                for token in sent
                if token._.verb_tense == "present_cont"
                or token._.verb_tense == "past_cont"
                or token._.verb_tense == "present_perfect_cont"
                or token._.verb_tense == "past_perfect_cont"
            ) and any(token for token in sent if token.text in words):
                sents.append(sent.text.split())

        debug = list(itertools.chain(*sents))
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class SY_INTENSIFIER(Metric):
    category = Syntactic
    name_en = "Intensifiers"
    name_local = name_en

    def count(doc):
        INT = ["do", "does", "did"]
        sents = []
        for sent in doc.sents:
            for token in sent:
                if (
                    token.head == token
                    and any(
                        child
                        for child in token.children
                        if child.dep_ == "aux"
                        and child.is_sent_start == False
                        and child.text in INT
                    )
                    and not any(child for child in token.subtree if child.dep_ == "neg")
                    and not any(
                        child
                        for child in sent
                        if child.is_sent_end and child.text == "?"
                    )
                ):
                    sents.append(list(itertools.chain(sent.text.split())))
        debug = list(itertools.chain(*sents))
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class SY_QUOT(Metric):
    category = Syntactic
    name_en = "Words in quotation marks"
    name_local = "Słowa w cudzysłowie"

    def count(doc):
        quote_positions = [i for i, token in enumerate(doc) if token.text in ['"', "'"]]
        if len(quote_positions) % 2 != 0:
            quote_positions.pop()
        debug = [
            token.text
            for i in range(0, len(quote_positions), 2)
            for token in doc[quote_positions[i] + 1 : quote_positions[i + 1]]
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug
