import re

from ...structures import Category, Metric
from ...utils import ratio
from .data.dictionaries import emoticons, lenny_faces


class Graphical(Category):
    lang = "de"
    name_en = "Graphical"
    name_local = "Graphische"


class GR_UPPER(Metric):
    category = Graphical
    name_en = "Capital letters"
    name_local = "Großbuchstaben"

    def count(doc):
        roman_pattern = r"^[IVXLCDM]+$"
        debug = [
            token.text
            for i, token in enumerate(doc)
            if (not token.is_sent_start or len(token.text) > 1)
            and token.text.isupper()
            and not re.match(roman_pattern, token.text)
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug


class GR_EMOT(Metric):
    category = Graphical
    name_en = "Emoticons"
    name_local = "Emoticons"

    def count(doc):
        emoticons_pattern = "|".join(map(re.escape, emoticons))
        debug = re.findall(emoticons_pattern, doc.text)
        result = len(debug)
        return ratio(result, len(doc)), debug


class GR_LENNY(Metric):
    category = Graphical
    name_en = "Lenny faces"
    name_local = "Lenny faces"

    def count(doc):
        debug = re.findall(lenny_faces, doc.text)
        result = len(debug)
        return ratio(result, len(doc)), debug


class GR_MENTION(Metric):
    category = Graphical
    name_en = "Direct mentions with @"
    name_local = "Direkte Erwähnungen mit @"

    def count(doc):
        matches = re.findall(r"(^@\w+)|\s(@\w+)", doc.text)
        debug = [match[0] or match[1] for match in matches if any(match)]
        result = len(debug)
        return ratio(result, len(doc)), debug


class GR_HASH(Metric):
    category = Graphical
    name_en = "Hashtags"
    name_local = "Hashtags"

    def count(doc):
        matches = re.findall(r"(^#\w+)|\s(#\w+)", doc.text)
        debug = [match[0] or match[1] for match in matches if any(match)]
        result = len(debug)
        return ratio(result, len(doc)), debug


class GR_LINK(Metric):
    category = Graphical
    name_en = "Hyperlinks"
    name_local = "Hyperlinks"

    def count(doc):
        debug = re.findall(
            "(?:http|ftp|https):\/\/(?:[\w_-]+(?:(?:\.[\w_-]+)+))(?:[\w.,@?^=%&:\/~+_#-]*[\w@?^=%&\/~+#-])",
            doc.text,
        )
        result = len(debug)
        return ratio(result, len(doc)), debug
