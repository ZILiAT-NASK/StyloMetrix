# https://stackoverflow.com/questions/6560354/how-would-i-create-a-custom-list-class-in-python

class StyloMetrixVector:
    def __init__(self, doc, metrics_group):
        self._dicts = [metric(doc) for metric in metrics_group]
        self.name = doc._.name

    def __repr__(self):
        return self._make_repr()

    def __str__(self):
        return str(self._dicts)

    def __len__(self):
        return len(self._dicts)

    def get_values(self):
        v = [metric["value"] for metric in self._dicts]
        return v

    def get_names(self):
        n = [metric["name_pl"] for metric in self._dicts]
        return n

    def get_codes(self):
        c = [metric["code"] for metric in self._dicts]
        return c

    def _make_repr(self):
        r = ', '.join([f"{d['code']}: {d['value']:.2f}" for d in self._dicts])
        return f"<{self.__class__.__name__} file {self.name}: {r}>"
