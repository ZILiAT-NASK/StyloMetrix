# Copyright (C) 2023  NASK PIB
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

from stylo_metrix.utils import sent_incidence
import itertools

"""
The algorithm of counting the distance between phrases is the following:
1. Separate the needed phrases in the sentence.
2. Take the tokes of the sentence without the phrases.
3. Count the number of tokens / length of the sentence.
4. Repeat the steps for all sentences in the document.
5. Sum the results and divide by the total number of sentences.
"""

class Distance(Category):
    lang = 'en'
    name_en = "Phrases Distance"

class SENT_D_VP(Metric):
    category = Distance
    name_en = "Distance between VPs"

    def count(doc):
        stat = []

        # Distance VPs in the sentence
        for sent in doc.sents:
            tokens = [token.text for token in sent if not token._.verb_tense]
            incidence = len(tokens) / len(sent)
            if len([*doc.sents]) == 1:
                return incidence, tokens
            else:
                stat.append(incidence)
                continue

        # distance of VPs in the doc
        result = sent_incidence(doc, stat)
        debug = {'TOKENS': tokens}
        return result, debug


class SENT_D_NP(Metric):
    category = Distance
    name_en = "Distance between NPs"

    def count(doc):
        stat = []

        # Distance NPs in the sentence
        for sent in doc.sents:
            NPs = [*map(lambda x: x.text.split(), [*sent.noun_chunks])]
            n = list(itertools.chain(*NPs))
            tokens = [token.text for token in sent if token.text not in n]
            incidence = len(tokens) / len(sent)
            if len([*doc.sents]) == 1:
                return incidence, tokens
            else:
                stat.append(incidence)
                continue

        # Distance of NPs in the doc
        result = sent_incidence(doc, stat)
        debug = {'TOKENS': tokens}
        return result, debug


class SENT_D_PP(Metric):
    category = Distance
    name_en = "Distance between PPs"

    def count(doc):
        stat = []

        # Distance PPs in the sentence
        for sent in doc.sents:
            PPs = [[*map(lambda x: x.text, [*token.subtree])] for token in sent if token.dep_ == 'prep']
            p = set(itertools.chain(*PPs))
            tokens = [token.text for token in sent if token.text not in p]
            incidence = len(tokens) / len(sent)
            if len([*doc.sents]) == 1:
                return incidence, tokens
            else:
                stat.append(incidence)
                continue

        # Distance of PPs in the doc
        result = sent_incidence(doc, stat)
        debug = {'TOKENS': tokens}
        return result, debug


class SENT_D_ADJP(Metric):
    category = Distance
    name_en = "Distance between ADJPs"

    def count(doc):
        stat = []

        # Distance ADJPs in the sentence
        for sent in doc.sents:
            ADJPs = [[*map(lambda x: x.text, [*token.children])] for token in sent if token._.adjectives]
            a = list(itertools.chain(*ADJPs))
            tokens = [token.text for token in sent if token.text not in a]
            incidence = len(tokens) / len(sent)
            if len([*doc.sents]) == 1:
                return incidence, tokens
            else:
                stat.append(incidence)
                continue

        # Distance of ADJPs in the doc
        result = sent_incidence(doc, stat)
        debug = {'TOKENS': tokens}
        return result, debug


class SENT_D_ADVP(Metric):
    category = Distance
    name_en = "Distance between ADVPs"

    def count(doc):
        stat = []

        # Distance ADVPs in the sentence
        for sent in doc.sents:
            ADVPs = [[token.text, *map(lambda x: x.text, [*token.children])] for token in sent if token._.adverbs]
            a = list(itertools.chain(*ADVPs))
            tokens = [token.text for token in sent if token.text not in a]
            incidence = len(tokens) / len(sent)
            if len([*doc.sents]) == 1:
                return incidence, tokens
            else:
                stat.append(incidence)
                continue

        # Distance of ADVPs in the doc
        result = sent_incidence(doc, stat)
        debug = {'TOKENS': tokens}
        return result, debug

