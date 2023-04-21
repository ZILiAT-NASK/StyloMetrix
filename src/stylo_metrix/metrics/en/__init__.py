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

from stylo_metrix.structures import Lang

class EnLang(Lang):
    definitions = ['english', 'angielski', 'en', 'eng']
    spacy_model = 'en_core_web_trf'

from .distance_en import *
from .grammatical_forms import *
from .parts_of_speech_en import *
from .lexical_en import *
from .syntactic_en import *
from .verb_tenses_en import *
from .text_statistics import *
from .figures_of_speech import *
from .psycholinguistics import *
from .text_statistics import *
from .social_media import *