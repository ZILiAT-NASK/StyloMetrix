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
    lang = "ukr"
    name_en = "Syntactic"
    name_local = name_en


class SY_NARRATIVE(Metric):
    category = Syntactic
    name_en = "Number of words in narrative sentences"
    name_local = name_en

    def count(doc):
        sents = [sent.text.split() for sent in doc.sents if sent[-1].text == "."]
        debug = list(itertools.chain.from_iterable(sents))
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class SY_NEGATIVE(Metric):
    category = Syntactic
    name_en = "Number of words in negative sentences"
    name_local = name_en

    def count(doc):
        neg = [
            sent.text.split()
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
            [item.text for item in token.sent if not item.is_punct]
            for token in doc
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
            sent.text.split()
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
            sent.text.split()
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


class SY_ELLIPSES(Metric):
    category = Syntactic
    name_en = "Number of words in elliptic sentences"
    name_local = name_en

    def count(doc):
        sents = [
            sent.text.split()
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
            debug.append(doc[start:end].text)
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


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
            sent.text.split()
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
        tokens = [sent.text.split() for sent in doc.sents if sent.text[-2:] == "?!"]
        debug = list(itertools.chain.from_iterable(tokens))
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class SY_NOUN_PHRASES(Metric):
    category = Syntactic
    name_en = "Number of noun phrases"
    name_local = name_en

    def count(doc):
        tags_ = ["NOUN", "PROPN"]
        dep = ["nmod", "amod", "discourse", "case"]
        noun_phrases = []

        for sent in doc.sents:
            # noun phrases without any modifiers
            subjects = [
                noun_phrases.append([[token.text]])
                for token in sent
                if token.dep_ in ["nsubj", "nsubjpass"] and len([*token.children]) == 0
            ]
            # noun phrases with modifiers
            chunks = []
            for token in sent:
                if token.pos_ in tags_ and len([*token.children]) > 0:
                    ph = []
                    for child in token.children:
                        if child.dep_ in dep and child.head.text not in ph:
                            ph.append(child.head.text)
                            ph.append(child.text)
                        elif child.dep_ in dep and child.head.text in ph:
                            ph.append(child.text)

                    chunks.append(ph)
            noun_phrases.append(chunks)
        debug_np = list(itertools.chain(*noun_phrases))
        debug = [item for sublist in debug_np for item in sublist]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug
