import math
import unittest

import spacy

from src.stylo_metrix.utils import incidence, ratio


class TestUtils(unittest.TestCase):
    def setUp(self) -> None:
        self.nlp = spacy.load("pl_nask")

    def test_ratio(self):
        v1, v2 = 1, 2
        result = ratio(v1, v2)

        self.assertEqual(result, v1 / v2)

    def test_ratio_exception(self):
        v1, v2 = 1, 0
        result = ratio(v1, v2)

        self.assertEqual(result, 0)

    def test_incidence(self):
        doc = list(range(10))
        selection = list(range(0, 10, 2))
        result = incidence(doc, selection)

        self.assertEqual(result, len(selection) / len(doc))


if __name__ == "__main__":
    unittest.main()
