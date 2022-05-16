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


class StyloMetrixVector:
    def __init__(self, name, metrics_values):
        self._dicts = metrics_values
        self.name = name

    def __repr__(self):
        return self._make_repr()

    def __str__(self):
        return str(self._dicts)

    def __len__(self):
        return len(self._dicts)

    def __iter__(self):
        for m in self._dicts:
            yield m

    def __getitem__(self, item):
        if isinstance(item, slice):
            return self.__class__(self.name, self._dicts[item])
        else:
            return self._dicts[item]

    def __copy__(self):
        self.__class__(self.name, self._dicts)

    def get_values(self):
        v = [metric["value"] for metric in self._dicts]
        return v

    def get_names(self):
        n = [metric["name_pl"] for metric in self._dicts]
        return n

    def get_codes(self):
        c = [metric["code"] for metric in self._dicts]
        return c

    def _make_repr(self):
        return f"<{self.__class__.__name__} for file: {self.name}, {len(self)} values>"
