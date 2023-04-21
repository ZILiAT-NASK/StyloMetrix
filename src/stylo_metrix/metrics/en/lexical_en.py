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


from stylo_metrix.structures import Metric, Category

from stylo_metrix.utils import incidence


class Lexical(Category):
    lang = 'en'
    name_en = "Lexical"


class L_TYPE_TOKEN_RATIO_LEMMAS(Metric):
    category = Lexical
    name_en = "Type-token ratio for words lemmas"

    def count(doc):
        types = set(token.lemma_ for token in doc._.words)
        result = incidence(doc, types)
        debug = {'TOKENS': types}
        return result, debug


class L_CONT_A(Metric):
    category = Lexical
    name_en = "Content words"

    def count(doc):
        search = [token.text for token in doc._.words if token._.is_content_word]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class L_FUNC_A(Metric):
    category = Lexical
    name_en = "Function words"

    def count(doc):
        search = [token.text for token in doc._.words if token._.is_function_word]
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug

class L_CONT_T(Metric):
    category = Lexical
    name_en = "Content words types"

    def count(doc):
        search = set(token.text for token in doc._.words if token._.is_content_word)
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class L_FUNC_T(Metric):
    category = Lexical
    name_en = "Function words types"

    def count(doc):
        search = set(token.text for token in doc._.words if token._.is_function_word)
        result = incidence(doc, search)
        debug = {'TOKENS': search}
        return result, debug


class L_SYL_G2(Metric):
    category = Lexical
    name_en = "Words formed of more than 2 syllables"

    def count(doc):
        lengths = [token._.syllables_count for token in doc if token._.syllables_count is not None]
        selected = [length for length in lengths if length > 2]
        result = incidence(doc, selected)
        debug = {'TOKENS': selected}
        return result, debug


"""NOUNS"""

class L_PLURAL_NOUNS(Metric):
    category = Lexical
    name_en = "Nouns in plural"

    def count(doc):
        nouns_plural = [token for token in doc if token.pos_ == "NOUN" and "Number=Plur" in token.morph]
        result = incidence(doc, nouns_plural)
        debug = {'TOKENS': nouns_plural}
        return result, debug


class L_SINGULAR_NOUNS(Metric):
    category = Lexical
    name_en = "Nouns in singular"

    def count(doc):
        nouns_sing = [token for token in doc if token.pos_ == "NOUN" and "Number=Sing" in token.morph]
        result = incidence(doc, nouns_sing)
        debug = {'TOKENS': nouns_sing}
        return result, debug


class L_PROPER_NAME(Metric):
    category = Lexical
    name_en = "Proper names"

    def count(doc):
        ents = [token for token in doc if token.pos_ == "PROPN"]
        result = incidence(doc, ents)
        debug = {'TOKENS': ents}
        return result, debug


class L_PERSONAL_NAME(Metric):
    category = Lexical
    name_en = "Personal names"

    def count(doc):
        ents = [list(ent) for ent in doc.ents if ent.label_ == 'PERSON']
        sum_ents = sum(ents, [])
        result = incidence(doc, sum_ents)
        debug = {'TOKENS': sum_ents}
        return result, debug


class L_NOUN_PHRASES(Metric):
    category = Lexical
    name_en = "Incidence of noun phrases"

    def count(doc):
        phrases = [noun_phrase for noun_phrase in doc.noun_chunks]
        np_ph = [noun for phrase in phrases for noun in phrase]
        result = incidence(doc, np_ph)
        debug = {'TOKENS': np_ph}
        return result, debug


"""PUNCTUATION"""


class L_PUNCT(Metric):
    category = Lexical
    name_en = "Punctuation"

    def count(doc):
        ents = [token for token in doc if token.pos_ == "PUNCT"]
        result = incidence(doc, ents)
        debug = {'TOKENS': ents}
        return result, debug


class L_PUNCT_DOT(Metric):
    category = Lexical
    name_en = "Punctuation - dots"

    def count(doc):
        ents = [token for token in doc if token.text == "."]
        result = incidence(doc, ents)
        debug = {'TOKENS': ents}
        return result, debug


