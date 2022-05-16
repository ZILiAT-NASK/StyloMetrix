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


import re

from stylo_metrix.pipeline.pl.pl_nask.dictionary_pl import DEMONSTRATIVE_PRONOUNS_LEMMAS, INFL_VERBS_TAGS, LEMMAS_DICT, \
    PRO_DICT, TAGS_DICT, WORDS_TAGS, CONTENT_WORDS, NON_CONTENT_WORDS


def classify_pos(token):
    if re.match(r"\s+", token.text):
        return 'ign'
    for pos, lemmas in LEMMAS_DICT.items():
        for lemma in lemmas:
            lemma_info = lemma.split('!')
            # if lemma_info[0] == "to":
            # print(lemma_info, token.tag_)
            if token.lemma_.lower() == lemma_info[0].lower():
                if len(lemma_info) > 1:
                    if token.tag_.split(':')[0] in lemma_info[1:]:
                        pass
                return pos
    for pos, tags in TAGS_DICT.items():
        if token.tag_.split(":")[0] in tags:
            return pos


def is_word(token):
    return token._.pos in WORDS_TAGS


def is_content_word(token):
    if token._.pos in CONTENT_WORDS:
        return 'cont'
    if token._.pos in NON_CONTENT_WORDS:
        return 'noncont'


def is_punctuation(token):
    return token._.pos == "pun"


def verb_inflection(token):
    if token.tag_.split(":")[0] == 'inf':
        children_tags = [token.tag_.split(":")[0] for token in token.children]
        if 'bedzie' in children_tags:
            return None
        return 'inf'
    if token.tag_.split(":")[0] in INFL_VERBS_TAGS:
        return 'infl'


def verb_person(token):
    # (p|s)(1|2|3) or None
    if token._.verb_inflection == 'infl':
        if token.i + 1 < len(token.doc) and token.doc[token.i + 1].tag_.split(":")[0] == 'aglt':
            feats = token.doc[token.i + 1].tag_.split(':')
        else:
            feats = token.tag_.split(':')
        res = ('p' if 'pl' in feats else '') + \
              ('s' if 'sg' in feats else '') + \
              ('1' if 'pri' in feats else '') + \
              ('2' if 'sec' in feats else '') + \
              ('3' if any(d in feats for d in ['ter', 'm1', 'm2', 'm3', 'f', 'n']) else '')
        if res != "":
            return res


def verb_future(token):
    if 'fin' in token.tag_.split(":") and 'perf' in token.tag_.split(':'):
        return 'futs'  # zrobię
    if 'bedzie' in token.tag_.split(":") and token.dep_ != 'aux':
        return 'futs'  # będzie (zielony)
    if 'praet' in token.tag_.split(":") or 'inf' in token.tag_.split(":"):
        children_tags = [token.tag_ for token in token.children]
        if 'bedzie' in children_tags:
            return 'futc'  # (będzie) robił


def verb_tense(token):
    # fut
    if token._.verb_future is not None:
        return 'fut'
    # pres
    if 'fin' in token.tag_.split(":") and 'imperf' in token.tag_.split(":"):
        return 'pres'  # robię
    # past
    if 'praet' in token.tag_.split(":"):
        return 'past'  # robił (oprócz (będzie) robił)


def verb_aspect(token):
    if token._.pos == 'v':
        if 'perf' in token.tag_.split(":"):
            return 'perf'
        if 'imperf' in token.tag_.split(":"):
            return 'imperf'


def verb_voice(token):
    if token._.pos == 'v':
        if 'impt' in token.tag_.split(":"):
            return 'impt'
        if 'qub' in token.tag_.split(":") and token.text == "by":
            return 'cond'


def participle_type(token):
    if token._.pos == 'v':
        if 'pcon' in token.tag_.split(":"):
            return 'pcon'
        if 'pant' in token.tag_.split(":"):
            return 'pant'
        if 'pact' in token.tag_.split(":"):
            return 'pact'
        if 'ppas' in token.tag_.split(":"):
            return 'ppas'


def noun_type(token):
    if 'ger' in token.tag_.split(":"):
        return 'ger'


def case(token):
    cases = ['nom', 'gen', 'dat', 'acc', 'inst', 'loc', 'voc']
    if token._.pos in ['n', 'adj', 'pro', 'num'] or token._.participle_type in ['pact', 'ppas']:
        attrs = token.tag_.split(":")
        for case in cases:
            if case in attrs:
                return case


def pronoun_type(token):
    if token._.pos == 'pro':
        if token.lemma_ in DEMONSTRATIVE_PRONOUNS_LEMMAS:
            return 'dem'
        for person, lemmas in PRO_DICT.items():
            if token.lemma_ in lemmas:
                return person
        feats = token.tag_.split(":")
        res = ('p' if 'pl' in feats else '') + \
              ('s' if 'sg' in feats else '') + \
              ('1' if 'pri' in feats else '') + \
              ('2' if 'sec' in feats else '') + \
              ('3' if 'ter' in feats else '')
        return res


def adjective_degree(token):
    if token._.pos == 'adj':
        if 'pos' in token.tag_.split(":"):
            return 'pos'
        if 'com' in token.tag_.split(":"):
            return 'com'
        if 'sup' in token.tag_.split(":"):
            return 'sup'


def adverb_degree(token):
    if token._.pos == 'adv':
        if 'pos' in token.tag_.split(":"):
            return 'pos'
        if 'com' in token.tag_.split(":"):
            return 'com'
        if 'sup' in token.tag_.split(":"):
            return 'sup'


def ign(token):
    return token._.pos == 'ign'
