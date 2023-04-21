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


class Punctuation(Category):
    lang = 'pl'
    name_en = "Punctuation"
    name_local = "Interpunkcyjne"


class PUNCT_TOTAL(Metric):
    category = Punctuation
    name_en = "Punctuation"
    name_local = "Interpunkcja"

    def count(doc):
        puncts = list(token.text for token in doc if token._.is_punctuation)
        count = len(puncts)
        debug = {"VALUES": puncts}
        return ratio(count, doc._.n_tokens), debug


class PUNCT_BI_NOUN(Metric):
    category = Punctuation
    name_en = "Punctuation following a verb"
    name_local = "Interpunkcja po rzeczowniku"

    def count(doc):
        punct = [doc[start:end] for match_id, start, end
                    in doc._.matches
                    if doc.vocab.strings[match_id] == PUNCT_BI_NOUN.code]
        count = len(punct) * 2
        debug = {"VALUES": punct}
        return ratio(count, doc._.n_tokens), debug


class PUNCT_BI_VERB(Metric):
    category = Punctuation
    name_en = "Punctuation following a noun"
    name_local = "Interpunkcja po czasowniku"

    def count(doc):
        punct = [doc[start:end] for match_id, start, end
                    in doc._.matches
                    if doc.vocab.strings[match_id] == PUNCT_BI_VERB.code]
        count = len(punct) * 2
        debug = {"VALUES": punct}
        return ratio(count, doc._.n_tokens), debug


# PUNCTUATION = [
#     PUNCT_TOTAL,
#     PUNCT_BI_NOUN,
#     PUNCT_BI_VERB,
# ]

# punctuation_group = MetricsGroup([m() for m in PUNCTUATION])
