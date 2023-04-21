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
import itertools

def simile(doc):
    label = "simile"
    ext = "stylistic"

    head_pos = ["AUX", "VERB"]
    prep_tokens = [token for token in doc if token.pos_ == 'ADP' and token.text == 'like' and token.head.pos_ in head_pos]
    check = [[child for child in token.children if child.dep_ == "pobj" or child.dep_ == "pcomp"] for token in prep_tokens]
    as_as = [token for token in doc if token.text == 'as' and token.dep_ == "prep" and token.head.pos_ in ["ADJ", "NOUN"]]
    result = list(itertools.chain(*check)) + as_as
    return result, ext, label


QUESTION_WORDS = ["what", "which", "who", "whom", "whose", "where", "when", "why", "how"]

def special_question(doc):
    label = "special_question"
    ext = "syntax"

    root = [[sent for token in doc if token.head == token and any(child for child in token.lefts if child.text.lower() in QUESTION_WORDS)] for sent in doc.sents]
    nested = list(itertools.chain(*root))
    result = list(itertools.chain(*nested))
    return result, ext, label


def general_question(doc):
        label = "general_question"
        ext = "syntax"

        general_question = []
        for sent in doc.sents:
              if any(token for token in sent if token.dep_ == "neg"):
                     continue 
              else:
                  broad_case = [sent for token in sent if token.is_sent_start and token.head == token and token.pos_ == "AUX"]
                  case_one = list(itertools.chain(*broad_case))
                  general_question.append(case_one)
                  
                  root = [sent for token in sent if token.head == token and any(child for child in token.lefts if child.dep_ == "aux"\
                                                                                    and child.is_sent_start) and sent not in case_one]
                  case_two = list(itertools.chain(*root))
                  general_question.append(case_two)
                  
                  middle = [sent for token in sent if token.head == token and any(child for child in token.lefts if child.dep_ == "aux") and\
                              any(c for c in token.lefts if c.is_punct) and sent[-1].text == "?"]
                  case_tree = list(itertools.chain(*middle))
                  general_question.append(case_tree)

        result = list(itertools.chain(*general_question))
        return result, ext, label


def negative_question(doc):
    label = "negative_question"
    ext = "syntax"

    general_question = []
    for sent in doc.sents:
            if any(token for token in sent if token.dep_ == "neg"):
                broad_case = [sent for token in sent if token.is_sent_start and token.head == token and token.pos_ == "AUX"]
                case_one = list(itertools.chain(*broad_case))
                general_question.append(case_one)
                
                root = [sent for token in sent if token.head == token and any(child for child in token.lefts if child.dep_ == "aux"\
                                                                                and child.is_sent_start) and sent not in case_one]
                case_two = list(itertools.chain(*root))
                general_question.append(case_two)
                
                middle = [sent for token in sent if token.head == token and any(child for child in token.lefts if child.dep_ == "aux") and\
                            any(c for c in token.lefts if c.is_punct) and sent[-1].text == "?"]
                case_tree = list(itertools.chain(*middle))
                general_question.append(case_tree)
    result = list(itertools.chain(*general_question))
    return result, ext, label


def tag_questions(doc):
    label = "tag_question"
    ext = "syntax"

    tag_question = [[sent for token in sent if token.dep_ == "ROOT" and any(token for token in token.rights if token.dep_ == "nsubj" or token.dep_ == "snubjpass")\
                     and any(token for token in token.lefts if token.text.lower() not in QUESTION_WORDS)] for sent in doc.sents]
    nested = list(itertools.chain(*tag_question))
    result = list(itertools.chain(*nested))
    return result, ext, label

FUNCTION_LIST = [simile, special_question, general_question, negative_question, tag_questions]

