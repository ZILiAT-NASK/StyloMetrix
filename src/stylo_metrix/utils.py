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


import statistics


def mean(l: list):
    try:
        result = statistics.mean(l)
    except statistics.StatisticsError:
        result = 0
    return result


def stdev(lst: list):
    try:
        result = statistics.stdev(lst)
    except statistics.StatisticsError:
        result = 0
    return result


def median(lst: list):
    try:
        result = statistics.median(lst)
    except statistics.StatisticsError:
        result = 0
    return result


def ratio(v1: int, v2: int):
    try:
        return v1 / v2
    except ZeroDivisionError:
        return 0


def select(doc, attr_dict):
    selection = [token for token in doc
                 if all([getattr(getattr(token, '_'), attr) == value for attr, value in attr_dict.items()])]
    return selection


def incidence(doc, selection):
    return ratio(len(selection), doc._.n_tokens)


def sent_incidence(doc, selection):
    return ratio(len(selection), doc._.n_sents)


def highlight_words(doc, tokens):
    return "".join(
        [(str(f"[[[{token}]]]") if token in tokens else str(token)) + token.whitespace_ for token in doc])


def start_end_quote(doc):
    for token in doc:
        if ("PunctSide=Ini" and "PunctType=Quot") in token.morph:
            start = token.i+1
            break
        else:
            start = None
    for token in reversed(doc):
        if ("PunctSide=Fin" and "PunctType=Quot") in token.morph:
            end = token.i-1
            break
        else:
            end = None
    return start, end
