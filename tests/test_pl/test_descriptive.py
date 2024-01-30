import unittest

from src.stylo_metrix.stylo_metrix import StyloMetrix


class TestDescriptivePL(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        lang = "pl"
        cls.sm = StyloMetrix(lang, debug=True)

    def test_DESC_ADV(self):
        metric = "DESC_ADV"
        test_text = "Tadeusz uważa ją za dziewczynę spotkaną uprzednio przelotnie w dworku i z tego powodu nie pozostaje w zalotach dłużny."
        expected_debug = ["uprzednio", "przelotnie"]
        expected_out = 0.1

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_DESC_ADV_ADV(self):
        metric = "DESC_ADV_ADV"
        test_text = "Tadeusz uważa ją za dziewczynę spotkaną uprzednio przelotnie w dworku i z tego powodu nie pozostaje w zalotach dłużny."
        expected_debug = ["uprzednio przelotnie"]
        expected_out = 0.1

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_DESC_ADV_ADJ(self):
        metric = "DESC_ADV_ADJ"
        test_text = "Obaj zwracają się w końcu do Wojskiego z prośbą o rozstrzygnięcie, ale ten odmawia stwierdzając, że polowanie na zające uwłacza jego godności i dlatego nie będzie się zajmował tak błahym nieporozumieniem."
        expected_debug = ["tak błahym"]
        expected_out = 0.058823529411764705

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_DESC_ADJ(self):
        metric = "DESC_ADJ"
        test_text = "Jednym z nich ma być ksiądz Robak - bernardyn, którego wygląd i zachowanie świadczą o jego żołnierskiej przeszłości, a który kwestuje po dworach szlacheckich i okolicznych karczmach. Księga II."
        expected_debug = ["szlacheckich", "i", "okolicznych"]
        expected_out = 0.09090909090909091

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_DESC_APOS_NPHR(self):
        metric = "DESC_APOS_NPHR"
        test_text = "x"
        expected_debug = []  # TODO
        expected_out = 0

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_DESC_APOS_VERB(self):
        metric = "DESC_APOS_VERB"
        test_text = "x"
        expected_debug = []  # TODO
        expected_out = 0

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_DESC_PRON_VOC(self):
        metric = "DESC_PRON_VOC"
        test_text = "x"
        expected_debug = []  # TODO
        expected_out = 0

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_ADJ_CP(self):
        metric = "G_ADJ_CP"
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
