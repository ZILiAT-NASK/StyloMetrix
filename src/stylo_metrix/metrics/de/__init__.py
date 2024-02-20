from ...structures import Lang


class DeLang(Lang):
    definitions = ["german", "niemiecki", "de"]
    spacy_model = "de_core_news_lg"


from .grammatical_forms import *
from .inflection import *
from .syntactic import *
from .punctuation import *
from .lexical import *
from .descriptive import *
from .graphical import *
