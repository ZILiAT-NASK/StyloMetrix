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

from ...structures import Lang

class UkrLang(Lang):
    definitions = ['ukrainian', 'ukraiński', 'ukr']
    spacy_model = 'uk_core_news_trf'

from .lexical_ukr import *
from .parts_of_speech_ukr import *
from .verb_forms_ukr import *
from .syntactic_ukr import *
from .readability_ukr import *
