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


from spacy_syllables import SpacySyllables

from stylo_metrix.pipeline.pl.metrics import Metrics
from stylo_metrix.pipeline.pl.params import Params
from stylo_metrix.pipeline.pl.pos_tagger import POSTagger
from stylo_metrix.pipeline.pl.psycholinguistic import Psycholinguistic
from stylo_metrix.pipeline.pl.sentence_segmenter import SentenceSegmenter

COMPONENTS_PL = [
    SpacySyllables,
    SentenceSegmenter,
    POSTagger,
    Psycholinguistic,
    Params,
    Metrics,
]
