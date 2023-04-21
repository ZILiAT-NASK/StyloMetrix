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

from stylo_metrix.pipeline.en.dictionary_en import LW_OPPOSITION_LIMITATION_CONTRADICTION, LW_AGREEMENT_ADDITION_SIMILARITY, LW_EXAMPLES_SUPPORT_EMPHRASIS, LW_EFFECT_RESULT_CONSEQUENCE, LW_CAUSE_PURPOSE, LW_SPACE_LOCATION_PLACE, LW_TIME_CHRONOLOGY_SEQUENCE, LW_MANNER, LW_CONDITION

def get_all_tokens(doc):
    tokens = [*doc]
    return tokens

def contradiction(doc):
    ext = "linking_words"
    label = "contradiction"

    tokens = get_all_tokens(doc)
    words = LW_OPPOSITION_LIMITATION_CONTRADICTION
    search = [token for token in tokens if token.text.lower() in words]
    return search, ext, label 

def agreement(doc):
    ext = "linking_words"
    label = "agreement"

    tokens = get_all_tokens(doc)
    words = LW_AGREEMENT_ADDITION_SIMILARITY
    search = [token for token in tokens if token.text.lower() in words]
    return search, ext, label

def examples(doc):
    ext = "linking_words"
    label = "examples"

    tokens = get_all_tokens(doc)
    words = LW_EXAMPLES_SUPPORT_EMPHRASIS
    search = [token for token in tokens if token.text.lower() in words]
    return search, ext, label

def cosequence(doc):
    ext = "linking_words"
    label = "cosequence"

    tokens = get_all_tokens(doc)
    words = LW_EFFECT_RESULT_CONSEQUENCE
    search = [token for token in tokens if token.text.lower() in words]
    return search, ext, label

def cause(doc):
    ext = "linking_words"
    label = "cause"

    tokens = get_all_tokens(doc)
    words = LW_CAUSE_PURPOSE
    search = [token for token in tokens if token.text.lower() in words]
    return search, ext, label

def location(doc):
    ext = "linking_words"
    label = "space"

    tokens = get_all_tokens(doc)
    words = LW_SPACE_LOCATION_PLACE
    search = [token for token in tokens if token.text.lower() in words]
    return search, ext, label

def time(doc):
    ext = "linking_words"
    label = "time"

    tokens = get_all_tokens(doc)
    words = LW_TIME_CHRONOLOGY_SEQUENCE
    search = [token for token in tokens if token.text.lower() in words]
    return search, ext, label

def manner(doc):
    ext = "linking_words"
    label = "manner"

    tokens = get_all_tokens(doc)
    words = LW_MANNER
    search = [token for token in tokens if token.text.lower() in words]
    return search, ext, label

def condition(doc):
    ext = "linking_words"
    label = "condition"
    
    tokens = get_all_tokens(doc)
    words = LW_CONDITION
    search = [token for token in tokens if token.text.lower() in words]
    return search, ext, label

FUNCTION_LIST = [contradiction, agreement, examples, cosequence, cause, location, time, manner, condition]