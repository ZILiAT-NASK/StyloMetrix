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


import unicodedata


class CustomPreprocessing:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer

    def __call__(self, string):
        right_quote = unicodedata.lookup('RIGHT DOUBLE QUOTATION MARK')
        left_quote = unicodedata.lookup('LEFT DOUBLE QUOTATION MARK')
        return self.tokenizer(string.replace(right_quote, '\"').replace(left_quote, '\"'))
