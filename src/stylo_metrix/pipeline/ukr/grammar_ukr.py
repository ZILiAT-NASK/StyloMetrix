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

def is_function_word(token):
    function_words_pos = ["PART", "SYM", "ADP", "X", "DET", "CCONJ", "SCONJ", "PUNCT", "INTJ"]
    return token.pos_ in function_words_pos


def is_content_word(token):
    if not token._.is_function_word:
        return True


def is_punctuation(token):
    if token.pos_ == "PUNCT":
        return True

"""CONJUGATION"""

def first_conj(doc):
    label = "first"
    ext = "conjugation"

    vowels = ["я", "а"]
    nouns = []

    for token in doc:
        if token.pos_ == "NOUN":
            if ("Gender=Fem" in token.morph or "Gender=Masc" in token.morph) and token.lemma_[-1] in vowels:
                nouns.append(token)
        if "Gender=Masc" in token.morph and token.ent_type_ == "PER" and token.lemma_[-1] in vowels:
            nouns.append(token)
    return nouns, ext, label

def second_conj(doc):
    label = "second"
    ext = "conjugation"


    vowels = ["я", "о", "е", "є"]
    consonants = ["б", "в", "г", "ґ", "д", "ж", "з", "й", "к","л", "м", "н", "п", "р", "с", "т", "у", 
              "ф", "х", "ц", "ч", "ш", "щ", "ь"]
    suffixes = ["ят", "ат", "ен"]


    nouns = []
    for token in doc:
        if token.pos_ == "NOUN" and ("Gender=Masc" in token.morph or "Gender=Neut" in token.morph):
            if token.lemma_[-1] in vowels or token.lemma_[-1] in consonants:
                nouns.append(token)
            if ("Case=Gen" in token.morph or "Case=Acc" in token.morph) and token.text[-3:-1] not in suffixes \
            and token.lemma_[:-1] in vowels and token not in nouns:
                nouns.append(token)
        if "Gender=Masc" in token.morph and token.pos_ == "PROPN" and token.lemma_[-1] in vowels:
            nouns.append(token)
                
    return nouns, ext, label

def third_conj(doc):
    label = "third"
    ext = "conjugation"


    consonants = ["б", "в", "г", "ґ", "д", "ж", "з", "й", "к","л", "м", "н", "п", "р", "с", "т", "у", 
              "ф", "х", "ц", "ч", "ш", "щ", "ь"]
    noun_exception = "мати"


    nouns = []
    for token in doc:
        if token.pos_ == "NOUN":
            if "Gender=Fem" in token.morph and token.lemma_[-1] in consonants:
                nouns.append(token)
        if token.text == noun_exception:
            nouns.append(token)
                
    return nouns, ext, label


def fourth_conj(doc):
    label = "forth"
    ext = "conjugation"

    vowels = ["я", "а"]
    suffixes = ["ят", "ат", "ен"]
    second = second_conj(doc)
    
    nouns = []
    for token in doc:
        if token.pos_ == "NOUN" and "Gender=Neut" in token.morph:
            if token.lemma_[:-1] in vowels and "Case=Nom" in token.morph and token not in second:
                nouns.append(token)
            if ("Case=Gen" in token.morph or "Case=Acc" in token.morph or "Case=Dat" in token.morph) and token.text[-3:-1] in suffixes \
            and token not in nouns:
                nouns.append(token)
                
    return nouns, ext, label


def transitive_verbs(doc):
    label = "tr"
    ext = "transitivity"

    pos = ["NOUN", "PRON", "PROPN"]

    tokens = [token for token in doc if any(child for child in token.children if child.pos_ in pos) 
    and token.pos_ == "VERB" and "VerbForm=Inf" not in token.morph]

    return tokens, ext, label


def intransitive_verbs(doc):
    label = "intr"
    ext = "transitivity"

    pos = ["NOUN", "PRON", "PROPN"]

    tokens = [token for token in doc if not any(child for child in token.children if child.pos_ in pos) 
             and token.pos_ == "VERB"]

    return tokens, ext, label


FUNCTION_LIST = [ 
first_conj,
second_conj,
third_conj,
fourth_conj,
transitive_verbs,
intransitive_verbs
]
