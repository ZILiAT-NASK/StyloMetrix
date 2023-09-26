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
from ...utils import incidence


class VerbFroms(Category):
    lang = 'ru'
    name_en = "Verbs Forms"
    

class VF_ROOT_VERB_IMPERFECT(Metric):
    category = VerbFroms
    name_en = "Incidence of root verbs in imperfect aspect"

    '''Root verbs and conjunctions in imperfect form: [ROOT | Aspect=Imp] + [conj | Aspect=Imp]'''

    def count(doc):
        verbs = [token.text for token in doc if token.dep_ == "ROOT" and "Aspect=Imp" in token.morph]
        conj_verbs = [token for token in doc 
                    if token.head.text in verbs and token.dep_ == "conj" and "Aspect=Imp" in token.morph]
        root_imperfect_verbs = verbs + conj_verbs
        result = incidence(doc, root_imperfect_verbs)
        return result, {}


# All verbs in imperfect form active voice 
class VF_ALL_VERB_IMPERFECT(Metric):
    category = VerbFroms
    name_en = "Incidence of all verbs in imperfect aspect, active voice"

    def count(doc):
        verbs = [token.text for token in doc if token.pos_ == "VERB" and "Aspect=Imp" in token.morph and "Voice=Act" in token.morph]
        result = incidence(doc, verbs)
        return result, {}


# Root verbs and conjunctions in perfect form / дієслова доконаного виду: [ROOT | Aspect=Perf] + [conj | Aspect=Perf]
class VF_ROOT_VERB_PERFECT(Metric):
    category = VerbFroms
    name_en = "Incidence of root verbs in perfect form"
    
    def count(doc):
        verbs = [token.text for token in doc if token.dep_ == "ROOT" and "Aspect=Perf" in token.morph]
        conj_verbs = [token for token in doc 
                    if token.head.text in verbs and token.dep_ == "conj" and "Aspect=Perf" in token.morph]
        root_perfect_verbs = verbs + conj_verbs
        result = incidence(doc, root_perfect_verbs)
        return result, {}


# All verbs in perfect form / дієслова доконаного виду
class VF_ALL_VERB_PERFECT(Metric):
    category = VerbFroms
    name_en = "Incidence of all verbs in perfect form"
    
    def count(doc):
        verbs = [token.text for token in doc if token.pos_ == "VERB" and "Aspect=Perf" in token.morph]
        result = incidence(doc, verbs)
        return result, {}


# Present tense, indicative mood, imperfect aspect / дієслова теперішнього недоконаного часу
class VF_PRESENT_IND_IMPERFECT(Metric):
    category = VerbFroms
    name_en = "Incidence of verbs in the present tense, indicative mood, imperfect aspect"
    
    def count(doc):
        verbs = [token.text for token in doc if "Aspect=Imp" in token.morph and "Tense=Pres" in token.morph
             and "VerbForm=Fin" in token.morph and "Mood=Ind" in token.morph]
        result = incidence(doc, verbs)
        return result, {}


# Past tense, indicative mood, imperfect aspect / дієслова минулого недоконаного часу
class VF_PAST_IND_IMPERFECT(Metric):
    category = VerbFroms
    name_en = "Incidence of verbs in the past tense, indicative mood, imperfect aspect"
    
    def count(doc):
        verbs = [token.text for token in doc if "Aspect=Imp" in token.morph and "Tense=Past" in token.morph
             and "VerbForm=Fin" in token.morph and "Mood=Ind" in token.morph]
        result = incidence(doc, verbs)
        return result, {}


# Present tense, indicative mood, perfect aspect
class VF_PRESENT_IND_PERFECT(Metric):
    category = VerbFroms
    name_en = "Incidence of verbs in the present tense, indicative mood, perfect aspect"
    
    def count(doc):
        verbs = [token.text for token in doc if "Aspect=Perf" in token.morph and "Tense=Pres" in token.morph
             and "VerbForm=Fin" in token.morph and "Mood=Ind" in token.morph]
        result = incidence(doc, verbs)
        return result, {}


# Past tense, indicative mood, perfect aspect / дієслова минулого доконаного часу
class VF_PAST_IND_PERFECT(Metric):
    category = VerbFroms
    name_en = "Incidence of verbs in the past tense, indicative mood, perfect aspect"
    
    def count(doc):
        verbs = [token.text for token in doc if "Aspect=Perf" in token.morph and "Tense=Past" in token.morph
             and "VerbForm=Fin" in token.morph and "Mood=Ind" in token.morph]
        result = incidence(doc, verbs)
        return result, {}


