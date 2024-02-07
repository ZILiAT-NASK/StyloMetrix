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
        test_text = "Wielki odkrywco wyobraźni, nadeszła dziś najwyższa pora, byśmy zaczęli żyć w przyjaźni, twórco czarnego pomidora."
        expected_debug = [
            (
                ["Wielki"],
                ["wyobraźni", "pomidora"],
                ["czarnego"],
                ["odkrywco", "twórco"],
            )
        ]
        expected_out = 0.3157894736842105

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_DESC_APOS_VERB(self):
        metric = "DESC_APOS_VERB"
        test_text = "Kierowniku, podpisałeś dokumenty, a może poszedłeś na kawę?"
        expected_debug = [(["Kierowniku"], ["podpisałeś", "poszedłeś"])]
        expected_out = 0.2727272727272727

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_DESC_ADJ_CP(self):
        metric = "DESC_ADJ_CP"
        test_text = "Wojna polsko-ruska pod biało-czerwoną flagą właśnie się rozpoczęła"
        expected_debug = ["polsko-ruska", "biało-czerwoną"]
        expected_out = 0.5

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_DESC_APOS_ADJ(self):
        metric = "DESC_APOS_ADJ"
        test_text = "Wielki odkrywco wyobraźni, nadeszła już najwyższa pora, byśmy zaczęli żyć w przyjaźni"
        expected_debug = [(["Wielki"], ["odkrywco"])]
        expected_out = 0.14285714285714285

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_DESC_PRON_VOC(self):
        metric = "DESC_PRON_VOC"
        test_text = "Ty impertynencie, jak mogłeś nam to zrobić?"
        expected_debug = ["Ty impertynencie"]
        expected_out = 0.2222222222222222

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_DESC_PRON_ADJ_VOC(self):
        metric = "DESC_PRON_ADJ_VOC"
        test_text = "Ty egocentryczny narcyzie, myślisz tylko o sobie"
        expected_debug = ["Ty egocentryczny narcyzie"]
        expected_out = 0.375

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)


if __name__ == "__main__":
    unittest.main()
