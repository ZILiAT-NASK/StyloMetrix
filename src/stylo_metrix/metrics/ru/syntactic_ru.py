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
from ...utils import ratio


class Syntactic(Category):
    lang = "ru"
    name_en = "Syntactic"
    name_local = name_en


class SY_NARRATIVE(Metric):
    category = Syntactic
    name_en = "Number of words in narrative sentences"
    name_local = name_en

    def count(doc):
        sents = [
            [item.text for item in sent if not item.is_punct]
            for sent in doc.sents
            if sent[-1].text == "."
        ]
        debug = list(itertools.chain.from_iterable(sents))
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class SY_NEGATIVE(Metric):
    category = Syntactic
    name_en = "Number of words in negative sentences"
    name_local = name_en

    def count(doc):
        neg = [
            [item.text for item in sent if not item.is_punct]
            for sent in doc.sents
            for token in sent
            if "Polarity=Neg" in token.morph
        ]
        debug = list(itertools.chain.from_iterable(neg))
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


# https://universaldependencies.org/u/dep/parataxis.html?
class SY_PARATAXIS(Metric):
    category = Syntactic
    name_en = "Number of words in parataxis sentences"
    name_local = name_en

    def count(doc):
        prt = [
            [item.text for item in sent if not item.is_punct]
            for sent in doc.sents
            for token in sent
            if "parataxis" in token.dep_
        ]
        debug = list(itertools.chain.from_iterable(prt))
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class SY_NON_FINITE(Metric):
    category = Syntactic
    name_en = "Number of words in sentences that do not have any root verbs"
    name_local = name_en

    def count(doc):
        sent = [
            [item.text for item in sent if not item.is_punct]
            for sent in doc.sents
            if not any(token for token in sent if token.pos_ == "VERB")
        ]
        debug = list(itertools.chain.from_iterable(sent))
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class SY_QUOTATIONS(Metric):
    category = Syntactic
    name_en = "Words in sentences with quotation marks"
    name_local = name_en

    def count(doc):
        sent = [
            [item.text for item in sent if not item.is_punct]
            for sent in doc.sents
            for token in sent
            if token.text == '"' or token.text == "'"
        ]
        debug = list(itertools.chain.from_iterable(sent))
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class SY_EXCLAMATION(Metric):
    category = Syntactic
    name_en = "Number of words in exclamatory sentences"
    name_local = name_en

    def count(doc):
        sent = [
            [item.text for item in sent if not item.is_punct]
            for sent in doc.sents
            for token in sent
            if token.text == "!"
        ]
        debug = list(itertools.chain.from_iterable(sent))
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class SY_QUESTION(Metric):
    category = Syntactic
    name_en = "Number of words in interrogative sentences"
    name_local = name_en

    def count(doc):
        sentences = [
            [item.text for item in sent if not item.is_punct]
            for sent in doc.sents
            if sent[-1].text == "?"
        ]
        debug = list(itertools.chain.from_iterable(sentences))
        result = ratio(len(debug), len(doc.text.split()))

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
    name_local = name_en

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
        debug = list(itertools.chain.from_iterable(sentences))
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class SY_QUESTION_SPECIAL(Metric):
    category = Syntactic
    name_en = "Number of words in special questions"
    name_local = name_en

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
        debug = list(itertools.chain.from_iterable(sentences))
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class SY_QUESTION_ALTERNATIVE(Metric):
    category = Syntactic
    name_en = "Number of words in alternative questions"
    name_local = name_en

    def count(doc):
        sentences = [
            [item.text for item in sent if not item.is_punct]
            for sent in doc.sents
            if sent[-1].text == "?"
            and any(token for token in sent if token.text == "или")
        ]
        debug = list(itertools.chain.from_iterable(sentences))
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class SY_QUESTION_TAG(Metric):
    category = Syntactic
    name_en = "Number of words in tag questions"
    name_local = name_en

    def count(doc):
        sentences = [
            [item.text for item in sent if not item.is_punct]
            for sent in doc.sents
            if sent[-1].text == "?"
            and any(token for token in sent if token.text in DISQUNCTIONS[:-1])
        ]
        debug = list(itertools.chain.from_iterable(sentences))
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class SY_ELLIPSES(Metric):
    category = Syntactic
    name_en = "Number of words in elliptic sentences"
    name_local = name_en

    def count(doc):
        sents = [
            [item.text for item in sent if not item.is_punct]
            for sent in doc.sents
            for token in sent
            if token.dep_ == "orphan"
        ]
        debug = list(itertools.chain.from_iterable(sents))
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class SY_POSITIONING(Metric):
    category = Syntactic
    name_en = "Number of positionings (прикладка)"
    name_local = name_en

    def count(doc):
        debug = []
        matcher = Matcher(doc.vocab)
        pattern = [
            {"POS": "ADJ"},
            {"MORPH": {"IS_SUBSET": ["PunctType=Dash"]}},
            {"POS": "NOUN"},
        ]
        matcher.add("positioning", [pattern])
        matches = matcher(doc)
        for match_id, start, end in matches:
            debug.append(doc[start:end])
        result = ratio(len(debug), len(doc.text.split()))

        return result, [item.text for item in debug]


class SY_CONDITIONAL(Metric):
    category = Syntactic
    name_en = "Number of words in conditional sentences"
    name_local = name_en

    def count(doc):
        tokens = [
            [token, token.head]
            for token in doc
            if token.dep_ == "aux" and "Mood=Cnd" in token.morph
        ]
        debug = [token.text for i in tokens for token in i]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class SY_IMPERATIVE(Metric):
    category = Syntactic
    name_en = "Number of words in imperative sentences"
    name_local = name_en

    def count(doc):
        tokens = [
            [item.text for item in sent if not item.is_punct]
            for sent in doc.sents
            for token in sent
            if "Mood=Imp" in token.morph and token.pos_ == "VERB"
        ]
        debug = list(itertools.chain.from_iterable(tokens))
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class SY_AMPLIFIED_SENT(Metric):
    category = Syntactic
    name_en = "Number of words in amplified sentences"
    name_local = name_en

    def count(doc):
        tokens = [
            [item.text for item in sent if not item.is_punct]
            for sent in doc.sents
            if sent.text[-2:] == "?!"
        ]
        debug = list(itertools.chain.from_iterable(tokens))
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug
