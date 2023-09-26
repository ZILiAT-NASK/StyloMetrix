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

from . import grammar_ukr as grammar
from spacy.tokens import Token


class POSTagger():

    def __init__(self, nlp):
        self.nlp = nlp

        Token.set_extension("conjugation", default=None, force=True)
        Token.set_extension("transitivity", default=None, force=True)
        Token.set_extension("is_function_word", default=False, force=True)
        Token.set_extension("is_content_word", default=False, force=True)
        Token.set_extension("is_punctuation", default=False, force=True)

    def __call__(self, doc):
        for token in doc:
            token._.set("is_function_word", grammar.is_function_word(token))
            token._.set("is_content_word", grammar.is_content_word(token))
            
        def assign_label(function_list):
            for function in function_list:
                lst, extension, label = function(doc)
                for token in lst:
                    token._.set(extension, label)
        assign_label(grammar.FUNCTION_LIST)

        return doc

