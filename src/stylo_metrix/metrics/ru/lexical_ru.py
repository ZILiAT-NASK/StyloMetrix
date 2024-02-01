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


import math

from ...structures import Category, Metric
from ...utils import ratio


class Lexical(Category):
    lang = "ru"
    name_en = "Lexical"
    name_local = name_en


# ---------------------------
# GENERAL LEXICAL INFORMATION
# ---------------------------


class L_TYPE_TOKEN_RATIO_LEMMAS(Metric):
    category = Lexical
    name_en = "Type-token ratio for words lemmas"
    name_local = name_en

    def count(doc):
        debug = set(token.lemma_ for token in doc if token.is_alpha)
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


# class HERDAN_TTR(Metric):
#     category = Lexical
#     name_en = "Herdan's TTR"
# name_local=name_en

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
# name_local=name_en

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
    name_local = name_en

    def count(doc):
        debug = [token.text for token in doc if token._.is_content_word]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class L_FUNC_A(Metric):
    category = Lexical
    name_en = "Incidence of Function words"
    name_local = name_en

    def count(doc):
        debug = [token.text for token in doc if token._.is_function_word]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class L_CONT_T(Metric):
    category = Lexical
    name_en = "Incidence of Content words types"
    name_local = name_en

    def count(doc):
        debug = set(token.text for token in doc if token._.is_content_word)
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class L_FUNC_T(Metric):
    category = Lexical
    name_en = "Incidence of Function words types"
    name_local = name_en

    def count(doc):
        debug = set(token.text for token in doc if token._.is_function_word)
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


# ---------------------------
# NOUNS
# ---------------------------


class L_PLURAL_NOUNS(Metric):
    category = Lexical
    name_en = "Incidence of nouns in plural"
    name_local = name_en

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ == "NOUN" and "Number=Plur" in token.morph
        ]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class L_SINGULAR_NOUNS(Metric):
    category = Lexical
    name_en = "Incidence of nouns in singular"
    name_local = name_en

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ == "NOUN" and "Number=Sing" in token.morph
        ]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class L_PROPER_NAME(Metric):
    category = Lexical
    name_en = "Incidence of proper names"
    name_local = name_en

    def count(doc):
        debug = [token.text for token in doc if token.pos_ == "PROPN"]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class L_PERSONAL_NAME(Metric):
    category = Lexical
    name_en = "Incidence of personal names"
    name_local = name_en

    def count(doc):
        debug = [ent.text for ent in doc.ents if ent.label_ == "PER"]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class L_ANIM_NOUN(Metric):
    category = Lexical
    name_en = "Incidence of animate nouns"
    name_local = name_en

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ == "NOUN" and "Animacy=Anim" in token.morph
        ]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class L_INANIM_NOUN(Metric):
    category = Lexical
    name_en = "Incidence of inanimate nouns"
    name_local = name_en

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ == "NOUN" and "Animacy=Inan" in token.morph
        ]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class L_NOUN_NEUTRAL(Metric):
    category = Lexical
    name_en = "Incidence of neutral nouns"
    name_local = name_en

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ == "NOUN" and "Gender=Neut" in token.morph
        ]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class L_NOUN_FAMININE(Metric):
    category = Lexical
    name_en = "Incidence of feminine nouns"
    name_local = name_en

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ == "NOUN" and "Gender=Fem" in token.morph
        ]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class L_NOUN_MASCULINE(Metric):
    category = Lexical
    name_en = "Incidence of masculine nouns"
    name_local = name_en

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ == "NOUN" and "Gender=Masc" in token.morph
        ]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class L_FEMININE_NAMES(Metric):
    category = Lexical
    name_en = "Incidence of feminine proper nouns"
    name_local = name_en

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ == "PROPN"
            and ("Animacy=Anim" in token.morph and "Gender=Fem" in token.morph)
        ]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class L_MASCULINE_NAMES(Metric):
    category = Lexical
    name_en = "Incidence of masculine proper nouns"
    name_local = name_en

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ == "PROPN"
            and ("Animacy=Anim" in token.morph and "Gender=Masc" in token.morph)
        ]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class L_SURNAMES(Metric):
    category = Lexical
    name_en = "Incidence of surnames"
    name_local = name_en

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ == "PROPN" and "NameType=Sur" in token.morph
        ]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class L_GIVEN_NAMES(Metric):
    category = Lexical
    name_en = "Incidence of given names"
    name_local = name_en

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ == "PROPN" and "NameType=Giv" in token.morph
        ]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


# https://universaldependencies.org/u/dep/flat.html


class L_FLAT_MULTIWORD(Metric):
    category = Lexical
    name_en = "Incidence of flat multiwords expressions"
    name_local = name_en

    def count(doc):
        flat = [[token.head.text, token.text] for token in doc if "flat" in token.dep_]
        debug = [token for i in flat for token in i]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class L_DIRECT_OBJ(Metric):
    category = Lexical
    name_en = "Incidence of direct objects"
    name_local = name_en

    def count(doc):
        debug = [token.text for token in doc if token.dep_ == "obj"]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class L_INDIRECT_OBJ(Metric):
    category = Lexical
    name_en = "Incidence of indirect objects"
    name_local = name_en

    def count(doc):
        debug = [
            token.text for token in doc if token.dep_ == "iobj" or token.dep_ == "obl"
        ]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


# ---------------------------
# NOUN CASES
# ---------------------------


class L_NOM_CASE(Metric):
    category = Lexical
    name_en = "Incidence of nouns in Nominative case"
    name_local = name_en

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ == "NOUN" and "Case=Nom" in token.morph
        ]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class L_GEN_CASE(Metric):
    category = Lexical
    name_en = "Incidence of nouns in Genitive case"
    name_local = name_en

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ == "NOUN" and "Case=Gen" in token.morph
        ]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class L_DAT_CASE(Metric):
    category = Lexical
    name_en = "Incidence of nouns in Dative case"
    name_local = name_en

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ == "NOUN" and "Case=Dat" in token.morph
        ]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class L_ACC_CASE(Metric):
    category = Lexical
    name_en = "Incidence of nouns in Accusative case"
    name_local = name_en

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ == "NOUN" and "Case=Acc" in token.morph
        ]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class L_INS_CASE(Metric):
    category = Lexical
    name_en = "Incidence of nouns in Instrumental case"
    name_local = name_en

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ == "NOUN" and "Case=Ins" in token.morph
        ]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class L_LOC_CASE(Metric):
    category = Lexical
    name_en = "Incidence of nouns in Locative case"
    name_local = name_en

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ == "NOUN" and "Case=Loc" in token.morph
        ]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


# ---------------------------
# ADJECTIVES
# ---------------------------


class L_QULITATIVE_ADJ_P(Metric):
    category = Lexical
    name_en = "Incidence of qualitative adj positive"
    name_local = name_en

    def count(doc):
        debug = [
            adj.text for adj in doc if adj.pos_ == "ADJ" and "Degree=Pos" in adj.morph
        ]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class L_RELATIVE_ADJ(Metric):
    category = Lexical
    name_en = "Incidence of relative adj"
    name_local = name_en

    def count(doc):
        degrees = ["Degree=Pos", "Degree=Cmp", "Degree=Sup"]
        debug = [
            adj.text
            for adj in doc
            if adj.pos_ == "ADJ" and not any(adj for i in degrees if i in adj.morph)
        ]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class L_QUALITATIVE_ADJ_CMP(Metric):
    category = Lexical
    name_en = "Incidence of qualitative comparative adj"
    name_local = name_en

    def count(doc):
        debug = [
            adj.text for adj in doc if adj.pos_ == "ADJ" and "Degree=Cmp" in adj.morph
        ]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class L_QUALITATIVE_ADJ_SUP(Metric):
    category = Lexical
    name_en = "Incidence of qualitative superlative adj"
    name_local = name_en

    def count(doc):
        debug = [
            adj.text for adj in doc if adj.pos_ == "ADJ" and "Degree=Sup" in adj.morph
        ]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class L_DIRECT_ADJ(Metric):
    category = Lexical
    name_en = "Incidence of direct adjective"
    name_local = name_en

    def count(doc):
        debug = []
        direct = [adj.text for adj in doc if adj.pos_ == "ADJ" and adj.dep_ == "amod"]
        conj = [
            token.text
            for token in doc
            if token.pos_ == "ADJ"
            and token.dep_ == "conj"
            and token.head.dep_ == "amod"
        ]
        debug = direct + conj
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class L_INDIRECT_ADJ(Metric):
    category = Lexical
    name_en = "Incidence of indirect adjective"
    name_local = name_en

    def count(doc):
        debug = []
        indirect = [
            adj.text
            for adj in doc
            if adj.pos_ == "ADJ" and (adj.dep_ != "amod" and adj.dep_ != "conj")
        ]
        conj = [
            token.text
            for token in doc
            if token.dep_ == "conj"
            and (token.head.dep_ != "amod" and token.head.pos_ == "ADJ")
        ]
        debug = indirect + conj
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


