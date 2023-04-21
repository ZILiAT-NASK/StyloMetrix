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

from abc import ABC

from stylo_metrix.structures import Metric, Category

from stylo_metrix.utils import ratio


class Graphical(Category):
    lang = 'pl'
    name_en = "Graphical"
    name_local = "Graficzne"


class GR_UPPER(Metric):
    category = Graphical
    name_en = "Capital letters"
    name_local = "Kapitaliki"

    def count(doc):
        upper = [token.text for token in doc if token.is_upper]
        count = len(upper)
        debug = {"TOKENS": upper}
        return ratio(count, doc._.n_tokens), debug


# GRAPHICAL = [
#     GR_UPPER,
# ]

# graphical_group = MetricsGroup([m() for m in GRAPHICAL])
