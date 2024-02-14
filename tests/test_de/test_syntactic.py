import unittest

from src.stylo_metrix.stylo_metrix import StyloMetrix


class TestSyntacticDE(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        lang = "de"
        cls.sm = StyloMetrix(lang, debug=True)

    def test_SY_OA(self):
        metric = "SY_OA"
        test_text = "Neue Gewohnheiten etablieren:"
        expected_debug = ["Gewohnheiten"]
        expected_out = 0.25

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_S_INF(self):
        metric = "SY_S_INF"
        test_text = "Neue Gewohnheiten etablieren:"
        expected_debug = ["Neue", "Gewohnheiten", "etablieren", ":"]
        expected_out = 1.0

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_APPR(self):
        metric = "SY_APPR"
        test_text = "6 Tipps aus der Wissenschaft Neue Angewohnheiten etablieren und alte loswerden – wie funktioniert das?"
        expected_debug = ["aus"]
        expected_out = 0.0625

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_S_INT(self):
        metric = "SY_S_INT"
        test_text = "6 Tipps aus der Wissenschaft Neue Angewohnheiten etablieren und alte loswerden – wie funktioniert das?"
        expected_debug = [
            "6",
            "Tipps",
            "aus",
            "der",
            "Wissenschaft",
            "Neue",
            "Angewohnheiten",
            "etablieren",
            "und",
            "alte",
            "loswerden",
            "–",
            "wie",
            "funktioniert",
            "das",
            "?",
        ]
        expected_out = 1.0

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_ADJD(self):
        metric = "SY_ADJD"
        test_text = "Und stimmt es tatsächlich, dass man dafür nur 21 Tage braucht?"
        expected_debug = ["tatsächlich"]
        expected_out = 0.07692307692307693

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_S_MAN(self):
        metric = "SY_S_MAN"
        test_text = "Und stimmt es tatsächlich, dass man dafür nur 21 Tage braucht?"
        expected_debug = [
            "Und",
            "stimmt",
            "es",
            "tatsächlich",
            ",",
            "dass",
            "man",
            "dafür",
            "nur",
            "21",
            "Tage",
            "braucht",
            "?",
        ]
        expected_out = 1.0

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_S_SUB(self):
        metric = "SY_S_SUB"
        test_text = "Und stimmt es tatsächlich, dass man dafür nur 21 Tage braucht?"
        expected_debug = [
            "Und",
            "stimmt",
            "es",
            "tatsächlich",
            ",",
            "dass",
            "man",
            "dafür",
            "nur",
            "21",
            "Tage",
            "braucht",
            "?",
        ]
        expected_out = 1.0

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_S_DE(self):
        metric = "SY_S_DE"
        test_text = "Der Faktencheck über neue Gewohnheiten."
        expected_debug = ["Der", "Faktencheck", "über", "neue", "Gewohnheiten", "."]
        expected_out = 1.0

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_S_NEG(self):
        metric = "SY_S_NEG"
        test_text = "Die Macht der Gewohnheit...ist nicht per se etwas Schlechtes"
        expected_debug = [
            "Die",
            "Macht",
            "der",
            "Gewohnheit",
            "...",
            "ist",
            "nicht",
            "per",
            "se",
            "etwas",
            "Schlechtes",
        ]
        expected_out = 1.0

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_PTKA(self):
        metric = "SY_PTKA"
        test_text = "Gewohnheiten haben meist einen schlechten Ruf – assoziieren wir sie doch sofort mit negativen Dingen wie Junkfood, Rauchen oder zu wenig Bewegung."
        expected_debug = ["zu"]
        expected_out = 0.041666666666666664

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_S_KOKOM(self):
        metric = "SY_S_KOKOM"
        test_text = "Gewohnheiten haben meist einen schlechten Ruf – assoziieren wir sie doch sofort mit negativen Dingen wie Junkfood, Rauchen oder zu wenig Bewegung."
        expected_debug = [
            "Gewohnheiten",
            "haben",
            "meist",
            "einen",
            "schlechten",
            "Ruf",
            "–",
            "assoziieren",
            "wir",
            "sie",
            "doch",
            "sofort",
            "mit",
            "negativen",
            "Dingen",
            "wie",
            "Junkfood",
            ",",
            "Rauchen",
            "oder",
            "zu",
            "wenig",
            "Bewegung",
            ".",
        ]
        expected_out = 1.0

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_S_COND3(self):
        metric = "SY_S_COND3"
        test_text = "Denn unser Gehirn wäre maßlos überfordert, wenn es jede kleine Handlung bewusst steuern müsste."
        expected_debug = [
            "Denn",
            "unser",
            "Gehirn",
            "wäre",
            "maßlos",
            "überfordert",
            ",",
            "wenn",
            "es",
            "jede",
            "kleine",
            "Handlung",
            "bewusst",
            "steuern",
            "müsste",
            ".",
        ]
        expected_out = 1.0

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_S_EX(self):
        metric = "SY_S_EX"
        test_text = "Lies auch: Journaling – diese Methode macht dich stärker!"
        expected_debug = [
            "Lies",
            "auch",
            ":",
            "Journaling",
            "–",
            "diese",
            "Methode",
            "macht",
            "dich",
            "stärker",
            "!",
        ]
        expected_out = 1.0

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_APPRART(self):
        metric = "SY_APPRART"
        test_text = "Fünf Tipps zum Anfangen"
        expected_debug = ["zum"]
        expected_out = 0.25

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_QUOT(self):
        metric = "SY_QUOT"
        test_text = 'Strategische Inkompetenz: Die Ausrede "Du kannst das viel besser" zieht ab jetzt nicht mehr Komfortzone verlassen:'
        expected_debug = ["Du", "kannst", "das", "viel", "besser"]
        expected_out = 0.25

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_DO(self):
        metric = "SY_DO"
        test_text = "Dadurch werden neue Verknüpfungen in unserem Hirn geschaffen, die sich – wenn wir weiterhin am Ball bleiben und die Bewegungen bzw. Handlungen immer wieder durchführen – festigen."
        expected_debug = ["sich"]
        expected_out = 0.034482758620689655

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_S_SUB_ZU(self):
        metric = "SY_S_SUB_ZU"
        test_text = "Wichtig ist laut Roth außerdem, sich selbst nach jedem Teilerfolg zu belohnen, um dem Gehirn positives Feedback zu geben."
        expected_debug = [
            "Wichtig",
            "ist",
            "laut",
            "Roth",
            "außerdem",
            ",",
            "sich",
            "selbst",
            "nach",
            "jedem",
            "Teilerfolg",
            "zu",
            "belohnen",
            ",",
            "um",
            "dem",
            "Gehirn",
            "positives",
            "Feedback",
            "zu",
            "geben",
            ".",
        ]
        expected_out = 1.0

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_S_COND1(self):
        metric = "SY_S_COND1"
        test_text = "Er empfiehlt, Gewohnheiten besonders dann zu ändern, wenn man in einer neuen Umgebung ist – etwa nach einem Umzug oder auch im Urlaub."
        expected_debug = [
            "Er",
            "empfiehlt",
            ",",
            "Gewohnheiten",
            "besonders",
            "dann",
            "zu",
            "ändern",
            ",",
            "wenn",
            "man",
            "in",
            "einer",
            "neuen",
            "Umgebung",
            "ist",
            "–",
            "etwa",
            "nach",
            "einem",
            "Umzug",
            "oder",
            "auch",
            "im",
            "Urlaub",
            ".",
        ]
        expected_out = 1.0

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_APPO(self):
        metric = "SY_APPO"
        test_text = "Unmerklich kommt man so der Theorie zuliebe zum Konstruieren von Tatsachen, statt es umgekehrt zu machen."
        expected_debug = ["zuliebe"]
        expected_out = 0.05555555555555555

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_S_COND2(self):
        metric = "SY_S_COND2"
        test_text = "Wenn ich genug Geld hätte, würde ich mir ein Auto kaufen"
        expected_debug = [
            "Wenn",
            "ich",
            "genug",
            "Geld",
            "hätte",
            ",",
            "würde",
            "ich",
            "mir",
            "ein",
            "Auto",
            "kaufen",
        ]
        expected_out = 1.0

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)


if __name__ == "__main__":
    unittest.main()
