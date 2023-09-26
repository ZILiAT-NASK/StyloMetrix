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


from ...structures import Category, Metric
from ...utils import incidence, log_incidence
import math

class Lexical(Category):
    lang = 'ru'
    name_en = "Lexical"


# ---------------------------
# GENERAL LEXICAL INFORMATION
# ---------------------------


class L_TYPE_TOKEN_RATIO_LEMMAS(Metric):
    category = Lexical
    name_en = "Type-token ratio for words lemmas"

    def count(doc):
        types = set(token.lemma_ for token in doc if token.pos_ not in ['PUNCT', 'X', 'SYM'])
        result = incidence(doc, types)
        return result, {}


class HERDAN_TTR(Metric):
    category = Lexical
    name_en = "Herdan's TTR"

    def count(doc):
        '''
        Function to calculate Herdan's TTR 
        param: doc - spacy doc object
        return: float - Herdan's TTR score
        '''
        # get types and tokens
        types = set([word.text for word in doc if word.is_alpha])
        tokens = [word.text for word in doc if word.is_alpha]

        # calculate Herdan's TTR
        return log_incidence(len(types), len(tokens)), {}


class MASS_TTR(Metric):
    category = Lexical
    name_en = "Mass TTR"

    def count(doc):
        '''
        Function to calculate Mass TTR 
        param: doc - spacy doc object
        return: float - Mass TTR score

        The TTR score that displays most stability with respect to the text length.
        '''
        # get types and tokens
        types = len(set([word.text for word in doc if word.is_alpha]))
        tokens = len([word.text for word in doc if word.is_alpha])
        try:
            if tokens > 0 and types > 0:
                return (math.log(tokens) - math.log(types)) / math.log2(tokens), {}
        except ZeroDivisionError:
            return 0.0, {}


class L_CONT_A(Metric):
    category = Lexical
    name_en = "Incidence of Content words"

    def count(doc):
        search = [token.text for token in doc if token.pos_ not in ['PUNCT', 'X', 'SYM'] and token._.is_content_word]
        result = incidence(doc, search)
        return result, {"CW": search}


class L_FUNC_A(Metric):
    category = Lexical
    name_en = "Incidence of Function words"

    def count(doc):
        search = [token.text for token in doc if token.pos_ not in ['PUNCT', 'X', 'SYM'] and token._.is_function_word]
        result = incidence(doc, search)
        return result, {"CW": search}


class L_CONT_T(Metric):
    category = Lexical
    name_en = "Incidence of Content words types"

    def count(doc):
        search = set(token.text for token in doc if token.pos_ not in ['PUNCT', 'X', 'SYM'] and token._.is_content_word)
        result = incidence(doc, search)
        return result, {}


class L_FUNC_T(Metric):
    category = Lexical
    name_en = "Incidence of Function words types"

    def count(doc):
        search = set(token.text for token in doc if token.pos_ not in ['PUNCT', 'X', 'SYM'] and token._.is_function_word)
        result = incidence(doc, search)
        return result, {}


# ---------------------------
# NOUNS
# ---------------------------

class L_PLURAL_NOUNS(Metric):
    category = Lexical
    name_en = "Incidence of nouns in plural"

    def count(doc):
        nouns_plural = [token for token in doc if token.pos_ == "NOUN" and "Number=Plur" in token.morph]
        result = incidence(doc, nouns_plural)
        return result, {}


class L_SINGULAR_NOUNS(Metric):
    category = Lexical
    name_en = "Incidence of nouns in singular"

    def count(doc):
        nouns_sing = [token for token in doc if token.pos_ == "NOUN" and "Number=Sing" in token.morph]
        result = incidence(doc, nouns_sing)
        return result, {}


class L_PROPER_NAME(Metric):
    category = Lexical
    name_en = "Incidence of proper names"

    def count(doc):
        ents = [token for token in doc if token.pos_ == "PROPN"]
        result = incidence(doc, ents)
        return result, {}


class L_PERSONAL_NAME(Metric):
    category = Lexical
    name_en = "Incidence of personal names"

    def count(doc):
        ents = [list(ent) for ent in doc.ents if ent.label_ == 'PER']
        sum_ents = sum(ents, [])
        result = incidence(doc, sum_ents)
        return result, {}

