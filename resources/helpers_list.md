# StyloMetrix
List of extensions and helper functions in version `v0.0.4`

Copyright (C) 2022  NASK PIB

## Extensions PL
| Extension | Possible values |
|---|---|
| `token._.pos` | abbr adj adv conj fore ign n num oth part prep pro v |
| `token._.is_word` | True False |
| `token._.is_punctuaction` | True False |
| `token._.content_word` | cont noncont None |
| `token._.verb_inflection` | infl None |
| `token._.verb_person` | s1 p1 s2 p2 s3 p3 None |
| `token._.verb_future` | futs futc None |
| `token._.verb_tense` | fut pres past None |
| `token._.verb_aspect` | perf imperf None |
| `token._.verb_voice` | impt cond None |
| `token._.participle_type` | pcon pant pact ppas None |
| `token._.noun_type` | ger None |
| `token._.case` | nom gen dat acc ins loc voc None |
| `token._.pronoun_type` | s1 p1 s2 p2 s3 p3 None |
| `token._.adjective_degree` | pos com sup None |
| `token._.adverb_degree` | pos com sup None |
| `token._.ign` | True False |
| `doc._.words` | *custom* | 
| `doc._.content_words` | *custom* | 
| `doc._.punctuation` | *custom* | 
| `doc._.n_tokens` | *custom* | 
| `doc._.n_words` | *custom* | 
| `doc._.n_content_words` | *custom* | 
| `doc._.n_punctuation` | *custom* | 
| `doc._.name` | *custom* | 

## Helper functions

Import method:
```python
from stylo_metrix.utils import incidence, ratio, mean, median, stdev
```

| Function | Description |
|---|---|
| `incidence(iterable)`| Calculates incidence as ratio of length of an iterable over `doc._.n_tokens`, returns `0` if `doc._.n_tokens` equals to `0` | 
| `ratio(value1, value2)`| Calculates ratio of one value over another, returns `0` if `value2` equals to `0` | 
| `mean(iterable)`| Calculates mean, returns `0` if `iterable` is empty | 
| `median(iterable)`| Calculates median, returns `0` if `iterable` is empty | 
| `stdev(iterable)`| Calculates standard deviation, returns `0` if `iterable` is empty | 
