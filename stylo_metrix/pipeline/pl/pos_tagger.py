from spacy.tokens import Token

import stylo_metrix.pipeline.pl.pl_nask.pos as pos


class POSTagger():

    def __init__(self, nlp):
        """
        pos: abbr adj adv conj fore ign n num oth part prep pro v
        is_word: True False
        is_content_word: True False
        is_punctuation: True False
        verb_inflection: infl None
        verb_person: (p|s)(1|2|3) None
        verb_future: futs futc None
        verb_tense: fut pres past None
        verb_aspect: perf imperf None
        verb_voice: impt cond None
        participle_type: pcon pant pact ppas None
        noun_type: ger None
        case: nom gen dat acc ins loc voc None
        pronoun_type: (p|s)(1|2|3) None
        adjective_degree: pos com sup None
        adverb_degree: pos com sup None
        ign: True False
        """
        self.nlp = nlp
        Token.set_extension("pos", default=None, force=True)
        Token.set_extension("is_word", default=False, force=True)
        Token.set_extension("is_content_word", default=False, force=True)
        Token.set_extension("is_punctuation", default=None, force=True)
        Token.set_extension("verb_inflection", default=None, force=True)
        Token.set_extension("verb_person", default=None, force=True)
        Token.set_extension("verb_future", default=None, force=True)
        Token.set_extension("verb_tense", default=None, force=True)
        Token.set_extension("verb_aspect", default=None, force=True)
        Token.set_extension("verb_voice", default=None, force=True)
        Token.set_extension("participle_type", default=None, force=True)
        Token.set_extension("noun_type", default=None, force=True)
        Token.set_extension("case", default=None, force=True)
        Token.set_extension("pronoun_type", default=None, force=True)
        Token.set_extension("adjective_degree", default=None, force=True)
        Token.set_extension("adverb_degree", default=None, force=True)
        Token.set_extension("ign", default=None, force=True)

    def __call__(self, doc):
        for token in doc:
            token._.set("pos", pos.classify_pos(token))
            token._.set("is_word", pos.is_word(token))
            token._.set("is_content_word", pos.is_content_word(token))
            token._.set("is_punctuation", pos.is_punctuation(token))
            token._.set("verb_inflection", pos.verb_inflection(token))
            token._.set("verb_person", pos.verb_person(token))
            token._.set("verb_future", pos.verb_future(token))
            token._.set("verb_tense", pos.verb_tense(token))
            token._.set("verb_aspect", pos.verb_aspect(token))
            token._.set("verb_voice", pos.verb_voice(token))
            token._.set("participle_type", pos.participle_type(token))
            token._.set("noun_type", pos.noun_type(token))
            token._.set("case", pos.case(token))
            token._.set("pronoun_type", pos.pronoun_type(token))
            token._.set("adjective_degree", pos.adjective_degree(token))
            token._.set("adverb_degree", pos.adverb_degree(token))
            token._.set("ign", pos.ign(token))
        return doc
