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


class StyloMetrixError(Exception):
    msg: str

    def __str__(self):
        return self.msg


class WrongTypeError(StyloMetrixError):
    msg = f"Trying to save wrong datatype (other than list of docs with \"metrics\" attribute)."

    def __init__(self):
        pass

    def __repr__(self):
        return str(self)


class EmptyListError(StyloMetrixError):
    msg = f"Trying to save empty list of StyloMetric vectors."

    def __init__(self):
        pass

    def __repr__(self):
        return str(self)


class AddMetricAlreadyExistsError(StyloMetrixError):
    msg = f"Metric already exists in metrics list."

    def __init__(self):
        pass

    def __repr__(self):
        return str(self)


class EmptyMetricsError(StyloMetrixError):
    msg = f"Trying to write empty vectors of metrics."

    def __init__(self):
        pass

    def __repr__(self):
        return str(self)


class MisalignedMetricsError(StyloMetrixError):
    msg = f"Vectors don't have matching metrics."

    def __init__(self):
        pass

    def __repr__(self):
        return str(self)
