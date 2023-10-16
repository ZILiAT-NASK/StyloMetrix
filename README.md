

# StyloMetrix

<a href="https://github.com/ZILiAT-NASK/StyloMetrix#stylometrix"><img alt="StyloMetrix" src="https://github.com/ZILiAT-NASK/StyloMetrix/blob/v0.0.0/resources/sm.png?raw=true" width="200"/></a><a href="https://www.nask.pl/"><img alt="NASK" src="https://github.com/ZILiAT-NASK/StyloMetrix/blob/v0.0.0/resources/nask.png?raw=true" width="200"/></a>

Zakład Inżynierii Lingwistycznej i Anailzy Tekstu, NASK PIB 

## 📌 Quick
💡 Stylometry tool in beta version for **Polish**, **English** and **Ukrainian** language, distributed as a **Python package**

💡 [Tutorial notebook](examples/Tutorial_pl.ipynb)

💡 List of built-in metrics for [Polish](resources/metrics_list_pl.md), [English](resources/metrics_list_en.md)

💡 [Helper functions and extensions](resources/helpers_list.md)

## 🔖 Citation
Please cite [this article](https://arxiv.org/pdf/2309.12810.pdf) when referring to StyloMetrix: 
<pre>
Okulska, I., Stetsenko, D., Kołos, A., Karlińska, A., Głąbińska, K., & Nowakowski, A. (2023). StyloMetrix: An Open-Source Multilingual Tool for Representing Stylometric Vectors. arXiv preprint arXiv:2309.12810.
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

Currently StyloMetrix is available for **Polish**, **English** and **Ukrainian** language! 

## 📢 Release
Our most recent release is:

`v0.1.0`
- Changing the structure of StyloMetrix
- Works mutch faster!
- New metrics and categories in Polish and English language
- Ukrainian language in beta version

<details>
<summary><b>Previous releases</b> ⌛</summary>

`v0.0.6`
- Add categories `Syntactic` and `Lexical` for English

`v0.0.4`
- Add **English beta** with built-in metrics in category `Grammatical Forms`


`v0.0.3`
- Add StyloMetrix structure
- Add [tutorial](examples/Quick%20Tutorial.ipynb)
- Add 6 built-in metrics categories for **Polish beta**: `Grammatical Forms`, `Inflection`, `Lexical`, `Psycholinguistic`, `Syntactic`, `Word Formation`
- Specify license & citation

</details>

## 🔨 Installation

### 1. Install spaCy 
Install `spacy` according to [spaCy install instructions](https://spacy.io/usage) 

### 2. Install model
▶ **For English**:

Install `en_core_web_trf` from [spaCy install instructions](https://spacy.io/usage)

▶ **For Polish**:

[Download and install model](http://mozart.ipipan.waw.pl/~rtuora/spacy/) `pl_nask` `v0.0.7`

📍 `pl_nask` is the new [HerBERT](https://github.com/allegro/HerBERT) based model from IPI PAN, requires `spacy==3.3`
```bash
python -m pip install <PATH_TO_MODEL/pl_nask-0.0.7.tar.gz> 
```
### 3. Install StyloMetrix
```bash
pip install stylo_metrix
```

## 🪁 How to use
1. Get your texts and import StyloMetrix:
```python
import stylo_metrix as sm

texts = ['Panno święta, co Jasnej bronisz Częstochowy I w Ostrej świecisz Bramie!',
        'Ofiarowany, martwą podniosłem powiekę; I zaraz mogłem pieszo, do Twych świątyń progu...',
        'W ludziach straty nie było. Ale wszystkie ławy Miały zwichnione nogi;']
```
2. Use StyloMetrix object for this texts:
```python
stylo = sm.StyloMetrix('pl')
metrics = stylo.transform(texts)
print(metrics)
```
3. Your results is now in `metrics` object.

That's it! Find out about more usages and customization options in [notebook tutorial](examples/Quick%20Tutorial.ipynb).

## 📈 Metrics
We have put care into creating a set of powerful built-in metrics. See the list below ⬇. However, since flexibility is strength, we provide an esy way to create new metrics.

**Polish** [(see full list)](resources/metrics_list_pl.md)

**English** [(see full list)](resources/metrics_list_en.md)

**Ukrainian** [(see full list)](resources/metrics_list_ukr.md)





## 📚 We use
- [spaCy](https://spacy.io/) (MIT License)
- [spacy-syllables](https://spacy.io/universe/project/spacy_syllables) (MIT License)
- [pl_nask model](http://mozart.ipipan.waw.pl/~rtuora/spacy/) (GNU GPL 3.0 License), Ryszard Tuora and Łukasz Kobyliński, "Integrating Polish Language Tools and Resources in spaCy". In: Proceedings of PP-RAI'2019 Conference, 16-18.10.2019, Wrocław, Poland.
- experimental data from [Imbir, K. K. (2016). Affective Norms for 4900 Polish Words Reload (ANPW_R): Assessments for valence, arousal, dominance, origin, significance, concreteness, imageability and, age of acquisition. Frontiers in Psychology, 7, Article 1081. https://doi.org/10.3389/fpsyg.2016.01081](https://www.frontiersin.org/articles/10.3389/fpsyg.2016.01081/full)
 

## 📪 Contact
Zakład Inżynierii Lingwistycznej i Anailzy Tekstu, Naukowa i Akademicka Sieć Komputerowa – Państwowy Instytut Badawczy 

**Adam Nowakowski** adam.nowakowski@nask.pl | **Inez Okulska** inez.okulska@nask.pl

Copyright (C) 2023  NASK PIB
