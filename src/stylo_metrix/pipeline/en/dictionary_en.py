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
    'adj': 'ADJ',
    'adv': 'ADV',
    'v': 'AUX VERB',
    'det': 'DET',
    'intj': 'INTJ',
    'conj': 'CONJ CCONJ SCONJ',
    'n': 'NOUN PROPN',
    'pro': 'PRON',
    'part': 'PART',
    'num': 'NUM',
    'prep': 'ADP'
}.items()}

# Tagsets
WORDS_POS = 'adj adv v intj det conj n pro part num prep'.split()

# https://semanticsimilarity.wordpress.com/function-word-lists/
# lemmas
FUNCTION_WORDS = """
a about above across after afterwards again against all almost alone along already also although always am among
amongst amoungst an and another any anyhow anyone anything anyway anywhere be around as at be became because be before
beforehand behind be below beside besides between beyond both but by can can could dare despite do do do do down during
each eg either else elsewhere enough etc even ever every everyone everything everywhere except few first for former
formerly from far furthermore have have have he hence she here hereabouts hereafter hereby herein hereinafter heretofore
hereunder hereupon herewith hers herself he himself his how however I ie if in indeed inside instead into be it its
itself last latter latterly least less lot lot many may I meanwhile might mine more moreover most mostly much must my
myself namely near need neither never nevertheless next no nobody none noone nor not nothing now nowhere of off often
oftentimes on once one only onto or other other otherwise ought our ours ourselves out outside over per perhaps rather
re same second several shall she should since so some somehow someone something sometime sometimes somewhat somewhere
still such than that the their their they themselves then thence there thereabouts thereafter thereby therefore therein
thereof thereon thereupon these they third this those though through throughout thru thus to together too top toward
towards under until up upon we use very via be we well be what whatever when whence whenever where whereafter whereas
whereby wherein whereupon wherever whether which while whither who whoever whole whom whose why whyever will with within
without would yes yet you your your yourself yourselves
""".strip().split()
