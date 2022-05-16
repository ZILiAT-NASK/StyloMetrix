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
from collections import Counter

from stylo_metrix.structures import Metric, MetricsGroup
from stylo_metrix.utils import incidence, ratio


class Lexical(Metric, ABC):
    category_pl = "Lexical"
    category_en = "Leksykalne"


class L_TTR_LA(Lexical):
    name_en = "Type-token ratio for words lemmas"
    name_pl = "Type-token ratio dla lemm wyrazów"

    def count(self, doc):
        types = set(token.lemma_ for token in doc._.words)
        result = incidence(doc, types)
        return result, {}


class L_TTR_IA(Lexical):
    name_en = "Type-token ratio for inflected words"
    name_pl = "Type-token ratio dla wyrazów w odmianach"

    def count(self, doc):
        types = set(token.norm_ for token in doc._.words)
        result = incidence(doc, types)
        return result, {}


class L_CONT_A(Lexical):
    name_en = "Content words incidence"
    name_pl = "Występowanie wyrazów samodzielnych"

    def count(self, doc):
        search = [token.text for token in doc._.words if token._.content_word == "cont"]
        result = incidence(doc, search)
        return result, {}


class L_NCONT_A(Lexical):
    name_en = "Non-content words incidence"
    name_pl = "Występowanie wyrazów niesamodzielnych"

    def count(self, doc):
        search = [token.text for token in doc._.words if token._.content_word == "noncont"]
        result = incidence(doc, search)
        return result, {'search': search}


class L_CONT_T(Lexical):
    name_en = "Content words types incidence"
    name_pl = "Występowanie typów wyrazów samodzielnych"

    def count(self, doc):
        search = set(token.text for token in doc._.words if token._.content_word == "cont")
        result = incidence(doc, search)
        return result, {}


class L_NCONT_T(Lexical):
    name_en = "Non-content words types incidence"
    name_pl = "Występowanie typów wyrazów niesamodzielnych"

    def count(self, doc):
        search = set(token.text for token in doc._.words if token._.content_word == "noncont")
        result = incidence(doc, search)
        return result, {}


class L_CONT_L(Lexical):
    name_en = "Lemmas of content words incidence"
    name_pl = "Występowanie lemm wyrazów samodzielnych"

    def count(self, doc):
        search = set(token.lemma_ for token in doc._.words if token._.content_word == "cont")
        result = incidence(doc, search)
        return result, {}


class L_NAME(Lexical):
    name_en = "Incidence of proper names (all words)"
    name_pl = "Występowanie nazw własnych (wszystkie wyrazy)"

    def count(self, doc):
        ents = [list(ent) for ent in doc.ents]
        sum_ents = sum(ents, [])
        result = incidence(doc, sum_ents)
        return result, {}


class L_PERSN(Lexical):
    name_en = "Incidence of personal names (all words)"
    name_pl = "Występowanie nazw osób (wszystkie wyrazy)"

    def count(self, doc):
        ents = [list(ent) for ent in doc.ents if ent.label_ == 'persName']
        sum_ents = sum(ents, [])
        result = incidence(doc, sum_ents)
        return result, {}


class L_TCCT1(Lexical):
    name_en = "Percentage of tokens covering 1% of most common types"
    name_pl = "Występowanie wyrazów wchodzących w skład 1% najczęstszych typów (min. 1 typ)"

    def count(self, doc):
        counter = Counter([token.lemma_ for token in doc])
        ile_typow = len(counter)
        proc_typow = round(ile_typow * 0.01)
        if proc_typow == 0:
            proc_typow = 1
        suma_wystapien = sum([n for word, n in counter.most_common(proc_typow)])
        result = ratio(suma_wystapien, doc._.n_tokens)
        return result, {
            "[MOST COMMON TYPES]": counter.most_common(proc_typow)
        }


class L_TCCT5(Lexical):
    name_en = "Percentage of tokens covering 5% of most common types"
    name_pl = "Występowanie wyrazów wchodzących w skład 5% najczęstszych typów (min. 1 typ)"

    def count(self, doc):
        counter = Counter([token.lemma_ for token in doc])
        ile_typow = len(counter)
        proc_typow = round(ile_typow * 0.05)
        if proc_typow == 0:
            proc_typow = 1
        suma_wystapien = sum([n for word, n in counter.most_common(proc_typow)])
        result = ratio(suma_wystapien, doc._.n_tokens)
        return result, {
            "[MOST COMMON TYPES]": counter.most_common(proc_typow)
        }


class L_SYL_G3(Lexical):
    name_en = "Words formed of more than 3 syllables incidence"
    name_pl = "Występowanie wyrazów o liczbie sylab większej niż 3"

    def count(self, doc):
        lengths = [token._.syllables_count for token in doc if token._.syllables_count is not None]
        selected = [length for length in lengths if length > 3]
        result = incidence(doc, selected)
        return result, {}


LEXICAL = [
    L_TTR_LA,
    L_TTR_IA,
    L_CONT_A,
    L_NCONT_A,
    L_CONT_T,
    L_NCONT_T,
    L_CONT_L,
    L_NAME,
    L_PERSN,
    L_TCCT1,
    L_TCCT5,
    L_SYL_G3,
]

lexical_group = MetricsGroup([m() for m in LEXICAL])
