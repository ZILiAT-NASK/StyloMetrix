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


from ...structures import Metric, Category
from ...utils import incidence, ratio


class PartOfSpeech(Category):
    lang = 'en'
    name_en = "Parts of speech"


class POS_VERB(Metric):
    category = PartOfSpeech
    name_en = "Verbs"

    def count(doc):
        search = [token for token in doc if token.pos_ in ["VERB", "AUX"]]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class POS_NOUN(Metric):
    category = PartOfSpeech
    name_en = "Nouns"

    def count(doc):
        search = [token for token in doc if token.pos_ == "NOUN"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class POS_ADJ(Metric):
    category = PartOfSpeech
    name_en = "Adjectives"

    def count(doc):
        search = [token for token in doc if token.pos_ == "ADJ"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class POS_ADV(Metric):
    category = PartOfSpeech
    name_en = "Adverbs"

    def count(doc):
        search = [token for token in doc if token.pos_ == "ADV"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class POS_DET(Metric):
    category = PartOfSpeech
    name_en = "Determiners"

    def count(doc):
        search = [token for token in doc if token.pos_ == "DET"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class POS_INTJ(Metric):
    category = PartOfSpeech
    name_en = "Interjections"

    def count(doc):
        search = [token for token in doc if token.pos_ == "INTJ"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class POS_CONJ(Metric):
    category = PartOfSpeech
    name_en = "Conjunctions"

    def count(doc):
        search = [token for token in doc if token.pos_ in  ["SCONJ", "CCONJ"]]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class POS_PART(Metric):
    category = PartOfSpeech
    name_en = "Particles"

    def count(doc):
        search = [token for token in doc if token.pos_ == "PART"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class POS_NUM(Metric):
    category = PartOfSpeech
    name_en = "Numerals"

    def count(doc):
        search = [token for token in doc if token.pos_ == "NUM"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class POS_PREP(Metric):
    category = PartOfSpeech
    name_en = "Prepositions"

    def count(doc):
        search = [token for token in doc if token.tag_ == "IN"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class POS_PRO(Metric):
    category = PartOfSpeech
    name_en = "Pronouns"

    def count(doc):
        search = [token for token in doc if token.pos_ == "PRON"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug

