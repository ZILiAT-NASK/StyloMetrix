import unittest

from src.stylo_metrix.stylo_metrix import StyloMetrix


class TestHurtlexEN(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        lang = "en"
        cls.sm = StyloMetrix(lang, debug=True)

    def test_AN(self):
        metric = "AN"
        test_text = "This sucker is nothing compared to that crocodilla. You are microörganisms. Sons of bitches."
        expected_debug = ["sucker", "crocodilla", "microörganisms", "bitches"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_DDP(self):
        metric = "DDP"
        test_text = "You are muthafucker. He's a moron. Here they use unintelligence."
        expected_debug = ["muthafucker", "moron", "unintelligence"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SVP(self):
        metric = "SVP"
        test_text = "Are you suffering fom indolency? Lazyness is one of the deadly sins. You're gourmandised."
        expected_debug = ["indolency", "Lazyness", "gourmandised"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_CDS(self):
        metric = "CDS"
        test_text = "Fashism is engraved in their nature. Don't be a rookie."
        expected_debug = ["Fashism", "rookie"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_DDF(self):
        metric = "DDF"
        test_text = (
            "He looks like a runt. Impaired are ugly. You are an emotional cripple."
        )
        expected_debug = ["runt", "Impaired", "ugly", "cripple"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IS(self):
        metric = "IS"
        test_text = (
            "That's total impoverishment. Poorness is pervasive in the third countries."
        )
        expected_debug = ["impoverishment", "Poorness"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_PS(self):
        metric = "PS"
        test_text = "Hey nigga. You're a nitwit. Inter-breeding didn't help us much."
        expected_debug = ["nigga", "nitwit", "breeding"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_RE(self):
        metric = "RE"
        test_text = "Sexual assults are common there. Crucifixion was in vein. He will always reman an abuser."
        expected_debug = ["Sexual", "Crucifixion", "abuser"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
        print(debug)
        print(expected_debug)

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_ASF(self):
        metric = "ASF"
        test_text = "This is a vajayjay. You are a pussy."
        expected_debug = ["vajayjay", "pussy"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_ASM(self):
        metric = "ASM"
        test_text = "You're a fuck-up. Look at your ballocks."
        expected_debug = ["fuck", "ballocks"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_OM(self):
        metric = "OM"
        test_text = (
            "He did it posteriorly. I hate this queerness. Homosexuals are people too."
        )
        expected_debug = ["posteriorly", "queerness", "Homosexuals"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_RCI(self):
        metric = "RCI"
        test_text = "Look at you, peasant.It was taken barbarically."
        expected_debug = ["peasant", "barbarically"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_DMC(self):
        metric = "DMC"
        test_text = (
            "You're a lazybones. Don't be a bastard. He's a faker. She can't be a fool."
        )
        expected_debug = ["lazybones", "bastard", "faker", "fool"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_OR(self):
        metric = "OR"
        test_text = "They're like potatoes. He's faggoty."
        expected_debug = ["potatoes", "faggoty"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_QAS(self):
        metric = "QAS"
        test_text = "He's such a businessperson. Following his rhetoric. That's pure parasitization."
        expected_debug = ["businessperson", "rhetoric", "parasitization"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_PA(self):
        metric = "PA"
        test_text = (
            "You're gonna be a bellboy. She's so pedantic. Stop acting like professors."
        )
        expected_debug = ["bellboy", "pedantic", "professors"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_PR(self):
        metric = "PR"
        test_text = "You're sonuvabitch. Whores are everywhere. Don't be sluts."
        expected_debug = ["sonuvabitch", "Whores", "sluts"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)


if __name__ == "__main__":
    unittest.main()
