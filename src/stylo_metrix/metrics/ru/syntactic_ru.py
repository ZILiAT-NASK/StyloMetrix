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

from spacy.matcher import Matcher

from ...structures import Category, Metric
from ...utils import incidence, ratio, start_end_quote


class Syntactic(Category):
    lang = "ru"
    name_en = "Syntactic"


class SY_DIRECT_SPEECH(Metric):
    category = Syntactic
    name_en = "Number of words in direct speech"

    def count(doc):
        start, end = start_end_quote(doc)
        if (start and end) != None:
            span = doc[start:end]
            span_words = [token for token in span if token.is_alpha]
            result = incidence(doc, span_words)
            return result, {"Direct Speech": span_words}
        else:
            result = ratio(len(doc), 0)
            return result, {}


class SY_NARRATIVE(Metric):
    category = Syntactic
    name_en = "Number of words in narrative sentences"

    def count(doc):
        sents = [
            [item.text for item in sent if not item.is_punct]
            for sent in doc.sents
            if sent[-1].text == "."
        ]
        flatten = list(itertools.chain.from_iterable(sents))
        result = ratio(len(flatten), len(doc.text.split()))
        debug = {"TOKENS": flatten}
        return result, debug


class SY_NEGATIVE(Metric):
    category = Syntactic
    name_en = "Number of words in negative sentences"

    def count(doc):
        neg = [
            [item.text for item in sent if not item.is_punct]
            for sent in doc.sents
            for token in sent
            if "Polarity=Neg" in token.morph
        ]
        flatten = list(itertools.chain.from_iterable(neg))
        result = ratio(len(flatten), len(doc.text.split()))
        debug = {"TOKENS": flatten}

        return result, debug


# https://universaldependencies.org/u/dep/parataxis.html?
class SY_PARATAXIS(Metric):
    category = Syntactic
    name_en = "Number of words in parataxis sentences"

    def count(doc):
        prt = [
            [item.text for item in sent if not item.is_punct]
            for sent in doc.sents
            for token in sent
            if "parataxis" in token.dep_
        ]
        flatten = list(itertools.chain.from_iterable(prt))
        result = ratio(len(flatten), len(doc.text.split()))
        debug = {"TOKENS": flatten}

        return result, debug


class SY_NON_FINITE(Metric):
    category = Syntactic
    name_en = "Number of words in sentences that do not have any root verbs"

    def count(doc):
        sent = [
            [item.text for item in sent if not item.is_punct]
            for sent in doc.sents
            if not any(token for token in sent if token.pos_ == "VERB")
        ]
        flatten = list(itertools.chain.from_iterable(sent))
        result = ratio(len(flatten), len(doc.text.split()))
        debug = {"TOKENS": flatten}
        return result, debug


class SY_QUOTATIONS(Metric):
    category = Syntactic
    name_en = "Number of words in sentences with quotation marks"

    def count(doc):
        sent = [
            [item.text for item in sent if not item.is_punct]
            for sent in doc.sents
            for token in sent
            if token.text == '"' or token.text == "'"
        ]
        flatten = list(itertools.chain.from_iterable(sent))
        result = ratio(len(flatten), len(doc.text.split()))
        debug = {"TOKENS": flatten}

        return result, debug


class SY_EXCLAMATION(Metric):
    category = Syntactic
    name_en = "Number of words in exclamatory sentences"

    def count(doc):
        sent = [
            [item.text for item in sent if not item.is_punct]
            for sent in doc.sents
            for token in sent
            if token.text == "!"
        ]
        flatten = list(itertools.chain.from_iterable(sent))
        result = ratio(len(flatten), len(doc.text.split()))
        debug = {"TOKENS": flatten}
        return result, debug


class SY_QUESTION(Metric):
    category = Syntactic
    name_en = "Number of words in interrogative sentences"

    def count(doc):
        sentences = [
            [item.text for item in sent if not item.is_punct]
            for sent in doc.sents
            if sent[-1].text == "?"
        ]
        flatten = list(itertools.chain.from_iterable(sentences))
        result = ratio(len(flatten), len(doc.text.split()))
        debug = {"TOKENS": flatten}
        return result, debug


DISQUNCTIONS = ["правда", "да", "или"]
QUESTION_WORDS = [
    "Что",
    "Кому",
    "Как",
    "Чего",
    "Сколько",
    "Скольким",
    "Кто",
    "Кого",
    "Почему",
    "Когда",
    "Где",
    "Куда",
    "Откуда",
    "Какой",
    "Кому",
    "Какая",
    "Какое",
    "Какие",
    "Чей",
    "Чья",
    "Чьё",
    "Чьи",
    "Чему",
    "Чем",
    "Кем",
]


