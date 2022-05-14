from stylo_metrix.structures.metric import Metric
from stylo_metrix.writer import write_text


class MetricsGroup:
    def __init__(self, *args):
        self._metrics = []
        for arg in args:
            self._add_metric(arg)

    def __repr__(self):
        return self._make_repr()

    def __str__(self):
        return self._make_txt()

    def __iter__(self):
        for m in self._metrics:
            yield m

    def __add__(self, other):
        if isinstance(other, Metric):
            return MetricsGroup(self._metrics + other)
        if isinstance(other, MetricsGroup):
            return MetricsGroup(self._metrics + other._metrics)
        return TypeError()

    def __iadd__(self, other):
        if isinstance(other, (Metric, MetricsGroup)):
            self._add_metric(other)
            return self
        raise TypeError()

    def __len__(self):
        return len(self._metrics)

    def get_codes(self):
        return [m.code for m in self._metrics]

    def _add_metric(self, m):
        if isinstance(m, Metric):
            self._metrics.append(m)
        elif isinstance(m, (list, tuple, MetricsGroup)):
            for x in m:
                self._add_metric(x)
        else:
            raise TypeError()

    # ------ printing ------

    def get_md(self):
        return self._make_md()

    def get_txt(self):
        return self._make_txt()

    def save_md(self, path):
        write_text(self._make_md(), path)

    def save_txt(self, path):
        write_text(self._make_txt(), path)

    def _make_md(self):
        str_list = [
            "| Nr | Kategoria | Kod | Nazwa |",
            "|---|---|---|---|",
            *[f"| 0 | {m.category_pl} | {m.code} | {m.name_pl} |" for m in self],
            "",
        ]
        return '\n'.join(str_list)

    def _make_txt(self):
        c = [4, 20, 16, 40]  # columns width
        str_list = [
            f"{'Nr':<{c[0]}} {'Kategoria':<{c[1]}} {'Kod':<{c[2]}} {'Nazwa':<{c[3]}}",
            '-' * (sum(c) + len(c) - 1),
            *[f"{str(0):<{c[0]}} {m.category_pl:<{c[1]}} {m.code:<{c[2]}} {m.name_pl:<{c[3]}}" for m in self],
            "",
        ]
        return '\n'.join(str_list)

    def _make_repr(self):
        r = ', '.join([metric.code for metric in self])
        return f"<MetricsGroup [{r}]>"