class L_ANIM_NOUN(Metric):
    category = Lexical
    name_en = "Incidence of animate nouns"

    def count(doc):
        nouns = [token for token in doc if token.pos_ == 'NOUN' and "Animacy=Anim" in token.morph]
        result = incidence(doc, nouns)
        return result, {}


class L_INANIM_NOUN(Metric):
    category = Lexical
    name_en = "Incidence of inanimate nouns"
    
    def count(doc):
        nouns = [token for token in doc if token.pos_ == 'NOUN' and "Animacy=Inan" in token.morph]
        result = incidence(doc, nouns)
        return result, {}


class L_NOUN_NEUTRAL(Metric):
    category = Lexical
    name_en = "Incidence of neutral nouns"

    def count(doc):
        nouns = [token for token in doc if token.pos_ == 'NOUN' and "Gender=Neut" in token.morph]
        result = incidence(doc, nouns)
        return result, {}


class L_NOUN_FAMININE(Metric):
    category = Lexical
    name_en = "Incidence of feminine nouns"

    def count(doc):
        nouns = [token for token in doc if token.pos_ == 'NOUN' and "Gender=Fem" in token.morph]
        result = incidence(doc, nouns)
        return result, {}


class L_NOUN_MASCULINE(Metric):
    category = Lexical
    name_en = "Incidence of masculine nouns"

    def count(doc):
        nouns = [token for token in doc if token.pos_ == 'NOUN' and "Gender=Masc" in token.morph]
        result = incidence(doc, nouns)
        return result, {}


class L_FEMININE_NAMES(Metric):
    category = Lexical
    name_en = "Incidence of feminine proper nouns"

    def count(doc):
        nouns = [token for token in doc if token.pos_ == "PROPN" and ("Animacy=Anim" in token.morph and "Gender=Fem" in token.morph)]
        result = incidence(doc, nouns)
        return result, {}


class L_MASCULINE_NAMES(Metric):
    category = Lexical
    name_en = "Incidence of masculine proper nouns"

    def count(doc):
        nouns = [token for token in doc if token.pos_ == "PROPN" and ("Animacy=Anim" in token.morph and "Gender=Masc" in token.morph)]
        result = incidence(doc, nouns)
        return result, {}


class L_SURNAMES(Metric):
    category = Lexical
    name_en = "Incidence of surnames"

    def count(doc):
        names = [token for token in doc if token.pos_ == "PROPN" and "NameType=Sur" in token.morph]
        result = incidence(doc, names)
        return result, {}


class L_GIVEN_NAMES(Metric):
    category = Lexical
    name_en = "Incidence of given names"

    def count(doc):
        names = [token for token in doc if token.pos_ == "PROPN" and "NameType=Giv" in token.morph]
        result = incidence(doc, names)
        return result, {}


class L_DIRECT_OBJ(Metric):
    category = Lexical
    name_en = "Incidence of direct objects"

    def count(doc):
        obj = [token for token in doc if token.dep_ == "obj"]
        result = incidence(doc, obj)
        return result, {}


class L_INDIRECT_OBJ(Metric):
    category = Lexical
    name_en = "Incidence of indirect objects"

    def count(doc):
        iobj = [token for token in doc if token.dep_ == "iobj" or token.dep_ == "obl"]
        result = incidence(doc, iobj)
        return result, {}


# ---------------------------
# NOUN CASES
# ---------------------------


class L_NOM_CASE(Metric):
    category = Lexical
    name_en = "Incidence of nouns in Nominative case"

    def count(doc):
        nouns = [token.text for token in doc if token.pos_ == "NOUN" and "Case=Nom" in token.morph]
        result = incidence(doc, nouns)
        return result, {}


class L_GEN_CASE(Metric):
    category = Lexical
    name_en = "Incidence of nouns in Genitive case"

    def count(doc):
        nouns = [token.text for token in doc if token.pos_ == "NOUN" and "Case=Gen" in token.morph]
        result = incidence(doc, nouns)
        return result, {}


class L_DAT_CASE(Metric):
    category = Lexical
    name_en = "Incidence of nouns in Dative case"

    def count(doc):
        nouns = [token.text for token in doc if token.pos_ == "NOUN" and "Case=Dat" in token.morph]
        result = incidence(doc, nouns)
        return result, {}


