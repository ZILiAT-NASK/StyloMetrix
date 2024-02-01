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


from ...structures import Category, Metric
from ...utils import ratio


class PartOfSpeech(Category):
    lang = "en"
    name_en = "Parts of speech"
    name_local = name_en


class POS_VERB(Metric):
    category = PartOfSpeech
    name_en = "Verbs"
    name_local = name_en

    def count(doc):
        debug = [token.text for token in doc if token.pos_ in ["VERB", "AUX"]]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class POS_NOUN(Metric):
    category = PartOfSpeech
    name_en = "Nouns"
    name_local = name_en

    def count(doc):
        debug = [token.text for token in doc if token.pos_ == "NOUN"]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class POS_ADJ(Metric):
    category = PartOfSpeech
    name_en = "Adjectives"
    name_local = name_en

    def count(doc):
        debug = [token.text for token in doc if token.pos_ == "ADJ"]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class POS_ADV(Metric):
    category = PartOfSpeech
    name_en = "Adverbs"
    name_local = name_en

    def count(doc):
        debug = [token.text for token in doc if token.pos_ == "ADV"]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class POS_DET(Metric):
    category = PartOfSpeech
    name_en = "Determiners"
    name_local = name_en

    def count(doc):
        debug = [token.text for token in doc if token.pos_ == "DET"]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class POS_INTJ(Metric):
    category = PartOfSpeech
    name_en = "Interjections"
    name_local = name_en

    def count(doc):
        debug = [token.text for token in doc if token.pos_ == "INTJ"]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class POS_CONJ(Metric):
    category = PartOfSpeech
    name_en = "Conjunctions"
    name_local = name_en

    def count(doc):
        debug = [token.text for token in doc if token.pos_ in ["SCONJ", "CCONJ"]]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class POS_PART(Metric):
    category = PartOfSpeech
    name_en = "Particles"
    name_local = name_en

    def count(doc):
        debug = [token.text for token in doc if token.pos_ == "PART"]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class POS_NUM(Metric):
    category = PartOfSpeech
    name_en = "Numerals"
    name_local = name_en

    def count(doc):
        debug = [token.text for token in doc if token.pos_ == "NUM"]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class POS_PREP(Metric):
    category = PartOfSpeech
    name_en = "Prepositions"
    name_local = name_en

    def count(doc):
        debug = [token.text for token in doc if token.tag_ == "IN"]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class POS_PRO(Metric):
    category = PartOfSpeech
    name_en = "Pronouns"
    name_local = name_en

    def count(doc):
        debug = [token.text for token in doc if token.pos_ == "PRON"]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug
