from spacy.tokens import Doc


class Params:
    name_count = 0

    def __init__(self, nlp):
        self.nlp = nlp
        Doc.set_extension("words", default=None, force=True)
        Doc.set_extension("content_words", default=None, force=True)
        Doc.set_extension("punctuation", default=None, force=True)
        Doc.set_extension("n_tokens", default=None, force=True)
        Doc.set_extension("n_words", default=None, force=True)
        Doc.set_extension("n_content_words", default=None, force=True)
        Doc.set_extension("n_punctuation", default=None, force=True)
        Doc.set_extension("name", default=None, force=True)
        Doc.set_extension("assign_name", method=self.assign_name, force=True)

    def __call__(self, doc):
        doc._.set("words", [token for token in doc if token._.is_word])
        doc._.set("content_words", [token for token in doc if token._.is_content_word])
        doc._.set("punctuation", [token for token in doc if token._.is_punctuation])
        doc._.set("n_tokens", len([token for token in doc if token._.pos != 'ign']))
        doc._.set("n_words", len(doc._.words))
        doc._.set("n_content_words", len(doc._.content_words))
        doc._.set("n_punctuation", len(doc._.punctuation))
        doc._.set("name", f"SM{Params.name_count:06d}")
        Params.name_count += 1
        return doc

    def assign_name(self, doc, name):
        doc._.name = name
        return doc
