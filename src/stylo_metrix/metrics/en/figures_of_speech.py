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

class FiguresOfSpeech(Category):
    lang = "en"
    name_en = "Figures of speech"


class FOS_SIMILE(Metric):
    category = FiguresOfSpeech
    name_en = "Simile"

    def count(doc):
        tokens = [[sent for token in sent if token._.stylistic == "simile"] for sent in doc.sents]
        search = list(itertools.chain(*tokens))
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class FOS_FRONTING(Metric):
    category = FiguresOfSpeech
    name_en = "Fronting"

    def count(doc):

        search = []
        heads = ["nsubj", "aux", "ROOT", "nsubjpass", "auxpass"]
        tags = ["prep", "pobj", "amod", "dobj"]

        for sent in doc.sents:
            tokens = []
            for token in sent:
                if token.dep_ not in heads:
                    tokens.append(token.dep_)
                else:
                    break
            search.append(sent if any(tag in tokens for tag in tags) else [])
        result = list(itertools.chain(*search))
        result = incidence(doc, tokens)
        debug = {'TOKENS': search}
        return result, debug