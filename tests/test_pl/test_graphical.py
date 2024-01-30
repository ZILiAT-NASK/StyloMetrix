import unittest

from src.stylo_metrix.stylo_metrix import StyloMetrix


class TestGraphicalPL(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        lang = "pl"
        cls.sm = StyloMetrix(lang, debug=True)

    def test_GR_UPPER(self):
        metric = "GR_UPPER"
        test_text = (
            ". W córce Stolnika zakochał się niegdyś znany awanturnik - Jacek Soplica."
        )
        expected_debug = ["W"]
        expected_out = 0.07692307692307693

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_GR_LINK(self):
        metric = "GR_LINK"
        test_text = "Czytaj więcej na https://www.bryk.pl/lektury/adam-mickiewicz/pan-tadeusz.streszczenie-szczegolowe#utm_source=paste&utm_medium=paste&utm_campaign=other"
        expected_debug = [
            "https://www.bryk.pl/lektury/adam-mickiewicz/pan-tadeusz.streszczenie-szczegolowe#utm_source=paste&utm_medium=paste&utm_campaign=other"
        ]
        expected_out = 0.25

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_GR_EMOJI(self):
        metric = "GR_EMOJI"
        test_text = "x"
        expected_debug = []  # TODO
        expected_out = 0

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_GR_EMOT(self):
        metric = "GR_EMOT"
        test_text = "x"
        expected_debug = []  # TODO
        expected_out = 0

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_GR_HASH(self):
        metric = "GR_HASH"
        test_text = "x"
        expected_debug = []  # TODO
        expected_out = 0

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_GR_LENNY(self):
        metric = "GR_LENNY"
        test_text = "x"
        expected_debug = []  # TODO
        expected_out = 0

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_GR_MENTION(self):
        metric = "GR_MENTION"
        test_text = "x"
        expected_debug = []  # TODO
        expected_out = 0

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)


if __name__ == "__main__":
    unittest.main()
