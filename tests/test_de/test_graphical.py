import unittest

from src.stylo_metrix.stylo_metrix import StyloMetrix


class TestGraphicalDE(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        lang = "de"
        cls.sm = StyloMetrix(lang, debug=True)

    def test_GR_EMOT(self):
        metric = "GR_EMOT"
        test_text = "Das wäre sehr lustig :-)"
        expected_debug = [":-)"]
        expected_out = 0.2

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_GR_HASH(self):
        metric = "GR_HASH"
        test_text = "Das wäre sehr lustig :-) #sowitzig"
        expected_debug = ["#sowitzig"]
        expected_out = 0.14285714285714285

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_GR_LENNY(self):
        metric = "GR_LENNY"
        test_text = "Ich werde euch nicht mehr vertrauen ¯\\\\_(ツ)\\_"
        expected_debug = ["¯\\\\_(ツ)\\_"]
        expected_out = 0.125

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_GR_LINK(self):
        metric = "GR_LINK"
        test_text = "Guck mal, was sie veröffentlicht haben --> https://www.welt.de"
        expected_debug = ["https://www.welt.de"]
        expected_out = 0.1

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_GR_MENTION(self):
        metric = "GR_MENTION"
        test_text = "@USERNAME, ich stimme überhaupt nicht zu!"
        expected_debug = ["@USERNAME"]
        expected_out = 0.125

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_GR_UPPER(self):
        metric = "GR_UPPER"
        test_text = "FIFA hat unsere Bundesliga schrecklicherweise betrogen."
        expected_debug = ["FIFA"]
        expected_out = 0.14285714285714285

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)


if __name__ == "__main__":
    unittest.main()
