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
from stylo_metrix.utils import incidence
import itertools


class PSYCHOLINGUISTICS(Category):
    lang = "en"
    name_en = "Psycholinguistics"

class PS_CONTRADICTION(Metric):
    category = PSYCHOLINGUISTICS
    name_en = "Opposition, limitation, contradiction"

    def count(doc):
        search = [token.text for token in doc if token._.linking_words == "contradiction"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug

class PS_AGREEMENT(Metric):
    category = PSYCHOLINGUISTICS
    name_en = "Agreement, similarity"

    def count(doc):
        search = [token.text for token in doc if token._.linking_words == "agreement"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug

class PS_EXAMPLES(Metric):
    category = PSYCHOLINGUISTICS
    name_en = "Examples, emphasis"

    def count(doc):
        search = [token.text for token in doc if token._.linking_words == "examples"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug

class PS_CONSEQUENCE(Metric):
    category = PSYCHOLINGUISTICS
    name_en = "Consequence, result"

    def count(doc):
        search = [token.text for token in doc if token._.linking_words == "consequence"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug

class PS_CAUSE(Metric):
    category = PSYCHOLINGUISTICS
    name_en = "Cause, purpose"

    def count(doc):
        search = [token.text for token in doc if token._.linking_words == "cause"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug

class PS_LOCATION(Metric):
    category = PSYCHOLINGUISTICS
    name_en = "Location, space"

    def count(doc):
        search = [token.text for token in doc if token._.linking_words == "space"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug
    
class PS_TIME(Metric):
    category = PSYCHOLINGUISTICS
    name_en = "Time"

    def count(doc):
        search = [token.text for token in doc if token._.linking_words == "time"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug

class PS_CONDITION(Metric):
    category = PSYCHOLINGUISTICS
    name_en = "Condition, hypothesis"

    def count(doc):
        search = [token.text for token in doc if token._.linking_words == "condition"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug

class PS_MANNER(Metric):
    category = PSYCHOLINGUISTICS
    name_en = "Manner"

    def count(doc):
        search = [token.text for token in doc if token._.linking_words == "manner"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class PS_SYNTACTIC_IRRITATION(Metric):
    category = PSYCHOLINGUISTICS
    name_en = "Incidents of continuous tenses as irritation markers"

    def count(doc):
        words = ["constantly", "continuously", "always", "all the time", "every time"]
        sents = []
        search = [sents.append(sent.text) for sent in doc.sents if any(token for token in sent if token._.verb_tense == "present_cont" or token._.verb_tense == "past_cont" or token._.verb_tense == "present_perfect_cont" or token._.verb_tense == "past_perfect_cont")
                  and any(token for token in sent if token.text in words)]
        result = incidence(doc, sents)
        debug = {'TOKENS': sents}
        return result, debug