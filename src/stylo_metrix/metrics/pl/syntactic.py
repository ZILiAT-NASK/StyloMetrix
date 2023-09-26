from spacy.matcher import DependencyMatcher
from spacy.matcher import Matcher
import re

from ...structures import Metric, Category
from ...utils import ratio

class Syntaktyka(Category):
    lang='pl'
    name_en='Syntactic'
    name_local='Syntaktyka'

class SY_FMWE(Metric):
    category = Syntaktyka
    name_en = "Flat multiword expressions"
    name_pl = "Związki wielowyrazowe"
 
    def count(doc):
        flat = [[token.head, token] for token in doc if "flat" in token.dep_]
        debug = [token for i in flat for token in i]
        result = len(debug)
        return ratio(result, len(doc)), debug
		
class SY_APPM(Metric):
    category = Syntaktyka
    name_en = "Appositional modifiers"
    name_pl = "Modyfikatory w apozycji"
 
    def count(doc):
        flat = [[token.head, token] for token in doc if "appos" in token.dep_]
        debug = [token for i in flat for token in i]
        result = len(debug)
        return ratio(result, len(doc)), debug

class SY_S_DE(Metric):
    category = Syntaktyka
    name_en = "Words in declarative sentences"
    name_local = "Wyrazy w zdaniach oznajmujących"

    def count(doc):
        decl = set([sent for sent in doc.sents for token in sent if token.text in ["."]])
        debug = [token for i in decl for token in i]
        result = len(debug)
        return ratio(result, len(doc)), debug
	
class SY_S_EX(Metric):
    category = Syntaktyka
    name_en = "Words in exclamatory sentences"
    name_local = "Wyrazy w zdaniach wykrzyknikowych"

    def count(doc):
        exl = set([sent for sent in doc.sents for token in sent if token.text == "!"])
        debug = [token for i in exl for token in i]
        result = len(debug)
        return ratio(result, len(doc)), debug
		
class SY_S_IN(Metric):
    category = Syntaktyka
    name_en = "Words in interrogative sentences"
    name_local = "Wyrazy w zdaniach pytających"

    def count(doc):
        quest = set([sent for sent in doc.sents for token in sent if token.text == "?"])
        debug = [token for i in quest for token in i]
        result = len(debug)
        return ratio(result, len(doc)), debug
		
class SY_S_NEG(Metric):
    category = Syntaktyka
    name_en = "Words in negative sentences"
    name_local = "Wyrazy w zdaniach przeczących"

    def count(doc):
        neg_sentences = []
        for sent in doc.sents:
            if any(token.dep_ in ["ROOT", "ccomp", "cop"] and token.pos_ in ["VERB", "AUX"] for token in sent) and any(token.dep_ == "advmod:neg" and token.pos_ == "PART" for token in sent):
                neg_sentences.append(sent)
        debug = [token for sent in neg_sentences for token in sent]
        result = len(debug)
        return ratio(result, len(doc)), debug
		
class SY_S_ELL(Metric):
    category = Syntaktyka
    name_en = "Words in ellipsis-ending sentences"
    name_local = "Wyrazy w zdaniach zakończonych wielokropkiem"

    def count(doc):
        ellipsis_pattern = r'\.\.\.'
        ellipsis_matches = re.finditer(ellipsis_pattern, doc.text)
        ellipsis_indices = [match.start() for match in ellipsis_matches]
        ellipsis_sentences = [sent for sent in doc.sents if any(token.idx in ellipsis_indices for token in sent)]
        total_words = len(list(doc))
        debug = [token.text for sent in ellipsis_sentences for token in sent]
        result = len(debug)
        return ratio(result, len(doc)), debug
		
class SY_S_VOC(Metric):
    category = Syntaktyka
    name_en = "Words in sentences with a noun in the vocative case"
    name_local = "Wyrazy w zdaniach z rzeczownikiem w wołaczu"

    def count(doc):
        result = 0
        inn7w = []
        for sent in doc.sents:
            if any(token.pos_ in ["NOUN", "PROPN"] and str(token.morph.get("Case")) == "['Voc']" for token in sent):
                inn7w.append(sent)      
        debug = [token for sent in inn7w for token in sent]
        result = len(debug)
        return ratio(result, len(doc)), debug

