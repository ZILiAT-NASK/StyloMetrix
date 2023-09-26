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


from spacy.matcher import Matcher
from ...structures import Category, Metric
from ...utils import incidence, ratio, start_end_quote
import itertools

class Syntactic(Category):
    lang = 'ru'
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
        sents = [sent.text.split() for sent in doc.sents if sent[-1].text == "."]
        flatten = list(itertools.chain.from_iterable(sents))
        result = incidence(doc, flatten)
        return result, {}


class SY_NEGATIVE(Metric):
    category = Syntactic
    name_en = "Number of words in negative sentences"

    def count(doc):
        neg = [sent.text.split() for sent in doc.sents for token in sent if "Polarity=Neg" in token.morph]
        flatten = list(itertools.chain.from_iterable(neg))
        result = incidence(doc, flatten)
        return result, {}


# https://universaldependencies.org/u/dep/parataxis.html?
class SY_PARATAXIS(Metric):
    category = Syntactic
    name_en = "Number of words in parataxis sentences"

    def count(doc):
        prt = [sent.text.split() for sent in doc.sents for token in sent if "parataxis" in token.dep_]
        flatten = list(itertools.chain.from_iterable(prt))
        result = incidence(doc, flatten)
        return result, {}

class SY_NON_FINITE(Metric):
    category = Syntactic
    name_en = "Number of words in sentences without any verbs"

    def count(doc):
        sent = [sent.text.split() for sent in doc.sents if not any(token for token in sent if token.pos_ == "VERB")]
        flatten = list(itertools.chain.from_iterable(sent))
        result = incidence(doc, sent)
        return result, {}


class SY_QUOTATIONS(Metric):
    category = Syntactic
    name_en = "Number of words in sentences with quotation marks"

    def count(doc):
        sent = [sent.text.split() for sent in doc.sents for token in sent if token.text == '"' or token.text == "'"]
        flatten = list(itertools.chain.from_iterable(sent))
        result = incidence(doc, flatten)
        return result, {}


class SY_EXCLAMATION(Metric):
    category = Syntactic
    name_en = "Number of words in exclamatory sentences"

    def count(doc):
        sent = [sent.text.split() for sent in doc.sents for token in sent if token.text == "!"]
        flatten = list(itertools.chain.from_iterable(sent))
        result = incidence(doc, flatten)
        return result, {}  


class SY_QUESTION(Metric):
    category = Syntactic
    name_en = "Number of words in interrogative sentences"

    def count(doc):
        sentences = [sent.text.split() for sent in doc.sents if sent[-1].text == '?']
        flatten = list(itertools.chain.from_iterable(sentences))
        result = incidence(doc, flatten)
        return result, {}

class SY_ELLIPSES(Metric):
    category = Syntactic
    name_en = "Number of words in elliptic sentences"

    def count(doc):
        sents = [sent.text.split() for sent in doc.sents for token in sent if token.dep_ == "orphan"]
        flatten = list(itertools.chain.from_iterable(sents))
        result = incidence(doc, flatten)
        return result, {}


class SY_CONDITIONAL(Metric):
    category = Syntactic
    name_en = "Number of words in conditional sentences"

    def count(doc):
        tokens = [[token, token.head] for token in doc if token.dep_ == "aux" and "Mood=Cnd" in token.morph]
        flatten = [token for i in tokens for token in i]
        result = incidence(doc, flatten)
        return result, {}


class SY_IMPERATIVE(Metric):
    category = Syntactic
    name_en = "Number of words in imperative sentences"

    def count(doc):
        tokens = [sent.text.split() for sent in doc.sents for token in sent if "Mood=Imp" in token.morph and token.pos_ == "VERB"]
        flatten = list(itertools.chain.from_iterable(tokens))
        result = incidence(doc, flatten)
        return result, {}


class SY_AMPLIFIED_SENT(Metric):
    category = Syntactic
    name_en = "Number of words in amplified sentences"

    def count(doc):
        tokens = [sent.text.split() for sent in doc.sents if sent.text[-2:] == "?!"]
        flatten = list(itertools.chain.from_iterable(tokens))
        result = incidence(doc, flatten)
        return result, {}
