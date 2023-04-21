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


from collections import Counter

from stylo_metrix.structures import Metric, Category

from stylo_metrix.utils import incidence, ratio


class Lexical(Category):
    lang = 'pl'
    name_en = "Lexical"
    name_local = "Leksykalne"


class L_TTR_LA(Metric):
    category = Lexical
    name_en = "Type-token ratio for words lemmas"
    name_local = "Type-token ratio dla lemm wyrazów"

    def count(doc):
        types = set(token.lemma_ for token in doc._.words)
        result = incidence(doc, types)
        debug = {'TOKENS': types}
        return result, debug


class L_TTR_IA(Metric):
    category = Lexical
    name_en = "Type-token ratio for inflected words"
    name_local = "Type-token ratio dla wyrazów w odmianach"

    def count(doc):
        types = set(token.norm_ for token in doc._.words)
        result = incidence(doc, types)
        debug = {'TOKENS': types}
        return result, debug


class L_CONT_A(Metric):
    category = Lexical
    name_en = "Content words"
    name_local = "Wyrazy samodzielne"

    def count(doc):
        search = [token.text for token in doc._.words if token._.content_word == "cont"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class L_NCONT_A(Metric):
    category = Lexical
    name_en = "Non-content words"
    name_local = "Wyrazy niesamodzielne"

    def count(doc):
        search = [token.text for token in doc._.words if token._.content_word == "noncont"]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class L_CONT_T(Metric):
    category = Lexical
    name_en = "Content words types"
    name_local = "Typy wyrazów samodzielnych"

    def count(doc):
        search = set(token.text for token in doc._.words if token._.content_word == "cont")
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class L_NCONT_T(Metric):
    category = Lexical
    name_en = "Non-content words types"
    name_local = "Typy wyrazów niesamodzielnych"

    def count(doc):
        search = set(token.text for token in doc._.words if token._.content_word == "noncont")
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class L_CONT_L(Metric):
    category = Lexical
    name_en = "Lemmas of content words types"
    name_local = "Typy lemm wyrazów samodzielnych"

    def count(doc):
        search = set(token.lemma_ for token in doc._.words if token._.content_word == "cont")
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class L_NAME(Metric):
    category = Lexical
    name_en = "Proper names"
    name_local = "Nazwy własne"

    def count(doc):
        ents = [list(ent) for ent in doc.ents]
        sum_ents = sum(ents, [])
        filtered_ents = [tok for tok in sum_ents if tok in doc._.tokens]
        result = incidence(doc, filtered_ents)
        debug = {'TOKENS': filtered_ents}
        return result, debug


class L_PERSN(Metric):
    category = Lexical
    name_en = "Personal names"
    name_local = "Nazwy osób"

    def count(doc):
        ents = [list(ent) for ent in doc.ents if ent.label_ == 'PERSNAME']
        sum_ents = sum(ents, [])
        filtered_ents = [tok for tok in sum_ents if tok in doc._.tokens]
        result = incidence(doc, filtered_ents)
        debug = {'TOKENS': filtered_ents}
        return result, debug


class L_PLACEN(Metric):
    category = Lexical
    name_en = "Place names"
    name_local = "Nazwy miejsc"

    def count(doc):
        ents = [list(ent) for ent in doc.ents if ent.label_ == 'PLACENAME']
        sum_ents = sum(ents, [])
        filtered_ents = [tok for tok in sum_ents if tok in doc._.tokens]
        result = incidence(doc, filtered_ents)
        debug = {'TOKENS': filtered_ents}
        return result, debug


class L_TCCT1(Metric):
    category = Lexical
    name_en = "Tokens covering 1% of most common types"
    name_local = "Wyrazy wchodzące w skład 1% najczęstszych typów"

    def count(doc):
        counter = Counter([token.lemma_ for token in doc._.tokens])
        avail_types = len(counter)
        n_types = round(avail_types * 0.01)
        if n_types == 0:
            n_types = 1
        inc = sum([n for word, n in counter.most_common(n_types)])
        result = ratio(inc, doc._.n_tokens)
        debug = {'TOKENS': counter.most_common(n_types)}
        return result, debug


class L_TCCT5(Metric):
    category = Lexical
    name_en = "Tokens covering 5% of most common types"
    name_local = "Wyrazy wchodzące w skład 5% najczęstszych typów"

    def count(doc):
        counter = Counter([token.lemma_ for token in doc._.tokens])
        avail_types = len(counter)
        n_types = round(avail_types * 0.05)
        if n_types == 0:
            n_types = 1
        inc = sum([n for word, n in counter.most_common(n_types)])
        result = ratio(inc, doc._.n_tokens)
        debug = {'TOKENS': counter.most_common(n_types)}
        return result, debug


class L_SYL_G3(Metric):
    category = Lexical
    name_en = "Words formed of more than 3 syllables"
    name_local = "Wyrazy o liczbie sylab większej niż 3"

    def count(doc):
        selected = [token for token in doc if token._.syllables_count is not None and token._.syllables_count > 3]
        result = incidence(doc, selected)
        debug = {'TOKENS': selected}
        return result, debug
