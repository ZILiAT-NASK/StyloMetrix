from abc import ABC

from stylo_metrix.structures import Metric, MetricsGroup
from stylo_metrix.utils import incidence


class WordFormation(Metric, ABC):
    category_pl = "Word Formation"
    category_en = "Słowotwórcze"
    affixes = ""

    def find_words_affix(self, doc, affixes, starts, pos):
        affixes = affixes.split(", ")
        data = [token for token in doc if token._.pos == pos] if pos else doc
        search = [token for token in data if
                  any([token.lemma_.startswith(e) if starts else token.lemma_.endswith(e)
                       for e in affixes]) and token.lemma_ not in affixes]
        result = incidence(doc, search)
        return result, {}


class NounsEnd(WordFormation, ABC):
    affixes = ""
    name_en = ""
    name_pl = "Występowanie rzeczowników zakończonych na "

    def count(self, doc):
        result, debug = self.find_words_affix(doc, affixes=self.__class__.affixes, starts=False, pos='n')
        return result, debug


class WF_NE_OSC(NounsEnd):
    """ przyrostek bardzo częsty, tworzy pojęcia abstrakcyjne """
    affixes = "ość"


class WF_NE_IK(NounsEnd):
    """ zdrobnienia - częste w tekstach potocznych, internetowych """
    affixes = "ik"


class WF_NE_EK(NounsEnd):
    """ zdrobnienia - częste w tekstach potocznych, internetowych """
    affixes = "ek"


class WF_NE_KA(NounsEnd):
    """ zdrobnienia - częste w tekstach potocznych, internetowych """
    affixes = "ka"


class WF_NE_KO(NounsEnd):
    """ zdrobnienia - częste w tekstach potocznych, internetowych """
    affixes = "ko"


class WF_NE_IYCIEL(NounsEnd):
    """ wykonawcy czynności i nosiciele cech """
    affixes = "iciel, yciel"


class WF_NE_OWIEC(NounsEnd):
    """ wykonawcy czynności i nosiciele cech """
    affixes = "owiec"


class WF_NE_ARZ(NounsEnd):
    """ wykonawcy czynności i nosiciele cech """
    affixes = "arz"


class WF_NE_OWICZ(NounsEnd):
    """ wykonawcy czynności i nosiciele cech """
    affixes = "owicz"


# -----------------------------------------------------------------

class AdjectivesStart(WordFormation, ABC):
    affixes = ""
    name_en = ""
    name_pl = "Występowanie przymiotników rozpoczynających się na "
    languages = "pl" + affixes

    def count(self, doc):
        result, debug = self.find_words_affix(doc, affixes=self.__class__.affixes, starts=True, pos='adj')
        return result, debug


# -----------------------------------------------------------------


class AdjectivesEnd(WordFormation, ABC):
    affixes = ""
    name_en = ""
    name_pl = "Występowanie przymiotników zakończonych na "
    languages = "pl" + affixes

    def count(self, doc):
        result, debug = self.find_words_affix(doc, affixes=self.__class__.affixes, starts=False, pos='adj')
        return result, debug


class WF_ADJE_OWY(AdjectivesEnd):
    """ najczęstsze przyrostki przymiotnikowe """
    affixes = "owy"
    tests = [("Widziałam fioletową rybę jedzącą surowe mięso.", 2 / 6)]


class WF_ADJE_SKI(AdjectivesEnd):
    """ najczęstsze przyrostki przymiotnikowe """
    affixes = "ski"


class WF_ADJE_LIWY(AdjectivesEnd):
    """ najczęstsze przyrostki przymiotnikowe """
    affixes = "liwy"


# ----------------------------------------------------


class AllStart(WordFormation, ABC):
    affixes = ""
    name_en = ""
    name_pl = "Występowanie wyrazów rozpoczynających się na "
    languages = "pl" + affixes

    def count(self, doc):
        result, debug = self.find_words_affix(doc, affixes=self.__class__.affixes, starts=True, pos=None)
        return result, debug


WORD_FORMATION = [
    WF_NE_OSC,
    WF_NE_IK,
    WF_NE_EK,
    WF_NE_KA,
    WF_NE_KO,
    WF_NE_IYCIEL,
    WF_NE_OWIEC,
    WF_NE_ARZ,
    WF_NE_OWICZ,
    WF_ADJE_OWY,
    WF_ADJE_SKI,
    WF_ADJE_LIWY,
]

word_formation_group = MetricsGroup([m() for m in WORD_FORMATION])
