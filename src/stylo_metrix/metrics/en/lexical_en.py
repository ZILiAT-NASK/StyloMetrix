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


from abc import ABC

from stylo_metrix.structures import Metric, MetricsGroup
from stylo_metrix.utils import incidence


class Lexical(Metric, ABC):
    category_en = "Lexical"


class L_TTR_LA(Lexical):
    name_en = "Type-token ratio for words lemmas"

    def count(self, doc):
        types = set(token.lemma_ for token in doc._.words)
        result = incidence(doc, types)
        return result, {}


class L_NAME(Lexical):
    name_en = "Incidence of proper names (all words)"

    def count(self, doc):
        ents = [token for token in doc if token.pos_ == "PROPN"]
        result = incidence(doc, ents)
        return result, {}


class L_PERSN(Lexical):
    name_en = "Incidence of personal names (all words)"

    def count(self, doc):
        ents = [list(ent) for ent in doc.ents if ent.label_ == 'PERSON']
        sum_ents = sum(ents, [])
        result = incidence(doc, sum_ents)
        return result, {}


class L_PUNCT(Lexical):
    name_en = "Incidence of punctuation per all words"

    def count(self, doc):
        ents = [token for token in doc if token.pos_ == "PUNCT"]
        result = incidence(doc, ents)
        return result, {}


class L_PUNCT_DOT(Lexical):
    name_en = "Incidence of dots per all words"

    def count(self, doc):
        ents = [token for token in doc if token.text == "."]
        result = incidence(doc, ents)
        return result, {}


class L_PUNCT_COM(Lexical):
    name_en = "Incidence of comma per all words"

    def count(self, doc):
        ents = [token for token in doc if token.text == ","]
        result = incidence(doc, ents)
        return result, {}


class L_CONT_A(Lexical):
    name_en = "Content words incidence"

    def count(self, doc):
        search = [token.text for token in doc._.words if token._.is_content_word]
        result = incidence(doc, search)
        return result, {"CW": search}


class L_FUNC_A(Lexical):
    name_en = "Function words incidence"

    def count(self, doc):
        search = [token.text for token in doc._.words if token._.is_function_word]
        result = incidence(doc, search)
        return result, {"CW": search}


class L_CONT_T(Lexical):
    name_en = "Content words types incidence"

    def count(self, doc):
        search = set(token.text for token in doc._.words if token._.is_content_word)
        result = incidence(doc, search)
        return result, {}


class L_FUNC_T(Lexical):
    name_en = "Function words types incidence"

    def count(self, doc):
        search = set(token.text for token in doc._.words if token._.is_function_word)
        result = incidence(doc, search)
        return result, {}


class L_SYL_G2(Lexical):
    name_en = "Words formed of more than 2 syllables incidence"

    def count(self, doc):
        lengths = [token._.syllables_count for token in doc if token._.syllables_count is not None]
        selected = [length for length in lengths if length > 2]
        result = incidence(doc, selected)
        return result, {}


class L_PUNCT_SEMC(Lexical):
    name_en = "Incidence of semicolon per all words"

    def count(self, doc):
        ents = [token for token in doc if token.text == ";"]
        result = incidence(doc, ents)
        return result, {}


class L_PUNCT_COL(Lexical):
    name_en = "Incidence of colon per all words"

    def count(self, doc):
        ents = [token for token in doc if token.text == ":"]
        result = incidence(doc, ents)
        return result, {}


class L_PUNCT_DASH(Lexical):
    name_en = "Incidence of dashes per all words"

    def count(self, doc):
        ents = [token for token in doc if token.text == "—"]
        result = incidence(doc, ents)
        return result, {}


"""
SUBJECT PRONOUNS
"""

class I_PRON(Lexical):
    name_en = "Incidence of 'I'-pronoun per all words"

    def count(self, doc):
        pers_pron = []
        for token in doc:
            if token.pos_ == "PRON" and ("Person=1" in token.morph) and ("Number=Sing" in token.morph):
                pers_pron.append(token)
        result = incidence(doc, pers_pron)
        return result, {}


