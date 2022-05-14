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


def highlight_words(doc, tokens):
    return "".join(
        [(str(f"[[[{token}]]]") if token in tokens else str(token)) + token.whitespace_ for token in doc])
