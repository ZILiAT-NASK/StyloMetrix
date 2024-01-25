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
from ...utils import incidence, log_incidence, ratio
import math

class Lexical(Category):
    lang = 'ukr'
    name_en = "Lexical"


# ---------------------------
# GENERAL LEXICAL INFORMATION
# ---------------------------


class L_TYPE_TOKEN_RATIO_LEMMAS(Metric):
    category = Lexical
    name_en = "Type-token ratio for words lemmas"

    def count(doc):
        search = set(token.lemma_ for token in doc if token.is_alpha)
        result = ratio(len(search), len(doc.text.split()))
        debug = {"TOKENS": search}
        return result, debug


# class HERDAN_TTR(Metric):
#     category = Lexical
#     name_en = "Herdan's TTR"

#     def count(doc):
#         '''
#         Function to calculate Herdan's TTR for the Ukrainian language
#         param: doc - spacy doc object
#         return: float - Herdan's TTR score
#         '''
#         # get types and tokens
#         types = set([word.text for word in doc if word.is_alpha])
#         tokens = [word.text for word in doc if word.is_alpha]
#         calculation = log_incidence(len(types), len(tokens))
#         # calculate Herdan's TTR
#         return calculation, {}


# class MASS_TTR(Metric):
#     category = Lexical
#     name_en = "Mass TTR"

#     def count(doc):
#         '''
#         Function to calculate Mass TTR for the Ukrainian language
#         param: doc - spacy doc object
#         return: float - Mass TTR score

#         The TTR score that displays most stability with respect to the text length.
#         '''
#         # get types and tokens
#         types = len(set([word.text for word in doc if word.is_alpha]))
#         tokens = len([word.text for word in doc if word.is_alpha])
#         try:
#             if tokens > 0 and types > 0:
#                 calculation = (math.log(tokens) - math.log(types)) / math.log2(tokens)
#                 return calculation, {}
#         except ZeroDivisionError:
#             return 0.0, {}

class L_CONT_A(Metric):
    category = Lexical
    name_en = "Incidence of Content words"

    def count(doc):
        search = [token.text for token in doc if token._.is_content_word]
        result = ratio(len(search), len(doc.text.split()))
        debug = {"TOKENS": search}
        return result, debug


class L_FUNC_A(Metric):
    category = Lexical
    name_en = "Incidence of Function words"

    def count(doc):
        search = [token.text for token in doc if token._.is_function_word]
        result = ratio(len(search), len(doc.text.split()))
        debug = {"TOKENS": search}
        return result, debug


class L_CONT_T(Metric):
    category = Lexical
    name_en = "Incidence of Content words types"

    def count(doc):
        search = set(token.text for token in doc if token._.is_content_word)
        result = ratio(len(search), len(doc.text.split()))
        debug = {"TOKENS": search}
        return result, debug


class L_FUNC_T(Metric):
    category = Lexical
    name_en = "Incidence of Function words types"

    def count(doc):
        search = set(token.text for token in doc if token._.is_function_word)
        result = ratio(len(search), len(doc.text.split()))
        debug = {"TOKENS": search}
        return result, debug


# ---------------------------
# NOUNS
# ---------------------------

class L_PLURAL_NOUNS(Metric):
    category = Lexical
    name_en = "Incidence of nouns in plural"

    def count(doc):
        nouns_plural = [token.text for token in doc if token.pos_ == "NOUN" and "Number=Plur" in token.morph]
        result = ratio(len(nouns_plural), len(doc.text.split()))
        debug = {"TOKENS": nouns_plural}
        return result, debug


class L_SINGULAR_NOUNS(Metric):
    category = Lexical
    name_en = "Incidence of nouns in singular"

    def count(doc):
        nouns_sing = [token.text for token in doc if token.pos_ == "NOUN" and "Number=Sing" in token.morph]
        result = ratio(len(nouns_sing), len(doc.text.split()))
        debug = {"TOKENS": nouns_sing}
        return result, debug


class L_PROPER_NAME(Metric):
    category = Lexical
    name_en = "Incidence of proper names"

    def count(doc):
        ents = [token.text for token in doc if token.pos_ == "PROPN"]
        result = ratio(len(ents), len(doc.text.split()))
        debug = {"TOKENS": ents}
        return result, debug


