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
class Pronouns(Category):
    lang = 'en'
    name_en = "Pronouns"

"""
SUBJECT PRONOUNS
"""

class L_I_PRON(Metric):
    category = Pronouns
    name_en = "'I' pronoun"

    def count(doc):
        pers_pron = [token for token in doc if token.pos_ == "PRON" and ("Person=1" in token.morph) and ("Number=Sing" in token.morph)]
        result = len(pers_pron) / len(doc.text.split())
        debug = {'TOKENS': pers_pron}
        return result, debug



class L_HE_PRON(Metric):
    category = Pronouns
    name_en = "'He' pronoun"

    def count(doc):
        search = [token for token in doc if token.lower_ == "he"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_SHE_PRON(Metric):
    category = Pronouns
    name_en = "'She' pronoun"

    def count(doc):
        search = [token for token in doc if token.lower_ == "she"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_IT_PRON(Metric):
    category = Pronouns
    name_en = "'It' pronoun"

    def count(doc):
        search = [token for token in doc if token.lower_ == "it" and "Case=Nom" in token.morph]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_YOU_PRON(Metric):
    category = Pronouns
    name_en = "'You' pronoun"

    def count(doc):
        search = [token for token in doc if token.lower_ == "you" and "Case=Nom" in token.morph]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_WE_PRON(Metric):
    category = Pronouns
    name_en = "'We' pronoun"

    def count(doc):
        search = [token for token in doc if token.lower_ == "we"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_THEY_PRON(Metric):
    category = Pronouns
    name_en = "'They' pronoun"

    def count(doc):
        search = [token for token in doc if token.lower_ == "they"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


"""
OBJECT PRONOUNS
"""

class L_ME_PRON(Metric):
    category = Pronouns
    name_en = "'Me' pronoun"

    def count(doc):
        search = [token for token in doc if token.lower_ == "me"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_YOU_OBJ_PRON(Metric):
    category = Pronouns
    name_en = "'You' object pronoun"

    def count(doc):
        search = [token for token in doc if token.lower_ == "you" and "Case=Nom" not in token.morph]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_HIM_PRON(Metric):
    category = Pronouns
    name_en = "'Him' object pronoun"

    def count(doc):
        search = [token for token in doc if token.lower_ == "him"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_HER_OBJECT_PRON(Metric):
    category = Pronouns
    name_en = "'Her' object pronoun"

    def count(doc):
        search = [token for token in doc if token.lower_ == "her" and "Case=Acc" in token.morph]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_IT_OBJECT_PRON(Metric):
    category = Pronouns
    name_en = "'It' pronoun"

    def count(doc):
        search = [token for token in doc if token.lower_ == "it" and "Case=Acc" in token.morph]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_US_PRON(Metric):
    category = Pronouns
    name_en = "'Us' pronoun"

    def count(doc):
        search = [token for token in doc if token.lower_ == "us"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_THEM_PRON(Metric):
    category = Pronouns
    name_en = "'Them' pronoun"

    def count(doc):
        search = [token for token in doc if token.lower_ == "them"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


"""
POSESSIVE PRONOUNS
"""

class L_MY_PRON(Metric):
    category = Pronouns
    name_en = "'My' pronoun"

    def count(doc):
        search = [token for token in doc if token.lower_ == "my"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_YOUR_PRON(Metric):
    category = Pronouns
    name_en = "'Your' pronoun"

    def count(doc):
        search = [token for token in doc if token.lower_ == "your"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_HIS_PRON(Metric):
    category = Pronouns
    name_en = "'His' pronoun"

    def count(doc):
        search = [token for token in doc if token.lower_ == "his"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_HER_PRON(Metric):
    category = Pronouns
    name_en = "'Her' possessive pronoun"

    def count(doc):
        search = [token for token in doc if token.lower_ == "her" and "Poss=Yes" in token.morph]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_ITS_PRON(Metric):
    category = Pronouns
    name_en = "'Its' possessive pronoun"

    def count(doc):
        search = [token for token in doc if token.lower_ == "its"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_OUR_PRON(Metric):
    category = Pronouns
    name_en = "'Our' possessive pronoun"

    def count(doc):
        search = [token for token in doc if token.lower_ == "our"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_THEIR_PRON(Metric):
    category = Pronouns
    name_en = "'Their' possessive pronoun"

    def count(doc):
        search = [token for token in doc if token.lower_ == "their"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_YOURS_PRON(Metric):
    category = Pronouns
    name_en = "'Yours' pronoun"

    def count(doc):
        search = [token for token in doc if token.lower_ == "yours"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_THEIRS_PRON(Metric):
    category = Pronouns
    name_en = "'Theirs' pronoun"

    def count(doc):
        search = [token for token in doc if token.lower_ == "theirs"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_HERS_PRON(Metric):
    category = Pronouns
    name_en = "'Hers' pronoun"

    def count(doc):
        search = [token for token in doc if token.lower_ == "hers"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_OURS_PRON(Metric):
    category = Pronouns
    name_en = "'Ours' possessive pronoun"

    def count(doc):
        search = [token for token in doc if token.lower_ == "ours"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


"""
REFLEXIVE PRONOUNS
"""

class L_MYSELF_PRON(Metric):
    category = Pronouns
    name_en = "'Myself' pronoun"

    def count(doc):
        search = [token for token in doc if token.lower_ == "myself"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_YOURSELF_PRON(Metric):
    category = Pronouns
    name_en = "'Yourself' pronoun"

    def count(doc):
        search = [token for token in doc if token.lower_ == "yourself"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_HIMSELF_PRON(Metric):
    category = Pronouns
    name_en = "'Himself' pronoun"

    def count(doc):
        search = [token for token in doc if token.lower_ == "himself"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_HERSELF_PRON(Metric):
    category = Pronouns
    name_en = "'Herself' pronoun"

    def count(doc):
        search = [token for token in doc if token.lower_ == "herself"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_ITSELF_PRON(Metric):
    category = Pronouns
    name_en = "'Itself' pronoun"

    def count(doc):
        search = [token for token in doc if token.lower_ == "itself"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_OURSELVES_PRON(Metric):
    category = Pronouns
    name_en = "'Ourselves' pronoun"

    def count(doc):
        search = [token for token in doc if token.lower_ == "ourselves"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug

class L_YOURSELVES_PRON(Metric):
    category = Pronouns
    name_en = "'Yourselves' pronoun"

    def count(doc):
        search = [token for token in doc if token.lower_ == "yourselves"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_THEMSELVES_PRON(Metric):
    category = Pronouns
    name_en = "'Themselves' pronoun"

    def count(doc):
        search = [token for token in doc if token.lower_ == "themselves"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


"""PRONOUNS GENERAL CASES"""


class L_FIRST_PERSON_SING_PRON(Metric):
    category = Pronouns
    name_en = "First person singular pronouns"

    def count(doc):
        search = [token for token in doc if "Person=1" in token.morph and "Number=Sing" in token.morph and token.pos_ == "PRON"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug
    

class L_SECOND_PERSON_PRON(Metric):
    category = Pronouns
    name_en = "Second person pronouns"

    def count(doc):
        search = [token for token in doc if "Person=2" in token.morph and token.pos_ == "PRON"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_THIRD_PERSON_SING_PRON(Metric):
    category = Pronouns
    name_en = "Third person singular pronouns"

    def count(doc):
        search = [token for token in doc if "Person=3" in token.morph and "Number=Sing" in token.morph and token.pos_ == "PRON"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug


class L_THIRD_PERSON_PLURAL_PRON(Metric):
    category = Pronouns
    name_en = "Third person plural pronouns"

    def count(doc):
        search = [token for token in doc if "Person=3" in token.morph and "Number=Plur" in token.morph and token.pos_ == "PRON"]
        result = ratio(len(search), len(doc.text.split()))
        debug = {'TOKENS': search}
        return result, debug  




