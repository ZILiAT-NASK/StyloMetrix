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

from utils import incidence, select, ratio


class GrammaticalForms(Category):
    lang = 'pl'
    name_en = "Grammatical Forms"
    name_local = "Formy gramatyczne"


class G_V(Metric):
    category = GrammaticalForms
    name_en = "Verb"
    name_local = "Czasowniki"

    def count(doc):
        selection = select(doc, {'pos': 'v'})
        result = incidence(doc, selection)
        debug = {'VALUES': selection}
        return result, debug


class G_N(Metric):
    category = GrammaticalForms
    name_en = "Nouns"
    name_local = "Rzeczowniki"

    def count(doc):
        selection = select(doc, {'pos': 'n'})
        result = incidence(doc, selection)
        debug = {'VALUES': selection}
        return result, debug


class G_ADJ(Metric):
    category = GrammaticalForms
    name_en = "Adjectives"
    name_local = "Przymiotniki"

    def count(doc):
        selection = select(doc, {'pos': 'adj'})
        result = incidence(doc, selection)
        debug = {'VALUES': selection}
        return result, debug


class G_ADV(Metric):
    category = GrammaticalForms
    name_en = "Adverbs"
    name_local = "Przysłówki"

    def count(doc):
        selection = select(doc, {'pos': 'adv'})
        result = incidence(doc, selection)
        debug = {'VALUES': selection}
        return result, debug


class G_PRO(Metric):
    category = GrammaticalForms
    name_en = "Pronouns"
    name_local = "Zaimki"

    def count(doc):
        selection = select(doc, {'pos': 'pro'})
        result = incidence(doc, selection)
        debug = {'VALUES': selection}
        return result, debug


class G_PRO_DEM(Metric):
    category = GrammaticalForms
    name_en = "Demonstrative pronouns"
    name_local = "Zaimki wskazujące"

    def count(doc):
        selection = select(doc, {'pos': 'pro', 'pronoun_type': 'dem'})
        result = incidence(doc, selection)
        debug = {'VALUES': selection}
        return result, debug
    

class APOSTROFA_ADJ(Metric):
    category = GrammaticalForms
    name_en = "Descriptive apostrophe"
    name_local = "Apostrofa opisowa"

    def count(doc):
        c = 0
        results = []
        dets = ["det", "amod"]
        for sent in doc.sents:
            inn7w = list(
                token.text
                for token in sent
                if token.pos_ == "NOUN" and str(token.morph.get("Case")) == "['Voc']"
            )
            pron = [
                token.text
                for token in sent
                if token.dep_ in dets and token.head.text in inn7w
            ]
            if inn7w and pron:
                results.append(sent)
                c = c + len(inn7w) + len(pron)
        debug = {"FOUND": results}
        return ratio(c, doc._.n_tokens), debug
    

class APOSTROFA_VERB(Metric):
    category = GrammaticalForms
    name_en = "Apostrophe together with a verb"
    name_local = "Apostrofa wraz z czasownikiem"

    def count(doc):
        c = 0
        results = []
        dets = ["det", "amod"]
        for sent in doc.sents:
            inn7w = list(
                token.text
                for token in sent
                if token.pos_ == "NOUN" and str(token.morph.get("Case")) == "['Voc']"
            )
            pron = [
                token.text
                for token in sent
                if token.pos_ == "VERB" and str(token.morph.get("Person")) == "['2']"
            ]
            if inn7w and pron:
                results.append(sent)
                c = c + len(inn7w) + len(pron)
        debug = {"FOUND": results}
        return ratio(c, doc._.n_tokens), debug
    

class VOC_CONTENT(Metric):
    category = GrammaticalForms
    name_en = "Apostrophe and amount of content words"
    name_local = "Apostrofa i ilość content words"

    def count(doc):
        c = 0
        results = []
        for sent in doc.sents:
            inn7w = list(
                token.text
                for token in sent
                if token.pos_ == "NOUN" and str(token.morph.get("Case")) == "['Voc']"
            )
            pron = [token.text for token in sent if token._.content_word == "cont"]
            if inn7w and pron:
                results.append(sent)
                c = c + len(inn7w) + len(pron)
        debug = {"FOUND": results}
        return ratio(c, doc._.n_tokens), debug