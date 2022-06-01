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


# Tagset dicts - Exclusive categories

TAGS_DICT = {key: value.upper().split() for key, value in {
    'adj': 'JJ JJR JJS',
    'adv': 'RB RBR RBS',
    'v': 'VB VBD VBG VBN VBP VBZ MD AUX',
    'to': 'TO',
    'det': 'DT PDT',
    'conj': 'CC IN',
    'n': 'NN NNS NNP NNPS',
    'pro': 'PRP PRP$',
    'part': 'RP'
}.items()}

# Tagsets
# WORDS_POS = 'abbr adj adv conj fore n num oth part prep pro v'.split()
# CONTENT_WORDS_POS = 'v n adj num adv prep'.split()
# PERS_PRO_TAGS = 'ppron12 ppron3'.split()
