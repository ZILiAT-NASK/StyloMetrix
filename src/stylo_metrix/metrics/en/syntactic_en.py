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
from stylo_metrix.utils import incidence


class Syntactic(Metric, ABC):
    category_en = "Syntactic"

class SY_S_Q(Syntactic):
    name_en = "Words in questions incidence"

    def count(self, doc):
        sentence_tokens = [[token for token in sent if '?' in sent.text] for sent in doc.sents]
        words = sum([[token for token in sent if token._.is_word] for sent in sentence_tokens], [])
        result = incidence(doc, words)
        return result, {"QS":sentence_tokens}

class SY_S_EX(Syntactic):
    name_en = "Words in exclamatory sentences incidence"

    def count(self, doc):
        sentence_tokens = [[token for token in sent if '!' in sent.text] for sent in doc.sents]
        words = sum([[token for token in sent if token._.is_word] for sent in sentence_tokens], [])
        result = incidence(doc, words)
        return result, {}

class SY_S_IMP(Syntactic):
    name_en = "Words in imperative sentences incidence"

    def count(self, doc):
        sentence_tokens = [[token for token in sent] for sent in doc.sents if "VerbForm=Inf" in sent[0].morph and sent[0].pos_ == "VERB"]
        words = sum([[token for token in sent if token._.is_word] for sent in sentence_tokens], [])
        result = incidence(doc, words)
        return result, {}


class SUBORD_SENT(Syntactic):
    name_en = "Words in subordinate sentences"

    def count(self, doc):
        sentence_tokens = []
        for sent in doc.sents:
            for token in sent:
                if token.pos_ == "SCONJ":
                    for tkn in sent:
                        if tkn.pos_ != "PUNCT":
                            sentence_tokens.append(tkn)

        result = incidence(doc, sentence_tokens)
        return result, {}


class SUBORD_SENT_PUNCT(Syntactic):
    name_en = "Punctuation in subordinate sentences per all words"

    def count(self, doc):
        sentence_tokens = []
        for sent in doc.sents:
            for token in sent:
                if token.pos_ == "SCONJ":
                    for tkn in sent:
                        if tkn.pos_ in "PUNCT":
                            sentence_tokens.append(tkn)

        result = incidence(doc, sentence_tokens)
        return result, {}


class COORD_SENT(Syntactic):
    name_en = "Words in coordinate sentences per all words"

    def count(self, doc):
        sentence_tokens = []
        for sent in doc.sents:
            for token in sent:
                if token.pos_ == "CCONJ":
                    for tkn in sent:
                        if tkn.pos_ != "PUNCT":
                            sentence_tokens.append(tkn)

        result = incidence(doc, sentence_tokens)
        return result, {}


class COORD_SENT_PUNCT(Syntactic):
    name_en = "Punctuation in coordinate sentences per all words"

    def count(self, doc):
        sentence_tokens = []
        for sent in doc.sents:
            for token in sent:
                if token.pos_ == "CCONJ":
                    for tkn in sent:
                        if tkn.pos_ in "PUNCT":
                            sentence_tokens.append(tkn)

        result = incidence(doc, sentence_tokens)
        return result, {}


class SIMPLE_SENTENCE(Syntactic):
    name_en = "Tokens in simple sentences per all words"

    def count(self, doc):
        sentence_tokens = [[sent for token in sent if token.pos_ == "SCONJ" or token.pos_ == "CCONJ"] for sent in doc.sents]
        flattened = [val for sublist in sentence_tokens for val in sublist]
        simple_sent = [[token for token in sent if token.pos_ != "PUNCT"] for sent in doc.sents if sent not in flattened]
        flattened_simple = [val for sublist in simple_sent for val in sublist]

        result = incidence(doc, flattened_simple)
        return result, {}


SYNTACTIC = [
    SY_S_Q,
    SY_S_EX,
    SY_S_IMP,
    SUBORD_SENT,
    SUBORD_SENT_PUNCT,
    COORD_SENT,
    COORD_SENT_PUNCT,
    SIMPLE_SENTENCE,
]

syntactic_group = MetricsGroup([m() for m in SYNTACTIC])