class SY_S_NOM(Metric):
    category = Syntaktyka
    name_en = "Words in nominal sentences"
    name_local = "Wyrazy w równoważnikach zdań"

    def count(doc):
        nom = set([sent for sent in doc.sents if all
        (token.pos_ == 'AUX' and 'VerbType=Quasi' in token.morph for token in sent if token.pos_ == 'AUX')
        and not any(token for token in sent if token.pos_ in ['VERB', 'AUX']
        and token.pos_ != 'AUX')])
        debug = [token for i in nom for token in i]
        result = len(debug)
        return ratio(result, len(doc)), debug
		
class SY_S_INF(Metric):
    category = Syntaktyka
    name_en = "Words in infinitive-only sentences without finite verbs"
    name_local = "Słowa w zdaniach z bezokolicznikami bez czasowników osobowych"
	
    def count(doc):
        inf = set([sent for sent in doc.sents if not any(token for token in sent if "VerbForm=Fin" in token.morph)
                and any(token for token in sent if "VerbForm=Inf" in token.morph)])
        debug = [token for i in inf for token in i]
        result = len(debug)
        return ratio(result, len(doc)), debug
		
class SY_NPRED(Metric):
    category = Syntaktyka
    name_en = "Nominal predicates"
    name_local = "Orzeczenia imienne"

    def count(doc):
        result = 0
        nom_pred = []

        for sent in doc.sents:
            for token in sent:
                if token.dep_ == 'cop' and token.head.pos_ in ['NOUN', 'ADJ', 'PRON'] and token.pos_ == 'AUX':
                    subject = token.head
                    predicate = token
                    result += 1
                    result += 1
                    nom_pred.append((predicate.text, subject.text))

        return ratio(result, len(doc)), nom_pred
		
class SY_MOD(Metric):
    category = Syntaktyka
    name_en = "Words within modifiers"
    name_local = "Wyrazy w przydawkach"

    def count(doc):
        mod_tags = ['amod', 'nmod', 'nmod:arg', 'acl', 'appos', 'det', 'det:poss']
        nouns = [token for token in doc if token.pos_ in ["NOUN", "PROPN"]]
        children_mods = [[ch for ch in list(noun.children) if ch.dep_ in mod_tags] for noun in nouns]
        mods_heads = sum(children_mods, [])
        mods_not_part_of_subtree = []
        for mod in mods_heads:
            list_without_current = [m for m in mods_heads if m is not mod]
            subtrees = [list(mod.subtree) for mod in list_without_current]
            subtrees_list = sum(subtrees, [])
            if mod not in subtrees_list:
                mods_not_part_of_subtree.append(mod)
        debug = [[el for el in list(head.subtree)] for head in mods_not_part_of_subtree]
        sum_subtrees = sum(debug, [])
        result = ratio(len(sum_subtrees), len(doc))
        return result, debug
		
class SY_NPHR(Metric):
    category = Syntaktyka
    name_en = "Words in nominal phrases"
    name_local = "Wyrazy we frazach nominalnych"

    def count(doc):
        nouns = [token for token in doc if token.pos_ in ['NOUN', 'PROPN']]
        nouns_not_part_of_subtree = []
        for noun in nouns:
            list_without_current = [n for n in nouns if n is not noun]
            subtrees = [list(noun.subtree) for noun in list_without_current]
            subtrees_list = sum(subtrees, [])
            if noun not in subtrees_list:
                nouns_not_part_of_subtree.append(noun)
        debug = [[word for word in list(noun.subtree)] for noun in nouns_not_part_of_subtree]
        sum_subtrees = sum(debug, [])
        result = ratio(len(sum_subtrees), len(doc))
        return result, debug
		
