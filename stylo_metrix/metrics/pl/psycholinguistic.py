from abc import ABC

from stylo_metrix.structures import Metric, MetricsGroup
from stylo_metrix.utils import incidence


class Psycholinguistic(Metric, ABC):
    category_pl = "Psycholinguistic"
    category_en = "Psycholingwistyczne"

    def get_above_mean(self, doc, nr_param):
        values = [token._.affective_norms[nr_param] for token in doc if token._.affective_norms is not None]
        search = [value for value in values if value > doc._.an_means[nr_param]]
        result = incidence(doc, search)
        return result

    def get_below_mean(self, doc, nr_param):
        values = [token._.affective_norms[nr_param] for token in doc if token._.affective_norms is not None]
        search = [value for value in values if value < doc._.an_means[nr_param]]
        result = incidence(doc, search)
        return result


class PS_M_VALan(Psycholinguistic):
    name_en = ""
    name_pl = "Procent wyrazów posiadających więcej niż średni znak emocji (valence)"

    def count(self, document):
        result = self.get_above_mean(document, 0)
        return result, {}


class PS_M_VALbn(Psycholinguistic):
    name_en = ""
    name_pl = "Procent wyrazów posiadających mniej niż średni znak emocji (valence)"

    def count(self, document):
        result = self.get_below_mean(document, 0)
        return result, {}


class PS_M_AROan(Psycholinguistic):
    name_en = ""
    name_pl = "Procent wyrazów posiadających więcej niż średnie pobudzenie (arousal)"

    def count(self, document):
        result = self.get_above_mean(document, 1)
        return result, {}


class PS_M_ARObn(Psycholinguistic):
    name_en = ""
    name_pl = "Procent wyrazów posiadających mniej niż średnie pobudzenie (arousal)"

    def count(self, document):
        result = self.get_below_mean(document, 1)
        return result, {}


class PS_M_DOMan(Psycholinguistic):
    name_en = ""
    name_pl = "Procent wyrazów posiadających więcej niż średnie opanowanie (dominance)"

    def count(self, document):
        result = self.get_above_mean(document, 2)
        return result, {}


class PS_M_DOMbn(Psycholinguistic):
    name_en = ""
    name_pl = "Procent wyrazów posiadających mniej niż średnie opanowanie (dominance)"

    def count(self, document):
        result = self.get_below_mean(document, 2)
        return result, {}


class PS_M_ORIan(Psycholinguistic):
    name_en = ""
    name_pl = "Procent wyrazów posiadających więcej niż średnie pochodzenie (origin)"

    def count(self, document):
        result = self.get_above_mean(document, 3)
        return result, {}


class PS_M_ORIbn(Psycholinguistic):
    name_en = ""
    name_pl = "Procent wyrazów posiadających mniej niż średnie pochodzenie (origin)"

    def count(self, document):
        result = self.get_below_mean(document, 3)
        return result, {}


class PS_M_SIGan(Psycholinguistic):
    name_en = ""
    name_pl = "Procent wyrazów posiadających więcej niż średnie znaczenie (significance)"

    def count(self, document):
        result = self.get_above_mean(document, 4)
        return result, {}


class PS_M_SIGbn(Psycholinguistic):
    name_en = ""
    name_pl = "Procent wyrazów posiadających mniej niż średnie znaczenie (significance)"

    def count(self, document):
        result = self.get_below_mean(document, 4)
        return result, {}


class PS_M_CONan(Psycholinguistic):
    name_en = ""
    name_pl = "Procent wyrazów posiadających więcej niż średnią konkretność (concreteness)"

    def count(self, document):
        result = self.get_above_mean(document, 5)
        return result, {}


class PS_M_CONbn(Psycholinguistic):
    name_en = ""
    name_pl = "Procent wyrazów posiadających mniej niż średnią konkretność (concreteness)"

    def count(self, document):
        result = self.get_below_mean(document, 5)
        return result, {}


class PS_M_IMGan(Psycholinguistic):
    name_en = ""
    name_pl = "Procent wyrazów posiadających więcej niż średnia wyobrażalność (imageability)"

    def count(self, document):
        result = self.get_above_mean(document, 6)
        return result, {}


class PS_M_IMGbn(Psycholinguistic):
    name_en = ""
    name_pl = "Procent wyrazów posiadających mniej niż średnia wyobrażalność (imageability)"

    def count(self, document):
        result = self.get_below_mean(document, 6)
        return result, {}


class PS_M_AGEan(Psycholinguistic):
    name_en = ""
    name_pl = "Procent wyrazów posiadających więcej niż średni wiek akwizycji (age of acquisition)"

    def count(self, document):
        result = self.get_above_mean(document, 7)
        return result, {}


class PS_M_AGEbn(Psycholinguistic):
    name_en = ""
    name_pl = "Procent wyrazów posiadających mniej niż średni wiek akwizycji (age of acquisition)"

    def count(self, document):
        result = self.get_below_mean(document, 7)
        return result, {}


PSYCHOLINGUISTIC_ABOVE_MEAN = [
    PS_M_VALan,
    PS_M_AROan,
    PS_M_DOMan,
    PS_M_ORIan,
    PS_M_SIGan,
    PS_M_CONan,
    PS_M_IMGan,
    PS_M_AGEan,
]

PSYCHOLINGUISTIC_BELOW_MEAN = [
    PS_M_VALbn,
    PS_M_ARObn,
    PS_M_DOMbn,
    PS_M_ORIbn,
    PS_M_SIGbn,
    PS_M_CONbn,
    PS_M_IMGbn,
    PS_M_AGEbn,
]

psycholinguistic_above_mean_group = MetricsGroup([m() for m in PSYCHOLINGUISTIC_ABOVE_MEAN])
psycholinguistic_below_mean_group = MetricsGroup([m() for m in PSYCHOLINGUISTIC_BELOW_MEAN])
psycholinguistic_group = psycholinguistic_above_mean_group + psycholinguistic_below_mean_group