# Future tense, indicative mood, perfect aspect / дієслова майбутнього доконаного часу
class VF_FUT_IND_PERFECT(Metric):
    category = VerbFroms
    name_en = "Incidence of verbs in the future tense, indicative mood, perfect aspect"
    
    def count(doc):
        verbs = [token.text for token in doc if "Aspect=Perf" in token.morph and "Tense=Fut" in token.morph
             and "VerbForm=Fin" in token.morph and "Mood=Ind" in token.morph]
        result = incidence(doc, verbs)
        return result, {}


# Future tense, indicative mood, imperfect aspect, simple verb form / дієслова майбутнього недоконаного часу простої форми
class VF_FUT_IND_IMPERFECT_SIMPLE(Metric):
    category = VerbFroms
    name_en = "Incidence of verbs in the future tense, indicative mood, imperfect aspect, simple verb forms"
    
    def count(doc):
        verbs = [token.text for token in doc if "Aspect=Imp" in token.morph and "Tense=Fut" in token.morph
             and "VerbForm=Fin" in token.morph and "Mood=Ind" in token.morph and token.pos_ != "AUX"]
        result = incidence(doc, verbs)
        return result, {}


# Future tense, indicative mood, complex verb forms / дієслова майбутнього недоконаного часу складеної форми
class VF_FUT_IND_COMPLEX(Metric):
    category = VerbFroms
    name_en = "Incidence of verbs in the future tense, indicative mood, complex verb forms"
    
    def count(doc):
        verbs = [token.text for token in doc if "Aspect=Imp" in token.morph and token.lemma_ == "быть" 
             and (token.dep_ == "cop" or token.dep_ == "aux")]
        conj = [token.head.text for token in doc if token.text in verbs]
        verb_list = verbs + conj
        result = incidence(doc, verb_list)
        return result, {}


class VF_INFINITIVE(Metric):
    category = VerbFroms
    name_en = "Incidence of verbs in infinitive"

    def count(doc):
        tokens = [token for token in doc if "VerbForm=Inf" in token.morph]
        result = incidence(doc, tokens)
        return result, {}


# class VF_PASSIVE(Metric):
#     category = VerbFroms
#     name_en = "Incidence of verbs in the passive form"

#     def count(doc):
#         tokens = [token.head for token in doc if (token.pos_ == "AUX" and token.dep_ == "cop") and "Voice=Pass" in token.head.morph]
#         result = incidence(doc, tokens)
#         return result, {}


# class VF_TRANSITIVE(Metric):
#     category = VerbFroms
#     name_en = "Incidence of transitive verbs"

#     def count(doc):
#         search = [token for token in doc if token._.transitivity == "tr"]
#         result = incidence(doc, search)
#         return result, {}


# class VF_INTRANSITIVE(Metric):
#     category = VerbFroms
#     name_en = "Incidence of intransitive verbs"

#     def count(doc):
#         search = [token for token in doc if token._.transitivity == "intr"]
#         result = incidence(doc, search)
#         return result, {}


# class VF_IMPERSONAL_VERBS(Metric):
#     category = VerbFroms
#     name_en = "Incidence of impersonal verbs"

#     def count(doc):
#         tokens = [token for token in doc if token.pos_ == "VERB" and 
#               ("Gender=Neut" in token.morph or any(i for i in token.children if "Gender=Neut" in i.morph))]
#         result = incidence(doc, tokens)
#         return result, {}


# class VF_PARTICIPLE_PASSIVE(Metric):
#     category = VerbFroms
#     name_en = "Incidence of passive participles"

#     def count(doc):
#         tokens = [token for token in doc if token.pos_ == "ADJ" and  "VerbForm=Part" in token.morph and "Aspect=Perf" in token.morph]
#         result = incidence(doc, tokens)
#         return result, {}


# class VF_PARTICIPLE_ACTIVE(Metric):
#     category = VerbFroms
#     name_en = "Incidence of active participles"

#     def count(doc):
#         tokens = [token for token in doc if token.pos_ == "ADJ" and  "VerbForm=Part" in token.morph and "Aspect=Imp" in token.morph]
#         result = incidence(doc, tokens)
#         return result, {}


# class VF_ADV_PRF_PART(Metric):
#     category = VerbFroms
#     name_en = "Incidence of adverbial perfect participles"

#     def count(doc):
#         tokens = [token for token in doc if token.dep_ == "advcl" and "VerbForm=Conv" in token.morph and "Aspect=Perf" in token.morph]
#         result = incidence(doc, tokens)
#         return result, {}


# class VF_ADV_IMPRF_PART(Metric):
#     category = VerbFroms
#     name_en = "Incidence of adverbial imperfect participles"

#     def count(doc):
#         tokens = [token for token in doc if token.dep_ == "advcl" and "VerbForm=Conv" in token.morph and "Aspect=Imp" in token.morph]
#         result = incidence(doc, tokens)
#         return result, {}