class SY_QUESTION_GENERAL(Metric):
    category = Syntactic
    name_en = "Number of words in general questions"

    def count(doc):
        sentences = []
        for sent in doc.sents:
            if (
                sent[-1].text == "?"
                and sent[0].pos_ == "VERB"
                and not any(
                    token
                    for token in [item.text for item in sent if not item.is_punct]
                    if token in DISQUNCTIONS or token in QUESTION_WORDS
                )
            ):
                sentences.append([item.text for item in sent if not item.is_punct])
            elif (
                sent[-1].text == "?"
                and sent[0].dep_ == "nsubj"
                and not any(
                    token
                    for token in [item.text for item in sent if not item.is_punct]
                    if token in DISQUNCTIONS or token in QUESTION_WORDS
                )
            ):
                sentences.append([item.text for item in sent if not item.is_punct])
        flatten = list(itertools.chain.from_iterable(sentences))
        result = ratio(len(flatten), len(doc.text.split()))
        debug = {"TOKENS": flatten}
        return result, debug


class SY_QUESTION_SPECIAL(Metric):
    category = Syntactic
    name_en = "Number of words in special questions"

    def count(doc):
        sentences = [
            [item.text for item in sent if not item.is_punct]
            for sent in doc.sents
            if sent[-1].text == "?"
            and any(
                token
                for token in [item.text for item in sent if not item.is_punct]
                if token in QUESTION_WORDS
            )
        ]
        flatten = list(itertools.chain.from_iterable(sentences))
        result = ratio(len(flatten), len(doc.text.split()))
        debug = {"TOKENS": flatten}
        return result, debug


class SY_QUESTION_ALTERNATIVE(Metric):
    category = Syntactic
    name_en = "Number of words in alternative questions"

    def count(doc):
        sentences = [
            [item.text for item in sent if not item.is_punct]
            for sent in doc.sents
            if sent[-1].text == "?"
            and any(token for token in sent if token.text == "или")
        ]
        flatten = list(itertools.chain.from_iterable(sentences))
        result = ratio(len(flatten), len(doc.text.split()))
        debug = {"TOKENS": flatten}
        return result, debug


class SY_QUESTION_TAG(Metric):
    category = Syntactic
    name_en = "Number of words in tag questions"

    def count(doc):
        sentences = [
            [item.text for item in sent if not item.is_punct]
            for sent in doc.sents
            if sent[-1].text == "?"
            and any(token for token in sent if token.text in DISQUNCTIONS[:-1])
        ]
        flatten = list(itertools.chain.from_iterable(sentences))
        result = ratio(len(flatten), len(doc.text.split()))
        debug = {"TOKENS": flatten}
        return result, debug


class SY_ELLIPSES(Metric):
    category = Syntactic
    name_en = "Number of words in elliptic sentences"

    def count(doc):
        sents = [
            [item.text for item in sent if not item.is_punct]
            for sent in doc.sents
            for token in sent
            if token.dep_ == "orphan"
        ]
        flatten = list(itertools.chain.from_iterable(sents))
        result = ratio(len(flatten), len(doc.text.split()))
        debug = {"TOKENS": flatten}
        return result, debug


class SY_POSITIONING(Metric):
    category = Syntactic
    name_en = "Number of positionings (прикладка)"

    def count(doc):
        tokens = []
        matcher = Matcher(doc.vocab)
        pattern = [
            {"POS": "ADJ"},
            {"MORPH": {"IS_SUBSET": ["PunctType=Dash"]}},
            {"POS": "NOUN"},
        ]
        matcher.add("positioning", [pattern])
        matches = matcher(doc)
        for match_id, start, end in matches:
            tokens.append(doc[start:end])
        result = ratio(len(tokens), len(doc.text.split()))
        debug = {"TOKENS": tokens}
        return result, debug


class SY_CONDITIONAL(Metric):
    category = Syntactic
    name_en = "Number of words in conditional sentences"

    def count(doc):
        tokens = [
            [token, token.head]
            for token in doc
            if token.dep_ == "aux" and "Mood=Cnd" in token.morph
        ]
        flatten = [token.text for i in tokens for token in i]
        result = ratio(len(flatten), len(doc.text.split()))
        debug = {"TOKENS": flatten}
        return result, debug


class SY_IMPERATIVE(Metric):
    category = Syntactic
    name_en = "Number of words in imperative sentences"

    def count(doc):
        tokens = [
            [item.text for item in sent if not item.is_punct]
            for sent in doc.sents
            for token in sent
            if "Mood=Imp" in token.morph and token.pos_ == "VERB"
        ]
        flatten = list(itertools.chain.from_iterable(tokens))
        result = ratio(len(flatten), len(doc.text.split()))
        debug = {"TOKENS": flatten}
        return result, debug


class SY_AMPLIFIED_SENT(Metric):
    category = Syntactic
    name_en = "Number of words in amplified sentences"

    def count(doc):
        tokens = [
            [item.text for item in sent if not item.is_punct]
            for sent in doc.sents
            if sent.text[-2:] == "?!"
        ]
        flatten = list(itertools.chain.from_iterable(tokens))
        result = ratio(len(flatten), len(doc.text.split()))
        debug = {"TOKENS": flatten}
        return result, debug
