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

from ..structures import Lang, Metric, Category


def get_all_metrics(lang):
    lang = Lang.get_language(lang)
    metrics = lang.get_metrics()
    return metrics


def get_all_categories(lang):
    lang = Lang.get_language(lang)
    categories = lang.get_categories()
    return categories


def custom_metric(lang, custom_category=None, metric_nlp=None):
    def decorator(count_function):
        lang_name = lang
        dec_lang = Lang.get_language(lang_name)
        cat_names = [cat.__name__ for cat in dec_lang.get_categories()]
        if 'CUSTOM' not in cat_names:
            class CUSTOM(Category):
                lang = lang_name
                name_en = 'Custom'
                name_local = 'Custom'
                count = count_function
        else:
            id = [cat.__name__ for cat in dec_lang.get_categories()].index('CUSTOM')
            CUSTOM = dec_lang.get_categories()[id]
        
        class Wrapper(Metric):
            category = custom_category if custom_category else CUSTOM
            nlp = metric_nlp
            name_en = 'Custom'
            name_local = 'Custom'

        Wrapper.set_code(count_function.__name__)

        return Wrapper
    return decorator
