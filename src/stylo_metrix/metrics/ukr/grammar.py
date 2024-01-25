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
    lang = 'ukr'
    name_en = "Grammar"

# Root verbs and conjunctions in imperfect form / дієслова недоконаного виду: [ROOT | Aspect=Imp] + [conj | Aspect=Imp]
class G_ROOT_VERB_IMPERFECT(Metric):
    category = Grammar
    name_en = "Incidence of root verbs in imperfect aspect"

    def count(doc):
        verbs = [token.text for token in doc if token.dep_ == "ROOT" and "Aspect=Imp" in token.morph]
        conj_verbs = [token.text for token in doc 
                    if token.head.text in verbs and token.dep_ == "conj" and "Aspect=Imp" in token.morph]
        root_imperfect_verbs = verbs + conj_verbs
        result = ratio(len(root_imperfect_verbs), len(doc.text.split()))
        debug = {'TOKENS': root_imperfect_verbs}
        return result, debug


# All verbs in imperfect form / дієслова недоконаного виду
class G_ALL_VERB_IMPERFECT(Metric):
    category = Grammar
    name_en = "Incidence of all verbs in imperfect aspect, active voice"

    def count(doc):
        verbs = [token.text for token in doc if token.pos_ == "VERB" and "Aspect=Imp" in token.morph]
        result = ratio(len(verbs), len(doc.text.split()))
        debug = {'TOKENS': verbs}
        return result, debug


# Root verbs and conjunctions in perfect form / дієслова доконаного виду: [ROOT | Aspect=Perf] + [conj | Aspect=Perf]
class G_ROOT_VERB_PERFECT(Metric):
    category = Grammar
    name_en = "Incidence of root verbs in perfect form"
    
    def count(doc):
        verbs = [token.text for token in doc if token.dep_ == "ROOT" and "Aspect=Perf" in token.morph]
        conj_verbs = [token.text for token in doc 
                    if token.head.text in verbs and token.dep_ == "conj" and "Aspect=Perf" in token.morph]
        root_perfect_verbs = verbs + conj_verbs
        result = ratio(len(root_perfect_verbs), len(doc.text.split()))
        debug = {'TOKENS': root_perfect_verbs}
        return result, debug


# All verbs in perfect form / дієслова доконаного виду
class G_ALL_VERB_PERFECT(Metric):
    category = Grammar
    name_en = "Incidence of all verbs in perfect form"
    
    def count(doc):
        verbs = [token.text for token in doc if token.pos_ == "VERB" and "Aspect=Perf" in token.morph]
        result = ratio(len(verbs), len(doc.text.split()))
        debug = {'TOKENS': verbs}
        return result, debug 


# Present tense, indicative mood, imperfect aspect / дієслова теперішнього недоконаного часу
class G_PRESENT_IND_IMPERFECT(Metric):
    category = Grammar
    name_en = "Incidence of verbs in the present tense, indicative mood, imperfect aspect"
    
    def count(doc):
        verbs = [token.text for token in doc if "Aspect=Imp" in token.morph and "Tense=Pres" in token.morph
             and "VerbForm=Fin" in token.morph and "Mood=Ind" in token.morph]
        result = ratio(len(verbs), len(doc.text.split()))
        debug = {'TOKENS': verbs}
        return result, debug


# Past tense, indicative mood, imperfect aspect / дієслова минулого недоконаного часу
class G_PAST_IND_IMPERFECT(Metric):
    category = Grammar
    name_en = "Incidence of verbs in the past tense, indicative mood, imperfect aspect"
    
    def count(doc):
        verbs = [token.text for token in doc if "Aspect=Imp" in token.morph and "Tense=Past" in token.morph
             and "VerbForm=Fin" in token.morph and "Mood=Ind" in token.morph]
        result = ratio(len(verbs), len(doc.text.split()))
        debug = {'TOKENS': verbs}
        return result, debug
    

# Past tense, indicative mood, perfect aspect / дієслова минулого доконаного часу
class G_PAST_IND_PERFECT(Metric):
    category = Grammar
    name_en = "Incidence of verbs in the past tense, indicative mood, perfect aspect"
    
    def count(doc):
        verbs = [token.text for token in doc if "Aspect=Perf" in token.morph and "Tense=Past" in token.morph
             and "VerbForm=Fin" in token.morph and "Mood=Ind" in token.morph]
        result = ratio(len(verbs), len(doc.text.split()))
        debug = {'TOKENS': verbs}
        return result, debug


