from ...structures import Metric, Category
from ...utils import ratio

class Czesci_mowy(Category):
    lang='pl'
    name_en='Part of Speech'
    name_local='Czesci_mowy'


class G_N(Metric):
    category = Czesci_mowy
    name_en = "Nouns"
    name_local = "Rzeczowniki"

    def count(doc):
        debug = [token.text for token in doc if token.pos_ in ['NOUN', 'PROPN']]
        result = len(debug)
        return ratio(result, len(doc)), debug
    
class G_V(Metric):
    category = Czesci_mowy
    name_en = "Verbs"
    name_local = "Czasowniki"

    def count(doc):
        debug = [token.text for token in doc if token.pos_ in ['VERB', 'AUX']
                 and str(token.morph.get('VerbType'))!='[\'Quasi\']']
        result = len(debug)
        return ratio(result, len(doc)), debug
		
class G_ADJ(Metric):
    category = Czesci_mowy
    name_en = "Adjectives"
    name_local = "Przymiotniki"

    def count(doc):
        debug = [token.text for token in doc if token.pos_ == 'ADJ'
                 and token.is_digit == False
                 and not str(token.morph.get('NumForm')) == '[\'Roman\']']
        result = len(debug)
        return ratio(result, len(doc)), debug

    
class G_ADV(Metric):
    category = Czesci_mowy
    name_en = "Adverbs"
    name_local = "Przysłówki"

    def count(doc):
        debug = [token.text for token in doc if token.pos_ == 'ADV' and token.is_punct == False]
        result = len(debug)
        return ratio(result, len(doc)), debug
		
class G_PRO(Metric):
    category = Czesci_mowy
    name_en = "Pronouns"
    name_local = "Zaimki"

    def count(doc):
        debug = [token.text for token in doc if token.morph.get('PronType')]
        result = len(debug)
        return ratio(result, len(doc)), debug
		
class G_PRO_PRS(Metric):
    category = Czesci_mowy
    name_en = "Personal pronouns"
    name_local = "Zaimki osobowe"

    def count(doc):
        debug = [token.text for token in doc if str(token.morph.get('PronType'))=='[\'Prs\']'
                and str(token.morph.get('Reflex'))!='[\'Yes\']'
                and str(token.morph.get('Poss'))!='[\'Yes\']']
        result = len(debug)
        return ratio(result, len(doc)), debug
		
class G_PRO_REL(Metric):
    category = Czesci_mowy
    name_en = "Relative pronouns"
    name_local = "Zaimki względne"

    def count(doc):
        debug = [token.text for token in doc if str(token.morph.get('PronType'))=='[\'Rel\']']      
        result = len(debug)
        return ratio(result, len(doc)), debug
		
class G_PRO_DEM(Metric):
    category = Czesci_mowy
    name_en = "Demonstrative pronouns"
    name_local = "Zaimki wskazujące"
   
    def count(doc):
        debug = [token.text for token in doc if token.pos_ in ['PRON', 'DET'] 
                and str(token.morph.get('PronType'))=='[\'Dem\']']         
        result = len(debug)
        return ratio(result, len(doc)), debug
		
class G_PRO_INT(Metric):
    category = Czesci_mowy
    name_en = "Interrogative pronouns"
    name_local = "Zaimki pytajne"
   
    def count(doc):
        debug = [token.text for token in doc if str(token.morph.get('PronType'))=='[\'Int\']']         
        result = len(debug)
        return ratio(result, len(doc)), debug
		
class G_PRO_IND(Metric):
    category = Czesci_mowy
    name_en = "Indefinite pronouns"
    name_local = "Zaimki nieokreślone"
   
    def count(doc):
        debug = [token.text for token in doc if str(token.morph.get('PronType'))=='[\'Ind\']']
        result = len(debug)
        return ratio(result, len(doc)), debug
		
class G_PRO_TOT(Metric):
    category = Czesci_mowy
    name_en = "Total pronouns"
    name_local = "Zaimki uogólniające"
   
    def count(doc):
        debug = [token.text for token in doc if str(token.morph.get('PronType'))=='[\'Tot\']']       
        result = len(debug)
        return ratio(result, len(doc)), debug
		
class G_PRO_NEG(Metric):
    category = Czesci_mowy
    name_en = "Negative pronouns"
    name_local = "Zaimki przeczące"
   
    def count(doc):
        debug = [token.text for token in doc if str(token.morph.get('PronType'))=='[\'Neg\']']         
        result = len(debug)
        return ratio(result, len(doc)), debug
		
class G_PRO_POS(Metric):
    category = Czesci_mowy
    name_en = "Possessive pronouns"
    name_local = "Zaimki dzierżawcze"
   
    def count(doc):
        list_pronouns = ['jej', 'jego', 'ich']
        debug = [token.text for token in doc if str(token.morph.get('Poss'))=='[\'Yes\']'
                or token.text in list_pronouns]
        result = len(debug)
        return ratio(result, len(doc)), debug
		