class L_PERSONAL_NAME(Metric):
    category = Lexical
    name_en = "Incidence of personal names"

    def count(doc):
        ents = [ent.text for ent in doc.ents if ent.label_ == 'PER']
        result = ratio(len(ents), len(doc.text.split()))
        debug = {"TOKENS": ents}
        return result, debug

class L_ANIM_NOUN(Metric):
    category = Lexical
    name_en = "Incidence of animate nouns"

    def count(doc):
        nouns = [token.text for token in doc if token.pos_ == 'NOUN' and "Animacy=Anim" in token.morph]
        result = ratio(len(nouns), len(doc.text.split()))
        debug = {"TOKENS": nouns}
        return result, debug


class L_INANIM_NOUN(Metric):
    category = Lexical
    name_en = "Incidence of inanimate nouns"
    
    def count(doc):
        nouns = [token.text for token in doc if token.pos_ == 'NOUN' and "Animacy=Inan" in token.morph]
        result = ratio(len(nouns), len(doc.text.split()))
        debug = {"TOKENS": nouns}
        return result, debug


class L_NOUN_NEUTRAL(Metric):
    category = Lexical
    name_en = "Incidence of neutral nouns"

    def count(doc):
        nouns = [token.text for token in doc if token.pos_ == 'NOUN' and "Gender=Neut" in token.morph]
        result =  ratio(len(nouns), len(doc.text.split()))
        debug = {"TOKENS": nouns}
        return result, debug


class L_NOUN_FAMININE(Metric):
    category = Lexical
    name_en = "Incidence of feminine nouns"

    def count(doc):
        nouns = [token.text for token in doc if token.pos_ == 'NOUN' and "Gender=Fem" in token.morph]
        result = ratio(len(nouns), len(doc.text.split()))
        debug = {"TOKENS": nouns}
        return result, debug


class L_NOUN_MASCULINE(Metric):
    category = Lexical
    name_en = "Incidence of masculine nouns"

    def count(doc):
        nouns = [token.text for token in doc if token.pos_ == 'NOUN' and "Gender=Masc" in token.morph]
        result = ratio(len(nouns), len(doc.text.split()))
        debug = {"TOKENS": nouns}
        return result, debug


class L_FEMININE_NAMES(Metric):
    category = Lexical
    name_en = "Incidence of feminine proper nouns"

    def count(doc):
        nouns = [token.text for token in doc if token.pos_ == "PROPN" and ("Animacy=Anim" in token.morph and "Gender=Fem" in token.morph)]
        result =  ratio(len(nouns), len(doc.text.split()))
        debug = {"TOKENS": nouns}
        return result, debug


class L_MASCULINE_NAMES(Metric):
    category = Lexical
    name_en = "Incidence of masculine proper nouns"

    def count(doc):
        nouns = [token.text for token in doc if token.pos_ == "PROPN" and ("Animacy=Anim" in token.morph and "Gender=Masc" in token.morph)]
        result = ratio(len(nouns), len(doc.text.split()))
        debug = {"TOKENS": nouns}
        return result, debug


class L_SURNAMES(Metric):
    category = Lexical
    name_en = "Incidence of surnames"

    def count(doc):
        names = [token.text for token in doc if token.pos_ == "PROPN" and "NameType=Sur" in token.morph]
        result = ratio(len(names), len(doc.text.split()))
        debug = {"TOKENS": names}
        return result, debug


class L_GIVEN_NAMES(Metric):
    category = Lexical
    name_en = "Incidence of given names"

    def count(doc):
        names = [token.text for token in doc if token.pos_ == "PROPN" and "NameType=Giv" in token.morph]
        result = ratio(len(names), len(doc.text.split()))
        debug = {"TOKENS": names}
        return result, debug


# https://universaldependencies.org/u/dep/flat.html

class L_FLAT_MULTIWORD(Metric):
    category = Lexical
    name_en = "Incidence of flat multiwords expressions"

    def count(doc):
        flat = [[token.head.text, token.text] for token in doc if "flat" in token.dep_]
        flatten = [token for i in flat for token in i]
        result =  ratio(len(flatten), len(doc.text.split()))
        debug = {"TOKENS": flatten}
        return result, debug


class L_DIMINUTIVES(Metric):
    category = Lexical
    name_en = "Incidence of diminutives"

    def count(doc):
        suffixes = ["еньк", "есеньк", "ісіньк", "юсіньк"]
        dimin = [token.text for token in doc if any(token for i in suffixes if i in token.text)]
        result =  ratio(len(dimin), len(doc.text.split()))
        debug = {"TOKENS": dimin}
        return result, debug


