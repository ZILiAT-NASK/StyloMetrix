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

from stylo_metrix.utils import ratio


class Destriptive(Category):
    lang = 'pl'
    name_en = "Descriptive"
    name_local = "Opisowe"


class DESC_ADJ(Metric):
    category = Destriptive
    name_en = "Adjectival description of qualities"
    name_local = "Opis właściwości przymiotnikowy"

    def count(doc):
        trigrams = [doc[start:end] for match_id, start, end
                    in doc._.matches
                    if doc.vocab.strings[match_id] == DESC_ADJ.code]
        count = sum(len(tr) for tr in trigrams)
        debug = {'TOKENS': trigrams}
        return ratio(count, doc._.n_tokens), debug


class DESC_ADV(Metric):
    category = Destriptive
    name_en = "Adverbial description of qualities"
    name_local = "Opis właściwości przysłówkowy"

    def count(doc):
        trigrams = [doc[start:end] for match_id, start, end
                    in doc._.matches
                    if doc.vocab.strings[match_id] == DESC_ADJ.code]
        count = sum(len(tr) for tr in trigrams)
        debug = {'TOKENS': trigrams}
        return ratio(count, doc._.n_tokens), debug


class DESC_NVA(Metric):
    category = Destriptive
    name_en = ""
    name_local = "Schemat 'Coś jest jakieś/działa jakoś' (N/PRON-V-ADJ/ADV)"

    def count(doc):
        trigrams = [doc[start:end] for match_id, start, end
                    in doc._.matches
                    if doc.vocab.strings[match_id] == DESC_ADJ.code]
        count = sum(len(tr) for tr in trigrams)
        debug = {'TOKENS': trigrams}
        return ratio(count, doc._.n_tokens), debug


class DESC_NVN(Metric):
    category = Destriptive
    name_en = ""
    name_local = "Schemat 'ktoś zrobił coś' (N-V-ADJ*-N)"

    def count(doc):
        trigrams = [doc[start:end] for match_id, start, end
                    in doc._.matches
                    if doc.vocab.strings[match_id] == DESC_ADJ.code]
        count = sum(len(tr) for tr in trigrams)
        debug = {'TOKENS': trigrams}
        return ratio(count, doc._.n_tokens), debug


# DESCRIPTIVE = [
#     DESC_ADJ,
#     DESC_ADV,
#     DESC_NVA,
#     DESC_NVN,
# ]

# descriptive_group = MetricsGroup([m() for m in DESCRIPTIVE])
