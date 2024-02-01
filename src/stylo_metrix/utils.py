# Copyright (C) 2024  NASK PIB
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


import math
import statistics


def ratio(v1: int, v2: int):
    try:
        return v1 / v2
    except ZeroDivisionError:
        return 0


def incidence(doc, selection):
    return ratio(len(selection), len(doc))


def log_incidence(n1: int, n2: int):
    try:
        result = math.log(n1) / math.log(n2)
        return result
    except ZeroDivisionError:
        return 0.0
