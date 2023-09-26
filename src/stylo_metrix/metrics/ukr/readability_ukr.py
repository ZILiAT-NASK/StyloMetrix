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


from ...structures import Category, Metric


class READABILITY(Category):
    lang = 'ukr'
    name_en = "Readability scores"


# ---------------------------
# GENERAL READABILITY SCORES APPLICABLE TO UKRAINIAN
# ---------------------------


class FKR(Metric):
    category = READABILITY
    name_en = "Flesch–Kincaid readability score for the Ukrainian language"

    def count(doc):
        '''
        Function to calculate Flesch–Kincaid readability score for the Ukrainian language
        param: doc - spacy doc object
        return: float - readability score

        UKR:
        У результаті ми отримуємо показник від 0 до 100 одиниць:
        - 70–80 балів свідчать про легкодоступність тексту й високий рівень засвоєння для учнів (якщо йдеться про підручники та навчальні видання);
        - 60–65 балів – середня доступність тексту, характерна для масмедіа;
        - 50–55 балів – рівень ділових текстів та професійних видань, а також якісної художньої літератури;
        - менше 30 – це складні наукові тексти.

        ENG:
        00.00–90.00	- Very easy to read. Easily understood by an average 11-year-old student.
        90.0–80.0	- Easy to read. Conversational English for consumers.
        80.0–70.0	- Fairly easy to read.
        70.0–60.0	- Easily understood by 13- to 15-year-old students.
        60.0–50.0	- Fairly difficult to read.
        50.0–30.0	- College	Difficult to read.
        30.0–10.0	- College graduate	Very difficult to read. Best understood by university graduates.
        10.0–0.0	- Professional	Extremely difficult to read. Best understood by university graduates.
        '''
        #  if the length of the text is less than 100 characters, return 0
        if len(doc.text) < 100:
            return 0.0, {}

        # total number of words in the whole document 
        total_words_count = len([word.text for word in doc if word.is_alpha])
        # total number of sentences in the whole document
        sentences = len([sent for sent in doc.sents])
        # sum of mean of words per sentence
        words_per_sentence = 0
        for sent in doc.sents:
            words_per_sentence += len([word.text for word in sent if word.is_alpha]) / sentences

        # total number of syllables in the whole document
        syllables = sum([word._.syllables_count for word in doc if word.is_alpha])

        # Flesch–Kincaid readability score
        fkr_score = (206.835 - 1.015 * (words_per_sentence) - 84.6 * (syllables / total_words_count))
        return fkr_score, {}
    

class FKGL(Metric):
    category = READABILITY
    name_en = "Function to calculate automated readability score for the Ukrainian language"

    def count(doc):
        '''
        Function to calculate readability score for the Ukrainian language
        param: doc - spacy doc object
        return: float - readability score

        If readability score >= 5.0, the text is considered to be easy to read
        '''

        # alpha parameter in readability equation. always 0.4 for Ukrainian
        ALPHA = 0.4
        # total number of words in the whole document 
        total_words_count = [word.text for word in doc if word.is_alpha]
        # second parameter for readability score
        second_param = len([w for w in total_words_count if len(w) >= 3]) / len(total_words_count)
        # total number of sentences in the whole document
        sentences = len([sent for sent in doc.sents])

        # sum of mean of words per sentence
        words_per_sentence = 0
        for sent in doc.sents:
            words_per_sentence += len([word.text for word in sent if word.is_alpha]) / sentences
        rb_score = (words_per_sentence + second_param) * ALPHA 
        return rb_score, {}