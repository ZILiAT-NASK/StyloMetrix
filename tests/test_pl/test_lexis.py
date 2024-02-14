import unittest

from src.stylo_metrix.stylo_metrix import StyloMetrix


class TestLexisPL(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        lang = "pl"
        cls.sm = StyloMetrix(lang, debug=True)

    def test_L_NAME(self):
        metric = "L_NAME"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = ["Litwo"]
        expected_out = 0.05

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_NAME_F(self):
        metric = "L_NAME_F"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = ["Litwo"]
        expected_out = 0.05

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_NAME_ENT(self):
        metric = "L_NAME_ENT"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = ["Litwo"]
        expected_out = 0.05

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_PLACEN_GEOG(self):
        metric = "L_PLACEN_GEOG"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = ["Litwo"]
        expected_out = 0.05

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_SYL_G1(self):
        metric = "L_SYL_G1"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = ["I", "ta", "się"]
        expected_out = 0.15

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_SYL_G2(self):
        metric = "L_SYL_G2"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = ["Księga", "Księga", "Litwo", "moja"]
        expected_out = 0.2

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_SYL_G3(self):
        metric = "L_SYL_G3"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = ["Ojczyzno"]
        expected_out = 0.05

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_SYL_G4(self):
        metric = "L_SYL_G4"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = ["Gospodarstwo", "rozpoczyna", "inwokacją"]
        expected_out = 0.15

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_TTR_IA(self):
        metric = "L_TTR_IA"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = {
            "moja",
            "i",
            "ta",
            "księga",
            "gospodarstwo",
            "litwo",
            "się",
            "ojczyzno",
            "inwokacją",
            "rozpoczyna",
        }
        expected_out = 0.5

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_TTR_LA(self):
        metric = "L_TTR_LA"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = {
            "inwokacja",
            "i",
            "mój",
            "ojczyzna",
            "litwa",
            "księga",
            "gospodarstwo",
            "rozpoczynać",
            "się",
            "ten",
        }
        expected_out = 0.5

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_CONT_A(self):
        metric = "L_CONT_A"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = [
            "Księga",
            "I",
            "Gospodarstwo",
            "Księga",
            "ta",
            "rozpoczyna",
            "inwokacją",
            "Litwo",
            "Ojczyzno",
            "moja",
        ]
        expected_out = 0.5

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_CONT_T(self):
        metric = "L_CONT_T"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = {
            "Litwo",
            "Gospodarstwo",
            "Ojczyzno",
            "moja",
            "ta",
            "I",
            "inwokacją",
            "Księga",
            "rozpoczyna",
        }
        expected_out = 0.45

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_CONT_L(self):
        metric = "L_CONT_L"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = {
            "Litwa",
            "inwokacja",
            "i",
            "mój",
            "ojczyzna",
            "księga",
            "gospodarstwo",
            "rozpoczynać",
            "ten",
        }
        expected_out = 0.45

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_FUNC_A(self):
        metric = "L_FUNC_A"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = ["się"]
        expected_out = 0.05

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_FUNC_T(self):
        metric = "L_FUNC_T"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = {"się"}
        expected_out = 0.05

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_FUNC_L(self):
        metric = "L_FUNC_L"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = {"się"}
        expected_out = 0.05

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_STOP(self):
        metric = "L_STOP"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = ["I", "ta", "się", "moja"]
        expected_out = 0.2

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_TCCT1(self):
        metric = "L_TCCT1"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = ["księga"]
        expected_out = 0.1

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_TCCT5(self):
        metric = "L_TCCT5"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = ["księga"]
        expected_out = 0.1

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_NAME_M(self):
        metric = "L_NAME_M"
        test_text = "Tadeusz po długiej nieobecności przybywa do rodzinnego domu."
        expected_debug = ["Tadeusz"]
        expected_out = 0.1111111111111111

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_PERSN(self):
        metric = "L_PERSN"
        test_text = "Tadeusz po długiej nieobecności przybywa do rodzinnego domu."
        expected_debug = ["Tadeusz"]
        expected_out = 0.1111111111111111

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_PERSN_M(self):
        metric = "L_PERSN_M"
        test_text = "Tadeusz po długiej nieobecności przybywa do rodzinnego domu."
        expected_debug = ["Tadeusz"]
        expected_out = 0.1111111111111111

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_ADVPHR(self):
        metric = "L_ADVPHR"
        test_text = "W czasach słusznie minionych to było niedopuszczalne."
        expected_debug = ["w czasach słusznie minionych"]
        expected_out = 0.5

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_GEOG_ADJ(self):
        metric = "L_GEOG_ADJ"
        test_text = "Po nim zaś głos zabiera Podkomorzy, krytykując bezmyślne naśladowanie francuskiej mody i obyczajów."
        expected_debug = ["francuskiej"]
        expected_out = 0.06666666666666667

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_PERSN_F(self):
        metric = "L_PERSN_F"
        test_text = "Do sali wchodzi Telimena, zajmuje miejsce obok Tadeusza i zaczyna go kokietować."
        expected_debug = ["Telimena"]
        expected_out = 0.07142857142857142

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_ORGN(self):
        metric = "L_ORGN"
        test_text = "Poeta wspomina w tym miejscu o tworzeniu się we Włoszech Legionów Polskich oraz o powstawaniu Księstwa Warszawskiego."
        expected_debug = ["Legionów", "Polskich"]
        expected_out = 0.1111111111111111

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_ETHN(self):
        metric = "L_ETHN"
        test_text = "W odpowiedzi na to sprowadził na zamek Moskali, a podczas walki zastrzelił Horeszkę."
        expected_debug = ["Moskali"]
        expected_out = 0.06666666666666667

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_ERROR(self):
        metric = "L_ERROR"
        test_text = "Znudzona tym wszystkim Telimena proponuje spacer po lesie napewno połączony z grzybobraniem."
        expected_debug = ["napewno"]
        expected_out = 0.07692307692307693

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_ADV_TEMP(self):
        metric = "L_ADV_TEMP"
        test_text = (
            "Później Telimena wsuwa w rękę Tadeusza klucz od swego pokoju i liścik."
        )
        expected_debug = ["Później"]
        expected_out = 0.07692307692307693

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_DATE(self):
        metric = "L_DATE"
        test_text = (
            "Rok 1812 Wiosną tego roku Napoleon wkracza ze swymi wojskami na Litwę."
        )
        expected_debug = ["Rok", "1812"]
        expected_out = 0.15384615384615385

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_ADV_DUR(self):
        metric = "L_ADV_DUR"
        test_text = "Cały czas mnie denerwujesz"
        expected_debug = ["cały czas"]
        expected_out = 0.5

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_ADV_FREQ(self):
        metric = "L_ADV_FREQ"
        test_text = "Wielokrotnie nadużyła już swoich przywilejów"
        expected_debug = ["wielokrotnie"]
        expected_out = 0.2

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_INTENSIF(self):
        metric = "L_INTENSIF"
        test_text = "W Biedronce jest dzisiaj hiperpromocja na gruszki!"
        expected_debug = ["hiperpromocja"]
        expected_out = 0.125

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_VULG(self):
        metric = "L_VULG"
        test_text = "Kolejny chujowy dzień przed nami"
        expected_debug = ["chujowy"]
        expected_out = 0.2

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)


if __name__ == "__main__":
    unittest.main()
