from ...structures import Category, Metric
from ...utils import ratio


class Syntactic(Category):
    lang = "de"
    name_en = "Syntactic"
    name_local = "Syntax"


class SY_ADJD(Metric):
    category = Syntactic
    name_en = "Adjectives"
    name_local = "Adjektive und Adverbien im Prädikativ"

    def count(doc):
        debug = [token.text for token in doc if "ADJD" in token.tag_.split(":")]
        result = len(debug)
        return ratio(result, len(doc)), debug


class SY_PTKA(Metric):
    category = Syntactic
    name_en = "Particles with adjective or adverb"
    name_local = "Partikeln mit Adjektiv oder Adverb"

    def count(doc):
        debug = [token.text for token in doc if "PTKA" in token.tag_.split(":")]
        result = len(debug)
        return ratio(result, len(doc)), debug


class SY_APPR(Metric):
    category = Syntactic
    name_en = "Adpositions, left of the noun"
    name_local = "Präpositionen, links des Nomens"

    def count(doc):
        debug = [token.text for token in doc if "APPR" in token.tag_.split(":")]
        result = len(debug)
        return ratio(result, len(doc)), debug


class SY_APPRART(Metric):
    category = Syntactic
    name_en = "Adpositions with fused articles"
    name_local = "Präpositionen mit verschmolzenen Artikeln"

    def count(doc):
        debug = [token.text for token in doc if "APPRART" in token.tag_.split(":")]
        result = len(debug)
        return ratio(result, len(doc)), debug


class SY_APPO(Metric):
    category = Syntactic
    name_en = "Postpositions"
    name_local = "Postpositionen"

    def count(doc):
        debug = [token.text for token in doc if "APPO" in token.tag_.split(":")]
        result = len(debug)
        return ratio(result, len(doc)), debug


class SY_DO(Metric):
    category = Syntactic
    name_en = "Dative object"
    name_local = "Dativobjekt"

    def count(doc):
        debug = [token.text for token in doc if token.dep_ == "da"]
        result = len(debug)
        return ratio(result, len(doc)), debug


class SY_OA(Metric):
    category = Syntactic
    name_en = "Accusative object"
    name_local = "Akkusativobjekt"

    def count(doc):
        debug = [token.text for token in doc if token.dep_ == "oa"]
        result = len(debug)
        return ratio(result, len(doc)), debug


class SY_S_DE(Metric):
    category = Syntactic
    name_en = "Words in declarative sentences"
    name_local = "Wörter in Aussagesätzen"

    def count(doc):
        decl = set(
            [sent for sent in doc.sents for token in sent if token.text in ["."]]
        )
        debug = [token.text for i in decl for token in i]
        result = len(debug)
        return ratio(result, len(doc)), debug


class SY_S_EX(Metric):
    category = Syntactic
    name_en = "Words in exclamatory sentences"
    name_local = "Wörter in Ausrufesätzen"

    def count(doc):
        exl = set([sent for sent in doc.sents for token in sent if token.text == "!"])
        debug = [token.text for i in exl for token in i]
        result = len(debug)
        return ratio(result, len(doc)), debug


class SY_S_INT(Metric):
    category = Syntactic
    name_en = "Words in interrogative sentences"
    name_local = "Wörter in Fragesätzen"

    def count(doc):
        quest = set([sent for sent in doc.sents for token in sent if token.text == "?"])
        debug = [token.text for i in quest for token in i]
        result = len(debug)
        return ratio(result, len(doc)), debug


class SY_S_NEG(Metric):
    category = Syntactic
    name_en = "Words in negative sentences"
    name_local = "Wörter in negativen Sätzen"

    def count(doc):
        neg_sentences = []
        for sent in doc.sents:
            if any("PTKNEG" in token.tag_.split(":") for token in sent):
                neg_sentences.append(sent)
        debug = [token.text for sent in neg_sentences for token in sent]
        result = len(debug)
        return ratio(result, len(doc)), debug


class SY_S_INF(Metric):
    category = Syntactic
    name_en = "Words in infinitive-only sentences without finite verbs"
    name_local = "Wörter in Infinitivsätzen ohne finiten Verben"

    def count(doc):
        inf = set(
            [
                sent
                for sent in doc.sents
                if not any(
                    token.text for token in sent if "VerbForm=Fin" in token.morph
                )
                and any(token.text for token in sent if "VerbForm=Inf" in token.morph)
            ]
        )
        debug = [token.text for i in inf for token in i]
        result = len(debug)
        return ratio(result, len(doc)), debug