class HE_PRON(Lexical):
    name_en = "Incidence of 'he'-pronoun per all words"

    def count(self, doc):
        pers_pron = []
        for token in doc:
            if token.lower_ == "he":
                pers_pron.append(token)
        result = incidence(doc, pers_pron)
        return result, {}


class SHE_PRON(Lexical):
    name_en = "Incidence of 'she'-pronoun per all words"

    def count(self, doc):
        pers_pron = []
        for token in doc:
            if token.lower_ == "she":
                pers_pron.append(token)
        result = incidence(doc, pers_pron)
        return result, {}


class IT_PRON(Lexical):
    name_en = "Incidence of 'it'-pronoun per all words"

    def count(self, doc):
        pers_pron = []
        for token in doc:
            if token.lower_ == "it" and "Case=Nom" in token.morph:
                pers_pron.append(token)
        result = incidence(doc, pers_pron)
        return result, {}


class YOU_PRON(Lexical):
    name_en = "Incidence of 'you'-pronoun per all words"

    def count(self, doc):
        pers_pron = []
        for token in doc:
            if token.lower_ == "you" and "Case=Nom" in token.morph:
                pers_pron.append(token)
        result = incidence(doc, pers_pron)
        return result, {}


class WE_PRON(Lexical):
    name_en = "Incidence of 'we'-pronoun per all words"

    def count(self, doc):
        pers_pron = []
        for token in doc:
            if token.lower_ == "we":
                pers_pron.append(token)
        result = incidence(doc, pers_pron)
        return result, {}


class THEY_PRON(Lexical):
    name_en = "Incidence of 'they'-pronoun per all words"

    def count(self, doc):
        pers_pron = []
        for token in doc:
            if token.lower_ == "they":
                pers_pron.append(token)
        result = incidence(doc, pers_pron)
        return result, {}


"""
OBJECT PRONOUNS
"""

class ME_PRON(Lexical):
    name_en = "Incidence of 'me'-pronoun per all words"

    def count(self, doc):
        pers_pron = []
        for token in doc:
            if token.lower_ == "me":
                pers_pron.append(token)
        result = incidence(doc, pers_pron)
        return result, {}


class YOU_OBJ_PRON(Lexical):
    name_en = "Incidence of 'you'-object pronoun per all words"

    def count(self, doc):
        pers_pron = []
        for token in doc:
            if token.lower_ == "you" and "Case=Nom" not in token.morph:
                pers_pron.append(token)
        result = incidence(doc, pers_pron)
        return result, {}


class HIM_PRON(Lexical):
    name_en = "Incidence of 'him'-object pronoun per all words"

    def count(self, doc):
        pers_pron = []
        for token in doc:
            if token.lower_ == "him":
                pers_pron.append(token)
        result = incidence(doc, pers_pron)
        return result, {}


class HER_OBJ_PRON(Lexical):
    name_en = "Incidence of 'her'-object pronoun per all words"

    def count(self, doc):
        pers_pron = []
        for token in doc:
            if token.lower_ == "her" and "Case=Acc" in token.morph:
                pers_pron.append(token)
        result = incidence(doc, pers_pron)
        return result, {}



class IT_OBJ_PRON(Lexical):
    name_en = "Incidence of 'it'-pronoun per all words"

    def count(self, doc):
        pers_pron = []
        for token in doc:
            if token.lower_ == "it" and "Case=Acc" in token.morph:
                pers_pron.append(token)
        result = incidence(doc, pers_pron)
        return result, {}


class US_PRON(Lexical):
    name_en = "Incidence of 'us'-pronoun per all words"

    def count(self, doc):
        pers_pron = []
        for token in doc:
            if token.lower_ == "us":
                pers_pron.append(token)
        result = incidence(doc, pers_pron)
        return result, {}