class L_DIRECT_OBJ(Metric):
    category = Lexical
    name_en = "Incidence of direct objects"

    def count(doc):
        obj = [token.text for token in doc if token.dep_ == "obj"]
        result =  ratio(len(obj), len(doc.text.split()))
        debug = {"TOKENS": obj}
        return result, debug


class L_INDIRECT_OBJ(Metric):
    category = Lexical
    name_en = "Incidence of indirect objects"

    def count(doc):
        iobj = [token.text for token in doc if token.dep_ == "iobj" or token.dep_ == "obl"]
        result = ratio(len(iobj), len(doc.text.split()))
        debug = {"TOKENS": iobj}
        return result, debug


# ---------------------------
# NOUN CASES
# ---------------------------


class L_NOM_CASE(Metric):
    category = Lexical
    name_en = "Incidence of nouns in Nominative case"

    def count(doc):
        nouns = [token.text for token in doc if token.pos_ == "NOUN" and "Case=Nom" in token.morph]
        result =  ratio(len(nouns), len(doc.text.split()))
        debug = {"TOKENS": nouns}
        return result, debug


class L_GEN_CASE(Metric):
    category = Lexical
    name_en = "Incidence of nouns in Genitive case"

    def count(doc):
        nouns = [token.text for token in doc if token.pos_ == "NOUN" and "Case=Gen" in token.morph]
        result =  ratio(len(nouns), len(doc.text.split()))
        debug = {"TOKENS": nouns}
        return result, debug


class L_DAT_CASE(Metric):
    category = Lexical
    name_en = "Incidence of nouns in Dative case"

    def count(doc):
        nouns = [token.text for token in doc if token.pos_ == "NOUN" and "Case=Dat" in token.morph]
        result =  ratio(len(nouns), len(doc.text.split()))
        debug = {"TOKENS": nouns}
        return result, debug


class L_ACC_CASE(Metric):
    category = Lexical
    name_en = "Incidence of nouns in Accusative case"

    def count(doc):
        nouns = [token.text for token in doc if token.pos_ == "NOUN" and "Case=Acc" in token.morph]
        result = ratio(len(nouns), len(doc.text.split()))
        debug = {"TOKENS": nouns}
        return result, debug


class L_INS_CASE(Metric):
    category = Lexical
    name_en = "Incidence of nouns in Instrumental case"

    def count(doc):
        nouns = [token.text for token in doc if token.pos_ == "NOUN" and "Case=Ins" in token.morph]
        result = ratio(len(nouns), len(doc.text.split()))
        debug = {"TOKENS": nouns}
        return result, debug


class L_LOC_CASE(Metric):
    category = Lexical
    name_en = "Incidence of nouns in Locative case"

    def count(doc):
        nouns = [token.text for token in doc if token.pos_ == "NOUN" and "Case=Loc" in token.morph]
        result = ratio(len(nouns), len(doc.text.split()))
        debug = {"TOKENS": nouns}
        return result, debug

class L_VOC_CASE(Metric):
    category = Lexical
    name_en = "Incidence of nouns in Vocative case"

    def count(doc):
        nouns = [token.text for token in doc if (token.pos_ == "NOUN" or token.pos_ == "PROPN") 
        and "Case=Voc" in token.morph]
        result = ratio(len(nouns), len(doc.text.split()))
        debug = {"TOKENS": nouns}
        return result, debug


# ---------------------------
# ADJECTIVES 
# ---------------------------


class L_QULITATIVE_ADJ_P(Metric):
    category = Lexical
    name_en = "Incidence of qualitative adj positive"

    def count(doc):
        adj = [adj.text for adj in doc if adj.pos_ == "ADJ" and "Degree=Pos" in adj.morph]
        result = ratio(len(adj), len(doc.text.split()))
        debug = {"TOKENS": adj}
        return result, debug


class L_RELATIVE_ADJ(Metric):
    category = Lexical
    name_en = "Incidence of relative adj"

    def count(doc):
        degrees = ["Degree=Pos", "Degree=Cmp", "Degree=Sup"]
        adj = [adj.text for adj in doc if adj.pos_ == "ADJ" 
        and not any(adj for i in degrees if i in adj.morph)]
        result = ratio(len(adj), len(doc.text.split()))
        debug = {"TOKENS": adj}
        return result, debug


