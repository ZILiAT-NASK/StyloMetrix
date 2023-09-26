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

from .metrics_group import MetricGroup


class LangMeta(type):
    def __str__(cls) -> str:
        return cls.definitions[0].capitalize()

    def __repr__(cls) -> str:
        return str(cls)

    def __call__(cls, *args, **kwargs):
        return cls


class Lang(metaclass=LangMeta):
    _all_languages = dict()
    def __init_subclass__(cls):
        cls.id = Lang._get_new_id()
        cls._categories = list()
        Lang._all_languages[cls.id] = cls

    def get_by_id(id):
        return Lang._all_languages[id]

    def _get_new_id():
        if Lang._all_languages:
            return max(Lang._all_languages)+1
        else:
            return 0

    def get_language(definition):
        language = None
        for subcls in Lang.__subclasses__():
            if definition.lower() in subcls.definitions:
                language = subcls
                break
        if language is None:
            raise Exception(f'There is no language with definition {definition}.')
        return language
    
    def get_all_languages():
        return Lang._all_languages

    @classmethod
    def register_category(cls, category):
        cls._categories.append(category)

    @classmethod
    def unregister_category(cls, category):
        cls._categories.remove(category)

    @classmethod
    def contains_category_name(cls, category):
        category_names = [cat.__name__ for cat in cls._categories]
        try:
            category_index = category_names.index(category.__name__)
            old_category = cls._categories[category_index]
            return old_category
        except ValueError:
            return None

    @classmethod
    def get_metrics(cls):
        metrics = MetricGroup()
        for category in cls.get_categories():
            metrics += category.get_metrics()
        return metrics

    @classmethod
    def get_categories(cls):
        return cls._categories

    @classmethod
    def to_json(cls):
        json_dict = {
            'id': cls.id,
            'definitions': cls.definitions,
            'spacy_model': cls.spacy_model,
            'categories': [category.to_json() for category in cls._categories]
        }

        return json.dumps(json_dict)
