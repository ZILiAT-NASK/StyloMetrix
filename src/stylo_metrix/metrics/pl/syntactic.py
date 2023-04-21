# Copyright (C) 2023  NASK PIB
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


from stylo_metrix.structures import Metric, Category

from stylo_metrix.utils import incidence, ratio


class Syntactic(Category):
    lang = 'pl'
    name_en = "Syntactic"
    name_local = "Składniowe"


class SY_S_DE(Metric):
    category = Syntactic
    name_en = "Words in declarative sentences incidence"
    name_local = "Wyrazy w zdaniach oznajmujących"

    def count(doc):
        sents = [sent for sent in doc.sents if sent[-1].text in ['.', '…']]
        words = sum([[token for token in sent if token._.is_word] for sent in sents], [])
        result = incidence(doc, words)
        debug = {'TOKENS': words}
        return result, debug


class SY_S_IN(Metric):
    category = Syntactic
    name_en = "Words in interrogative sentences incidence"
    name_local = "Wyrazy w zdaniach pytających"

    def count(doc):
        sents = [sent for sent in doc.sents if sent[-1].text in ['?']]
        words = sum([[token for token in sent if token._.is_word] for sent in sents], [])
        result = incidence(doc, words)
        debug = {'TOKENS': words}
        return result, debug


class SY_S_EX(Metric):
    category = Syntactic
    name_en = "Words in exclamative sentences incidence"
    name_local = "Wyrazy w zdaniach rozkazujących"

    def count(doc):
        sents = [sent for sent in doc.sents if sent[-1].text in ['!']]
        words = sum([[token for token in sent if token._.is_word] for sent in sents], [])
        result = incidence(doc, words)
        debug = {'TOKENS': words}
        return result, debug


class SY_S_INIT(Metric):
    category = Syntactic
    name_en = "Words being initial word in sentence incidence"
    name_local = "Wyrazy będące pierwszym wyrazem zdania"

    def count(doc):
        words = [sent[0] for sent in doc.sents]
        result = incidence(doc, words)
        debug = {'TOKENS': words}
        return result, debug


class SY_NPHR(Metric):
    category = Syntactic
    name_en = "Words in nominal phrases incidence"
    name_local = "Wyrazy we frazach nominalnych"

    def count(doc):
        nouns = [token for token in doc if token.pos_ == 'NOUN']
        nouns_not_part_of_subtree = []
        for noun in nouns:
            list_without_current = [n for n in nouns if n is not noun]
            subtrees = [list(noun.subtree) for noun in list_without_current]
            subtrees_list = sum(subtrees, [])
            if noun not in subtrees_list:
                nouns_not_part_of_subtree.append(noun)
        subtrees = [[word for word in list(noun.subtree) if word._.is_word] for noun in nouns_not_part_of_subtree]
        sum_subtrees = sum(subtrees, [])
        result = incidence(doc, sum_subtrees)
        debug = {"TOKENS": subtrees}
        return result, debug


class SY_MOD(Metric):
    category = Syntactic
    name_en = "Words in modifiers incidence"
    name_local = "Wyrazy w przydawkach"

    def count(doc):
        mod_tags = ['amod', 'nmod', 'nmod:arg', 'acl']
        nouns = [token for token in doc if token.pos_ == "NOUN"]
        children_mods = [[ch for ch in list(noun.children) if ch.dep_ in mod_tags] for noun in nouns]
        mods_heads = sum(children_mods, [])
        mods_not_part_of_subtree = []
        for mod in mods_heads:
            list_without_current = [m for m in mods_heads if m is not mod]
            subtrees = [list(mod.subtree) for mod in list_without_current]
            subtrees_list = sum(subtrees, [])
            if mod not in subtrees_list:
                mods_not_part_of_subtree.append(mod)
        subtrees = [[el for el in list(head.subtree) if el._.is_word] for head in mods_not_part_of_subtree]
        sum_subtrees = sum(subtrees, [])
        result = incidence(doc, sum_subtrees)
        debug = {"TOKENS": subtrees}
        return result, debug


class SY_INV_EP(Metric):
    category = Syntactic
    name_en = "Epithet inversion"
    name_local = "Inwersja epitetu"

    def count(doc):
        inv = [doc[start:end] for match_id, start, end
                    in doc._.matches
                    if doc.vocab.strings[match_id] == SY_INV_EP.code]
        count = sum(len(i) for i in inv)
        debug = {'TOKENS': inv}
        return ratio(count, doc._.n_tokens), debug


class SY_INV_OBJ(Metric):
    category = Syntactic
    name_en = "Inversion - object as sentence start"
    name_local = "Inwersja - rozpoczęcie zdania od dopełnienia"

    def count(doc):
        sents = [[token for token in sent if token.dep_ == "iobj" and token.i < token.head.i] for sent in doc.sents]
        count = len(sum(sents, []))
        debug = {'TOKENS': sents}
        return ratio(count, doc._.n_tokens), debug


class SY_SUBORD(Metric):
    category = Syntactic
    name_en = "Subordinating conjunctions"
    name_local = "Łączniki zdań podrzędnie złożonych"

    def count(doc):
        sconj = list(token.text for token in doc if token.pos_ == 'SCONJ')
        count = len(sconj)
        debug = {'TOKENS': sconj}
        return ratio(count, doc._.n_tokens), debug


class SY_COORD(Metric):
    category = Syntactic
    name_en = "Coordinating conjunctions"
    name_local = "Łączniki zdań współrzędnie złożonych"

    def count(doc):
        cconj = list(token.text for token in doc if token.pos_ == 'CCONJ')
        count = len(cconj)
        debug = {'TOKENS': cconj}
        return ratio(count, doc._.n_tokens), debug


class SY_COND(Metric):
    category = Syntactic
    name_en = "Conditional conjunctions"
    name_local = "Spójniki warunkowe"

    def count(doc):
        vocab = ['jeśli', 'jeżeli', 'skoro']
        conditions = list(token.text for token in doc if token.lower_ in vocab)
        debug = {'TOKENS': conditions}
        return ratio(len(conditions), doc._.n_tokens), debug


class SY_NOM_SENT(Metric):
    category = Syntactic
    name_en = "Nominal phrases"
    name_local = "Równoważniki zdań"

    def count(doc):
        sents = [list(sent) for sent in doc.sents if not any(t.pos_ == 'VERB' for t in sent)]
        tokens = sum(sents, [])
        filtered_tokens = [t for t in tokens if t in doc._.tokens]
        result = ratio(len(filtered_tokens), doc._.n_tokens)
        debug = {'VALUES': sents}
        return result, debug


# SYNTACTIC = [
#     SY_S_DE,
#     SY_S_IN,
#     SY_S_EX,
#     SY_S_INIT,
#     SY_NPHR,
#     SY_MOD,
#     SY_INV_EP,
#     SY_INV_OBJ,
#     SY_SUBORD,
#     SY_COORD,
#     SY_COND,
#     SY_NOM_SENT,
# ]

# syntactic_group = MetricsGroup([m() for m in SYNTACTIC])
