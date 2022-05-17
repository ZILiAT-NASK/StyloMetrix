

# StyloMetrix

<a href="https://github.com/ZILiAT-NASK/StyloMetrix"><img alt="StyloMetrix" src="https://github.com/ZILiAT-NASK/StyloMetrix/blob/v0.0.0/resources/sm.png?raw=true" width="200"/></a><a href="https://www.nask.pl/"><img alt="NASK" src="https://github.com/ZILiAT-NASK/StyloMetrix/blob/v0.0.0/resources/nask.png?raw=true" width="200"/></a>

Zakład Inżynierii Lingwistycznej i Anailzy Tekstu, NASK PIB 

## 📌 Quick
💡 [Tutorial notebook](examples/Quick%20Tutorial.ipynb)

💡 [List of built-in metrics](resources/metrics_list.md)

💡 [Helper functions and extensions](resources/helpers_list.md)

## 🔖 Citation
Please cite [this article](https://wydawnictwo.umg.edu.pl/pp-rai2022/pdfs/41_pp-rai-2022-121.pdf) when referring to StyloMetrix: 
<pre>
Okulska, I., & Zawadzka, A. Styles with Benefits. The StyloMetrix Vectors for Stylistic and Semantic Text Classification of Small-Scale Datasets and Different Sample Length.
</pre>


## 🔔 About
StyloMetrix is a tool for creating **text representations** as **StyloMetrix vectors**. Each metric in vector quantifies a linguistic feature in text. Therefore a detailed information of the style of text can be translated to numeric values and used for - whatever you want!

The metrics are:
- **interpretable** - each metric represents an aspect of linguistic knowledge
- **normalized** - metrics express number of ocurrences of given feature per number of tokens in text, which lets us escape scaling effect in texts of different lengths
- **reproducible** - values of metrics can be recalculated or even counted manually giving always the same output. The representation doesn't depend on any random factor or seeding
- **customizable** - if your needs exceed the scope of built-in metrics, create your own! Don't forget to share your work and contribute to the community of StyloMetrix!

A StyloMetrix vector can be used as:
- **stylometric signature** that encodes the writing style of the author and the genre 
- input for classifiers of **supervised** or **unsupervised learning**, for example Random Forest classifier or feature selection algorithms
- values for **statistical analyses in science**
- set of linguistic data for manual reference

The tool offers **customization of vectors** by selecting from built-in metrics or **creating new metrics** according to user's needs. We provide a user-friendly interface to support these tasks. See instructions below! ⬇

Currently StyloMetrix is available for **Polish language** 🇵🇱, an **English Stylometrix** 🇬🇧 is on its way! 

## 📢 Release
Our most recent release is:

<code>v0.0</code> 
- Add StyloMetrix structure
- Add [tutorial](examples/Quick%20Tutorial.ipynb)
- Add 6 built-in metrics categories: `Grammatical Forms`, `Inflection`, `Lexical`, `Psycholinguistic`, `Syntactic`, `Word Formation`
- Specify license & citation

## 🔨 Installation
1. [Download model](http://mozart.ipipan.waw.pl/~rtuora/spacy/) `pl_nask`

📍 `pl_nask` is the new [HerBERT](https://github.com/allegro/HerBERT) based model from IPI PAN
```bash
pip install <PATH_TO_MODEL/pl_nask-0.0.x.tar.gz> 
```
2. Install StyloMetrix
```bash
pip install stylo_metrix
```

## 🪁 How to use
1. Add StyloMetrix pipe to spaCy pipeline:
```python
import spacy
import stylo_metrix
nlp = spacy.load('pl_nask')
nlp.add_pipe("stylo_metrix")
```
2. Use for any text:
```python
doc = nlp("W ten piękny dzień na niebie nie było ani jednej chmurki.")
doc._.stylo_metrix_vector
```
3. Find your results in `doc._.stylo_metrix_vector` extension, or `doc._.smv` for conveninece.

That's it! Find out about more usages and customization options in [extended use section](#extended_use) or [notebook tutorial](examples/Quick%20Tutorial.ipynb).

## 📈 Metrics
We have put care into creating a set of powerful built-in metrics. See the list below ⬇. However, since flexibility is strength, we provide an esy way to [create new metrics](#1-create-custom-metrics) and [mix existing groups](#3-create-groups). See the [extended use section](#extended_use)!

| Group | Import |
|---|---|
| Grammatical Forms | grammatical_forms_group |
| Inflection | inflection_group |
| Lexical | lexical_group |
| Psycholinguistic | psycholinguistic_group |
| Punctuation | punctuation_group |
| Syntactic | syntactic_group |
| Word Formation | word_formation_group |
| All ⬆ | original_group |

<a name="extended_use"></a>
## 🚀 Extended use
See our [notebook tutorial](examples/Quick%20Tutorial.ipynb) for complete instructions!


Imports that you will use:
```python
from stylo_metrix.structures import CustomMetric, MetricsGroup
from stylo_metrix.utils import incidence, ratio
```

### 1. Create custom metrics
Quickest way: write a function that returns a value and decorate it with `CustomMetric()`. You can use all spaCy features:
```python
@CustomMetric("Liczba niepustych tokenów")
def METRIC(doc):
    result = doc._.n_tokens
    return result
```

Or add more details and debug to keep your metrics clean:

```python
@CustomMetric(name_pl="Występowanie czasowników w 3 os. l. poj.", name_en="Third person singular verb incidence")
def VERBS_3S(doc):
    verbs = [token for token in doc
            if token._.pos == "v" and token._.verb_person == "s3"]
    result = ratio(len(verbs), doc._.n_tokens)
    debug = {"verbs": verbs, "n_tokens": doc._.n_tokens}
    return result, debug
```


### 2. Use new metrics
Put your metrics in a group and update `nlp` object so they know to use your new group:
```python
my_group = MetricsGroup(TEST1, TEST2)
nlp.metrics_group = my_group
```
Now run `nlp(text)` and that's it! Find the metric in `doc._.stylo_metrix_vector` or `doc._.smv`.

### 3. Create groups
Put custom metrics in groups to manage them. Create new `MetricsGroup` or concatenate groups:
```python
group = MetricsGroup(METRIC, VERBS_3S)
# <MetricsGroup [METRIC, VERBS_3S]>
```
Import groups of metrics from our built-in set:
```python
from stylo_metrix.metrics.pl import verbs_tenses_group, verbs_aspects_group
large_group = group + verbs_tenses_group + verbs_aspects_group
# <MetricsGroup [METRIC, VERBS_3S, IN_V_PAST, IN_V_PRES, IN_V_FUT, IN_V_FUTS, IN_V_FUTC, IN_V_PERF, IN_V_IMPERF]>
```

### 4. Save documentation
Keep your work clean by saving record of your metrics. You can `get_codes()` or `get_descriptions()` as list of strings for tagging, `get_md()` or `get_txt()` to  print a neatly formatted table of metrics or `save_txt(path)` and `save_md(path)` to have your list generated and saved in one line:
```python
group.get_txt()
# Nr   Kategoria            Kod              Nazwa                                   
# -----------------------------------------------------------------------------------
# Dodane metryki       METRIC           Metric METRIC                           
# Dodane metryki       VERBS_3S         Metric VERBS_3S                         
# ...
# Fleksja              IN_V_IMPERF      Występowanie czasowników w aspekcie niedokonanym
```

### 5. Use built-in extensions and functions
We share some features to facilitate your work. See the full list of [helper functions and extensions](resources/helpers_list.md).

#### Extensions
Skip repetetive searches using built-in extensions. Some of them are: `token._.pos` for part of speech or `doc._.n_tokens`.

#### Functions
Use built-in functions to replace most frequent lines of code and escape most common errors (like zero division). Currently we provide the following functions: `incidence`, `mean`, `median`, `ratio`, `stdev`.

Let's use them to calculate verbs starting with `A` letter in text.
```python
@CustomMetric("Czasowniki rozpoczynające się na A")
def A_VERBS(doc):
    search = [token for token in doc 
              if token._.pos == 'v' and token.prefix_ == 'a']
    result = incidence(doc, search)
    debug = {'verbs': search}
    return result, debug

A_VERBS(nlp("Aneta często angażowała się w absorbujące aktywności, ale nie potrafiła pływać."))
# {'value': 0.15384615384615385,
#  'code': 'A_VERBS',
#  'name_pl': 'Metric A_VERBS',
#  'category_pl': 'Dodane metryki',
#  'debug': {'verbs': [angażowała, absorbujące]}}
```

## 📚 We use
- [spaCy](https://spacy.io/) (MIT License)
- [spacy-syllables](https://spacy.io/universe/project/spacy_syllables) (MIT License)
- [pl_nask model](http://mozart.ipipan.waw.pl/~rtuora/spacy/) (GNU GPL 3.0 License), Ryszard Tuora and Łukasz Kobyliński, "Integrating Polish Language Tools and Resources in spaCy". In: Proceedings of PP-RAI'2019 Conference, 16-18.10.2019, Wrocław, Poland.
- experimental data from [Imbir, K. K. (2016). Affective Norms for 4900 Polish Words Reload (ANPW_R): Assessments for valence, arousal, dominance, origin, significance, concreteness, imageability and, age of acquisition. Frontiers in Psychology, 7, Article 1081. https://doi.org/10.3389/fpsyg.2016.01081](https://www.frontiersin.org/articles/10.3389/fpsyg.2016.01081/full)
 

## 📪 Contact
Zakład Inżynierii Lingwistycznej i Anailzy Tekstu, Naukowa i Akademicka Sieć Komputerowa – Państwowy Instytut Badawczy 

**Anna Zawadzka** anna.zawadzka@nask.pl | **Inez Okulska** inez.okulska@nask.pl

Copyright (C) 2022  NASK PIB