class L_PUNCT_COM(Metric):
    category = Lexical
    name_en = "Punctuation - comma"

    def count(doc):
        ents = [token for token in doc if token.text == ","]
        result = incidence(doc, ents)
        debug = {'TOKENS': ents}
        return result, debug


class L_PUNCT_SEMC(Metric):
    category = Lexical
    name_en = "Punctuation - semicolon"

    def count(doc):
        ents = [token for token in doc if token.text == ";"]
        result = incidence(doc, ents)
        debug = {'TOKENS': ents}
        return result, debug


class L_PUNCT_COL(Metric):
    category = Lexical
    name_en = "Punctuation - colon"

    def count(doc):
        ents = [token for token in doc if token.text == ":"]
        result = incidence(doc, ents)
        debug = {'TOKENS': ents}
        return result, debug


class L_PUNCT_DASH(Metric):
    category = Lexical
    name_en = "Punctuation - dashes"

    def count(doc):
        ents = [token for token in doc if token.text == "—"]
        result = incidence(doc, ents)
        debug = {'TOKENS': ents}
        return result, debug


"""
SUBJECT PRONOUNS
"""

class L_I_PRON(Metric):
    category = Lexical
    name_en = "'I' pronoun"

    def count(doc):
        pers_pron = [token for token in doc if token.pos_ == "PRON" and ("Person=1" in token.morph) and ("Number=Sing" in token.morph)]
        result = incidence(doc, pers_pron)
        debug = {'TOKENS': pers_pron}
        return result, debug


class L_HE_PRON(Metric):
    category = Lexical
    name_en = "'He' pronoun"

    def count(doc):
        pers_pron = [token for token in doc if token.lower_ == "he"]
        result = incidence(doc, pers_pron)
        debug = {'TOKENS': pers_pron}
        return result, debug


class L_SHE_PRON(Metric):
    category = Lexical
    name_en = "'She' pronoun"

    def count(doc):
        pers_pron = [token for token in doc if token.lower_ == "she"]
        result = incidence(doc, pers_pron)
        debug = {'TOKENS': pers_pron}
        return result, debug


class L_IT_PRON(Metric):
    category = Lexical
    name_en = "'It' pronoun"

    def count(doc):
        pers_pron = [token for token in doc if token.lower_ == "it" and "Case=Nom" in token.morph]
        result = incidence(doc, pers_pron)
        debug = {'TOKENS': pers_pron}
        return result, debug


class L_YOU_PRON(Metric):
    category = Lexical
    name_en = "'You' pronoun"

    def count(doc):
        pers_pron = [token for token in doc if token.lower_ == "you" and "Case=Nom" in token.morph]
        result = incidence(doc, pers_pron)
        debug = {'TOKENS': pers_pron}
        return result, debug


class L_WE_PRON(Metric):
    category = Lexical
    name_en = "'We' pronoun"

    def count(doc):
        pers_pron = [token for token in doc if token.lower_ == "we"]
        result = incidence(doc, pers_pron)
        debug = {'TOKENS': pers_pron}
        return result, debug


class L_THEY_PRON(Metric):
    category = Lexical
    name_en = "'They' pronoun"

    def count(doc):
        pers_pron = [token for token in doc if token.lower_ == "they"]
        result = incidence(doc, pers_pron)
        debug = {'TOKENS': pers_pron}
        return result, debug


"""
OBJECT PRONOUNS
"""

class L_ME_PRON(Metric):
    category = Lexical
    name_en = "'Me' pronoun"

    def count(doc):
        pers_pron = [token for token in doc if token.lower_ == "me"]
        result = incidence(doc, pers_pron)
        debug = {'TOKENS': pers_pron}
        return result, debug


class L_YOU_OBJ_PRON(Metric):
    category = Lexical
    name_en = "'You' object pronoun"

    def count(doc):
        pers_pron = [token for token in doc if token.lower_ == "you" and "Case=Nom" not in token.morph]
        result = incidence(doc, pers_pron)
        debug = {'TOKENS': pers_pron}
        return result, debug


