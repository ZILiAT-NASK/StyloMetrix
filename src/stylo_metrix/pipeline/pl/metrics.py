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


from spacy.tokens import Doc

from stylo_metrix.metrics.pl import original_group
from stylo_metrix.structures.stylo_metrix_vector import StyloMetrixVector


class Metrics:

    def __init__(self, nlp):
        self.nlp = nlp
        Doc.set_extension("smv", default=None, force=True)
        Doc.set_extension("stylo_metrix_vector", default=None, force=True)
        nlp.metrics_group = original_group

    def __call__(self, doc):
        values = [metric(doc) for metric in self.nlp.metrics_group]
        vector = StyloMetrixVector(doc._.name, values)
        doc._.set("smv", vector)
        doc._.set("stylo_metrix_vector", vector)
        return doc

    def add_metrics(self, metric): pass

    def set_metrics(self, metrics_group): pass

    def remove_metrics(self, id): pass