class G_NUM(Metric):
    category = Czesci_mowy
    name_en = "Numerals"
    name_local = "Liczebniki"

    def count(doc):
        debug = [token.text for token in doc if token.morph.get('NumForm')
                 or token.pos_ == 'NUM']
        result = len(debug)
        return ratio(result, len(doc)), debug

class G_CNUM(Metric):
    category = Czesci_mowy
    name_en = "Collective numerals"
    name_local = "Liczebniki zbiorowe"

    def count(doc):
        debug = [token.text for token in doc if token.pos_ == 'NUM'
                 and [str(token.morph.get('NumType')) == "['Sets']"
                 or any('col' in tag_part for tag_part in token.tag_.split(':'))]
                 and str(token.morph.get('NumForm')) != "['Digit']"]        
        result = len(debug)
        return ratio(result, len(doc)), debug
		
class G_PART(Metric):
    category = Czesci_mowy
    name_en = "Particles"
    name_local = "Partykuły"

    def count(doc):
        debug = [token.text for token in doc if 'part' in token.tag_.split(':')           
             and str(token.morph.get('Reflex')) != "['Yes']"]
        result = len(debug)
        return ratio(result, len(doc)), debug
		
class G_ADP(Metric):
    category = Czesci_mowy
    name_en = "Adpositions"
    name_local = "Przyimki"

    def count(doc):
        debug = [token.text for token in doc if token.pos_ == 'ADP']
        result = len(debug)
        return ratio(result, len(doc)), debug
		
class G_INTJ(Metric):
    category = Czesci_mowy
    name_en = "Interjections"
    name_local = "Wykrzykniki"

    def count(doc):
        debug = [token.text for token in doc if token.pos_ == 'INTJ']
        result = len(debug)
        return ratio(result, len(doc)), debug
		
class G_SYM(Metric):
    category = Czesci_mowy
    name_en = "Symbols"
    name_local = "Symbole"

    def count(doc):
        debug = [token.text for token in doc if token.pos_ == 'SYM']
        result = len(debug)
        return ratio(result, len(doc)), debug

class G_ABBR(Metric):
    category = Czesci_mowy
    name_en = "Abbreviations"
    name_local = "Skrótowce" 

    def count(doc):
        debug = [token.text for token in doc if 'brev' in token.tag_.split(':')]
        result = len(debug)
        return ratio(result, len(doc)), debug
		
class G_CONJ(Metric):
    category = Czesci_mowy
    name_en = "Conjunctions"
    name_local = "Spójniki"

    def count(doc):
        debug = [token.text for token in doc if token.pos_ in ['CCONJ', 'SCONJ']]                       
        result = len(debug)
        return ratio(result, len(doc)), debug
		
class G_CCONJ(Metric):
    category = Czesci_mowy
    name_en = "Coordinating conjunctions"
    name_local = "Łączniki zdan współrzędnie złożonych"

    def count(doc):
        debug = [token.text for token in doc if token.pos_ == 'CCONJ']
        result = len(debug)
        return ratio(result, len(doc)), debug
		
class G_SCONJ(Metric):
    category = Czesci_mowy
    name_en = "Subordinating conjunctions"
    name_local = "Łączniki zdań podrzędnie złożonych"

    def count(doc):
        debug = [token.text for token in doc if token.pos_ == 'SCONJ']
        result = len(debug)
        return ratio(result, len(doc)), debug

class G_OTHER(Metric):
    category = Czesci_mowy
    name_en = "Other parts of speech"
    name_local = "Inne części mowy"

    def count(doc):
        debug = [token for token in doc if token.pos_ == 'X'
        and str(token.morph.get('Abbr'))!='[\'Yes\']']
        result = len(debug)
        return ratio(result, len(doc)), debug

class APOS_ADJ(Metric):
    category = Czesci_mowy
    name_en = "Descriptive apostrophe with an adjective"
    name_local = "Apostrofa opisowa z przymiotnikiem"

    def count(doc):
        result = 0
        dets = ["det", "amod"]
        debug = []

        for sent in doc.sents:
            inn7w = [
                token.text
                for token in sent
                if (token.pos_ in ["NOUN", "PROPN"] and str(token.morph.get("Case")) == "['Voc']") or
                  (token.pos_ in ["NOUN", "PROPN"] and token.dep_ == "vocative")
            ]

            pron = [
                token.text
                for token in sent
                if token.dep_ in dets and token.head.text in inn7w
            ]
            if inn7w and pron:
                debug.append((pron, inn7w))
                result = result + len(inn7w) + len(pron)

        return ratio(result, len(doc)), debug