class L_HIM_PRON(Metric):
    category = Lexical
    name_en = "'Him' object pronoun"

    def count(doc):
        pers_pron = [token for token in doc if token.lower_ == "him"]
        result = incidence(doc, pers_pron)
        debug = {'TOKENS': pers_pron}
        return result, debug


class L_HER_OBJECT_PRON(Metric):
    category = Lexical
    name_en = "'Her' object pronoun"

    def count(doc):
        pers_pron = [token for token in doc if token.lower_ == "her" and "Case=Acc" in token.morph]
        result = incidence(doc, pers_pron)
        debug = {'TOKENS': pers_pron}
        return result, debug


class L_IT_OBJECT_PRON(Metric):
    category = Lexical
    name_en = "'It' pronoun"

    def count(doc):
        pers_pron = [token for token in doc if token.lower_ == "it" and "Case=Acc" in token.morph]
        result = incidence(doc, pers_pron)
        debug = {'TOKENS': pers_pron}
        return result, debug


class L_US_PRON(Metric):
    category = Lexical
    name_en = "'Us' pronoun"

    def count(doc):
        pers_pron = [token for token in doc if token.lower_ == "us"]
        result = incidence(doc, pers_pron)
        debug = {'TOKENS': pers_pron}
        return result, debug


class L_THEM_PRON(Metric):
    category = Lexical
    name_en = "'Them' pronoun"

    def count(doc):
        pers_pron = [token for token in doc if token.lower_ == "them"]
        result = incidence(doc, pers_pron)
        debug = {'TOKENS': pers_pron}
        return result, debug


"""
POSSESSIVE PRONOUNS
"""

class L_MY_PRON(Metric):
    category = Lexical
    name_en = "'My' pronoun"

    def count(doc):
        pers_pron = [token for token in doc if token.lower_ == "my"]
        result = incidence(doc, pers_pron)
        debug = {'TOKENS': pers_pron}
        return result, debug


class L_YOUR_PRON(Metric):
    category = Lexical
    name_en = "'Your' pronoun"

    def count(doc):
        pers_pron = [token for token in doc if token.lower_ == "your"]
        result = incidence(doc, pers_pron)
        debug = {'TOKENS': pers_pron}
        return result, debug


class L_HIS_PRON(Metric):
    category = Lexical
    name_en = "'His' pronoun"

    def count(doc):
        pers_pron = [token for token in doc if token.lower_ == "his"]
        result = incidence(doc, pers_pron)
        debug = {'TOKENS': pers_pron}
        return result, debug


class L_HER_PRON(Metric):
    category = Lexical
    name_en = "'Her' possessive pronoun"

    def count(doc):
        pers_pron = [token for token in doc if token.lower_ == "her" and "Poss=Yes" in token.morph]
        result = incidence(doc, pers_pron)
        debug = {'TOKENS': pers_pron}
        return result, debug


class L_ITS_PRON(Metric):
    category = Lexical
    name_en = "'Its' possessive pronoun"

    def count(doc):
        pers_pron = [token for token in doc if token.lower_ == "its"]
        result = incidence(doc, pers_pron)
        debug = {'TOKENS': pers_pron}
        return result, debug


class L_OUR_PRON(Metric):
    category = Lexical
    name_en = "'Our' possessive pronoun"

    def count(doc):
        pers_pron = [token for token in doc if token.lower_ == "our"]
        result = incidence(doc, pers_pron)
        debug = {'TOKENS': pers_pron}
        return result, debug


class L_THEIR_PRON(Metric):
    category = Lexical
    name_en = "'Their' possessive pronoun"

    def count(doc):
        pers_pron = [token for token in doc if token.lower_ == "their"]
        result = incidence(doc, pers_pron)
        debug = {'TOKENS': pers_pron}
        return result, debug


class L_YOURS_PRON(Metric):
    category = Lexical
    name_en = "'Yours' pronoun"

    def count(doc):
        pers_pron = [token for token in doc if token.lower_ == "yours"]
        result = incidence(doc, pers_pron)
        debug = {'TOKENS': pers_pron}
        return result, debug


