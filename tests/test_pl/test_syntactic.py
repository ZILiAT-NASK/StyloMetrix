import unittest

from src.stylo_metrix.stylo_metrix import StyloMetrix


class TestSyntacticPL(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        lang = "pl"
        cls.sm = StyloMetrix(lang, debug=True)

    def test_SY_FMWE(self):
        metric = "SY_FMWE"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = ["Księga", "I"]
        expected_out = 0.1

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_APPM(self):
        metric = "SY_APPM"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = ["inwokacją", "Litwo"]
        expected_out = 0.1

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_S_DE(self):
        metric = "SY_S_DE"
        test_text = "Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = [
            "Gospodarstwo",
            "Księga",
            "ta",
            "rozpoczyna",
            "się",
            "inwokacją",
            ":",
            "“",
            "Litwo",
            ",",
            "Ojczyzno",
            "moja",
            ".",
            ".",
            ".",
            "”",
            ".",
        ]
        expected_out = 1.0

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_S_ELL(self):
        metric = "SY_S_ELL"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = [
            "Księga",
            "ta",
            "rozpoczyna",
            "się",
            "inwokacją",
            ":",
            "“",
            "Litwo",
            ",",
            "Ojczyzno",
            "moja",
            ".",
            ".",
            ".",
            "”",
            ".",
        ]
        expected_out = 0.8

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_S_VOC(self):
        metric = "SY_S_VOC"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = [
            "Księga",
            "ta",
            "rozpoczyna",
            "się",
            "inwokacją",
            ":",
            "“",
            "Litwo",
            ",",
            "Ojczyzno",
            "moja",
            ".",
            ".",
            ".",
            "”",
            ".",
        ]
        expected_out = 0.8

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_S_NOM(self):
        metric = "SY_S_NOM"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = ["Księga", "I", ".", "Gospodarstwo"]
        expected_out = 0.2

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_MOD(self):
        metric = "SY_MOD"
        test_text = "Panno święta, co bronisz pięknej i sławnej Częstochowy i świecisz w zabytkowej i starej bramie wiekuistej światłości."
        expected_debug = [
            "święta",
            "pięknej",
            "sławnej",
            "zabytkowej",
            "starej",
            "wiekuistej",
            "światłości",
        ]
        expected_out = 0.3684210526315789

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_NPHR(self):
        metric = "SY_NPHR"
        test_text = "Panno święta, co bronisz pięknej i sławnej Częstochowy i świecisz w zabytkowej i starej bramie wiekuistej światłości."
        expected_debug = [
            ["Panno", "święta"],
            ["Częstochowy", "pięknej", "i", "sławnej"],
            ["bramie", "zabytkowej", "i", "starej", "światłości", "wiekuistej"],
        ]
        expected_out = 0.631578947368421

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_INV_EPI(self):
        metric = "SY_INV_EPI"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = ["I"]
        expected_out = 0.05

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_INIT(self):
        metric = "SY_INIT"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = ["Księga", "Księga"]
        expected_out = 0.1

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_INV_OBJ(self):
        metric = "SY_INV_OBJ"
        test_text = "Tadeusz po długiej nieobecności przybywa do rodzinnego domu."
        expected_debug = [["po", "długiej", "nieobecności", "przybywa"]]
        expected_out = 0.4444444444444444

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_S_NEG(self):
        metric = "SY_S_NEG"
        test_text = "Tadeusz uważa ją za dziewczynę spotkaną uprzednio przelotnie w dworku i z tego powodu nie pozostaje w zalotach dłużny."
        expected_debug = [
            "Tadeusz",
            "uważa",
            "ją",
            "za",
            "dziewczynę",
            "spotkaną",
            "uprzednio",
            "przelotnie",
            "w",
            "dworku",
            "i",
            "z",
            "tego",
            "powodu",
            "nie",
            "pozostaje",
            "w",
            "zalotach",
            "dłużny",
            ".",
        ]
        expected_out = 1.0

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_NPRED(self):
        metric = "SY_NPRED"
        test_text = "Jednym z nich ma być ksiądz Robak - bernardyn, którego wygląd i zachowanie świadczą o jego żołnierskiej przeszłości, a który kwestuje po dworach szlacheckich i okolicznych karczmach. Księga II."
        expected_debug = [("być", "Jednym")]
        expected_out = 0.06060606060606061

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_S_EX(self):
        metric = "SY_S_EX"
        test_text = "Kochajmy się!"
        expected_debug = ["Kochajmy", "się", "!"]
        expected_out = 1.0

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_QUOT(self):
        metric = "SY_QUOT"
        test_text = "Byliśmy wczoraj w kinie na filmie 'Różowa pantera'"
        expected_debug = ["Różowa", "pantera"]
        expected_out = 0.2

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_SIMILE_ADJ(self):
        metric = "SY_SIMILE_ADJ"
        test_text = "On jest głupi jak but"
        expected_debug = ["głupi jak but"]
        expected_out = 0.6

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_S_IN(self):
        metric = "SY_S_IN"
        test_text = "Pójdziemy do kina?"
        expected_debug = ["Pójdziemy", "do", "kina", "?"]
        expected_out = 1.0

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_S_INF(self):
        metric = "SY_S_INF"
        test_text = "Wytępić całe to bydło!"
        expected_debug = ["Wytępić", "całe", "to", "bydło", "!"]
        expected_out = 1.0

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)


if __name__ == "__main__":
    unittest.main()
