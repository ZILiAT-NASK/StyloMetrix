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

from .metric import Metric

class MetricGroup:
    def __init__(self, metrics=None):
        if isinstance(metrics, MetricGroup):
            self.metrics = metrics.metrics
        else:
            self.metrics = set(metrics) if metrics else set()

    def to_list(self):
        metrics = self._get_sorted_metrics()
        metrics = [metric.id for metric in metrics]
        return(metrics)

    def __add__(self, other):
        if isinstance(other, MetricGroup):
            other_metrics = other.metrics
        elif issubclass(other, Metric):
            other_metrics = set((other,))
        else:
            other_metrics = None
        metric_list = self.metrics.union(other_metrics)
        return MetricGroup(metric_list)

    def __sub__(self, other):
        if isinstance(other, MetricGroup):
            other_metrics = other.metrics
        elif issubclass(other, Metric):
            other_metrics = set((other,))
        metric_list = self.metrics.difference(other_metrics)
        return MetricGroup(metric_list)

    def __str__(self):
        metrics = self._get_sorted_metrics()
        out = list()
        for id, metric in enumerate(metrics):
            metric_str = f'{id}  |  {metric.details()}'
            out.append(metric_str)
        return '\n'.join(out)

    def __getitem__(self, key):
        if isinstance(key, slice):
            indexes = range(*key.indices(len(self)))
            metrics = list()
            for id in indexes:
                metric = self[id]
                metrics.append(metric)
            return MetricGroup(metrics)
        return self._get_sorted_metrics()[key]

    def __len__(self):
        return len(self.metrics)

    def _get_sorted_metrics(self):
        metrics = list(self.metrics)
        metrics = sorted(metrics, key=self._sort_fun)
        return metrics

    def _sort_fun(self, metric_el):
        return (metric_el.id)
