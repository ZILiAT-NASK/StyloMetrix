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

from ...utils import ratio
from pathlib import Path
import pandas as pd
import os

ANIM = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/hurtlex/animals.txt'), "r", encoding='utf-8').read().split("\n")
DDP_ = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/hurtlex/cognitive_disabilities.txt'), "r", encoding='utf-8').read().split("\n")
SVP_ = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/hurtlex/deadly_sins.txt'), "r", encoding='utf-8').read().split("\n")
CDS_ = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/hurtlex/derogatory_words.txt"), "r", encoding='utf-8').read().split("\n")
DDF_ = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/hurtlex/disabilities.txt"), "r", encoding='utf-8').read().split("\n")
IS_ = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/hurtlex/economic_disadvantage.txt"), "r", encoding='utf-8').read().split("\n")
PS_ = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/hurtlex/ethnic_slurs.txt"), "r", encoding='utf-8').read().split("\n")
RE_ = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/hurtlex/felonies.txt"), "r", encoding='utf-8').read().split("\n")
ASF_ = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/hurtlex/female_genetalia.txt"), "r", encoding='utf-8').read().split("\n")
ASM_ = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/hurtlex/male_genetalia.txt"), "r", encoding='utf-8').read().split("\n")
OM_ = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/hurtlex/homosexuality.txt"), "r", encoding='utf-8').read().split("\n")
RCI_ = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/hurtlex/locations.txt"), "r", encoding='utf-8').read().split("\n")
DMC_ = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/hurtlex/moral.txt"), "r", encoding='utf-8').read().split("\n")
OR_ = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/hurtlex/plants.txt"), "r", encoding='utf-8').read().split("\n")
QAS_ = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/hurtlex/potential.txt"), "r", encoding='utf-8').read().split("\n")
PA_ = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/hurtlex/professions.txt"), "r", encoding='utf-8').read().split("\n")
PR_ = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/hurtlex/prostitution.txt"), "r", encoding='utf-8').read().split("\n")

class Hurtlex(Category):
    """
    Lexical metric based on Hurtlex: https://github.com/valeriobasile/hurtlex
    Each class is a category of profanity words. 
    """
    lang = 'en'
    name_en = "Hurtlex"

class AN(Metric):
    category = Hurtlex
    name_en = "Animals"

    def count(doc):
        words = [word.strip("\t") for word in ANIM]
        search = [token for token in doc if token.lemma_.lower()  in words]
        result = ratio(len(search), len(doc.text.split()))
        debug = {"TOKENS": search}
        return result, debug
        

class DDP(Metric):
    category = Hurtlex
    name_en = "cognitive disabilities and diversity"

    def count(doc):
        words = [word.strip("\t") for word in DDP_]
        search = [token for token in doc if token.lemma_.lower()  in words]
        result = ratio(len(search), len(doc.text.split()))
        debug = {"TOKENS": search}
        return result, debug


class SVP(Metric):
    category = Hurtlex
    name_en = "words related to the seven deadly sins of the Christian tradition"

    def count(doc):
        words =  [word.strip("\t") for word in SVP_]
        search = [token for token in doc if token.lemma_.lower() in words]
        result = ratio(len(search), len(doc.text.split()))
        debug = {"TOKENS": search}
        return result, debug


class CDS(Metric):
    category = Hurtlex
    name_en = "derogatory words"

    def count(doc):
        words = [word.strip("\t") for word in CDS_]
        search = [token for token in doc if token.lemma_.lower() in words]
        result = ratio(len(search), len(doc.text.split()))
        debug = {"TOKENS": search}
        return result, debug


class DDF(Metric):
    category = Hurtlex
    name_en = "physical disabilities and diversity"

    def count(doc):
        
        words = [word.strip("\t") for word in DDF_]
        search = [token for token in doc if token.lemma_.lower() in words]
        result = ratio(len(search), len(doc.text.split()))
        debug = {"TOKENS": search}
        return result, debug
        
class IS(Metric):
    category = Hurtlex
    name_en = "words related to social and economic disadvantage"

    def count(doc):
        words = [word.strip("\t") for word in IS_]
        search = [token for token in doc if token.lemma_.lower() in words]
        result = ratio(len(search), len(doc.text.split()))
        debug = {"TOKENS": search}
        return result, debug


class PS(Metric):
    category = Hurtlex
    name_en = "negative stereotypes ethnic slurs"

    def count(doc):
        words = [word.strip("\t") for word in PS_]
        search = [token for token in doc if token.lemma_.lower() in words]
        result = ratio(len(search), len(doc.text.split()))
        debug = {"TOKENS": search}
        return result, debug


class RE(Metric):
    category = Hurtlex
    name_en = "felonies and words related to crime and immoral behavior"

    def count(doc):
        words = [word.strip("\t") for word in RE_]
        search = [token for token in doc if token.lemma_.lower() in words]
        result = ratio(len(search), len(doc.text.split()))
        debug = {"TOKENS": search}
        return result, debug
        

class ASF(Metric):
    category = Hurtlex
    name_en = "female genitalia"

    def count(doc):
        words = [word.strip("\t") for word in ASF_]
        search = [token for token in doc if token.lemma_.lower() in words]
        result = ratio(len(search), len(doc.text.split()))
        debug = {"TOKENS": search}
        return result, debug


class ASM(Metric):
    category = Hurtlex
    name_en = "male genitalia"

    def count(doc):
        words = [word.strip("\t") for word in ASM_]
        search = [token for token in doc if token.lemma_.lower() in words]
        result = ratio(len(search), len(doc.text.split()))
        debug = {"TOKENS": search}
        return result, debug
        

class OM(Metric):
    category = Hurtlex
    name_en = "words related to homosexuality"

    def count(doc):
        words = [word.strip("\t") for word in OM_]
        search = [token for token in doc if token.lemma_.lower() in words]
        result = ratio(len(search), len(doc.text.split()))
        debug = {"TOKENS": search}
        return result, debug

class RCI(Metric):
    category = Hurtlex
    name_en = "locations and demonyms"

    def count(doc):
        words = [word.strip("\t") for word in RCI_]
        search = [token for token in doc if token.lemma_.lower() in words]
        result = ratio(len(search), len(doc.text.split()))
        debug = {"TOKENS": search}
        return result, debug
        

class DMC(Metric):
    category = Hurtlex
    name_en = "moral and behavioral defects"

    def count(doc):
        words = [word.strip("\t") for word in DMC_]
        search = [token for token in doc if token.lemma_.lower() in words]
        result = ratio(len(search), len(doc.text.split()))
        debug = {"TOKENS": search}
        return result, debug


class OR(Metric):
    category = Hurtlex
    name_en = "plants"

    def count(doc):
        words = [word.strip("\t") for word in OR_]
        search = [token for token in doc if token.lemma_.lower() in words]
        result = ratio(len(search), len(doc.text.split()))
        debug = {"TOKENS": search}
        return result, debug


class QAS(Metric):
    category = Hurtlex
    name_en = "with potential negative connotations"

    def count(doc):
        words = [word.strip("\t") for word in QAS_]
        search = [token for token in doc if token.lemma_.lower() in words]
        result = ratio(len(search), len(doc.text.split()))
        debug = {"TOKENS": search}
        return result, debug
        

class PA(Metric):
    category = Hurtlex
    name_en = "professions and occupations"

    def count(doc):
        words = [word.strip("\t") for word in PA_]
        search = [token for token in doc if token.lemma_.lower() in words]
        result = ratio(len(search), len(doc.text.split()))
        debug = {"TOKENS": search}
        return result, debug
        

class PR(Metric):
    category = Hurtlex
    name_en = "words related to prostitution"

    def count(doc):
        words = [word.strip("\t") for word in PR_]
        search = [token for token in doc if token.lemma_.lower() in words]
        result = ratio(len(search), len(doc.text.split()))
        debug = {"TOKENS": search}
        return result, debug