# Future tense, indicative mood, perfect aspect / дієслова майбутнього доконаного часу
class G_FUT_IND_PERFECT(Metric):
    category = Grammar
    name_en = "Incidence of verbs in the future tense, indicative mood, perfect aspect"
    
    def count(doc):
        verbs = [token.text for token in doc if "Aspect=Perf" in token.morph and "Tense=Fut" in token.morph
             and "VerbForm=Fin" in token.morph and "Mood=Ind" in token.morph]
        result = ratio(len(verbs), len(doc.text.split()))
        debug = {'TOKENS': verbs}
        return result, debug 


# Future tense, indicative mood, imperfect aspect, simple verb form / дієслова майбутнього недоконаного часу простої форми
class G_FUT_IND_IMPERFECT_SIMPLE(Metric):
    category = Grammar
    name_en = "Incidence of verbs in the future tense, indicative mood, imperfect aspect, simple verb forms"
    
    def count(doc):
        verbs = [token.text for token in doc if "Aspect=Imp" in token.morph and "Tense=Fut" in token.morph
             and "VerbForm=Fin" in token.morph and "Mood=Ind" in token.morph and token.pos_ != "AUX"]
        result = ratio(len(verbs), len(doc.text.split()))
        debug = {'TOKENS': verbs}
        return result, debug 


# Future tense, indicative mood, complex verb forms / дієслова майбутнього недоконаного часу складеної форми
class G_FUT_IND_COMPLEX(Metric):
    category = Grammar
    name_en = "Incidence of verbs in the future tense, indicative mood, complex verb forms"
    
    def count(doc):
        verbs = [token.text for token in doc if "Aspect=Imp" in token.morph and "Tense=Fut" in token.morph 
             and (token.dep_ == "cop" or token.dep_ == "aux")]
        conj = [token.head.text for token in doc if token.text in verbs]
        verb_list = verbs + conj
        result = ratio(len(verb_list), len(doc.text.split()))
        debug = {'TOKENS': verb_list}
        return result, debug


class G_FIRST_CONJ(Metric):
    category = Grammar
    name_en = "Incidence of verbs in the first conjugation"

    def count(doc):
        vowels = ["я", "а"]
        nouns = []
        for token in doc:
            if token.pos_ == "NOUN":
                if ("Gender=Fem" in token.morph or "Gender=Masc" in token.morph) and token.lemma_[-1] in vowels:
                    nouns.append(token.text)
            if "Gender=Masc" in token.morph and token.ent_type_ == "PER" and token.lemma_[-1] in vowels:
                nouns.append(token.text)
        result = ratio(len(nouns), len(doc.text.split()))
        debug = {'TOKENS': nouns}
        return result, debug


class G_SECOND_CONJ(Metric):
    category = Grammar
    name_en = "Incidence of verbs in the second conjugation"

    def count(doc):
        vowels = ["я", "о", "е", "є"]
        consonants = ["б", "в", "г", "ґ", "д", "ж", "з", "й", "к","л", "м", "н", "п", "р", "с", "т", "у", 
                "ф", "х", "ц", "ч", "ш", "щ", "ь"]
        suffixes = ["ят", "ат", "ен"]
        nouns = []
        for token in doc:
            if token.pos_ == "NOUN" and ("Gender=Masc" in token.morph or "Gender=Neut" in token.morph):
                if token.lemma_[-1] in vowels or token.lemma_[-1] in consonants:
                    nouns.append(token.text)
                if ("Case=Gen" in token.morph or "Case=Acc" in token.morph) and token.text[-3:-1] not in suffixes \
                and token.lemma_[:-1] in vowels and token.text not in nouns:
                    nouns.append(token.text)
            if "Gender=Masc" in token.morph and token.pos_ == "PROPN" and token.lemma_[-1] in vowels:
                nouns.append(token.text)
                
        result = ratio(len(nouns), len(doc.text.split()))
        debug = {'TOKENS': nouns}
        return result, debug


class G_THIRD_CONJ(Metric):
    category = Grammar
    name_en = "Incidence of verbs in the third conjugation"

    def count(doc):
        consonants = ["б", "в", "г", "ґ", "д", "ж", "з", "й", "к","л", "м", "н", "п", "р", "с", "т", "у", 
                    "ф", "х", "ц", "ч", "ш", "щ", "ь"]
        noun_exception = "мати"
        nouns = []
        for token in doc:
            if token.pos_ == "NOUN":
                if "Gender=Fem" in token.morph and token.lemma_[-1] in consonants:
                    nouns.append(token.text)
            if token.text == noun_exception:
                nouns.append(token.text)
        result = ratio(len(nouns), len(doc.text.split()))
        debug = {'TOKENS': nouns}
        return result, debug 


