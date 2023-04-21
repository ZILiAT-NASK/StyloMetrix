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


from spacy.tokens import Doc


class Params:
    def __init__(self, nlp):
        self.nlp = nlp
        Doc.set_extension("words", default=None, force=True)
        # Doc.set_extension("content_words", default=None, force=True)
        # Doc.set_extension("punctuation", default=None, force=True)
        Doc.set_extension("n_tokens", default=None, force=True)
        Doc.set_extension("n_sents", default=None, force=True)
        # Doc.set_extension("n_words", default=None, force=True)
        # Doc.set_extension("n_content_words", default=None, force=True)
        # Doc.set_extension("n_punctuation", default=None, force=True)

    def __call__(self, doc):
        doc._.set("words", [token for token in doc if token._.is_word])
        # doc._.set("content_words", [token for token in doc if token._.content_word == 'cont'])
        # doc._.set("punctuation", [token for token in doc if token._.is_punctuation])
        doc._.set("n_tokens", len([token for token in doc]))
        doc._.set("n_sents", len([sent for sent in doc.sents]))
        # doc._.set("n_words", len(doc._.words))
        # doc._.set("n_content_words", len(doc._.content_words))
        # doc._.set("n_punctuation", len(doc._.punctuation))
        return doc