class L_ACC_CASE(Metric):
    category = Lexical
    name_en = "Incidence of nouns in Accusative case"

    def count(doc):
        nouns = [token.text for token in doc if token.pos_ == "NOUN" and "Case=Acc" in token.morph]
        result = incidence(doc, nouns)
        return result, {}


class L_INS_CASE(Metric):
    category = Lexical
    name_en = "Incidence of nouns in Instrumental case"

    def count(doc):
        nouns = [token.text for token in doc if token.pos_ == "NOUN" and "Case=ins" in token.morph]
        result = incidence(doc, nouns)
        return result, {}


class L_LOC_CASE(Metric):
    category = Lexical
    name_en = "Incidence of nouns in Locative case"

    def count(doc):
        nouns = [token.text for token in doc if token.pos_ == "NOUN" and "Case=Loc" in token.morph]
        result = incidence(doc, nouns)
        return result, {}



# ---------------------------
# ADJECTIVES 
# ---------------------------


class L_QULITATIVE_ADJ_P(Metric):
    category = Lexical
    name_en = "Incidence of qualitative adj positive"

    def count(doc):
        adj = [adj for adj in doc if adj.pos_ == "ADJ" 
        and "Degree=Pos" in adj.morph]
        result = incidence(doc, adj)
        return result, {}


class L_RELATIVE_ADJ(Metric):
    category = Lexical
    name_en = "Incidence of relative adj"

    def count(doc):
        degrees = ["Degree=Pos", "Degree=Cmp", "Degree=Sup"]
        adj = [adj for adj in doc if adj.pos_ == "ADJ" 
        and not any(adj for i in degrees if i in adj.morph)]
        result = incidence(doc, adj)
        return result, {}


class L_QUALITATIVE_ADJ_CMP(Metric):
    category = Lexical
    name_en = "Incidence of relative adj"

    def count(doc):
        adj = [adj for adj in doc if adj.pos_ == "ADJ" and "Degree=Cmp" in adj.morph]
        result = incidence(doc, adj)
        return result, {}


class L_QUALITATIVE_ADJ_SUP(Metric):
    category = Lexical
    name_en = "Incidence of qualitative superlative adj"

    def count(doc):
        adj = [adj for adj in doc if adj.pos_ == "ADJ" and "Degree=Sup" in adj.morph]
        result = incidence(doc, adj)
        return result, {}


class L_DIRECT_ADJ(Metric):
    category = Lexical
    name_en = "Incidence of direct adjective"

    def count(doc):
        adj = []
        direct = [adj for adj in doc if adj.pos_ == "ADJ" and adj.dep_ == "amod"]
        conj = [token for token in doc if token.pos_ == "ADJ" and token.dep_ == "conj" and token.head.dep_ == "amod"]
        adj = direct + conj
        result = incidence(doc, adj)
        return result, {}


class L_INDIRECT_ADJ(Metric):
    category = Lexical
    name_en = "Incidence of indirect adjective"

    def count(doc):
        adj = []
        indirect = [adj for adj in doc if adj.pos_ == "ADJ" and (adj.dep_ != "amod" and adj.dep_ != "conj")]
        conj = [token for token in doc if token.dep_ == "conj" and (token.head.dep_ != "amod" and token.head.pos_ == "ADJ")]
        adj = indirect + conj
        result = incidence(doc, adj)
        return result, {}


# ---------------------------
# PUNCTUATION
# ---------------------------


class L_PUNCT(Metric):
    category = Lexical
    name_en = "Incidence of punctuation"

    def count(doc):
        ents = [token for token in doc if token.pos_ == "PUNCT"]
        result = incidence(doc, ents)
        return result, {}


class L_PUNCT_DOT(Metric):
    category = Lexical
    name_en = "Incidence of dots"

    def count(doc):
        ents = [token for token in doc if token.text == "."]
        result = incidence(doc, ents)
        return result, {}


class L_PUNCT_COM(Metric):
    category = Lexical
    name_en = "Incidence of comma"

    def count(doc):
        ents = [token for token in doc if token.text == ","]
        result = incidence(doc, ents)
        return result, {}