class L_THEIRS_PRON(Metric):
    category = Lexical
    name_en = "'Theirs' pronoun"

    def count(doc):
        pers_pron = [token for token in doc if token.lower_ == "theirs"]
        result = incidence(doc, pers_pron)
        debug = {'TOKENS': pers_pron}
        return result, debug


class L_HERS_PRON(Metric):
    category = Lexical
    name_en = "'Hers' pronoun"

    def count(doc):
        pers_pron = [token for token in doc if token.lower_ == "hers"]
        result = incidence(doc, pers_pron)
        debug = {'TOKENS': pers_pron}
        return result, debug


class L_OURS_PRON(Metric):
    category = Lexical
    name_en = "'Ours' possessive pronoun"

    def count(doc):
        pers_pron = [token for token in doc if token.lower_ == "ours"]
        result = incidence(doc, pers_pron)
        debug = {'TOKENS': pers_pron}
        return result, debug


"""
REFLEXIVE PRONOUNS
"""

class L_MYSELF_PRON(Metric):
    category = Lexical
    name_en = "'Myself' pronoun"

    def count(doc):
        pers_pron = [token for token in doc if token.lower_ == "myself"]
        result = incidence(doc, pers_pron)
        debug = {'TOKENS': pers_pron}
        return result, debug


class L_YOURSELF_PRON(Metric):
    category = Lexical
    name_en = "'Yourself' pronoun"

    def count(doc):
        pers_pron = [token for token in doc if token.lower_ == "yourself"]
        result = incidence(doc, pers_pron)
        debug = {'TOKENS': pers_pron}
        return result, debug


class L_HIMSELF_PRON(Metric):
    category = Lexical
    name_en = "'Himself' pronoun"

    def count(doc):
        pers_pron = [token for token in doc if token.lower_ == "himself"]
        result = incidence(doc, pers_pron)
        debug = {'TOKENS': pers_pron}
        return result, debug


class L_HERSELF_PRON(Metric):
    category = Lexical
    name_en = "'Herself' pronoun"

    def count(doc):
        pers_pron = [token for token in doc if token.lower_ == "herself"]
        result = incidence(doc, pers_pron)
        debug = {'TOKENS': pers_pron}
        return result, debug


class L_ITSELF_PRON(Metric):
    category = Lexical
    name_en = "'Itself' pronoun"

    def count(doc):
        pers_pron = [token for token in doc if token.lower_ == "itself"]
        result = incidence(doc, pers_pron)
        debug = {'TOKENS': pers_pron}
        return result, debug


class L_OURSELVES_PRON(Metric):
    category = Lexical
    name_en = "'Ourselves' pronoun"

    def count(doc):
        pers_pron = [token for token in doc if token.lower_ == "ourselves"]
        result = incidence(doc, pers_pron)
        debug = {'TOKENS': pers_pron}
        return result, debug

class L_YOURSELVES_PRON(Metric):
    category = Lexical
    name_en = "'Yourselves' pronoun"

    def count(doc):
        pers_pron = [token for token in doc if token.lower_ == "yourselves"]
        result = incidence(doc, pers_pron)
        debug = {'TOKENS': pers_pron}
        return result, debug


class L_THEMSELVES_PRON(Metric):
    category = Lexical
    name_en = "'Themselves' pronoun"

    def count(doc):
        pers_pron = [token for token in doc if token.lower_ == "themselves"]
        result = incidence(doc, pers_pron)
        debug = {'TOKENS': pers_pron}
        return result, debug


"""
POSSESSIVE NOUNS WITH 'S
"""

class L_POSSESSIVES(Metric):
    category = Lexical
    name_en = "Nouns in possessive case"
    
    def count(doc):
        pers_pron = [token for token in doc if token.pos_ == "PART" and token.dep_ == "case"]
        result = incidence(doc, pers_pron)
        debug = {'TOKENS': pers_pron}
        return result, debug