class THEM_PRON(Lexical):
    name_en = "Incidence of 'them'-pronoun per all words"

    def count(self, doc):
        pers_pron = []
        for token in doc:
            if token.lower_ == "them":
                pers_pron.append(token)
        result = incidence(doc, pers_pron)
        return result, {}


"""
POSSESSIVE PRONOUNS
"""

class MY_PRON(Lexical):
    name_en = "Incidence of 'my'-pronoun per all words"

    def count(self, doc):
        pers_pron = []
        for token in doc:
            if token.lower_ == "my":
                pers_pron.append(token)
        result = incidence(doc, pers_pron)
        return result, {}


class YOUR_PRON(Lexical):
    name_en = "Incidence of 'your'-pronoun per all words"

    def count(self, doc):
        pers_pron = []
        for token in doc:
            if token.lower_ == "your":
                pers_pron.append(token)
        result = incidence(doc, pers_pron)
        return result, {}


class HIS_PRON(Lexical):
    name_en = "Incidence of 'his'-pronoun per all words"

    def count(self, doc):
        pers_pron = []
        for token in doc:
            if token.lower_ == "his":
                pers_pron.append(token)
        result = incidence(doc, pers_pron)
        return result, {}


class HER_PRON(Lexical):
    name_en = "Incidence of 'her'-possessive pronoun per all words"

    def count(self, doc):
        pers_pron = []
        for token in doc:
            if token.lower_ == "her" and "Poss=Yes" in token.morph:
                pers_pron.append(token)
        result = incidence(doc, pers_pron)
        return result, {}


class ITS_PRON(Lexical):
    name_en = "Incidence of 'its'-possessive pronoun per all words"

    def count(self, doc):
        pers_pron = []
        for token in doc:
            if token.lower_ == "its":
                pers_pron.append(token)
        result = incidence(doc, pers_pron)
        return result, {}


class OUR_PRON(Lexical):
    name_en = "Incidence of 'our'-possessive pronoun per all words"

    def count(self, doc):
        pers_pron = []
        for token in doc:
            if token.lower_ == "our":
                pers_pron.append(token)
        result = incidence(doc, pers_pron)
        return result, {}


class THEIR_PRON(Lexical):
    name_en = "Incidence of 'their'-possessive pronoun per all words"

    def count(self, doc):
        pers_pron = []
        for token in doc:
            if token.lower_ == "their":
                pers_pron.append(token)
        result = incidence(doc, pers_pron)
        return result, {}


class YOURS_PRON(Lexical):
    name_en = "Incidence of 'yours'-pronoun per all words"

    def count(self, doc):
        pers_pron = []
        for token in doc:
            if token.lower_ == "theirs":
                pers_pron.append(token)
        result = incidence(doc, pers_pron)
        return result, {}


class THEIRS_PRON(Lexical):
    name_en = "Incidence of 'theirs'-pronoun per all words"

    def count(self, doc):
        pers_pron = []
        for token in doc:
            if token.lower_ == "theirs":
                pers_pron.append(token)
        result = incidence(doc, pers_pron)
        return result, {}


class HERS_PRON(Lexical):
    name_en = "Incidence of 'hers'-pronoun per all words"

    def count(self, doc):
        pers_pron = []
        for token in doc:
            if token.lower_ == "hers":
                pers_pron.append(token)
        result = incidence(doc, pers_pron)
        return result, {}


class OURS_PRON(Lexical):
    name_en = "Incidence of 'ours'-possessive pronoun per all words"

    def count(self, doc):
        pers_pron = []
        for token in doc:
            if token.lower_ == "ours":
                pers_pron.append(token)
        result = incidence(doc, pers_pron)
        return result, {}


"""
REFLEXIVE PRONOUNS
"""

class MYSELF_PRON(Lexical):
    name_en = "Incidence of 'myself'-pronoun per all words"

    def count(self, doc):
        pers_pron = []
        for token in doc:
            if token.lower_ == "myself":
                pers_pron.append(token)
        result = incidence(doc, pers_pron)
        return result, {}


