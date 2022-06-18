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


from stylo_metrix.metrics.pl.grammatical_forms import grammatical_forms_group
from stylo_metrix.metrics.pl.inflection import (
    verbs_inflection_group,
    verbs_persons_group,
    verbs_tenses_group,
    verbs_aspects_group,
    verbs_moods_group,
    verbs_participles_group,
    verbs_derivation_group,
    nouns_cases_group,
    pronouns_cases_group,
    pronouns_persons_group,
    adjectives_degrees_group,
    adverbs_degrees_group,
    verbs_group,
    nouns_group,
    pronouns_group,
    adjectives_group,
    adverbs_group,
    inflection_group,
)
from stylo_metrix.metrics.pl.lexical import lexical_group
from stylo_metrix.metrics.pl.psycholinguistic import (
    psycholinguistic_above_mean_group,
    psycholinguistic_below_mean_group,
    psycholinguistic_group,
)
from stylo_metrix.metrics.pl.syntactic import syntactic_group
from stylo_metrix.metrics.pl.word_formation import word_formation_group

original_group = grammatical_forms_group \
                 + inflection_group \
                 + lexical_group \
                 + psycholinguistic_group \
                 + syntactic_group \
                 + word_formation_group
