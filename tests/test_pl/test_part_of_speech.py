import unittest

from src.stylo_metrix.stylo_metrix import StyloMetrix


class TestPart_of_SpeechPL(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        lang = "pl"
        cls.sm = StyloMetrix(lang, debug=True)

    def test_G_N(self):
        metric = "G_N"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = [
            "Księga",
            "Gospodarstwo",
            "Księga",
            "inwokacją",
            "Litwo",
            "Ojczyzno",
        ]
        expected_out = 0.3

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_V(self):
        metric = "G_V"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = ["rozpoczyna"]
        expected_out = 0.05

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_PRO(self):
        metric = "G_PRO"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = ["ta", "się", "moja"]
        expected_out = 0.15

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_PRO_DEM(self):
        metric = "G_PRO_DEM"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = ["ta"]
        expected_out = 0.05

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_PRO_POS(self):
        metric = "G_PRO_POS"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = ["moja"]
        expected_out = 0.05

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_NUM(self):
        metric = "G_NUM"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = ["I"]
        expected_out = 0.05

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_ADJ(self):
        metric = "G_ADJ"
        test_text = "Tadeusz po długiej nieobecności przybywa do rodzinnego domu."
        expected_debug = ["długiej", "rodzinnego"]
        expected_out = 0.2222222222222222

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_ADP(self):
        metric = "G_ADP"
        test_text = "Tadeusz po długiej nieobecności przybywa do rodzinnego domu."
        expected_debug = ["po", "do"]
        expected_out = 0.2222222222222222

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_PRO_IND(self):
        metric = "G_PRO_IND"
        test_text = "Kieruje się do swego dawnego pokoju, ale ze zdziwieniem stwierdza, że komnata ta jest przez kogoś zamieszkiwana."
        expected_debug = ["kogoś"]
        expected_out = 0.05

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_CONJ(self):
        metric = "G_CONJ"
        test_text = "Kieruje się do swego dawnego pokoju, ale ze zdziwieniem stwierdza, że komnata ta jest przez kogoś zamieszkiwana."
        expected_debug = ["ale", "że"]
        expected_out = 0.1

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_CCONJ(self):
        metric = "G_CCONJ"
        test_text = "Kieruje się do swego dawnego pokoju, ale ze zdziwieniem stwierdza, że komnata ta jest przez kogoś zamieszkiwana."
        expected_debug = ["ale"]
        expected_out = 0.05

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_SCONJ(self):
        metric = "G_SCONJ"
        test_text = "Kieruje się do swego dawnego pokoju, ale ze zdziwieniem stwierdza, że komnata ta jest przez kogoś zamieszkiwana."
        expected_debug = ["że"]
        expected_out = 0.05

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_PRO_REL(self):
        metric = "G_PRO_REL"
        test_text = "Przez okno panicz dostrzega młodą dziewczynę, która podlewa w ogródku kwiaty."
        expected_debug = ["która"]
        expected_out = 0.07692307692307693

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_PART(self):
        metric = "G_PART"
        test_text = "Młodzieniec wita się z Wojskim, który opowiada o aktualnych wydarzeniach, zwłaszcza o sporze, jaki zaistniał pomiędzy Hrabią a Sędzią."
        expected_debug = ["zwłaszcza"]
        expected_out = 0.043478260869565216

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_ADV(self):
        metric = "G_ADV"
        test_text = "Następnie młodzieniec wita się z Sędzią."
        expected_debug = ["Następnie"]
        expected_out = 0.14285714285714285

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_PRO_PRS(self):
        metric = "G_PRO_PRS"
        test_text = "Po nim zaś głos zabiera Podkomorzy, krytykując bezmyślne naśladowanie francuskiej mody i obyczajów."
        expected_debug = ["nim"]
        expected_out = 0.06666666666666667

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_CNUM(self):
        metric = "G_CNUM"
        test_text = "Obaj zwracają się w końcu do Wojskiego z prośbą o rozstrzygnięcie, ale ten odmawia stwierdzając, że polowanie na zające uwłacza jego godności i dlatego nie będzie się zajmował tak błahym nieporozumieniem."
        expected_debug = ["Obaj"]
        expected_out = 0.029411764705882353

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_PRO_TOT(self):
        metric = "G_PRO_TOT"
        test_text = "Od tego momentu Gerwazy poprzysiągł Soplicom zemstę i zwalczał ich na każdym kroku."
        expected_debug = ["każdym"]
        expected_out = 0.07142857142857142

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_PRO_INT(self):
        metric = "G_PRO_INT"
        test_text = "Między innymi opowiada historię, jak Wielki Łowczy Dworu, Kozodusin, wtrącił do więzienia urzędnika, którego charty zagryzły jej ulubionego pieska."
        expected_debug = ["jak"]
        expected_out = 0.041666666666666664

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_PRO_NEG(self):
        metric = "G_PRO_NEG"
        test_text = "Rozmawiając o malarstwie i sztuce Telimena oświadcza, że nic nie dorówna pejzażowi włoskiemu."
        expected_debug = ["nic"]
        expected_out = 0.06666666666666667

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_APOS_ADJ(self):
        metric = "APOS_ADJ"
        test_text = "x"
        expected_debug = []  # TODO
        expected_out = 0

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_ABBR(self):
        metric = "G_ABBR"
        test_text = "x"
        expected_debug = []  # TODO
        expected_out = 0

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_INTJ(self):
        metric = "G_INTJ"
        test_text = "x"
        expected_debug = []  # TODO
        expected_out = 0

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_OTHER(self):
        metric = "G_OTHER"
        test_text = "x"
        expected_debug = []  # TODO
        expected_out = 0

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_SYM(self):
        metric = "G_SYM"
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
