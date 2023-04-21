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
from collections import Counter, defaultdict
from stylo_metrix.utils import sent_incidence, incidence

class Statistics(Category):
    lang = 'en'
    name_en = "General Statistics"

class SENT_ST_WRDSPERSENT(Metric):
    category = Statistics
    name_en = "Difference between the number of words and the number of sentences"

    def count(doc):
        stat = len([*doc]) - len([*doc.sents])
        result = stat / len([*doc])
        debug = {'TOKENS': [*doc]}
        return result, debug


"""
The algorithme of counting statistical metrics is the following:
1. Take the dependency tegs in every sentence 
2. Save them in separate sents
3. Compare each subsequent set to the previous one
4. Calculate the needed statictical feature between two sets and save it in the list
5. Sum up the values in the list and divide by the number of sentences in the doc
"""


class SENT_ST_DIFFERENCE(Metric):
    category = Statistics
    name_en = "Symmetric difference between nodes in sentences per doc"

    def count(doc):

        sets = [set([token.dep_ for token in sent]) for sent in doc.sents]
        stat = []
        if len(sets) > 1:
            for i in range(0, len(sets)-1, 1):
                difference = sets[i].symmetric_difference(sets[i+1])
                diffs = len(difference) / (len(sets[i])+len(sets[i+1]))
                stat.append(diffs)
            result = sent_incidence(doc, stat)
            debug = {'TOKENS': difference}
            return result, debug
        else:
            result = 0.0
            return result, {}

    

class SENT_ST_SYMMETRY(Metric):
    category = Statistics
    name_en = "Similarity between nodes in sentences per doc"

    def count(doc):

        sets = [set([token.dep_ for token in sent]) for sent in doc.sents]
        stat = []
        if len(sets) > 1:
            for i in range(0, len(sets)-1, 1):
                similarity = sets[i].intersection(sets[i+1])
                sim = len(similarity) / (len(sets[i])+len(sets[i+1]))
                stat.append(sim)
            result = sent_incidence(doc, stat)
            debug = {'TOKENS': similarity}
            return result, debug
        else:
            result = 0.0
            return result, {}
        

class ST_REPETITIONS_WORDS(Metric):
    category = Statistics
    name_en = "Repetitions of words in text"

    def count(doc):
        doc_list = [token.text for token in doc if token._.is_content_word]
        bow = Counter(doc_list)
        repetitions = [value for _, value in bow.items() if value > 1]
        result = sum(repetitions) / doc._.n_tokens
        debug = [key for key, value in bow.items() if value > 1]

        return result, debug


class ST_REPETITIONS_SENT(Metric):
    category = Statistics
    name_en = "Repetitions of sentences in text"

    def count(doc):
        dict_sent = defaultdict(list)
        SENT_SET = set([*doc.sents])

        if len(SENT_SET) > 1:
            count = 1
            for sent in doc.sents:
                if sent in dict_sent.keys():
                    count += 1
                    dict_sent[sent] = count
                else:
                    dict_sent[sent] = count
        words = [value for _, value in dict_sent.items() if value > 1]
        result = incidence(doc, words)
        debug = [key for key, value in dict_sent.items() if value > 1]
        return result, debug