class YOURSELF_PRON(Lexical):
    name_en = "Incidence of 'yourself'-pronoun per all words"

    def count(self, doc):
        pers_pron = []
        for token in doc:
            if token.lower_ == "yourself":
                pers_pron.append(token)
        result = incidence(doc, pers_pron)
        return result, {}


class HIMSELF_PRON(Lexical):
    name_en = "Incidence of 'himself'-pronoun per all words"

    def count(self, doc):
        pers_pron = []
        for token in doc:
            if token.lower_ == "himself":
                pers_pron.append(token)
        result = incidence(doc, pers_pron)
        return result, {}


class HERSELF_PRON(Lexical):
    name_en = "Incidence of 'herself'-pronoun per all words"

    def count(self, doc):
        pers_pron = []
        for token in doc:
            if token.lower_ == "herself":
                pers_pron.append(token)
        result = incidence(doc, pers_pron)
        return result, {}


class ITSELF_PRON(Lexical):
    name_en = "Incidence of 'itself'-pronoun per all words"

    def count(self, doc):
        pers_pron = []
        for token in doc:
            if token.lower_ == "itself":
                pers_pron.append(token)
        result = incidence(doc, pers_pron)
        return result, {}


class OURSELVES_PRON(Lexical):
    name_en = "Incidence of 'ourselves'-pronoun per all words"

    def count(self, doc):
        pers_pron = []
        for token in doc:
            if token.lower_ == "ourselves":
                pers_pron.append(token)
        result = incidence(doc, pers_pron)
        return result, {}

class YOURSELVES_PRON(Lexical):
    name_en = "Incidence of 'yourselves'-pronoun per all words"

    def count(self, doc):
        pers_pron = []
        for token in doc:
            if token.lower_ == "yourselves":
                pers_pron.append(token)
        result = incidence(doc, pers_pron)
        return result, {}


class THEMSELVES_PRON(Lexical):
    name_en = "Incidence of 'themselves'-pronoun per all words"

    def count(self, doc):
        pers_pron = []
        for token in doc:
            if token.lower_ == "themselves":
                pers_pron.append(token)
        result = incidence(doc, pers_pron)
        return result, {}


"""
POSSESSIVE NOUNS WITH 'S
"""

class POSSESSIVES(Lexical):
    name_en = "Incidence of nouns in possessive case per all words"

    def count(self, doc):
        pers_pron = []
        for token in doc:
            if token.pos_ == "PART" and token.dep_ == "case":
                pers_pron.append(token)
        result = incidence(doc, pers_pron)
        return result, {}


LEXICAL = [
    L_TTR_LA,
    L_NAME,
    L_PERSN,
    L_PUNCT,
    L_PUNCT_COM,
    L_PUNCT_SEMC,
    L_PUNCT_COL,
    L_PUNCT_DASH,
    L_CONT_A,
    L_FUNC_A,
    L_CONT_T,
    L_FUNC_T,
    L_SYL_G2,
    I_PRON,
    HE_PRON,
    SHE_PRON,
    IT_PRON,
    YOU_PRON,
    WE_PRON,
    THEY_PRON,
    ME_PRON,
    YOU_OBJ_PRON,
    HIM_PRON,
    HER_OBJ_PRON,
    IT_OBJ_PRON,
    US_PRON,
    THEM_PRON,
    MY_PRON,
    YOUR_PRON,
    HIS_PRON,
    HER_PRON,
    ITS_PRON,
    OUR_PRON,
    THEIR_PRON,
    YOURS_PRON,
    THEIRS_PRON,
    HERS_PRON,
    OURS_PRON,
    MYSELF_PRON,
    YOURSELF_PRON,
    HIMSELF_PRON,
    HERSELF_PRON,
    ITSELF_PRON,
    OURSELVES_PRON,
    YOURSELVES_PRON,
    THEMSELVES_PRON,
    POSSESSIVES,
]

lexical_group = MetricsGroup([m() for m in LEXICAL])
