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


from spacy.tokens import Doc, Token

from stylo_metrix.pipeline.pl.resources.experimental_data import MEANS, PSYCHOLINGUISTIC_DATA


class Psycholinguistic():

    def __init__(self, nlp):
        self.nlp = nlp
        Token.set_extension("affective_norms", default=None, force=True)  # type dict
        Doc.set_extension("an_means", default=MEANS, force=True)

    def __call__(self, doc):
        for token in doc:
            if token.lemma_ in PSYCHOLINGUISTIC_DATA.keys():
                token._.set("affective_norms", PSYCHOLINGUISTIC_DATA[token.lemma_])
        return doc
