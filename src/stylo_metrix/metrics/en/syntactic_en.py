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


from stylo_metrix.structures import Metric, Category

import itertools
from stylo_metrix.utils import incidence, ratio, start_end_quote


class Syntactic(Category):
    lang = 'en'
    name_en = "Syntactic"


class SY_QUESTION(Metric):
    category = Syntactic
    name_en = "Words in questions"

    def count(doc):
        sentence_tokens = [[token for token in sent if token._.is_word]
                           for sent in doc.sents if "?" in sent.text]
        result = incidence(doc, sentence_tokens)
        debug = {'TOKENS': sentence_tokens}
        return result, debug


class SY_EXCLAMATION(Metric):
    category = Syntactic
    name_en = "Words in exclamatory sentences"

    def count(doc):

        sentence_tokens = [[token for token in sent if token._.is_word] for sent in doc.sents if
                           '!' in sent.text]
        result = incidence(doc, sentence_tokens)
        debug = {'TOKENS': sentence_tokens}
        return result, debug


class SY_IMPERATIVE(Metric):
    category = Syntactic
    name_en = "Words in imperative sentences"

    def count(doc):

        sentence_tokens = [[token for token in sent if token._.is_word] for sent in doc.sents if
                           "VerbForm=Inf" in sent[0].morph and sent[0].tag_ == "VB"]
        result = incidence(doc, sentence_tokens)
        debug = {'TOKENS': sentence_tokens}
        return result, debug


class SY_SUBORD_SENT(Metric):
    category = Syntactic
    name_en = "Words in subordinate sentences"

    def count(doc):
        subord_sentences = [sent for sent in doc.sents if any(token.pos_ == "SCONJ" or token.tag_ == "WDT" for token in sent)]
        join_sents = [*itertools.chain(*subord_sentences)]
        result = incidence(doc, join_sents)
        debug = {'TOKENS': join_sents}
        return result, debug


class SY_SUBORD_SENT_PUNCT(Metric):
    category = Syntactic
    name_en = "Punctuation in subordinate sentences"

    def count(doc):
        sub_sent_punct = [sent for sent in doc.sents if any(token.pos_ == "SCONJ" for token in sent)]
        join_sents = itertools.chain(*sub_sent_punct)
        sent_tok = [tkn for tkn in join_sents if tkn.pos_ in "PUNCT"]
        result = incidence(doc, sent_tok)
        debug = {'TOKENS': sent_tok}
        return result, debug


class SY_COORD_SENT(Metric):
    category = Syntactic
    name_en = "Words in coordinate sentences"

    def count(doc):
        coord_sentences = [sent for sent in doc.sents if any("ConjType=Cmp" in token.morph for token in sent)]
        join_sents = [*itertools.chain(*coord_sentences)]
        result = incidence(doc, join_sents)
        debug = {'TOKENS': join_sents}
        return result, debug


class SY_COORD_SENT_PUNCT(Metric):
    category = Syntactic
    name_en = "Punctuation in coordinate sentences"

    def count(doc):
        coord_sent_punct = [sent for sent in doc.sents if any(token.pos_ == "CCONJ" for token in sent)]
        join_sents = itertools.chain(*coord_sent_punct)
        sent_tok = [tkn for tkn in join_sents if tkn.pos_ in "PUNCT"]
        result = incidence(doc, sent_tok)
        debug = {'TOKENS': sent_tok}
        return result, debug


class SY_SIMPLE_SENT(Metric):
    category = Syntactic
    name_en = "Tokens in simple sentences"

    def count(doc):
        simple_sent = [sent for sent in doc.sents if
                       any("ConjType=Cmp" not in token.morph or token.pos_ != "SCONJ" for token in sent)]
        join_sent = [*itertools.chain(*simple_sent)]
        result = incidence(doc, join_sent)
        debug = {'TOKENS': join_sent}
        return result, debug


class SY_DIRECT_SPEECH(Metric):
    category = Syntactic
    name_en = "Words in direct speech"

    def count(doc):
        start, end = start_end_quote(doc)
        if (start and end) != None:
            span = doc[start:end]
            span_words = [token for token in span]
            result = incidence(doc, span_words)
            debug = {'TOKENS': span_words}
            return result, debug
        else:
            result = ratio(len(doc), 0)
            return result, {}


class SY_INVERSE_PATTERNS(Metric):
    category = Syntactic
    name_en = "Incidents of inverse patterns"

    def count(doc):

        # if token is npadvmod and goes before the ROOT verb
        pattern_1 = [token for sent in doc.sents for token in sent if token.dep_ == "npadvmod" and token.i < token.head.i]
        # if token is dep and goes before the ROOT verb
        pattern_2 = [token for sent in doc.sents for token in sent if token.dep_ == "dep" and token.i < token.head.i]
        # if token is dobj and goes before the ROOT verb
        pattern_3 = [token for sent in doc.sents for token in sent if token.dep_ == "dobj" and token.i < token.head.i]
        # if token determines a relative clause and goes before the ROOT
        pattern_4 = [token for sent in doc.sents for token in sent if token.dep_ == "relcl" and token.i < token.head.i]
        # if token is the ROOT in the Past Tense and the token is sentence start
        pattern_5 = [token for sent in doc.sents for token in sent if token.dep_ == "ROOT" and "Tense=Past" in token.morph and token.is_sent_start]

        patterns = pattern_1 + pattern_2 + pattern_3 + pattern_4 + pattern_5
        result = incidence(doc, patterns)
        debug = {'TOKENS': patterns}
        return result, debug


class SY_SPECIAL_QUESTIONS(Metric):
    category = Syntactic
    name_en = "Incidents of special questions"

    def count(doc):
        sentence_tokens = [[token for token in sent if token._.syntax == "special_question"] for sent in doc.sents]
        search = list(itertools.chain(*sentence_tokens))
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class SY_GENERAL_QUESTIONS(Metric):
    category = Syntactic
    name_en = "Incidents of general questions"

    def count(doc):
        sentence_tokens = [[token for token in sent if token._.syntax == "general_question"] for sent in doc.sents]
        search = list(itertools.chain(*sentence_tokens))
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class SY_NEGATIVE_QUESTIONS(Metric):
    category = Syntactic
    name_en = "Incidents of negative questions"

    def count(doc):
        sentence_tokens = [[token for token in sent if token._.syntax == "negative_question"] for sent in doc.sents]
        search = list(itertools.chain(*sentence_tokens))
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class SY_TAG_QUESTIONS(Metric):
    category = Syntactic
    name_en = "Incidents of negative questions"

    def count(doc):
        sentence_tokens = [[token for token in sent if token._.syntax == "tag_question"] for sent in doc.sents]
        search = list(itertools.chain(*sentence_tokens))
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug