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

class PlLang(Lang):
    definitions = ['polish', 'polski', 'pl', 'pol']
    spacy_model = 'pl_nask'

from .descriptive import *
from .graphical import *
from .inflection import *
from .lexis import *
from .part_of_speech import *
from .psycholinguistics import *
from .punctuation import *
from .syntactic import *