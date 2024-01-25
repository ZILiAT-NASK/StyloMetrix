import unittest

from src.stylo_metrix.stylo_metrix import StyloMetrix


class TestPosUKR(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        lang = "ukr"
        cls.sm = StyloMetrix(lang, debug=True)

    def test_POS_VERB(self):
        metric = "POS_VERB"
        test_text = "Один чоловік побачив на базарі, що мисливець продає живого зайця."
        expected_debug = ["побачив", "продає"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_POS_NOUN(self):
        metric = "POS_NOUN"
        test_text = "Один чоловік побачив на базарі, що мисливець продає живого зайця."
        expected_debug = ["чоловік", "базарі", "мисливець", "зайця"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_POS_ADJ(self):
        metric = "POS_ADJ"
        test_text = "Один чоловік побачив на базарі, що мисливець продає живого зайця."
        expected_debug = ["живого"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_POS_ADV(self):
        metric = "POS_ADV"
        test_text = (
            "Вже веснянки заспівали. Із стріх закрапало, а з гір струмочки покотилися."
        )
        expected_debug = ["Вже"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_POS_DET(self):
        metric = "POS_DET"
        test_text = "Завтра я піду на прогулянку. Мій чоловік придбає для мене цю каблучку. Я напушу листа."
        expected_debug = ["Мій", "цю"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_POS_INTJ(self):
        metric = "POS_INTJ"
        test_text = "Хей! Тут немає цуценяти."
        expected_debug = ["Хей"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_POS_CONJ(self):
        metric = "POS_CONJ"
        test_text = "Її вважають автором багатьох народних пісень: “Ой, не ходи, Грицю” й “Засвіт встали козаченьки” та інших."
        expected_debug = ["й", "та"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_POS_PART(self):
        metric = "POS_PART"
        test_text = "Її вважають автором багатьох народних пісень: “Ой, не ходи, Грицю” й “Засвіт встали козаченьки” та інших."
        expected_debug = ["не"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_POS_NUM(self):
        metric = "POS_NUM"
        test_text = "7 - щасливе число."
        expected_debug = ["7"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_POS_PREP(self):
        metric = "POS_PREP"
        test_text = "Я купила квиток на поїзд."
        expected_debug = ["на"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_POS_PRO(self):
        metric = "POS_PRO"
        test_text = "Я купила квиток на поїзд."
        expected_debug = ["Я"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_POS_OTHER(self):
        metric = "POS_OTHER"
        test_text = "А він тільки xfgh pdl jklw"
        expected_debug = ["xfgh", "pdl", "jklw"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)


if __name__ == "__main__":
    unittest.main()