class G_FOURTH_CONJ(Metric):
    category = Grammar
    name_en = "Incidence of verbs in the fourth conjugation"

    def count(doc):
        vowels = ["я", "а"]
        suffixes = ["ят", "ат", "ен"]
        _, debug = G_SECOND_CONJ(doc)
        second_conj = [token for token in debug['TOKENS']]

        nouns = []
        for token in doc:
            if token.pos_ == "NOUN" and "Gender=Neut" in token.morph:
                if token.lemma_[:-1] in vowels and "Case=Nom" in token.morph and token.text not in second_conj:
                    nouns.append(token.text)
                if ("Case=Gen" in token.morph or "Case=Acc" in token.morph or "Case=Dat" in token.morph) and token.text[-3:-1] in suffixes \
                and token.text not in nouns:
                    nouns.append(token.text)
        result = ratio(len(nouns), len(doc.text.split()))
        debug = {'TOKENS': nouns}
        return result, debug


class G_INFINITIVE(Metric):
    category = Grammar
    name_en = "Incidence of verbs in infinitive"

    def count(doc):
        tokens = [token.text for token in doc if "VerbForm=Inf" in token.morph]
        result = ratio(len(tokens), len(doc.text.split()))
        debug = {'TOKENS': tokens}
        return result, debug


class G_PASSIVE(Metric):
    category = Grammar
    name_en = "Incidence of verbs in the passive form"

    def count(doc):
        tokens = [token.head.text for token in doc if token.pos_ == "VERB" and ("Person=0" in token.morph and "Aspect=Perf" in token.morph)]
        result = ratio(len(tokens), len(doc.text.split()))
        debug = {'TOKENS': tokens}
        return result, debug


class G_TRANSITIVE(Metric):
    category = Grammar
    name_en = "Incidence of transitive verbs"

    def count(doc):
        search = [token.text for token in doc if token._.transitivity == "tr"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class G_INTRANSITIVE(Metric):
    category = Grammar
    name_en = "Incidence of intransitive verbs"

    def count(doc):
        search = [token.text for token in doc if token._.transitivity == "intr"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class G_IMPERSONAL_VERBS(Metric):
    category = Grammar
    name_en = "Incidence of impersonal verbs"

    def count(doc):
        tokens = [token.text for token in doc if token.pos_ == "VERB" and 
              ("Gender=Neut" in token.morph or any(i for i in token.children if "Gender=Neut" in i.morph))]
        result = ratio(len(tokens), len(doc.text.split()))
        debug = {'TOKENS': tokens}
        return result, debug


class G_PARTICIPLE_PASSIVE(Metric):
    category = Grammar
    name_en = "Incidence of passive participles"

    def count(doc):
        tokens = [token.text for token in doc if token.pos_ == "ADJ" and  "VerbForm=Part" in token.morph and "Aspect=Perf" in token.morph]
        result = ratio(len(tokens), len(doc.text.split()))
        debug = {'TOKENS': tokens}
        return result, debug 


class G_PARTICIPLE_ACTIVE(Metric):
    category = Grammar
    name_en = "Incidence of active participles"

    def count(doc):
        tokens = [token.text for token in doc if token.pos_ == "ADJ" and  "VerbForm=Part" in token.morph and "Aspect=Imp" in token.morph]
        result = ratio(len(tokens), len(doc.text.split()))
        debug = {'TOKENS': tokens}
        return result, debug


class G_ADV_PRF_PART(Metric):
    category = Grammar
    name_en = "Incidence of adverbial perfect participles"

    def count(doc):
        tokens = [token.text for token in doc if token.dep_ == "advcl" and "VerbForm=Conv" in token.morph and "Aspect=Perf" in token.morph]
        result = ratio(len(tokens), len(doc.text.split()))
        debug = {'TOKENS': tokens}
        return result, debug


class G_ADV_IMPRF_PART(Metric):
    category = Grammar
    name_en = "Incidence of adverbial imperfect participles"

    def count(doc):
        tokens = [token.text for token in doc if token.dep_ == "advcl" and "VerbForm=Conv" in token.morph and "Aspect=Imp" in token.morph]
        result = ratio(len(tokens), len(doc.text.split()))
        debug = {'TOKENS': tokens}
        return result, debug
