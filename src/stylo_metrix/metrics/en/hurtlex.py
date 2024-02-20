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


import os
from pathlib import Path

import pandas as pd

from ...structures import Category, Metric
from ...utils import ratio

ANIM = (
    open(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "data/hurtlex/animals.txt"
        ),
        "r",
        encoding="utf-8",
    )
    .read()
    .split("\n")
)
DDP_ = (
    open(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "data/hurtlex/cognitive_disabilities.txt",
        ),
        "r",
        encoding="utf-8",
    )
    .read()
    .split("\n")
)
SVP_ = (
    open(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "data/hurtlex/deadly_sins.txt"
        ),
        "r",
        encoding="utf-8",
    )
    .read()
    .split("\n")
)
CDS_ = (
    open(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "data/hurtlex/derogatory_words.txt",
        ),
        "r",
        encoding="utf-8",
    )
    .read()
    .split("\n")
)
DDF_ = (
    open(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "data/hurtlex/disabilities.txt"
        ),
        "r",
        encoding="utf-8",
    )
    .read()
    .split("\n")
)
IS_ = (
    open(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "data/hurtlex/economic_disadvantage.txt",
        ),
        "r",
        encoding="utf-8",
    )
    .read()
    .split("\n")
)
PS_ = (
    open(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "data/hurtlex/ethnic_slurs.txt"
        ),
        "r",
        encoding="utf-8",
    )
    .read()
    .split("\n")
)
RE_ = (
    open(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "data/hurtlex/felonies.txt"
        ),
        "r",
        encoding="utf-8",
    )
    .read()
    .split("\n")
)
ASF_ = (
    open(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "data/hurtlex/female_genetalia.txt",
        ),
        "r",
        encoding="utf-8",
    )
    .read()
    .split("\n")
)
ASM_ = (
    open(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "data/hurtlex/male_genetalia.txt",
        ),
        "r",
        encoding="utf-8",
    )
    .read()
    .split("\n")
)
OM_ = (
    open(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "data/hurtlex/homosexuality.txt"
        ),
        "r",
        encoding="utf-8",
    )
    .read()
    .split("\n")
)
RCI_ = (
    open(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "data/hurtlex/locations.txt"
        ),
        "r",
        encoding="utf-8",
    )
    .read()
    .split("\n")
)
DMC_ = (
    open(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "data/hurtlex/moral.txt"
        ),
        "r",
        encoding="utf-8",
    )
    .read()
    .split("\n")
)
OR_ = (
    open(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "data/hurtlex/plants.txt"
        ),
        "r",
        encoding="utf-8",
    )
    .read()
    .split("\n")
)
QAS_ = (
    open(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "data/hurtlex/potential.txt"
        ),
        "r",
        encoding="utf-8",
    )
    .read()
    .split("\n")
)
PA_ = (
    open(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "data/hurtlex/professions.txt"
        ),
        "r",
        encoding="utf-8",
    )
    .read()
    .split("\n")
)
PR_ = (
    open(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "data/hurtlex/prostitution.txt"
        ),
        "r",
        encoding="utf-8",
    )
    .read()
    .split("\n")
)


class Hurtlex(Category):
    """
    Lexical metric based on Hurtlex: https://github.com/valeriobasile/hurtlex
    Each class is a category of profanity words.
    """

    lang = "en"
    name_en = "Hurtlex"
    name_local = name_en


class AN(Metric):
    category = Hurtlex
    name_en = "Animals"
    name_local = name_en

    def count(doc):
        words = [word.strip() for word in ANIM]
        debug = [token.text for token in doc if token.lemma_.lower() in words]
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug


class DDP(Metric):
    category = Hurtlex
    name_en = "cognitive disabilities and diversity"
    name_local = name_en

    def count(doc):
        words = [word.strip() for word in DDP_]
        debug = [token.text for token in doc if token.lemma_.lower() in words]
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug


