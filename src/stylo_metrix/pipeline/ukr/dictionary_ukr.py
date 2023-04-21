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


# Tagset based on UD 
POS_DICT = {key: value.upper().split() for key, value in {
    'adj': 'ADJ',
    'adv': 'ADV',
    'v': 'AUX VERB',
    'det': 'DET',
    'intj': 'INTJ',
    'conj': 'CCONJ SCONJ',
    'n': 'NOUN PROPN',
    'pro': 'PRON',
    'part': 'PART',
    'num': 'NUM',
    'prep': 'ADP',
    'punct': 'PUNCT',
    'other': "X",
    'symb': "SYM"
}.items()}

# POS based on UD 
WORDS_POS = 'adj adv v intj det conj n pro part num prep'.split()