class SY_INV_OBJ(Metric):
    category = Syntaktyka
    name_en = "OVS word order"
    name_local = "Inwersja zdania, rozpoczęcie od dopełnienia"

    def count(doc):    
        nlp = SY_INV_OBJ.get_nlp()
        result = []
        counter = 0
        matcher = DependencyMatcher(nlp.vocab)        
        pattern = [# anchor token: root
            {   "RIGHT_ID" : "verb",
                "RIGHT_ATTRS": {"DEP": {"IN" : ["ROOT", 'xcomp']}}},
           
           # root >-- left child
           
            {   "LEFT_ID": "verb",  
                "REL_OP": ">--",
                "RIGHT_ID": "left child",
                "RIGHT_ATTRS": {"MORPH": {"INTERSECTS": ["Case=Gen", "Case=Dat", "Case=Acc", "Case=Ins", "Case=Loc"]}}
                  }
           ]
                
        matcher.add("LEFT_CHILD", [pattern])
        matches = matcher(doc)

        for i in range(len(matches)):
            match_id, token_ids = matches[i]
            match = []
            for l in doc[token_ids[1]].lefts:
              match.append(l)
            for n in range((token_ids[0]+1)-token_ids[1]):
              match.append(doc[token_ids[1]+n])
            result.append(match)
        
        counter = sum([len(listElem) for listElem in result])
        
        debug = {'FOUND': result}
        return ratio(counter, len(doc)), debug
		
class SY_INV_EPI(Metric):
    category = Syntaktyka
    name_en = "Inverted epithet"
    name_local = "Inwersja epitetu"

    def count(doc):    
        result = [token.text for token in doc if token.pos_ == "ADJ" and token.head.pos_ == "NOUN" and token in token.head.rights]
        debug = {'FOUND': result}
        return ratio(len(result), len(doc)), debug
		
class SY_INIT(Metric):
    category = Syntaktyka
    name_en = "Words being the initial token in a sentence"
    name_local = "Wyrazy będące pierwszym wyrazem zdania"

    def count(doc):
        debug = [sent[0].text for sent in doc.sents if sent]
        result = len(debug)
        return ratio(result, len(doc)), debug
		
class SY_QUOT(Metric):
    category = Syntaktyka
    name_en = "Number of words in quotation marks"
    name_local = "Słowa w cudzysłowie"

    def count(doc):
        quote_positions = [i for i, token in enumerate(doc) if token.text in ['"', "'"]]
        if len(quote_positions) % 2 != 0:
            quote_positions.pop()
        debug = [token for i in range(0, len(quote_positions), 2)
                                for token in doc[quote_positions[i] + 1 : quote_positions[i + 1]]]
        result = len(debug)
        return ratio(result, len(doc)), debug
		
class SY_SIMILE_NP(Metric):
    category = Syntaktyka
    name_en = "Similes (noun/pronoun)"
    name_local = "Porównania (rzeczownik/zaimek)"

    def count(doc):
        result = 0
        debug = []

        for sent in doc.sents:
            subj = [
                token.text for token in sent
                if token.pos_ in ['NOUN', 'PROPN', 'PRON']
                and token.dep_ == 'nsubj'
            ]

            sim = [
                token.text for token in sent
                  if token.pos_ == 'SCONJ'
                  and str(token.morph.get("ConjType")) == '[\'Cmpr\']'
                  ]

            obl = [
                token.text for token in sent
                if token.dep_ == 'obl:cmpr'
            ]

            if subj and sim and obl:
                debug.append((subj, sim, obl))
                result = result + len(subj) + len(sim) + len(obl)

        return ratio(result, len(doc)), debug

class SY_SIMILE_ADJ(Metric):
    category = Syntaktyka
    name_en = "Similes (adjective)"
    name_local = "Porównania (przymiotnik)"

    def count(doc):
        nlp = SY_SIMILE_ADJ.get_nlp()
        matcher = Matcher(nlp.vocab)
        pattern = [{"POS": {"IN": ["ADJ"]}}, {"POS": {"IN": ["SCONJ"]}, "MORPH": {"INTERSECTS": ["ConjType=Cmpr"]}}, {"POS": {"IN": ["NOUN", "PROPN"]}}]
        matcher.add("nazwa", [pattern])
        matches = matcher(doc)
        debug = [doc[start:end].text for _, start, end in matches]
        tri_gram_count = len(debug) * 3
        result = tri_gram_count
        return ratio(result, len(doc)), debug
