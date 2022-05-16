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
TAGS_DICT = {key: value.split() for key, value in {
    'abbr': 'brev',
    'adj': 'adj adja adjp adjc',
    'adv': 'adv',
    'conj': 'conj comp',
    'fore': 'xxx',
    'ign': 'aglt ign',
    'n': 'subst depr ger',
    'num': 'num numcol',
    'oth': 'burk interj',
    'part': 'qub',
    'prep': 'prep',
    'pro': 'ppron12 ppron3 siebie',
    'pun': 'interp',
    'v': 'fin bedzie praet impt imps inf pcon pant pact ppas winien pred',
}.items()}

# Tagsets
WORDS_TAGS = 'abbr adj adv conj fore n num oth part prep pro v'.split()
CONTENT_WORDS = 'v n adj adv num pro'.split()
NON_CONTENT_WORDS = 'part conj prep abbr fore oth'.split()
INFL_VERBS_TAGS = 'fin bedzie praet impt'.split()
PERS_PRO_TAGS = 'ppron12 ppron3'.split()

# Exceptions lemmas
PRO_S1_LEMMAS = 'mój'.split()
PRO_P1_LEMMAS = 'nasz'.split()
PRO_LEMMAS = """
    co!comp!prep 
    jaki jakiś 
    każdy który 
    nic niektóry nikt 
    ów 
    sam!subst się swój!impt 
    taki!subst ten to!comp!conj!part!pred tym!conj
    wszyscy wszystek wszystko wtedy
    """.split()
# PRO_LEMMAS nie da się dobrze ustalić: inny jak pewny taki tam to???

PRO_DICT = {
    's1': PRO_S1_LEMMAS,
    'p1': PRO_P1_LEMMAS,
}

# PRONOUNS

# Zaimki rzeczowne
PRO_S1 = 'ja'.split()
PRO_S2 = 'ty'.split()
PRO_S3 = 'on ona ono'.split()
PRO_P1 = 'my'.split()
PRO_P2 = 'wy'.split()
PRO_P3 = 'oni one'.split()
SUBSTANTIVE_PRONOUNS_LEMMAS = PRO_S1 + PRO_S2 + PRO_S3 + PRO_P1 + PRO_P2 + PRO_P3

# Zaimki dzierżawcze
PPRO_S1 = 'mój'.split()
PPRO_S2 = 'twój'.split()
PPRO_S3 = 'jego jej'.split()
PPRO_P1 = 'nasz'.split()
PPRO_P2 = 'wasz'.split()
PPRO_P3 = 'ich'.split()
PPRO_OTHER = 'swój czyj czyjś czyjkolwiek niczyj'.split()
POSSESSIVE_PRONOUNS_LEMMAS = PPRO_S1 + PPRO_S2 + PPRO_S3 + PPRO_P1 + PPRO_P2 + PPRO_P3 + PPRO_OTHER

# Zaimki wg osoby
S1 = PRO_S1 + PPRO_S1
S2 = PRO_S2 + PPRO_S2
S3 = PRO_S3 + PPRO_S3
P1 = PRO_P1 + PPRO_P1
P2 = PRO_P2 + PPRO_P2
P3 = PRO_P3 + PPRO_P3

# Zaimki zwrotne
REFLEXIVE_PRONOUNS_LEMMAS = 'się siebie'.split()

# Zaimki określone (wskazujące)
DEMONSTRATIVE_PRONOUNS_LEMMAS = """
    ten ta to ci te tamten tamta tamto tamci tamte ów owa owo owi owe taki taka takie tacy takie tak tu tam stąd
    stamtąd tędy wtedy
    """.split()

# Zaimki pytajne i względne
INTERROGATIVE_AND_RELATIVE_PRONOUNS_LEMMAS = """
    kto co który jaki kiedy gdzie jak którędy skąd dokąd ile
    """.split()

# Zaimki nieokreślone
INDEFINITE_PRONOUNS_LEMMAS = \
    [pro + 'kolwiek' for pro in INTERROGATIVE_AND_RELATIVE_PRONOUNS_LEMMAS] + \
    [pro + 'ś' for pro in INTERROGATIVE_AND_RELATIVE_PRONOUNS_LEMMAS] + \
    'niektóry niejaki'.split()

# Zaimki upowszechniające
UNIVERSAL_PRONOUNS_LEMMAS = """
    każdy każda każde wszyscy wszystkie wszystko wszystek zawsze wszędzie
    """.split()

# Zaimki przeczące
NEGATIVE_PRONOUNS_LEMMAS = """
    nikt nic żaden żadna żadne niczyj nigdzie nigdy znikąd donikąd nijak
    """.split()

# Inne zaimki znalezione poza klasyfikacją
OTHER_PRONOUNS_LEMMAS = 'sam'.split()
# nie da się znaleźć: pewien

PRONOUNS_LEMMAS = \
    SUBSTANTIVE_PRONOUNS_LEMMAS + \
    POSSESSIVE_PRONOUNS_LEMMAS + \
    REFLEXIVE_PRONOUNS_LEMMAS + \
    DEMONSTRATIVE_PRONOUNS_LEMMAS + \
    INTERROGATIVE_AND_RELATIVE_PRONOUNS_LEMMAS + \
    INDEFINITE_PRONOUNS_LEMMAS + \
    UNIVERSAL_PRONOUNS_LEMMAS + \
    NEGATIVE_PRONOUNS_LEMMAS + \
    OTHER_PRONOUNS_LEMMAS

LEMMAS_DICT = {
    'pro': PRONOUNS_LEMMAS,
}