class L_QUALITATIVE_ADJ_CMP(Metric):
    category = Lexical
    name_en = "Incidence of qualitative comparative adj"

    def count(doc):
        adj = [adj.text for adj in doc if adj.pos_ == "ADJ" and "Degree=Cmp" in adj.morph]
        result =  ratio(len(adj), len(doc.text.split()))
        debug  = {"TOKENS": adj}
        return result, debug


class L_QUALITATIVE_ADJ_SUP(Metric):
    category = Lexical
    name_en = "Incidence of qualitative superlative adj"

    def count(doc):
        adj = [adj.text for adj in doc if adj.pos_ == "ADJ" and "Degree=Sup" in adj.morph]
        result = ratio(len(adj), len(doc.text.split()))
        debug = {"TOKENS": adj}
        return result, debug


class L_DIRECT_ADJ(Metric):
    category = Lexical
    name_en = "Incidence of direct adjective"

    def count(doc):
        adj = []
        direct = [adj.text for adj in doc if adj.pos_ == "ADJ" and adj.dep_ == "amod"]
        conj = [token.text for token in doc if token.pos_ == "ADJ" and token.dep_ == "conj" and token.head.dep_ == "amod"]
        adj = direct + conj
        result = ratio(len(adj), len(doc.text.split()))
        debug = {"TOKENS": adj}
        return result, debug


class L_INDIRECT_ADJ(Metric):
    category = Lexical
    name_en = "Incidence of indirect adjective"

    def count(doc):
        adj = []
        indirect = [adj.text for adj in doc if adj.pos_ == "ADJ" and (adj.dep_ != "amod" and adj.dep_ != "conj")]
        conj = [token.text for token in doc if token.dep_ == "conj" and (token.head.dep_ != "amod" and token.head.pos_ == "ADJ")]
        adj = indirect + conj
        result = ratio(len(adj), len(doc.text.split()))
        debug = {"TOKENS": adj}
        return result, debug


# ---------------------------
# PUNCTUATION
# ---------------------------


class L_PUNCT(Metric):
    category = Lexical
    name_en = "Incidence of punctuation"

    def count(doc):
        ents = [token.text for token in doc if token.pos_ == "PUNCT"]
        result = ratio(len(ents), len(doc.text.split()))
        debug = {"TOKENS": ents}
        return result, debug


class L_PUNCT_DOT(Metric):
    category = Lexical
    name_en = "Incidence of dots"

    def count(doc):
        ents = [token.text for token in doc if token.text == "."]
        result = ratio(len(ents), len(doc.text.split()))
        debug = {"TOKENS": ents}
        return result, debug


class L_PUNCT_COM(Metric):
    category = Lexical
    name_en = "Incidence of comma"

    def count(doc):
        ents = [token.text for token in doc if token.text == ","]
        result = ratio(len(ents), len(doc.text.split()))
        debug = {"TOKENS": ents}
        return result, debug


class L_PUNCT_SEMC(Metric):
    category = Lexical
    name_en = "Incidence of semicolon"

    def count(doc):
        ents = [token.text for token in doc if token.text == ";"]
        result = ratio(len(ents), len(doc.text.split()))
        debug = {"TOKENS": ents}
        return result, debug


class L_PUNCT_COL(Metric):
    category = Lexical
    name_en = "Incidence of colon"

    def count(doc):
        ents = [token.text for token in doc if token.text == ":"]
        result = ratio(len(ents), len(doc.text.split()))
        debug = {"TOKENS": ents}
        return result, debug


class L_PUNCT_DASH(Metric):
    category = Lexical
    name_en = "Incidence of dashes"

    def count(doc):
        ents = [token.text for token in doc if token.text == "—"]
        result = ratio(len(ents), len(doc.text.split()))
        debug = {"TOKENS": ents}
        return result, debug
# ---------------------------
# NUMERALS
# ---------------------------
class L_NUM_CARD(Metric):
    category = Lexical
    name_en = "Incidence of numerals cardinals"

    def count(doc):
        tokens = [token.text for token in doc if "NumType=Card" in token.morph]
        result = ratio(len(tokens), len(doc.text.split()))
        debug = {"TOKENS": tokens}
        return result, debug


class L_NUM_ORD(Metric):
    category = Lexical
    name_en = "Incidence of numerals ordinals"

    def count(doc):
        tokens = [token.text for token in doc if "NumType=Ord" in token.morph]
        result = ratio(len(tokens), len(doc.text.split()))
        debug = {"TOKENS": tokens}
        return result, debug
