import unittest

from src.stylo_metrix.stylo_metrix import StyloMetrix


class TestPosEN(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        lang = "en"
        cls.sm = StyloMetrix(lang, debug=True)

    def test_POS_VERB(self):
        metric = "POS_VERB"
        test_text = "The project must be completed by the end of the month. The house must be built by the end of the year."
        expected_debug = ["must", "be", "completed", "must", "be", "built"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_POS_NOUN(self):
        metric = "POS_NOUN"
        test_text = "The project must be completed by the end of the month. The house must be built by the end of the year."
        expected_debug = ["project", "end", "month", "house", "end", "year"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_POS_ADJ(self):
        metric = "POS_ADJ"
        test_text = "She is an attrective girl. He was extremely bored at the class."
        expected_debug = ["attrective", "bored"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_POS_ADV(self):
        metric = "POS_ADV"
        test_text = "She is an attrective girl. He was extremely bored at the class."
        expected_debug = ["extremely"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_POS_DET(self):
        metric = "POS_DET"
        test_text = "The project must be completed by the end of the month. A house must be built by the end of the year."
        expected_debug = ["The", "the", "the", "A", "the", "the"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_POS_INTJ(self):
        metric = "POS_INTJ"
        test_text = "Wow, that sounds great! OMG, that was close."
        expected_debug = ["Wow", "OMG"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_POS_CONJ(self):
        metric = "POS_CONJ"
        test_text = "She was there, but it felt as if she drifted off to another world."
        expected_debug = ["but", "as", "if"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_POS_PART(self):
        metric = "POS_PART"
        test_text = "They want to connect the dots between the Trump campaign and the Russian government."
        expected_debug = ["to"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_POS_NUM(self):
        metric = "POS_NUM"
        test_text = "They met five years ago in the same place where they had met for the first time. The class starts at 9:00 am."
        expected_debug = ["five", "9:00"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_POS_PREP(self):
        metric = "POS_PREP"
        test_text = "We stood by the riverbank. She fell into the water."
        expected_debug = ["by", "into"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_POS_PRO(self):
        metric = "POS_PRO"
        test_text = "We stood by the riverbank. She fell into the water."
        expected_debug = ["We", "She"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)


if __name__ == "__main__":
    unittest.main()
