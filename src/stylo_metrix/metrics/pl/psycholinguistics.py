from ...structures import Metric, Category
from ...utils import ratio

from .data.dictionaries import POSITIVITY_H, POSITIVITY_L, NEGATIVITY_H, NEGATIVITY_L
from .data.dictionaries import REFLECTIVENESS_H, REFLECTIVENESS_L
from .data.dictionaries import AUTOMATICITY_H, AUTOMATICITY_L, AROUSAL_L, AROUSAL_H
from .data.dictionaries import SIGNIFICANCE_H, SIGNIFICANCE_L


class Psycholingwistyka(Category):
    lang='pl'
    name_en='Psycholinguistics'
    name_local='Psycholingwistyka'


class PS_M_POSa(Metric):
    category = Psycholingwistyka
    name_en = "Words having more than mean positivity"
    name_local = "Wyrazy posiadające więcej niż średnią pozytywność (POSITIVITY)"

    def count(doc):
        debug = [token.text for token in doc if token.lemma_ in POSITIVITY_H]
        result = len(debug)
        return ratio(result, len(doc)), debug
		
class PS_M_POSb(Metric):
    category = Psycholingwistyka
    name_en = "Words having less than mean positivity"
    name_local = "Wyrazy posiadające mniej niż średnią pozytywność (POSITIVITY)"

    def count(doc):
        debug = [token.text for token in doc if token.lemma_ in POSITIVITY_L]
        result = len(debug)
        return ratio(result, len(doc)), debug
		
class PS_M_NEGa(Metric):
    category = Psycholingwistyka
    name_en = "Words having more than mean negativity"
    name_local = "Wyrazy posiadające więcej niż średnią negatywność (NEGATIVITY)"

    def count(doc):
        debug = [token.text for token in doc if token.lemma_ in NEGATIVITY_H]
        result = len(debug)
        return ratio(result, len(doc)), debug
		
class PS_M_NEGb(Metric):
    category = Psycholingwistyka
    name_en = "Words having less than mean negativity"
    name_local = "Wyrazy posiadające mniej niż średnią negatywność (NEGATIVITY)"

    def count(doc):
        debug = [token.text for token in doc if token.lemma_ in NEGATIVITY_L]
        result = len(debug)
        return ratio(result, len(doc)), debug
		
class PS_M_REFa(Metric):
    category = Psycholingwistyka
    name_en = "Words having more than mean reflectiveness"
    name_local = "Wyrazy posiadające więcej niż średnią refleksyjność (REFLECTIVENESS)"
    
    def count(doc):
        debug = [token.text for token in doc if token.lemma_ in REFLECTIVENESS_H]
        result = len(debug)
        return ratio(result, len(doc)), debug
		
class PS_M_REFb(Metric):
    category = Psycholingwistyka
    name_en = "Words having less than mean reflectiveness"
    name_local = "Wyrazy posiadające mniej niż średnią refleksyjność (REFLECTIVENESS)"
    
    def count(doc):
        debug = [token.text for token in doc if token.lemma_ in REFLECTIVENESS_L]
        result = len(debug)
        return ratio(result, len(doc)), debug
		
class PS_M_AUTa(Metric):
    category = Psycholingwistyka
    name_en = "Words having more than mean automaticity"
    name_local = "Wyrazy posiadające więcej niż średnią automatyczność (AUTOMATICITY)"
    
    def count(doc):
        debug = [token.text for token in doc if token.lemma_ in AUTOMATICITY_H]
        result = len(debug)
        return ratio(result, len(doc)), debug
		
class PS_M_AUTb(Metric):
    category = Psycholingwistyka
    name_en = "Words having less than mean automaticity"
    name_local = "Wyrazy posiadające mniej niż średnią automatyczność (AUTOMATICITY)"
    
    def count(doc):
        debug = [token.text for token in doc if token.lemma_ in AUTOMATICITY_L]
        result = len(debug)
        return ratio(result, len(doc)), debug
		
class PS_M_AROa(Metric):
    category = Psycholingwistyka
    name_en = "Words having more than mean arousal"
    name_local = "Wyrazy posiadające więcej niż średnie pobudzenie (arousal)"
    
    def count(doc):
        debug = [token.text for token in doc if token.lemma_ in AROUSAL_H]
        result = len(debug)
        return ratio(result, len(doc)), debug
		
class PS_M_AROb(Metric):
    category = Psycholingwistyka
    name_en = "Words having less than mean arousal"
    name_local = "Wyrazy posiadające mniej niż średnie pobudzenie (arousal)"
    
    def count(doc):
        debug = [token.text for token in doc if token.lemma_ in AROUSAL_L]
        result = len(debug)
        return ratio(result, len(doc)), debug
		
class PS_M_SIGa(Metric):
    category = Psycholingwistyka
    name_en = "Words having more than mean significance"
    name_local = "Wyrazy posiadające więcej niż średnie znaczenie (significance)"

    def count(doc):
        debug = [token.text for token in doc if token.lemma_ in SIGNIFICANCE_H]
        result = len(debug)
        return ratio(result, len(doc)), debug
		
class PS_M_SIGb(Metric):
    category = Psycholingwistyka
    name_en = "Words having less than mean significance"
    name_local = "Wyrazy posiadające mniej niż średnie znaczenie (significance)"

    def count(doc):
        debug = [token.text for token in doc if token.lemma_ in SIGNIFICANCE_L]
        result = len(debug)
        return ratio(result, len(doc)), debug
	