class SY_S_MAN(Metric):
    category = Syntactic
    name_en = "Words in sentences with the pronoun 'man'"
    name_local = "Wörter in Man-Aussagen"

    def count(doc):
        man = set(
            [
                sent
                for sent in doc.sents
                for token in sent
                if (token.text.lower() == "man" and token.dep_ == "sb")
            ]
        )
        debug = [token.text for i in man for token in i]
        result = len(debug)
        return ratio(result, len(doc)), debug


class SY_S_SUB(Metric):
    category = Syntactic
    name_en = "Words in subordinate sentences (excluding 'zu')"
    name_local = "Wörter in subordinierten Sätzen (ohne 'zu')"

    def count(doc):
        sub_sentences = []
        for sent in doc.sents:
            if any("KOUS" in token.tag_.split(":") for token in sent):
                sub_sentences.append(sent)
        debug = [token.text for sent in sub_sentences for token in sent]
        result = len(debug)
        return ratio(result, len(doc)), debug


class SY_S_SUB_ZU(Metric):
    category = Syntactic
    name_en = "Words in subordinate sentences with 'zu'"
    name_local = "Wörter in subordinierten Sätzen mit 'zu'"

    def count(doc):
        sub_sentences = []
        for sent in doc.sents:
            if any("KOUI" in token.tag_.split(":") for token in sent):
                sub_sentences.append(sent)
        debug = [token.text for sent in sub_sentences for token in sent]
        result = len(debug)
        return ratio(result, len(doc)), debug


class SY_S_KOKOM(Metric):
    category = Syntactic
    name_en = "Words in sentences with a comparative conjunction"
    name_local = "Wörter in Sätzen mit einer komparativen Konjunktion"

    def count(doc):
        comp_sentences = []
        for sent in doc.sents:
            if any("KOKOM" in token.tag_.split(":") for token in sent):
                comp_sentences.append(sent)
        debug = [token.text for sent in comp_sentences for token in sent]
        result = len(debug)
        return ratio(result, len(doc)), debug


class SY_S_COND1(Metric):
    category = Syntactic
    name_en = "Words in factual conditional sentences"
    name_local = "Wörter in realen Konditionalsätzen"

    def count(doc):
        cond_sentences = []
        for sent in doc.sents:
            if any(token.text.lower() == "wenn" for token in sent):
                if any(
                    token.pos_ in ["VERB", "AUX"]
                    and "Tense=Pres" in token.morph
                    and not any("VerbForm=Part" in token.morph for token in sent)
                    for token in sent
                ):
                    cond_sentences.append(sent)

        debug = [token.text for sent in cond_sentences for token in sent]
        result = len(debug)
        return ratio(result, len(doc)), debug


class SY_S_COND2(Metric):
    category = Syntactic
    name_en = "Words in potential conditional sentences"
    name_local = "Wörter in potentialen Konditionalsätzen"

    def count(doc):
        cond_sentences = []
        for sent in doc.sents:
            if any(token.text.lower() == "wenn" for token in sent):
                if any(
                    token.pos_ in ["VERB", "AUX"]
                    and "Mood=Sub" in token.morph
                    and not any("VerbForm=Part" in token.morph for token in sent)
                    for token in sent
                ):
                    cond_sentences.append(sent)

        debug = [token.text for sent in cond_sentences for token in sent]
        result = len(debug)
        return ratio(result, len(doc)), debug


class SY_S_COND3(Metric):
    category = Syntactic
    name_en = "Words in unreal conditional sentences"
    name_local = "Wörter in irrealen Konditionalsätzen"

    def count(doc):
        cond_sentences = []
        for sent in doc.sents:
            if any(token.text.lower() == "wenn" for token in sent):
                if any(
                    token.pos_ in ["VERB", "AUX"] and "Mood=Sub" in token.morph
                    for token in sent
                ):
                    if any("VerbForm=Part" in token.morph for token in sent):
                        cond_sentences.append(sent)

        debug = [token.text for sent in cond_sentences for token in sent]
        result = len(debug)
        return ratio(result, len(doc)), debug


class SY_QUOT(Metric):
    category = Syntactic
    name_en = "Words in quotation marks"
    name_local = "Wörter in Anführungszeichen"

    def count(doc):
        quote_positions = [i for i, token in enumerate(doc) if token.text in ['"', "'"]]
        if len(quote_positions) % 2 != 0:
            quote_positions.pop()
        debug = [
            token.text
            for i in range(0, len(quote_positions), 2)
            for token in doc[quote_positions[i] + 1 : quote_positions[i + 1]]
        ]
        result = len(debug)
        return ratio(result, len(doc)), debug
