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


from ...structures import Metric, Category
from ...utils import incidence, log_incidence, ratio
import math 
import regex as re
from spacy_syllables import SpacySyllables
LW_CAUSE_PURPOSE = """in the event that, granted that, provided that, in case, in the event, as long as, for the purpose of, with the intention, with this in mind, in the hope that, to the end that, for fear that, in order to, seeing, being that, in view of, whenever, lest, in case, privided that, given that, only, even if, so that, so as to, owing to, due to, inasmuch as""".strip().split(", ")

class Lexical(Category):
    lang = 'en'
    name_en = "Lexical"
        

class L_REF(Metric):
    category = Lexical
    name_en = "References"

    def count(doc):
        search = [token.text for token in doc if token.text.startswith('@')]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_HASHTAG(Metric):
    category = Lexical
    name_en = "Hashtags"

    def count(doc):
        search = re.findall(r'#\w+', doc.text)
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug
    
class L_MENTION(Metric):
    category = Lexical
    name_en = "Mentions"

    def count(doc):
        search = [token.text for token in doc if token.text.startswith('@') and len(token.text) > 1]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug

class L_RT(Metric):
    category = Lexical
    name_en = "Retweets"

    def count(doc):
        search = [token.text for token in doc if token.text == "RT" or token.text == "rt"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug
    

class L_LINKS(Metric):
    category = Lexical
    name_en = "Links"

    def count(doc):
        expr = r"\w+\.\w+.com\/.*"
        search = re.findall(r'https?://[^\s\n\r]+', doc.text) + re.findall(expr, doc.text)
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug
    

class L_CONT_A(Metric):
    category = Lexical
    name_en = "Content words"

    def count(doc):
        search = [token.text for token in doc if token._.is_content_word and token.is_alpha]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_FUNC_A(Metric):
    category = Lexical
    name_en = "Function words"

    def count(doc):
        search = [token.text for token in doc if token._.is_function_word]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug

class L_CONT_T(Metric):
    category = Lexical
    name_en = "Content words types"

    def count(doc):
        search = set(token.text for token in doc if token._.is_content_word and token.is_alpha)
        result = ratio(len(search), len(doc.text.split()))
        return result, {}


class L_FUNC_T(Metric):
    category = Lexical
    name_en = "Function words types"

    def count(doc):
        search = set(token.text for token in doc if token._.is_function_word)
        result = ratio(len(search), len(doc.text.split()))
        return result, {}


"""NOUNS"""

class L_PLURAL_NOUNS(Metric):
    category = Lexical
    name_en = "Nouns in plural"

    def count(doc):
        search = [token for token in doc if token.pos_ == "NOUN" and "Number=Plur" in token.morph]
        result =  ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_SINGULAR_NOUNS(Metric):
    category = Lexical
    name_en = "Nouns in singular"

    def count(doc):
        search = [token for token in doc if token.pos_ == "NOUN" and "Number=Sing" in token.morph]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_PROPER_NAME(Metric):
    category = Lexical
    name_en = "Proper names"

    def count(doc):
        search = [token for token in doc if token.pos_ == "PROPN"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_PERSONAL_NAME(Metric):
    category = Lexical
    name_en = "Personal names"

    def count(doc):
        ents = [list(ent) for ent in doc.ents if ent.label_ == 'PERSON']
        search = sum(ents, [])
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_NOUN_PHRASES(Metric):
    category = Lexical
    name_en = "Incidence of noun phrases"

    def count(doc):
        phrases = [noun_phrase for noun_phrase in doc.noun_chunks]
        search = [noun for phrase in phrases for noun in phrase]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


"""PUNCTUATION"""


class L_PUNCT(Metric):
    category = Lexical
    name_en = "Punctuation"

    def count(doc):
        search = [token for token in doc if token.pos_ == "PUNCT"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_PUNCT_DOT(Metric):
    category = Lexical
    name_en = "Punctuation - dots"

    def count(doc):
        search = [token for token in doc if token.text == "."]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_PUNCT_COM(Metric):
    category = Lexical
    name_en = "Punctuation - comma"

    def count(doc):
        search = [token for token in doc if token.text == ","]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_PUNCT_SEMC(Metric):
    category = Lexical
    name_en = "Punctuation - semicolon"

    def count(doc):
        search = [token for token in doc if token.text == ";"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_PUNCT_COL(Metric):
    category = Lexical
    name_en = "Punctuation - colon"

    def count(doc):
        search = [token for token in doc if token.text == ":"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_PUNCT_DASH(Metric):
    category = Lexical
    name_en = "Punctuation - dashes"

    def count(doc):
        search = [token for token in doc if token.text == "—"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


"""
POSSESSIVE NOUNS WITH 'S
"""

class L_POSSESSIVES(Metric):
    category = Lexical
    name_en = "Nouns in possessive case"
    
    def count(doc):
        search = [token for token in doc if token.pos_ == "PART" and token.dep_ == "case"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


"""
ADJECTIVES & ADVERBS DEGREES OF COMPARISON
"""

class L_ADJ_POSITIVE(Metric):
    category = Lexical
    name_en = "Adjectives in positive degree"

    def count(doc):
        search = [token for token in doc if token.pos_ == "ADJ" and "Degree=Pos" in token.morph and token.tag_ == "JJ"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_ADJ_COMPARATIVE(Metric):
    category = Lexical
    name_en = "Adjectives in comparative degree"

    def count(doc):
        search = [token for token in doc if (token.pos_ == "ADJ" or token.pos_ == "ADV") and ("Degree=Cmp" in token.morph or token.dep_ == "acomp") and (token.tag_ == "JJ" or token.tag_ == "RBR" or token.tag_ == "JJR")]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_ADJ_SUPERLATIVE(Metric):
    category = Lexical
    name_en = "Adjectives in superlative degree"

    def count(doc):
        search = [token for token in doc if (token.pos_ == "ADJ" or token.pos_ == "ADV") and "Degree=Sup" in token.morph and (token.tag_ == "JJS" or token.tag_ == "RBS")]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_ADV_POSITIVE(Metric):
    category = Lexical
    name_en = "Adverbs in positive degree"

    def count(doc):
        search = [token for token in doc if token._.adverbs == "positive_adverb"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_ADV_COMPARATIVE(Metric):
    category = Lexical
    name_en = "Adverbs in comparative degree"

    def count(doc):
        search = [token for token in doc if token.pos_ == "ADV" and ("Degree=Cmp" in token.morph or token.tag_ == "RB") and token.dep_ == "advmod"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_ADV_SUPERLATIVE(Metric):
    category = Lexical
    name_en = "Adverbs in superlative degree"

    def count(doc):
        search = search = [token for token in doc if (token.pos_ == "ADJ" or token.pos_ == "ADV") and (token.tag_ == "RB" or "Degree=Sup" in token.morph) and (token.dep_ == "advmod" or token.dep_ == "attr")]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug

"""
Lexical
"""
class PS_CONTRADICTION(Metric):
    category = Lexical
    name_en = "Opposition, limitation, contradiction"

    def count(doc):
        search = [token.text for token in doc if token._.linking_words == "contradiction"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug

class PS_AGREEMENT(Metric):
    category = Lexical
    name_en = "Agreement, similarity"

    def count(doc):
        search = [token.text for token in doc if token._.linking_words == "agreement"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug

class PS_EXAMPLES(Metric):
    category = Lexical
    name_en = "Examples, emphasis"

    def count(doc):
        search = [token.text for token in doc if token._.linking_words == "examples"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug

class PS_CONSEQUENCE(Metric):
    category = Lexical
    name_en = "Consequence, result"

    def count(doc):
        search = [token.text for token in doc if token._.linking_words == "cosequence"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug

class PS_CAUSE(Metric):
    category = Lexical
    name_en = "Cause, purpose"

    def count(doc):
        words = [word.split() for word in LW_CAUSE_PURPOSE]
        search = [token for token in doc for word in words if token.text.lower() in word]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug

class PS_LOCATION(Metric):
    category = Lexical
    name_en = "Location, space"

    def count(doc):
        search = [token.text for token in doc if token._.linking_words == "space"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug
    
class PS_TIME(Metric):
    category = Lexical
    name_en = "Time"

    def count(doc):
        search = [token.text for token in doc if token._.linking_words == "time"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug

class PS_CONDITION(Metric):
    category = Lexical
    name_en = "Condition, hypothesis"

    def count(doc):
        search = [token.text for token in doc if token._.linking_words == "condition"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug

class PS_MANNER(Metric):
    category = Lexical
    name_en = "Manner"

    def count(doc):
        search = [token.text for token in doc if token._.linking_words == "manner"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug