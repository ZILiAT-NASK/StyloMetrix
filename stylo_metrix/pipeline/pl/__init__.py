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
