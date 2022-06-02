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


class Lexical(Metric, ABC):
    category_en = "Lexical"


class L_TTR_LA(Lexical):
    name_en = "Type-token ratio for words lemmas"

    def count(self, doc):
        types = set(token.lemma_ for token in doc._.words)
        result = incidence(doc, types)
        return result, {}


class L_NAME(Lexical):
    name_en = "Incidence of proper names (all words)"

    def count(self, doc):
        ents = [token for token in doc if token.pos_ == "PROPN"]
        result = incidence(doc, ents)
        return result, {}


class L_PERSN(Lexical):
    name_en = "Incidence of personal names (all words)"

    def count(self, doc):
        ents = [list(ent) for ent in doc.ents if ent.label_ == 'PERSON']
        sum_ents = sum(ents, [])
        result = incidence(doc, sum_ents)
        return result, {}


class L_CONT_A(Lexical):
    name_en = "Content words incidence"

    def count(self, doc):
        search = [token.text for token in doc._.words if token._.is_content_word]
        result = incidence(doc, search)
        return result, {"CW": search}


class L_FUNC_A(Lexical):
    name_en = "Function words incidence"

    def count(self, doc):
        search = [token.text for token in doc._.words if token._.is_function_word]
        result = incidence(doc, search)
        return result, {"CW": search}


class L_CONT_T(Lexical):
    name_en = "Content words types incidence"

    def count(self, doc):
        search = set(token.text for token in doc._.words if token._.is_content_word)
        result = incidence(doc, search)
        return result, {}


class L_FUNC_T(Lexical):
    name_en = "Function words types incidence"

    def count(self, doc):
        search = set(token.text for token in doc._.words if token._.is_function_word)
        result = incidence(doc, search)
        return result, {}


class L_SYL_G2(Lexical):
    name_en = "Words formed of more than 2 syllables incidence"

    def count(self, doc):
        lengths = [token._.syllables_count for token in doc if token._.syllables_count is not None]
        selected = [length for length in lengths if length > 2]
        result = incidence(doc, selected)
        return result, {}


LEXICAL = [
    L_TTR_LA,
    L_NAME,
    L_PERSN,
    L_CONT_A,
    L_FUNC_A,
    L_CONT_T,
    L_FUNC_T,
    L_SYL_G2,
]

lexical_group = MetricsGroup([m() for m in LEXICAL])
