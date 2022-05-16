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


from spacy.language import Language

from stylo_metrix.pipeline.en import COMPONENTS_EN
from stylo_metrix.pipeline.pl import COMPONENTS_PL


@Language.factory("stylo_metrix")
class StyloMetrixPipe():

    def __init__(self, nlp, name):
        lang = nlp.config["nlp"]["lang"]
        if lang == "pl":
            self.components = [component(nlp) for component in COMPONENTS_PL]
        elif lang == "en":
            self.components = [component(nlp) for component in COMPONENTS_EN]
        else:
            print(f"The language code [{lang}] is not supported by StyloMetrix.")

    def __call__(self, doc):
        for component in self.components:
            doc = component(doc)
        return doc
