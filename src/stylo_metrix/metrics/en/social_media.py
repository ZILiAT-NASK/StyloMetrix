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
from ...structures import Metric, Category
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from ...utils import incidence


class Social_Media(Category):
    lang = 'en'
    name_en = "Social Media"


class MASKED(Metric):
    category = Social_Media
    name_en = "Including characters masking real meaning of words"

    def count(doc):
        debug = []
        expression = r"\w{0,}[^A-Za-z\s]{1,}\w{0,}[^A-Za-z\s]{0,}\w{0,}"

        for match in re.finditer(expression, doc.text):
            start, end = match.span()
            span = doc.char_span(start, end)
            # This is a Span object or None if match doesn't map to valid token sequence
            if span is not None:
                debug.append(span.text)

        result = incidence(doc, debug)
        return result, debug
    

class DIGIT(Metric):
    category = Social_Media
    name_en = "Including urls"

    def count(doc):
        debug = [token for token in doc if token.is_digit == True]
        result = incidence(doc, debug)
        return result, debug

class POSITIV(Metric):
    category = Social_Media
    name_en = "Positive words based on VADER Sentiment"

    def count(doc):
        debug = []
        analyzer = SentimentIntensityAnalyzer()
        for token in doc:
            vs = analyzer.polarity_scores(token.text)
            score = vs['compound']
            if score >= 0.05:
                debug.append(token.text)

        result = incidence(doc, debug)
        return result, debug

class NEGATIV(Metric):
    category = Social_Media
    name_en = "Negative words based on VADER Sentiment"

    def count(doc):
        debug = []
        analyzer = SentimentIntensityAnalyzer()
        for token in doc:
            vs = analyzer.polarity_scores(token.text)
            score = vs['compound']
            if score <= -0.05:
                debug.append(token.text)

        result = incidence(doc, debug)
        return result, debug


class NEUTRAL(Metric):
    category = Social_Media
    name_en = "Neutral words based on VADER Sentiment"

    def count(doc):
        debug = []
        analyzer = SentimentIntensityAnalyzer()
        for token in doc:
            vs = analyzer.polarity_scores(token.text)
            score = vs['compound']
            if score > -0.05 and score < 0.05:
                debug.append(token.text)
        result = incidence(doc, debug)
        return result, debug


class DECR(Metric):
    category = Social_Media
    name_en = "DECR Intensifiers"

    def count(doc):

        lexicon = ['almost',
                   'barely',
                   'difficult',
                   'few',
                   'fewer',
                   'fewest',
                   'hardly',
                   'just',
                   'enough',
                   'kind of',
                   'kinda',
                   'kindof',
                   'kind-of',
                   'less',
                   'little',
                   'little',
                   'low',
                   'lower',
                   'lowest',
                   'marginal',
                   'marginally',
                   'minor',
                   'occasional',
                   'occasionally',
                   'only',
                   'partly',
                   'relatively',
                   'ridiculously',
                   'scarce',
                   'scarcely',
                   'slight',
                   'slightly',
                   'small',
                   'somewhat',
                   'sort of',
                   'sorta',
                   'sortof',
                   'sort-of']

        exception = [
            'sort',
            'kind'
        ]
        debug = []
        for token in doc:
            if token.lemma in lexicon:
                debug.append(token.text)
            elif token.i < len(doc) - 1 and token.text in exception and token.nbor().text == 'of':
                debug.append(token.text)
                debug.append('of')

        result = incidence(doc, debug)
        return result, debug

class INCR(Metric):
    category = Social_Media
    name_en = "INCR Intensifiers"

    def count(doc):
        lexicon = ['absolute',
                   'absolutely',
                   'amazingly',
                   'awfully',
                   'big',
                   'bigger',
                   'biggest',
                   'certainly',
                   'complete',
                   'completely',
                   'considerable',
                   'considerably',
                   'decidedly',
                   'deeply',
                   'definitely',
                   'effing',
                   'enormous',
                   'enormously',
                   'entirely',
                   'especially',
                   'exceedingly',
                   'exceptional',
                   'exceptionally',
                   'extra',
                   'extraordinarily',
                   'extreme',
                   'extremely',
                   'fabulously',
                   'fairly',
                   'flippin',
                   'flipping',
                   'frackin',
                   'fracking',
                   'frickin',
                   'fricking',
                   'friggin',
                   'frigging',
                   'fuckin',
                   'fucking',
                   'fuggin',
                   'fugging',
                   'fully',
                   'great',
                   'greatly',
                   'hella',
                   'high',
                   'higher',
                   'highest',
                   'highly',
                   'huge',
                   'hugely',
                   'immensely',
                   'incredible',
                   'incredibly',
                   'intensely',
                   'lot',
                   'major',
                   'majorly',
                   'more',
                   'most',
                   'much',
                   'obviously',
                   'particularly',
                   'perfectly',
                   'pretty',
                   'purely',
                   'quite',
                   'rather',
                   'real',
                   'really',
                   'remarkably',
                   'significantly',
                   'so',
                   'some',
                   'strongly',
                   'substantially',
                   'such',
                   'super',
                   'terribly',
                   'thoroughly',
                   'total',
                   'totally',
                   'tremendous',
                   'tremendously',
                   'uber',
                   'unbelievably',
                   'unusually',
                   'utter',
                   'utterly',
                   'vastly',
                   'very']

        debug = [token for token in doc if token.text in lexicon]

        result = incidence(doc, debug)
        return result, debug