import unittest

from src.stylo_metrix.stylo_metrix import StyloMetrix


class TestInflectionDE(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        lang = "de"
        cls.sm = StyloMetrix(lang, debug=True)

    def test_IN_N_PL(self):
        metric = "IN_N_PL"
        test_text = "Neue Gewohnheiten etablieren:"
        expected_debug = ["Gewohnheiten"]
        expected_out = 0.25

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_N_FP(self):
        metric = "IN_N_FP"
        test_text = "Neue Gewohnheiten etablieren:"
        expected_debug = ["Gewohnheiten"]
        expected_out = 0.25

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_N_4ACC(self):
        metric = "IN_N_4ACC"
        test_text = "Neue Gewohnheiten etablieren:"
        expected_debug = ["Gewohnheiten"]
        expected_out = 0.25

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_ADJ_POS(self):
        metric = "IN_ADJ_POS"
        test_text = "Neue Gewohnheiten etablieren:"
        expected_debug = ["Neue"]
        expected_out = 0.25

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_INF(self):
        metric = "IN_V_INF"
        test_text = "Neue Gewohnheiten etablieren:"
        expected_debug = ["etablieren"]
        expected_out = 0.25

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_N_SG(self):
        metric = "IN_N_SG"
        test_text = "6 Tipps aus der Wissenschaft Neue Angewohnheiten etablieren und alte loswerden – wie funktioniert das?"
        expected_debug = ["Wissenschaft"]
        expected_out = 0.0625

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_N_FS(self):
        metric = "IN_N_FS"
        test_text = "6 Tipps aus der Wissenschaft Neue Angewohnheiten etablieren und alte loswerden – wie funktioniert das?"
        expected_debug = ["Wissenschaft"]
        expected_out = 0.0625

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_N_MP(self):
        metric = "IN_N_MP"
        test_text = "6 Tipps aus der Wissenschaft Neue Angewohnheiten etablieren und alte loswerden – wie funktioniert das?"
        expected_debug = ["Tipps"]
        expected_out = 0.0625

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_N_1NOM(self):
        metric = "IN_N_1NOM"
        test_text = "6 Tipps aus der Wissenschaft Neue Angewohnheiten etablieren und alte loswerden – wie funktioniert das?"
        expected_debug = ["Tipps"]
        expected_out = 0.0625

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_N_3DAT(self):
        metric = "IN_N_3DAT"
        test_text = "6 Tipps aus der Wissenschaft Neue Angewohnheiten etablieren und alte loswerden – wie funktioniert das?"
        expected_debug = ["Wissenschaft"]
        expected_out = 0.0625

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_PRO_SG(self):
        metric = "IN_PRO_SG"
        test_text = "6 Tipps aus der Wissenschaft Neue Angewohnheiten etablieren und alte loswerden – wie funktioniert das?"
        expected_debug = ["das"]
        expected_out = 0.0625

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_PRO_1NOM(self):
        metric = "IN_PRO_1NOM"
        test_text = "6 Tipps aus der Wissenschaft Neue Angewohnheiten etablieren und alte loswerden – wie funktioniert das?"
        expected_debug = ["das"]
        expected_out = 0.0625

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_ART_SG(self):
        metric = "IN_ART_SG"
        test_text = "6 Tipps aus der Wissenschaft Neue Angewohnheiten etablieren und alte loswerden – wie funktioniert das?"
        expected_debug = ["der"]
        expected_out = 0.0625

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_ART_DEF_SG(self):
        metric = "IN_ART_DEF_SG"
        test_text = "6 Tipps aus der Wissenschaft Neue Angewohnheiten etablieren und alte loswerden – wie funktioniert das?"
        expected_debug = ["der"]
        expected_out = 0.0625

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_ART_F(self):
        metric = "IN_ART_F"
        test_text = "6 Tipps aus der Wissenschaft Neue Angewohnheiten etablieren und alte loswerden – wie funktioniert das?"
        expected_debug = ["der"]
        expected_out = 0.0625

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_ART_3DAT(self):
        metric = "IN_ART_3DAT"
        test_text = "6 Tipps aus der Wissenschaft Neue Angewohnheiten etablieren und alte loswerden – wie funktioniert das?"
        expected_debug = ["der"]
        expected_out = 0.0625

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_ART_DEF_3DAT(self):
        metric = "IN_ART_DEF_3DAT"
        test_text = "6 Tipps aus der Wissenschaft Neue Angewohnheiten etablieren und alte loswerden – wie funktioniert das?"
        expected_debug = ["der"]
        expected_out = 0.0625

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_FIN(self):
        metric = "IN_V_FIN"
        test_text = "Wie viele von unseren täglichen Handlungen von Gewohnheiten beeinflusst werden, lässt sich nur schwer schätzen, weil das individuell unterschiedlich ist."
        expected_debug = ["werden", "lässt", "ist"]
        expected_out = 0.13043478260869565

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_PRES(self):
        metric = "IN_V_PRES"
        test_text = "Wie viele von unseren täglichen Handlungen von Gewohnheiten beeinflusst werden, lässt sich nur schwer schätzen, weil das individuell unterschiedlich ist."
        expected_debug = ["werden", "lässt", "ist"]
        expected_out = 0.13043478260869565

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_3SG(self):
        metric = "IN_V_3SG"
        test_text = "6 Tipps aus der Wissenschaft Neue Angewohnheiten etablieren und alte loswerden – wie funktioniert das?"
        expected_debug = ["funktioniert"]
        expected_out = 0.0625

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_3PL(self):
        metric = "IN_V_3PL"
        test_text = "Wie viele von unseren täglichen Handlungen von Gewohnheiten beeinflusst werden, lässt sich nur schwer schätzen, weil das individuell unterschiedlich ist."
        expected_debug = ["werden"]
        expected_out = 0.0625

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_ADV_POS(self):
        metric = "IN_ADV_POS"
        test_text = "Und stimmt es tatsächlich, dass man dafür nur 21 Tage braucht?"
        expected_debug = ["tatsächlich"]
        expected_out = 0.07692307692307693

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_PRO_3SG(self):
        metric = "IN_PRO_3SG"
        test_text = "Und stimmt es tatsächlich, dass man dafür nur 21 Tage braucht?"
        expected_debug = ["es"]
        expected_out = 0.07692307692307693

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_N_MS(self):
        metric = "IN_N_MS"
        test_text = "Der Faktencheck über neue Gewohnheiten."
        expected_debug = ["Faktencheck"]
        expected_out = 0.16666666666666666

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_ART_M(self):
        metric = "IN_ART_M"
        test_text = "Der Faktencheck über neue Gewohnheiten."
        expected_debug = ["Der"]
        expected_out = 0.16666666666666666

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_ART_1NOM(self):
        metric = "IN_ART_1NOM"
        test_text = "Der Faktencheck über neue Gewohnheiten."
        expected_debug = ["Der"]
        expected_out = 0.16666666666666666

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_ART_DEF_1NOM(self):
        metric = "IN_ART_DEF_1NOM"
        test_text = "Der Faktencheck über neue Gewohnheiten."
        expected_debug = ["Der"]
        expected_out = 0.16666666666666666

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_N_NS(self):
        metric = "IN_N_NS"
        test_text = "Die Macht der Gewohnheit...ist nicht per se etwas Schlechtes"
        expected_debug = ["Schlechtes"]
        expected_out = 0.09090909090909091

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_N_2GEN(self):
        metric = "IN_N_2GEN"
        test_text = "Die Macht der Gewohnheit...ist nicht per se etwas Schlechtes"
        expected_debug = ["Gewohnheit"]
        expected_out = 0.09090909090909091

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_ART_2GEN(self):
        metric = "IN_ART_2GEN"
        test_text = "Die Macht der Gewohnheit...ist nicht per se etwas Schlechtes"
        expected_debug = ["der"]
        expected_out = 0.09090909090909091

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_ART_DEF_2GEN(self):
        metric = "IN_ART_DEF_2GEN"
        test_text = "Die Macht der Gewohnheit...ist nicht per se etwas Schlechtes"
        expected_debug = ["der"]
        expected_out = 0.09090909090909091

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_AUX_FIN(self):
        metric = "IN_V_AUX_FIN"
        test_text = "Die Macht der Gewohnheit...ist nicht per se etwas Schlechtes"
        expected_debug = ["ist"]
        expected_out = 0.09090909090909091

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_AUX2_FIN(self):
        metric = "IN_V_AUX2_FIN"
        test_text = "Die Macht der Gewohnheit...ist nicht per se etwas Schlechtes"
        expected_debug = ["ist"]
        expected_out = 0.09090909090909091

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_PRO_PL(self):
        metric = "IN_PRO_PL"
        test_text = "Wie viele von unseren täglichen Handlungen von Gewohnheiten beeinflusst werden, lässt sich nur schwer schätzen, weil das individuell unterschiedlich ist."
        expected_debug = ["viele", "unseren"]
        expected_out = 0.08695652173913043

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_PRO_3DAT(self):
        metric = "IN_PRO_3DAT"
        test_text = "Wie viele von unseren täglichen Handlungen von Gewohnheiten beeinflusst werden, lässt sich nur schwer schätzen, weil das individuell unterschiedlich ist."
        expected_debug = ["unseren"]
        expected_out = 0.043478260869565216

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_PRO_4ACC(self):
        metric = "IN_PRO_4ACC"
        test_text = "Du hasst mich, du hasst mich, du hast mich gefragt und ich habe nichts gesagt"
        expected_debug = ["mich", "mich", "mich"]
        expected_out = 0.17647058823529413

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_POSS_1PL(self):
        metric = "IN_POSS_1PL"
        test_text = "Wie viele von unseren täglichen Handlungen von Gewohnheiten beeinflusst werden, lässt sich nur schwer schätzen, weil das individuell unterschiedlich ist."
        expected_debug = ["unseren"]
        expected_out = 0.043478260869565216

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_PAST(self):
        metric = "IN_V_PAST"
        test_text = "Ich hatte so was überhaupt nicht erwartet, bevor er das mit uns mitteilte. Niemand wusste nichts davon. Wir haben eine andere Antwort erwartet"
        expected_debug = [
            "mitteilte",
            "wusste",
            (["haben"], ["erwartet"]),
            (["hatte"], ["erwartet"]),
        ]
        expected_out = 0.23076923076923078

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_PP(self):
        metric = "IN_V_PP"
        test_text = "Wie viele von unseren täglichen Handlungen von Gewohnheiten beeinflusst werden, lässt sich nur schwer schätzen, weil das individuell unterschiedlich ist."
        expected_debug = ["beeinflusst"]
        expected_out = 0.043478260869565216

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_PERFEKT(self):
        metric = "IN_V_PERFEKT"
        test_text = "Für Sherlock Holmes ist sie immer nur DIE Frau. Ich habe kaum je gehört, daß er sie anders genannt hätte."
        expected_debug = [("habe", "gehört")]
        expected_out = 0.08695652173913043

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_FUT1(self):
        metric = "IN_V_FUT1"
        test_text = (
            "Ich werde die ganze Nacht singen und tanzen, weil du schlafen wirst."
        )
        expected_debug = [(["werde", "wirst"], ["singen", "tanzen", "schlafen"])]
        expected_out = 0.35714285714285715

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_FUT(self):
        metric = "IN_V_FUT"
        test_text = "Ich werde die ganze Nacht singen und tanzen. Du wirst so was nicht bei Freitag erledigt haben"
        expected_debug = [
            (["werde"], ["singen", "tanzen"]),
            (["wirst"], ["erledigt"], ["haben"]),
        ]
        expected_out = 0.3333333333333333

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_PASS(self):
        metric = "IN_V_PASS"
        test_text = "Wie viele von unseren täglichen Handlungen von Gewohnheiten beeinflusst werden, lässt sich nur schwer schätzen, weil das individuell unterschiedlich ist."
        expected_debug = [(["werden"], ["beeinflusst"])]
        expected_out = 0.08695652173913043

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_N_NP(self):
        metric = "IN_N_NP"
        test_text = "Der Professor für Sozialpsychologie Bas Verplanken, der sich seit über 20 Jahren mit dem Einfluss von Angewohnheiten auf unser Leben und Wesen beschäftigt, geht allerdings von rund 30 bis 50 Prozent aus."
        expected_debug = ["Jahren"]
        expected_out = 0.02857142857142857

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_PRO_1PL(self):
        metric = "IN_PRO_1PL"
        test_text = "Gewohnheiten haben meist einen schlechten Ruf – assoziieren wir sie doch sofort mit negativen Dingen wie Junkfood, Rauchen oder zu wenig Bewegung."
        expected_debug = ["wir"]
        expected_out = 0.041666666666666664

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_ART_IND_SG(self):
        metric = "IN_ART_IND_SG"
        test_text = "Gewohnheiten haben meist einen schlechten Ruf – assoziieren wir sie doch sofort mit negativen Dingen wie Junkfood, Rauchen oder zu wenig Bewegung."
        expected_debug = ["einen"]
        expected_out = 0.041666666666666664

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_ART_4ACC(self):
        metric = "IN_ART_4ACC"
        test_text = "Gewohnheiten haben meist einen schlechten Ruf – assoziieren wir sie doch sofort mit negativen Dingen wie Junkfood, Rauchen oder zu wenig Bewegung."
        expected_debug = ["einen"]
        expected_out = 0.041666666666666664

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_ART_IND_4ACC(self):
        metric = "IN_ART_IND_4ACC"
        test_text = "Gewohnheiten haben meist einen schlechten Ruf – assoziieren wir sie doch sofort mit negativen Dingen wie Junkfood, Rauchen oder zu wenig Bewegung."
        expected_debug = ["einen"]
        expected_out = 0.041666666666666664

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_1PL(self):
        metric = "IN_V_1PL"
        test_text = "Gewohnheiten assoziieren wir doch sofort mit negativen Dingen wie Junkfood, Rauchen oder zu wenig Bewegung."
        expected_debug = ["assoziieren"]
        expected_out = 0.058823529411764705

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_PRO_3PL(self):
        metric = "IN_PRO_3PL"
        test_text = "Dabei sind sie an sich nichts Schlechtes."
        expected_debug = ["sie"]
        expected_out = 0.125

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_SUB(self):
        metric = "IN_V_SUB"
        test_text = "Wissenschaftler:innen gehen sogar davon aus, dass wir ohne sie nicht lebensfähig wären."
        expected_debug = ["wären"]
        expected_out = 0.0625

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_PAST_SUB(self):
        metric = "IN_V_PAST_SUB"
        test_text = "Er sagte, er ginge mit mit ins Kino."
        expected_debug = ["ginge"]
        expected_out = 0.1

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_AUX_MOD_FIN(self):
        metric = "IN_V_AUX_MOD_FIN"
        test_text = "Denn unser Gehirn wäre maßlos überfordert, wenn es jede kleine Handlung bewusst steuern müsste."
        expected_debug = ["müsste"]
        expected_out = 0.0625

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_PAST_IMP_MOD(self):
        metric = "IN_V_PAST_IMP_MOD"
        test_text = (
            "Ich wollte dich einladen, leider konnte ich dein Telefonnumer nicht finden"
        )
        expected_debug = ["wollte", "konnte"]
        expected_out = 0.16666666666666666

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_PAST_SUB_PLUSQ(self):
        metric = "IN_V_PAST_SUB_PLUSQ"
        test_text = "Sie hätte das Konzert besuchen dürfen, wenn sie ihre Hausaufgaben gemacht hätte."
        expected_debug = [["hätte", "hätte", "gemacht", "besuchen", "dürfen"]]
        expected_out = 0.35714285714285715

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_ADV_CMP(self):
        metric = "IN_ADV_CMP"
        test_text = "Lies auch: Journaling – diese Methode macht dich stärker!"
        expected_debug = ["stärker"]
        expected_out = 0.09090909090909091

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_PRO_2SG(self):
        metric = "IN_PRO_2SG"
        test_text = "Lies auch: Journaling – diese Methode macht dich stärker!"
        expected_debug = ["dich"]
        expected_out = 0.09090909090909091

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_2SG(self):
        metric = "IN_V_2SG"
        test_text = 'Strategische Inkompetenz: Die Ausrede "Du kannst das viel besser" zieht ab jetzt nicht mehr Komfortzone verlassen:'
        expected_debug = ["kannst"]
        expected_out = 0.05

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_ART_PL(self):
        metric = "IN_ART_PL"
        test_text = "Ohne Gewohnheiten wären wir außerdem nicht in der Lage, Neues zu lernen – weil unser Gehirn sich die neu erworbenen Fähigkeiten schlicht nicht merken könnte."
        expected_debug = ["die"]
        expected_out = 0.037037037037037035

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_ART_DEF_PL(self):
        metric = "IN_ART_DEF_PL"
        test_text = "Ohne Gewohnheiten wären wir außerdem nicht in der Lage, Neues zu lernen – weil unser Gehirn sich die neu erworbenen Fähigkeiten schlicht nicht merken könnte."
        expected_debug = ["die"]
        expected_out = 0.037037037037037035

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_ART_N(self):
        metric = "IN_ART_N"
        test_text = "In unserem Handlungsgedächtnis werden alle erfolgreichen Bewegungen und Handlungen abgespeichert, beim nächsten Mal erinnert sich das Gehirn daran."
        expected_debug = ["das"]
        expected_out = 0.05

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_ART_DEF_4ACC(self):
        metric = "IN_ART_DEF_4ACC"
        test_text = "Das Thema Gewohnheiten ist für die Wissenschaft ein wichtiges und vielfach untersuchtes Thema – einerseits, weil wir sie so dringend brauchen, andererseits, weil sie uns oft ausbremsen und wir uns mit ungesunden Gewohnheiten selbst schaden."
        expected_debug = ["die"]
        expected_out = 0.02564102564102564

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_VVIZU(self):
        metric = "IN_V_VVIZU"
        test_text = "Es ist also ratsam, nicht alle guten Vorsätze (regelmäßig Sport, weniger Ungesundes essen, mit dem Rauchen aufhören...) auf einmal anzugehen."
        expected_debug = ["anzugehen"]
        expected_out = 0.037037037037037035

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_ADJ_CMP(self):
        metric = "IN_ADJ_CMP"
        test_text = "Hat man sich große Vorsätze vorgenommen, gelingen diese eher, wenn man sie in kleinere Zwischenschritte unterteilt, erklärt der deutsche Biologe und Hirnforscher Gerhard Roth."
        expected_debug = ["kleinere"]
        expected_out = 0.03571428571428571

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_POSS_3SG(self):
        metric = "IN_POSS_3SG"
        test_text = "Die Art, wie man sich selbst belohnt, sollte man dabei variieren – damit die Belohnungen nicht zur Gewohnheit werden und ihre Wirkung verlieren."
        expected_debug = ["ihre"]
        expected_out = 0.038461538461538464

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_POSS_3PL(self):
        metric = "IN_POSS_3PL"
        test_text = "Die Art, wie man sich selbst belohnt, sollte man dabei variieren – damit die Belohnungen nicht zur Gewohnheit werden und ihre Wirkung verlieren."
        expected_debug = ["ihre"]
        expected_out = 0.038461538461538464

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_PAST_IMP(self):
        metric = "IN_V_PAST_IMP"
        test_text = "Die Art, wie man sich selbst belohnt, sollte man dabei variieren – damit die Belohnungen nicht zur Gewohnheit werden und ihre Wirkung verlieren."
        expected_debug = ["sollte"]
        expected_out = 0.038461538461538464

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_PAST_IMP_AUX(self):
        metric = "IN_V_PAST_IMP_AUX"
        test_text = "Die Art, wie man sich selbst belohnt, sollte man dabei variieren – damit die Belohnungen nicht zur Gewohnheit werden und ihre Wirkung verlieren."
        expected_debug = ["sollte"]
        expected_out = 0.038461538461538464

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_ART_IND_1NOM(self):
        metric = "IN_ART_IND_1NOM"
        test_text = "Eine neue Umgebung nutzen:"
        expected_debug = ["Eine"]
        expected_out = 0.2

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_ART_IND_3DAT(self):
        metric = "IN_ART_IND_3DAT"
        test_text = "Er empfiehlt, Gewohnheiten besonders dann zu ändern, wenn man in einer neuen Umgebung ist – etwa nach einem Umzug oder auch im Urlaub."
        expected_debug = ["einer", "einem"]
        expected_out = 0.07692307692307693

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_POSS_2SG(self):
        metric = "IN_POSS_2SG"
        test_text = "Wenn du dir zum Beispiel angewöhnen willst, jeden Morgen ein großes Glas Wasser zu trinken, kannst du das jedes Mal machen, wenn du deinen ersten Kaffee trinkst."
        expected_debug = ["deinen"]
        expected_out = 0.03225806451612903

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_2PL(self):
        metric = "IN_V_2PL"
        test_text = "Wenn du dir zum Beispiel angewöhnen willst, jeden Morgen ein großes Glas Wasser zu trinken, kannst du das jedes Mal machen, wenn du deinen ersten Kaffee trinkst."
        expected_debug = ["willst"]
        expected_out = 0.03225806451612903

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_ADJ_SUP(self):
        metric = "IN_ADJ_SUP"
        test_text = "Aus wissenschaftlicher Sicht ist einer der größten Motivationsfaktoren, wenn unsere Ziele mit unseren Werten übereinstimmen."
        expected_debug = ["größten"]
        expected_out = 0.058823529411764705

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_PAST_IMP2(self):
        metric = "IN_V_PAST_IMP2"
        test_text = '"Diese Idee stammt aus einem Selbsthilfebuch aus den 60er-Jahren und ist ehrlich gesagt lächerlich – die Grundaussage bezog sich auch nicht auf Gewohnheiten, sondern darauf, wie lange es dauert, bis man sich nach einer Schönheits-OP an das neue Spiegelbild gewöhnt", erklärt die britische Psychologin Wendy Wood.'
        expected_debug = ["bezog"]
        expected_out = 0.018867924528301886

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_ADV_SUP(self):
        metric = "IN_ADV_SUP"
        test_text = "Am schnellsten sollten wir diese Sache erledigen"
        expected_debug = ["schnellsten"]
        expected_out = 0.14285714285714285

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_ART_IND_2GEN(self):
        metric = "IN_ART_IND_2GEN"
        test_text = "Das kleine Herz eines kleinen Kindes stand still für Stunden"
        expected_debug = ["eines"]
        expected_out = 0.1

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_POSS_1SG(self):
        metric = "IN_POSS_1SG"
        test_text = (
            "Komm, ich zeig dir, wie groß meine Liebe ist und bringe mich für dich um"
        )
        expected_debug = ["meine"]
        expected_out = 0.058823529411764705

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_POSS_2PL(self):
        metric = "IN_POSS_2PL"
        test_text = (
            "Komm, ich zeig dir, wie groß eure Liebe ist und bringe mich für dich um"
        )
        expected_debug = ["eure"]
        expected_out = 0.058823529411764705

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_PRO_1SG(self):
        metric = "IN_PRO_1SG"
        test_text = "Es ist die Eifersucht, die mich auffrisst immer dann, wenn du nicht in meiner Nähe bist"
        expected_debug = ["mich"]
        expected_out = 0.05555555555555555

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_PRO_2GEN(self):
        metric = "IN_PRO_2GEN"
        expected_debug = ["meines"]
        expected_out = 0.14285714285714285

        test_text = "Du bist die wahre Liebe meines Lebens"
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_PRO_2PL(self):
        metric = "IN_PRO_2PL"
        expected_debug = ["euch"]
        test_text = (
            "Komm, schau mal, wie gross meine Liebe ist, ich bringe mich für euch um"
        )
        expected_out = 0.058823529411764705

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_1SG(self):
        metric = "IN_V_1SG"
        test_text = (
            "Komm, ich zeige dir, wie groß meine Liebe ist und bringe mich für dich um"
        )
        expected_debug = ["zeige", "bringe"]
        expected_out = 0.058823529411764705

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_FUT2(self):
        metric = "IN_V_FUT2"
        test_text = "Ich werde es bei Dienstag erledigt haben"
        expected_debug = [(["werde"], ["erledigt"], ["haben"])]
        expected_out = 0.42857142857142855

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_KOND1(self):
        metric = "IN_V_KOND1"
        test_text = "Ich würde gerne ein Paar Bücher kaufen."
        expected_debug = [("würde", "kaufen")]
        expected_out = 0.25

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_KOND2(self):
        metric = "IN_V_KOND2"
        test_text = "Ich würde ihn danach gefragt haben."
        expected_debug = [["würde", "gefragt", "haben"]]
        expected_out = 0.42857142857142855

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_PASS_MOD(self):
        metric = "IN_V_PASS_MOD"
        test_text = "Der Professor muss befragt werden. Der Professor musste befragt werden. Der Professor hat befragt werden müssen"
        expected_debug = [
            (["muss"], ["befragt"], ["werden"]),
            (["musste"], ["befragt"], ["werden"]),
            (["müssen"], ["befragt"], ["werden"]),
        ]
        expected_out = 0.5

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_PLUSQUAM(self):
        metric = "IN_V_PLUSQUAM"
        test_text = "Ich hatte ihn angerufen, bevor er nach Hause kam"
        expected_debug = [(["hatte"], ["angerufen"])]
        expected_out = 0.2

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_PRES_SUB(self):
        metric = "IN_V_PRES_SUB"
        test_text = "Es lebe der Frieden!"
        expected_debug = ["lebe"]
        expected_out = 0.2

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)


if __name__ == "__main__":
    unittest.main()
