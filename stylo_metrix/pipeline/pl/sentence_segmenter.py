class SentenceSegmenter():

    def __init__(self, nlp):
        self.nlp = nlp

    def __call__(self, doc):
        return self.segment(doc)

    def segment(self, doc):
        for token in doc[:-2]:
            if token.tag_ == 'brev':
                if doc[token.i + 2].text[0].isupper():
                    doc[token.i + 2].is_sent_start = True
                else:
                    doc[token.i + 2].is_sent_start = False
        return doc
