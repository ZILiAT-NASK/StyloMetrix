from abc import ABC

from stylo_metrix.structures import Metric, MetricsGroup
from stylo_metrix.utils import incidence


class Syntactic(Metric, ABC):
    category_pl = "Syntactic"
    category_en = "Składniowe"


class SY_S_DE(Syntactic):
    name_en = "Words in declarative sentences incidence"
    name_pl = "Występowanie wyrazów należących do zdań oznajmujących wśród wszystkich wyrazów"

    def count(self, doc):
        sents = [sent for sent in doc.sents if sent[-1].text in ['.', '…']]
        words = sum([[token for token in sent if token._.is_word] for sent in sents], [])
        result = incidence(doc, words)
        return result, {}


class SY_S_IN(Syntactic):
    name_en = "Words in interrogative sentences incidence"
    name_pl = "Występowanie wyrazów należących do zdań pytających wśród wszystkich wyrazów"

    def count(self, doc):
        sents = [sent for sent in doc.sents if sent[-1].text in ['?']]
        words = sum([[token for token in sent if token._.is_word] for sent in sents], [])
        result = incidence(doc, words)
        return result, {}


class SY_S_EX(Syntactic):
    name_en = "Words in exclamative sentences incidence"
    name_pl = "Występowanie wyrazów należących do zdań rozkazujących wśród wszystkich wyrazów"

    def count(self, doc):
        sents = [sent for sent in doc.sents if sent[-1].text in ['!']]
        words = sum([[token for token in sent if token._.is_word] for sent in sents], [])
        result = incidence(doc, words)
        return result, {}


class SY_S_INIT(Syntactic):
    name_en = "Words being initial words in sentence incidence"
    name_pl = "Procent wyrazów będących pierwszym wyrazem zdania"

    def count(self, doc):
        words = [sent[0] for sent in doc.sents]
        result = incidence(doc, words)
        return result, {}


class SY_NPHR(Syntactic):
    name_en = "Words in nominal phrases incidence"
    name_pl = "Procent wyrazów wchodzących w skład fraz nominalnych wśród wszystkich wyrazów"

    def count(self, doc):
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
        return result, {
            "[SUBTREES]": subtrees,
        }


class SY_MOD(Syntactic):
    name_en = "Words in modifiers incidence"
    name_pl = "Procent wyrazów wchodzących w skład przydawek wśród wszystkich wyrazów"

    def count(self, doc):
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
        return result, {
            "[SUBTREES]": subtrees
        }


SYNTACTIC = [
    SY_S_DE,
    SY_S_IN,
    SY_S_EX,
    SY_S_INIT,
    SY_NPHR,
    SY_MOD,
]

syntactic_group = MetricsGroup([m() for m in SYNTACTIC])
