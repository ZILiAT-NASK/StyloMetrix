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

import json

from .language import Lang
from .metrics_group import MetricGroup


class CategoryMeta(type):
    def __str__(cls) -> str:
        return cls.__name__

    def __repr__(cls) -> str:
        return str(cls)

    def __call__(cls, *args, **kwargs):
        return cls
    

class Category(metaclass=CategoryMeta):
    _all_categories = dict()
    def __init_subclass__(cls):
        cls.id = Category._get_new_id()
        cls._metrics = list()
        cls.lang = Lang.get_language(cls.lang)
        cls._register_to_lang(cls.lang)
        Category._all_categories[cls.id] = cls

    def get_by_id(id):
        return Category._all_categories[id]

    def _get_new_id():
        if Category._all_categories:
            return max(Category._all_categories)+1
        else:
            return 0

    @classmethod
    def set_lang(cls, lang):
        old_lang = cls.lang

        if isinstance(lang, str):
            new_lang = Lang.get_language(lang)
        elif issubclass(lang, Lang):
            new_lang = lang

        if new_lang is not old_lang:
            old_lang.unregister_category(cls)
            cls._register_to_lang(new_lang)
            cls.lang = new_lang

    @classmethod
    def register_metric(cls, metric):
        cls._metrics.append(metric)

    @classmethod
    def unregister_metric(cls, metric):
        cls._metrics.remove(metric)

    @classmethod
    def get_metrics(cls):
        return MetricGroup(cls._metrics)

    @classmethod
    def contains_metric_name(cls, metric=None, code=None):
        metric_codes = [met.code for met in cls._metrics]
        try:
            if metric:
                metric_index = metric_codes.index(metric.code)
            if code:
                metric_index = metric_codes.index(code)
            old_metric = cls._metrics[metric_index]
            return old_metric
        except ValueError:
            return None

    @classmethod
    def _register_to_lang(cls, lang):
        old_category = lang.contains_category_name(cls)
        
        if old_category:
            for metric in old_category.get_metrics():
                metric.set_category(cls)
            lang.unregister_category(old_category)

        lang.register_category(cls)

    @classmethod
    def to_json(cls):
        json_dict = {
            'id': cls.id,
            'name_en': cls.name_en,
            'name_local': cls.name_local,
            'metrics': [metric.to_json() for metric in cls._metrics]
        }

        return json.dumps(json_dict)
