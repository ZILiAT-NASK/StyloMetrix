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
from ...utils import ratio


class Grammar(Category):
    lang = "ru"
    name_en = "Grammar"
    name_local = name_en


class G_ROOT_VERB_IMPERFECT(Metric):
    category = Grammar
    name_en = "Incidence of root verbs in imperfect aspect"
    name_local = name_en

    def count(doc):
        verbs = [
            token.text
            for token in doc
            if token.dep_ == "ROOT" and "Aspect=Imp" in token.morph
        ]
        conj_verbs = [
            token.text
            for token in doc
            if token.head.text in verbs
            and token.dep_ == "conj"
            and "Aspect=Imp" in token.morph
        ]
        debug = verbs + conj_verbs
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug


# All verbs in imperfect form / дієслова недоконаного виду
class G_ALL_VERB_IMPERFECT(Metric):
    category = Grammar
    name_en = "Incidence of all verbs in imperfect aspect, active voice"
    name_local = name_en

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ == "VERB" and "Aspect=Imp" in token.morph
        ]
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug


# Root verbs and conjunctions in perfect form / дієслова доконаного виду: [ROOT | Aspect=Perf] + [conj | Aspect=Perf]
class G_ROOT_VERB_PERFECT(Metric):
    category = Grammar
    name_en = "Incidence of root verbs in perfect form"
    name_local = name_en

    def count(doc):
        verbs = [
            token.text
            for token in doc
            if token.dep_ == "ROOT" and "Aspect=Perf" in token.morph
        ]
        conj_verbs = [
            token.text
            for token in doc
            if token.head.text in verbs
            and token.dep_ == "conj"
            and "Aspect=Perf" in token.morph
        ]
        debug = verbs + conj_verbs
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug


# All verbs in perfect form / дієслова доконаного виду
class G_ALL_VERB_PERFECT(Metric):
    category = Grammar
    name_en = "Incidence of all verbs in perfect form"
    name_local = name_en

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ == "VERB" and "Aspect=Perf" in token.morph
        ]
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug


# Present tense, indicative mood, imperfect aspect / дієслова теперішнього недоконаного часу
class G_PRESENT_IND_IMPERFECT(Metric):
    category = Grammar
    name_en = (
        "Incidence of verbs in the present tense, indicative mood, imperfect aspect"
    )
    name_local = name_en

    def count(doc):
        debug = [
            token.text
            for token in doc
            if "Aspect=Imp" in token.morph
            and "Tense=Pres" in token.morph
            and "VerbForm=Fin" in token.morph
            and "Mood=Ind" in token.morph
        ]
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug


# Past tense, indicative mood, imperfect aspect / дієслова минулого недоконаного часу
class G_PAST_IND_IMPERFECT(Metric):
    category = Grammar
    name_en = "Incidence of verbs in the past tense, indicative mood, imperfect aspect"
    name_local = name_en

    def count(doc):
        debug = [
            token.text
            for token in doc
            if "Aspect=Imp" in token.morph
            and "Tense=Past" in token.morph
            and "VerbForm=Fin" in token.morph
            and "Mood=Ind" in token.morph
        ]
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug


# Past tense, indicative mood, perfect aspect / дієслова минулого доконаного часу
class G_PAST_IND_PERFECT(Metric):
    category = Grammar
    name_en = "Incidence of verbs in the past tense, indicative mood, perfect aspect"
    name_local = name_en

    def count(doc):
        debug = [
            token.text
            for token in doc
            if "Aspect=Perf" in token.morph
            and "Tense=Past" in token.morph
            and "VerbForm=Fin" in token.morph
            and "Mood=Ind" in token.morph
        ]
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug


# Future tense, indicative mood, perfect aspect / дієслова майбутнього доконаного часу
class G_FUT_IND_PERFECT(Metric):
    category = Grammar
    name_en = "Incidence of verbs in the future tense, indicative mood, perfect aspect"
    name_local = name_en

    def count(doc):
        debug = [
            token.text
            for token in doc
            if "Aspect=Perf" in token.morph
            and "Tense=Fut" in token.morph
            and "VerbForm=Fin" in token.morph
            and "Mood=Ind" in token.morph
        ]
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug


# Future tense, indicative mood, imperfect aspect, simple verb form / дієслова майбутнього недоконаного часу простої форми
class G_FUT_IND_IMPERFECT_SIMPLE(Metric):
    category = Grammar
    name_en = "Incidence of verbs in the future tense, indicative mood, imperfect aspect, simple verb forms"
    name_local = name_en

    def count(doc):
        debug = [
            token.text
            for token in doc
            if "Aspect=Imp" in token.morph
            and "Tense=Fut" in token.morph
            and "VerbForm=Fin" in token.morph
            and "Mood=Ind" in token.morph
            and token.pos_ != "AUX"
        ]
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug


# Future tense, indicative mood, complex verb forms / дієслова майбутнього недоконаного часу складеної форми
class G_FUT_IND_COMPLEX(Metric):
    category = Grammar
    name_en = (
        "Incidence of verbs in the future tense, indicative mood, complex verb forms"
    )
    name_local = name_en

    def count(doc):
        verbs = [
            token.text
            for token in doc
            if "Aspect=Imp" in token.morph
            and token.lemma_ == "быть"
            and (token.dep_ == "cop" or token.dep_ == "aux")
        ]
        conj = [token.head.text for token in doc if token.text in verbs]
        debug = verbs + conj
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug


class G_INFINITIVE(Metric):
    category = Grammar
    name_en = "Incidence of verbs in infinitive"
    name_local = name_en

    def count(doc):
        debug = [token.text for token in doc if "VerbForm=Inf" in token.morph]
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug


class G_PASSIVE(Metric):
    category = Grammar
    name_en = "Incidence of verbs in the passive form"
    name_local = name_en

    def count(doc):
        debug = [
            token.head.text
            for token in doc
            if token.pos_ == "VERB"
            and ("Aspect=Perf" in token.morph and "Voice=Pass" in token.morph)
        ]
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug


class G_TRANSITIVE(Metric):
    category = Grammar
    name_en = "Incidence of transitive verbs"
    name_local = name_en

    def count(doc):
        pos = ["NOUN", "PRON", "PROPN"]
        debug = [
            token.text
            for token in doc
            if any(child for child in token.children if child.pos_ in pos)
            and token.pos_ == "VERB"
            and "VerbForm=Inf" not in token.morph
        ]
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug


class G_INTRANSITIVE(Metric):
    category = Grammar
    name_en = "Incidence of intransitive verbs"
    name_local = name_en

    def count(doc):
        pos = ["NOUN", "PRON", "PROPN"]
        debug = [
            token.text
            for token in doc
            if not any(child for child in token.children if child.pos_ in pos)
            and token.pos_ == "VERB"
        ]
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug


class G_IMPERSONAL_VERBS(Metric):
    category = Grammar
    name_en = "Incidence of impersonal verbs"
    name_local = name_en

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ == "VERB"
            and (
                "Gender=Neut" in token.morph
                or any(i for i in token.children if "Gender=Neut" in i.morph)
            )
        ]
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug


class G_PARTICIPLE_PASSIVE(Metric):
    category = Grammar
    name_en = "Incidence of passive participles"
    name_local = name_en

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ == "ADJ"
            and "VerbForm=Part" in token.morph
            and "Aspect=Perf" in token.morph
        ]
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug


class G_PARTICIPLE_ACTIVE(Metric):
    category = Grammar
    name_en = "Incidence of active participles"
    name_local = name_en

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.pos_ == "ADJ"
            and "VerbForm=Part" in token.morph
            and "Aspect=Imp" in token.morph
        ]
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug


class G_ADV_PRF_PART(Metric):
    category = Grammar
    name_en = "Incidence of adverbial perfect participles"
    name_local = name_en

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.dep_ == "advcl"
            and "VerbForm=Conv" in token.morph
            and "Aspect=Perf" in token.morph
        ]
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug


class G_ADV_IMPRF_PART(Metric):
    category = Grammar
    name_en = "Incidence of adverbial imperfect participles"
    name_local = name_en

    def count(doc):
        debug = [
            token.text
            for token in doc
            if token.dep_ == "advcl"
            and "VerbForm=Conv" in token.morph
            and "Aspect=Imp" in token.morph
        ]
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug
