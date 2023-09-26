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

class MetricMeta(type):
    def __str__(cls) -> str:
        return cls.code

    def __repr__(cls) -> str:
        return str(cls)

    def __call__(cls, doc):
        if cls is Metric:
            return cls
        else:
            return cls.count(doc)


class Metric(metaclass=MetricMeta):
    _all_metrics = dict()
    
    def __init_subclass__(cls):
        cls.id = Metric._get_new_id()
        cls.code = cls.__name__
        cls._register_to_category(cls.category)
        Metric._all_metrics[cls.id] = cls

    def get_by_id(id):
        return Metric._all_metrics[id]

    def _get_new_id():
        if Metric._all_metrics:
            return max(Metric._all_metrics)+1
        else:
            return 0

    @classmethod
    def details(cls):
        return f'{cls.category}  |  {cls}  |  {cls.name_en}'

    @classmethod
    def set_category(cls, category):
        old_category = cls.category

        if category is not old_category:
            old_category.unregister_metric(cls)
            cls._register_to_category(category)
            cls.category = category

    @classmethod
    def set_code(cls, new_code):
        old_metric = cls.category.contains_metric_name(code=new_code)

        if old_metric:
            cls.category.unregister_metric(old_metric)
            if old_metric is not cls:
                Metric._all_metrics.pop(old_metric.id)

        cls.__name__ = new_code
        cls.code = new_code

    @classmethod
    def _register_to_category(cls, category):
        old_metric = category.contains_metric_name(cls)

        if old_metric:
            category.unregister_metric(old_metric)
            if old_metric is not cls:
                Metric._all_metrics.pop(old_metric.id)

        category.register_metric(cls)

    @classmethod
    def to_json(cls):
        json_dict = {
            'id': cls.id,
            'code': cls.code,
            'name_en': cls.name_en,
            'name_local': cls.name_local
        }

        return json.dumps(json_dict)
    
    @classmethod
    def set_nlp(cls, nlp):
        cls._nlp = nlp

    @classmethod
    def get_nlp(cls):
        return cls._nlp
