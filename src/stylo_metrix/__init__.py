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


from stylo_metrix.functions import analyze_dir, analyze_text, save_csv, save_npy, remove_empty_columns
from stylo_metrix.pipeline.stylo_metrix_pipe import StyloMetrixPipe
from stylo_metrix.structures import CustomMetric, Metric, MetricsGroup
from stylo_metrix.utils import incidence, ratio, mean, median, stdev