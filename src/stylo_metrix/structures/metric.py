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


from abc import ABC, abstractmethod
from collections.abc import Callable

from spacy.tokens import Doc


class Metric(ABC):
    name_pl: str
    name_en: str
    category_pl: str
    category_en: str

    def __init__(self):
        self.code = self.__class__.__name__

    def __call__(self, doc):
        value, debug = self.count(doc)
        return {
            "value": value,
            "code": self.code,
            "name_pl": self.name_pl,
            "name_en": self.name_en,
            "category_pl": self.category_pl,
            "category_en": self.category_en,
            # "id": ,
            "filename": doc._.name,
            "debug": debug,
        }

    def __repr__(self):
        return f"<Metric {self.code}>"

    @abstractmethod
    def count(self, doc):
        pass

    def __lt__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __eq__(self, other):
        pass

    def set_category(self, category_pl=None, category_en=None):
        if category_pl:
            self.category_pl = category_pl
        if category_en:
            self.category_en = category_en


class CustomMetric(Metric):
    """Decorator class"""

    def __init__(self, name_pl=None, name_en=None):
        self.name_pl = name_pl
        self.name_en = name_en
        self.category_pl = "Dodane metryki"
        self.category_en = "Custom metrics"

    def __call__(self, arg):
        if isinstance(arg, Callable):
            self._count_method = arg
            self.code = arg.__name__
            if not self.name_pl:
                self.name_pl = f"Metryka {self.code}"
            if not self.name_en:
                self.name_pl = f"Metric {self.code}"
            return self
        elif isinstance(arg, Doc):
            return super().__call__(arg)
        else:
            return TypeError()

    def count(self, doc):
        result = self._count_method(doc)
        if isinstance(result, tuple):
            return result
        return result, {}