class SVP(Metric):
    category = Hurtlex
    name_en = "words related to the seven deadly sins of the Christian tradition"
    name_local = name_en

    def count(doc):
        words = [word.strip() for word in SVP_]
        debug = [token.text for token in doc if token.lemma_.lower() in words]
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug


class CDS(Metric):
    category = Hurtlex
    name_en = "derogatory words"
    name_local = name_en

    def count(doc):
        words = [word.strip() for word in CDS_]
        debug = [token.text for token in doc if token.lemma_.lower() in words]
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug


class DDF(Metric):
    category = Hurtlex
    name_en = "physical disabilities and diversity"
    name_local = name_en

    def count(doc):
        words = [word.strip() for word in DDF_]
        debug = [token.text for token in doc if token.lemma_.lower() in words]
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug


class IS(Metric):
    category = Hurtlex
    name_en = "words related to social and economic disadvantage"
    name_local = name_en

    def count(doc):
        words = [word.strip() for word in IS_]
        debug = [token.text for token in doc if token.lemma_.lower() in words]
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug


class PS(Metric):
    category = Hurtlex
    name_en = "negative stereotypes ethnic slurs"
    name_local = name_en

    def count(doc):
        words = [word.strip() for word in PS_]
        debug = [token.text for token in doc if token.lemma_.lower() in words]
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug


class RE(Metric):
    category = Hurtlex
    name_en = "felonies and words related to crime and immoral behavior"
    name_local = name_en

    def count(doc):
        words = [word.strip() for word in RE_]
        debug = [token.text for token in doc if token.lemma_.lower() in words]
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug


class ASF(Metric):
    category = Hurtlex
    name_en = "female genitalia"
    name_local = name_en

    def count(doc):
        words = [word.strip() for word in ASF_]
        debug = [token.text for token in doc if token.lemma_.lower() in words]
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug


class ASM(Metric):
    category = Hurtlex
    name_en = "male genitalia"
    name_local = name_en

    def count(doc):
        words = [word.strip() for word in ASM_]
        debug = [token.text for token in doc if token.lemma_.lower() in words]
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug


class OM(Metric):
    category = Hurtlex
    name_en = "words related to homosexuality"
    name_local = name_en

    def count(doc):
        words = [word.strip() for word in OM_]
        debug = [token.text for token in doc if token.lemma_.lower() in words]
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug


class RCI(Metric):
    category = Hurtlex
    name_en = "locations and demonyms"
    name_local = name_en

    def count(doc):
        words = [word.strip() for word in RCI_]
        debug = [token.text for token in doc if token.lemma_.lower() in words]
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug


class DMC(Metric):
    category = Hurtlex
    name_en = "moral and behavioral defects"
    name_local = name_en

    def count(doc):
        words = [word.strip() for word in DMC_]
        debug = [token.text for token in doc if token.lemma_.lower() in words]
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug


class OR(Metric):
    category = Hurtlex
    name_en = "plants"
    name_local = name_en

    def count(doc):
        words = [word.strip() for word in OR_]
        debug = [token.text for token in doc if token.lemma_.lower() in words]
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug


class QAS(Metric):
    category = Hurtlex
    name_en = "with potential negative connotations"
    name_local = name_en

    def count(doc):
        words = [word.strip() for word in QAS_]
        debug = [token.text for token in doc if token.lemma_.lower() in words]
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug


class PA(Metric):
    category = Hurtlex
    name_en = "professions and occupations"
    name_local = name_en

    def count(doc):
        words = [word.strip() for word in PA_]
        debug = [token.text for token in doc if token.lemma_.lower() in words]
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug


class PR(Metric):
    category = Hurtlex
    name_en = "words related to prostitution"
    name_local = name_en

    def count(doc):
        words = [word.strip() for word in PR_]
        debug = [token.text for token in doc if token.lemma_.lower() in words]
        result = ratio(len(debug), len(doc.text.split()))
        
        return result, debug
