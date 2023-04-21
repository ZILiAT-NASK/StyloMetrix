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


from spacy.matcher import Matcher
from spacy.tokens import Doc


class MatcherComponent:
    def __init__(self, nlp):
        self.nlp = nlp
        self.matcher = Matcher(nlp.vocab)
        self._add_patterns()
        Doc.set_extension("matches", default=None, force=True)

    def __call__(self, doc):
        doc._.matches = self.matcher(doc)
        return doc

    def _add_patterns(self):
        # DES
        DESC_ADV = [{"POS": "ADV"}, {"POS": "PUNCT", "OP": "*"}, {"POS": "CCONJ"}, {"POS": "ADV"}]
        self.matcher.add("DESC_ADV", [DESC_ADV])
        DESC_ADJ = [{"POS": "ADJ"}, {"POS": "PUNCT", "OP": "*"}, {"POS": "CCONJ"}, {"POS": "ADJ"}]
        self.matcher.add("DESC_ADJ", [DESC_ADJ])
        DESC_NVA = [{"POS": {"IN": ["NOUN", "PRON"]}}, {"POS": {"IN": ["VERB", "AUX"]}}, {"POS": {"IN": ["ADJ", "ADV"]}}]
        self.matcher.add("DESC_NVA", [DESC_NVA])
        DESC_NVN = [{"POS": "NOUN"}, {"POS": "VERB"}, {"POS": "ADJ", 'OP': '*'}, {"POS": "NOUN"}]
        self.matcher.add("DESC_NVN", [DESC_NVN])

        # PU
        PUNCT_BI_NOUN = [{"POS": "NOUN"}, {"IS_SPACE": True, "OP": "*"}, {"IS_PUNCT": True}]
        self.matcher.add("PUNCT_BI_NOUN", [PUNCT_BI_NOUN])
        PUNCT_BI_VERB = [{"POS": "VERB"}, {"IS_SPACE": True, "OP": "*"}, {"IS_PUNCT": True}]
        self.matcher.add("PUNCT_BI_VERB", [PUNCT_BI_VERB])

        # SY
        SY_INV_EP = [{"POS": "NOUN"}, {"POS": "ADJ"}, {"POS": "NOUN", 'OP':'!'}]
        self.matcher.add("SY_INV_EP", [SY_INV_EP])


