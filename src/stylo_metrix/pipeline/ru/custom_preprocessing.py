import unicodedata


class CustomPreprocessing():
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer

    def __call__(self, string):
        right_quote = unicodedata.lookup('RIGHT DOUBLE QUOTATION MARK')
        left_quote = unicodedata.lookup('LEFT DOUBLE QUOTATION MARK')
        return self.tokenizer(string.replace(right_quote, '\"').replace(left_quote, '\"'))