class L_PUNCT_SEMC(Metric):
    category = Lexical
    name_en = "Incidence of semicolon"

    def count(doc):
        ents = [token for token in doc if token.text == ";"]
        result = incidence(doc, ents)
        return result, {}


class L_PUNCT_COL(Metric):
    category = Lexical
    name_en = "Incidence of colon"

    def count(doc):
        ents = [token for token in doc if token.text == ":"]
        result = incidence(doc, ents)
        return result, {}


class L_PUNCT_DASH(Metric):
    category = Lexical
    name_en = "Incidence of dashes"

    def count(doc):
        ents = [token for token in doc if token.text == "—"]
        result = incidence(doc, ents)
        return result, {}

# NUMERALS

class L_NUM_CARD(Metric):
    category = Lexical
    name_en = "Incidence of numerals cardinals"

    def count(doc):
        tokens = [token for token in doc if "NumType=Card" in token.morph]
        result = incidence(doc, tokens)
        return result, {}


class L_NUM_ORD(Metric):
    category = Lexical
    name_en = "Incidence of numerals ordinals"

    def count(doc):
        tokens = [token for token in doc if "NumType=Ord" in token.morph]
        result = incidence(doc, tokens)
        return result, {}

# PRONOUNS

class L_PRON_DEM(Metric):
    category = Lexical
    name_en = "Incidence of demonstrative pronouns"

    def count(doc):
        tokens = [token for token in doc if "PronType=Dem" in token.morph]
        result = incidence(doc, tokens)
        return result, {}


class L_PRON_PRS(Metric):
    category = Lexical
    name_en = "Incidence of personal pronouns"

    def count(doc):
        tokens = [token for token in doc if "PronType=Prs" in token.morph]
        result = incidence(doc, tokens)
        return result, {}


class L_PRON_TOT(Metric):
    category = Lexical
    name_en = "Incidence of total pronouns"

    def count(doc):
        tokens = [token for token in doc if "PronType=Tot" in token.morph]
        result = incidence(doc, tokens)
        return result, {}


class L_PRON_REL(Metric):
    category = Lexical
    name_en = "Incidence of relative pronouns"

    def count(doc):
        tokens = [token for token in doc if "PronType=Rel" in token.morph]
        result = incidence(doc, tokens)
        return result, {}


class L_PRON_INT(Metric):
    category = Lexical
    name_en = "Incidence of indexical pronouns"

    def count(doc):
        tokens = [token for token in doc if "PronType=Int" in token.morph]
        result = incidence(doc, tokens)
        return result, {}


class L_PRON_RFL(Metric):
    category = Lexical
    name_en = "Incidence of reflexive pronoun"

    def count(doc):
        tokens = [token for token in doc if "Reflex=Yes" in token.morph and "PronType=Prs" in token.morph]
        result = incidence(doc, tokens)
        return result, {}



class L_PRON_POS(Metric):
    category = Lexical
    name_en = "Incidence of posessive pronoun"

    def count(doc):
        tokens = [token for token in doc if "Poss=Yes" in token.morph and "PronType=Prs" in token.morph]
        result = incidence(doc, tokens)
        return result, {}


class L_PRON_NEG(Metric):
    category = Lexical
    name_en = "Incidence of negative pronoun"

    def count(doc):
        tokens = [token for token in doc if "PronType=Neg" in token.morph]
        result = incidence(doc, tokens)
        return result, {}


# ADVERBS


class L_ADV_POS(Metric):
    category = Lexical
    name_en = "Incidence of positive adverbs"

    def count(doc):
        tokens = [token for token in doc if "Degree=Pos" in token.morph and token.pos_ == "ADV"]
        result = incidence(doc, tokens)
        return result, {}


class L_ADV_CMP(Metric):
    category = Lexical
    name_en = "Incidence of comparative adverbs"

    def count(doc):
        tokens = [token for token in doc if "Degree=Cmp" in token.morph and token.pos_ == "ADV"]
        result = incidence(doc, tokens)
        return result, {}


class L_ADV_SUP(Metric):
    category = Lexical
    name_en = "Incidence of superlative adverbs"

    def count(doc):
        tokens = [token for token in doc if "Degree=Sup" in token.morph and token.pos_ == "ADV"]
        result = incidence(doc, tokens)
        return result, {}