# ---------------------------
# PUNCTUATION
# ---------------------------


class L_PUNCT(Metric):
    category = Lexical
    name_en = "Incidence of punctuation"
    name_local = name_en

    def count(doc):
        debug = [token.text for token in doc if token.pos_ == "PUNCT"]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class L_PUNCT_DOT(Metric):
    category = Lexical
    name_en = "Incidence of dots"
    name_local = name_en

    def count(doc):
        debug = [token.text for token in doc if token.text == "."]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class L_PUNCT_COM(Metric):
    category = Lexical
    name_en = "Incidence of comma"
    name_local = name_en

    def count(doc):
        debug = [token.text for token in doc if token.text == ","]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class L_PUNCT_SEMC(Metric):
    category = Lexical
    name_en = "Incidence of semicolon"
    name_local = name_en

    def count(doc):
        debug = [token.text for token in doc if token.text == ";"]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class L_PUNCT_COL(Metric):
    category = Lexical
    name_en = "Incidence of colon"
    name_local = name_en

    def count(doc):
        debug = [token.text for token in doc if token.text == ":"]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class L_PUNCT_DASH(Metric):
    category = Lexical
    name_en = "Incidence of dashes"
    name_local = name_en

    def count(doc):
        debug = [token.text for token in doc if token.text == "—"]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


# ---------------------------
# NUMERALS
# ---------------------------
class L_NUM(Metric):
    category = Lexical
    name_en = "Incidence of numerals"
    name_local = name_en

    def count(doc):
        debug = [token.text for token in doc if token.pos_ == "NUM"]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


# ---------------------------
# PRONOUNS
# ---------------------------


class L_PRON_REL(Metric):
    category = Lexical
    name_en = "Incidence of relative pronouns"
    name_local = name_en

    def count(doc):
        debug = [token.text for token in doc if "PronType=Rel" in token.morph]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class L_PRON_INT(Metric):
    category = Lexical
    name_en = "Incidence of indexical pronouns"
    name_local = name_en

    def count(doc):
        debug = [token.text for token in doc if "PronType=Int" in token.morph]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class L_PRON_RFL(Metric):
    category = Lexical
    name_en = "Incidence of reflexive pronoun"
    name_local = name_en

    def count(doc):
        debug = [
            token.text
            for token in doc
            if "Reflex=Yes" in token.morph and "PronType=Prs" in token.morph
        ]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class L_PRON_POS(Metric):
    category = Lexical
    name_en = "Incidence of posessive pronoun"
    name_local = name_en

    def count(doc):
        debug = [
            token.text
            for token in doc
            if "Poss=Yes" in token.morph and "PronType=Prs" in token.morph
        ]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class L_PRON_NEG(Metric):
    category = Lexical
    name_en = "Incidence of negative pronoun"
    name_local = name_en

    def count(doc):
        debug = [token.text for token in doc if "PronType=Neg" in token.morph]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


# ---------------------------
# ADVERBS
# ---------------------------


class L_ADV_POS(Metric):
    category = Lexical
    name_en = "Incidence of positive adverbs"
    name_local = name_en

    def count(doc):
        debug = [
            token.text
            for token in doc
            if "Degree=Pos" in token.morph and token.pos_ == "ADV"
        ]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class L_ADV_CMP(Metric):
    category = Lexical
    name_en = "Incidence of comparative adverbs"
    name_local = name_en

    def count(doc):
        debug = [
            token.text
            for token in doc
            if "Degree=Cmp" in token.morph and token.pos_ == "ADV"
        ]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug


class L_ADV_SUP(Metric):
    category = Lexical
    name_en = "Incidence of superlative adverbs"
    name_local = name_en

    def count(doc):
        debug = [
            token.text
            for token in doc
            if "Degree=Sup" in token.morph and token.pos_ == "ADV"
        ]
        result = ratio(len(debug), len(doc.text.split()))

        return result, debug
