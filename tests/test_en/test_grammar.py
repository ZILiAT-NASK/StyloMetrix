import unittest

from src.stylo_metrix.stylo_metrix import StyloMetrix


class TestGrammarEN(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        lang = "en"
        cls.sm = StyloMetrix(lang, debug=True)

    def test_VF_INFINITIVE(self):
        metric = "VF_INFINITIVE"
        test_text = "To live dangerously is his motto. He likes to do things that make his heart race. She is not brave enough to wrestle with crocodiles. "
        expected_debug = ["live", "do", "race", "wrestle"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_PASSIVE(self):
        metric = "G_PASSIVE"
        test_text = "The book is bought and read by many people. The task will be finished till tomorrow. Silvia's life had been saved by Dr. Richard. The house was built in 1990. The cake is baked by John."
        expected_debug = [
            "is",
            "bought",
            "read",
            "will",
            "be",
            "finished",
            "had",
            "been",
            "saved",
            "was",
            "built",
            "is",
            "baked",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_ACTIVE(self):
        metric = "G_ACTIVE"
        test_text = "She was happy because her novel had been published by a famous company. He felt guilty because he'd been caught cheating on the exam. She'll go to the cinema tomorrow and meet Alex there. I’ll be waiting for you at the station. Will you be okay? It's about a girl who discovers a secret portal in her basement."
        expected_debug = [
            "was",
            "felt",
            "'ll",
            "go",
            "meet",
            "’ll",
            "be",
            "waiting",
            "Will",
            "be",
            "'s",
            "discovers",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_PRESENT(self):
        metric = "G_PRESENT"
        test_text = "I have always loved fantasy stories, so I decided to try my hand at one. He has been working on his project since Monday. Does she like reading book?"
        expected_debug = ["have", "loved", "has", "been", "working", "Does", "like"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_PAST(self):
        metric = "G_PAST"
        test_text = "I had never seen such a beautiful sunset before I visited Hawaii. He was being chased and bitten by a dog when he fell down. They didn't do particularly well on the exams."
        expected_debug = [
            "had",
            "seen",
            "visited",
            "was",
            "being",
            "chased",
            "bitten",
            "fell",
            "did",
            "do",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_FUTURE(self):
        metric = "G_FUTURE"
        test_text = "They’ll come as soon as they finish their work. We won't be able to go to the party. She will be being interviewed by the manager at 10 a.m. tomorrow. By next week, I will have finished my project."
        expected_debug = [
            "’ll",
            "come",
            "wo",
            "be",
            "will",
            "be",
            "being",
            "interviewed",
            "will",
            "have",
            "finished",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_MODALS_SIMPLE(self):
        metric = "G_MODALS_SIMPLE"
        test_text = "We can do that tomorrow. She should be ready till 9pm. You mustn't smoke here. You may go to the cinema. Could you help me with my homework? I might go to the party."
        expected_debug = [
            "can",
            "do",
            "should",
            "be",
            "must",
            "smoke",
            "may",
            "go",
            "Could",
            "help",
            "might",
            "go",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_MODALS_CONT(self):
        metric = "G_MODALS_CONT"
        test_text = "Tom may be sleeping. She must be doing her homework now. You should be working on your project. You can be playing football. Could you be helping me with my homework?"
        expected_debug = [
            "may",
            "be",
            "sleeping",
            "must",
            "be",
            "doing",
            "should",
            "be",
            "working",
            "can",
            "be",
            "playing",
            "Could",
            "be",
            "helping",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_MODALS_PERFECT(self):
        metric = "G_MODALS_PERFECT"
        test_text = "She would have done that long time ago, if not for him. She must have bought this on her way back home. I might have gone to the party. I don't know where John is. He could have missed the train."
        expected_debug = [
            "would",
            "have",
            "done",
            "must",
            "have",
            "bought",
            "might",
            "have",
            "gone",
            "could",
            "have",
            "missed",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)


if __name__ == "__main__":
    unittest.main()
