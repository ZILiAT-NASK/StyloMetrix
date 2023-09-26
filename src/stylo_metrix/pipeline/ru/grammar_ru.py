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


def is_function_word(token):
    function_words_pos = ["PART", "SYM", "ADP", "X", "DET", "CCONJ", "SCONJ", "PUNCT", "INTJ"]
    if token.pos_ in function_words_pos:
        return True


def is_content_word(token):
    if not token._.is_function_word:
        return True


def is_punctuation(token):
    if token.pos_ == "PUNCT":
        return True


# def transitive_verbs(doc):
#     label = "tr"
#     ext = "transitivity"

#     pos = ["NOUN", "PRON", "PROPN"]

#     tokens = [token for token in doc if any(child for child in token.children if child.pos_ in pos) 
#     and token.pos_ == "VERB" and "VerbForm=Inf" not in token.morph]

#     return tokens, ext, label


# def intransitive_verbs(doc):
#     label = "intr"
#     ext = "transitivity"

#     pos = ["NOUN", "PRON", "PROPN"]

#     tokens = [token for token in doc if not any(child for child in token.children if child.pos_ in pos) 
#              and token.pos_ == "VERB"]

#     return tokens, ext, label


# FUNCTION_LIST = [
# transitive_verbs,
# intransitive_verbs
# ]
