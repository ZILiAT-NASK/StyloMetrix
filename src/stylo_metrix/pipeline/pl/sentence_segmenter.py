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


class SentenceSegmenter():

    def __init__(self, nlp):
        self.nlp = nlp

    def __call__(self, doc):
        return self.segment(doc)

    def segment(self, doc):
        for token in doc[:-2]:
            if token.tag_ == 'brev':
                if doc[token.i + 2].text[0].isupper():
                    doc[token.i + 2].is_sent_start = True
                else:
                    doc[token.i + 2].is_sent_start = False
        return doc
