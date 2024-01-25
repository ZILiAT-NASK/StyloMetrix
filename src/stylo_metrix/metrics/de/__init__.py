from ...structures import Lang


class DeLang(Lang):
    definitions = ["german", "niemiecki", "de"]
    spacy_model = "de_core_news_lg"


from .descriptive import *
from .grammatical_forms import *
from .graphical import *
from .inflection import *
from .lexical import *
from .punctuation import *
from .syntactic import *