# ---------------------------
# PRONOUNS
# ---------------------------
class L_PRON_DEM(Metric):
    category = Lexical
    name_en = "Incidence of demonstrative pronouns"

    def count(doc):
        tokens = [token.text for token in doc if "PronType=Dem" in token.morph]
        result = ratio(len(tokens), len(doc.text.split()))
        debug = {"TOKENS": tokens}
        return result, debug


class L_PRON_PRS(Metric):
    category = Lexical
    name_en = "Incidence of personal pronouns"

    def count(doc):
        tokens = [token.text for token in doc if "PronType=Prs" in token.morph]
        result = ratio(len(tokens), len(doc.text.split()))
        debug = {"TOKENS": tokens}
        return result, debug


class L_PRON_TOT(Metric):
    category = Lexical
    name_en = "Incidence of total pronouns"

    def count(doc):
        tokens = [token.text for token in doc if "PronType=Tot" in token.morph]
        result = ratio(len(tokens), len(doc.text.split()))
        debug = {"TOKENS": tokens}
        return result, debug


class L_PRON_REL(Metric):
    category = Lexical
    name_en = "Incidence of relative pronouns"

    def count(doc):
        tokens = [token.text for token in doc if "PronType=Rel" in token.morph]
        result = ratio(len(tokens), len(doc.text.split()))
        debug = {"TOKENS": tokens}
        return result, debug


class L_PRON_INT(Metric):
    category = Lexical
    name_en = "Incidence of indexical pronouns"

    def count(doc):
        tokens = [token.text for token in doc if "PronType=Int" in token.morph]
        result = ratio(len(tokens), len(doc.text.split()))
        debug = {"TOKENS": tokens}
        return result, debug


class L_PRON_RELATIVE(Metric):
    category = Lexical
    name_en = "Incidence of relative pronoun 'що'"

    def count(doc):
        tokens = [token.text for token in doc if token.pos_ == "SCONJ" and token.dep_ == "mark"]
        result = ratio(len(tokens), len(doc.text.split()))
        debug = {"TOKENS": tokens}
        return result, debug


class L_PRON_RFL(Metric):
    category = Lexical
    name_en = "Incidence of reflexive pronoun"

    def count(doc):
        tokens = [token.text for token in doc if "Reflex=Yes" in token.morph and "PronType=Prs" in token.morph]
        result = ratio(len(tokens), len(doc.text.split()))
        debug = {"TOKENS": tokens}
        return result, debug


class L_PRON_POS(Metric):
    category = Lexical
    name_en = "Incidence of posessive pronoun"

    def count(doc):
        tokens = [token.text for token in doc if "Poss=Yes" in token.morph and "PronType=Prs" in token.morph]
        result = ratio(len(tokens), len(doc.text.split()))
        debug = {"TOKENS": tokens}
        return result, debug


class L_PRON_NEG(Metric):
    category = Lexical
    name_en = "Incidence of negative pronoun"

    def count(doc):
        tokens = [token.text for token in doc if "PronType=Neg" in token.morph]
        result = ratio(len(tokens), len(doc.text.split()))
        debug = {"TOKENS": tokens}
        return result, debug

# ---------------------------
# ADVERBS
# ---------------------------

class L_ADV_POS(Metric):
    category = Lexical
    name_en = "Incidence of positive adverbs"

    def count(doc):
        tokens = [token.text for token in doc if "Degree=Pos" in token.morph and token.pos_ == "ADV"]
        result = ratio(len(tokens), len(doc.text.split()))
        debug = {"TOKENS": tokens}
        return result, debug


class L_ADV_CMP(Metric):
    category = Lexical
    name_en = "Incidence of comparative adverbs"

    def count(doc):
        tokens = [token.text for token in doc if "Degree=Cmp" in token.morph and token.pos_ == "ADV"]
        result = ratio(len(tokens), len(doc.text.split()))
        debug = {"TOKENS": tokens}
        return result, debug


class L_ADV_SUP(Metric):
    category = Lexical
    name_en = "Incidence of superlative adverbs"

    def count(doc):
        tokens = [token.text for token in doc if "Degree=Sup" in token.morph and token.pos_ == "ADV"]
        result = ratio(len(tokens), len(doc.text.split()))
        debug = {"TOKENS": tokens}
        return result, debug
