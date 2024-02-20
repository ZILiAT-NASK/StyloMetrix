import unittest

from src.stylo_metrix.stylo_metrix import StyloMetrix


class TestSyntaxEN(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        lang = "en"
        cls.sm = StyloMetrix(lang, debug=True)

    def test_SY_QUESTION(self):
        metric = "SY_QUESTION"
        test_text = (
            "How have you been? Are you going for a walk? You like her, don't you?"
        )

        expected_debug = [
            "How",
            "have",
            "you",
            "been?",
            "Are",
            "you",
            "going",
            "for",
            "a",
            "walk?",
            "You",
            "like",
            "her,",
            "don't",
            "you?",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_NARRATIVE(self):
        metric = "SY_NARRATIVE"
        test_text = (
            "You can call me by my name. She was tired and upset. Do you like cookies?"
        )

        expected_debug = [
            "You",
            "can",
            "call",
            "me",
            "by",
            "my",
            "name.",
            "She",
            "was",
            "tired",
            "and",
            "upset.",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_NEGATIVE_QUESTIONS(self):
        metric = "SY_NEGATIVE_QUESTIONS"
        test_text = "Don't you want to see her? How can't you recognize him? Aren't you happy? Do you like cookies?"

        expected_debug = [
            "Don't",
            "you",
            "want",
            "to",
            "see",
            "her?",
            "Aren't",
            "you",
            "happy?",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_SPECIAL_QUESTIONS(self):
        metric = "SY_SPECIAL_QUESTIONS"
        test_text = "Don't you want to see her? How can't you recognize him? Aren't you happy? Do you like cookies? Who are those guys and what were they doing?"

        expected_debug = [
            "How",
            "can't",
            "you",
            "recognize",
            "him?",
            "Who",
            "are",
            "those",
            "guys",
            "and",
            "what",
            "were",
            "they",
            "doing?",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_TAG_QUESTIONS(self):
        metric = "SY_TAG_QUESTIONS"
        test_text = "You don't want to see her, do you? How can't you recognize him? You don't like cookies, do you? Who are those guys and what were they doing?"

        expected_debug = [
            "You",
            "don't",
            "want",
            "to",
            "see",
            "her,",
            "do",
            "you?",
            "You",
            "don't",
            "like",
            "cookies,",
            "do",
            "you?",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_GENERAL_QUESTIONS(self):
        metric = "SY_GENERAL_QUESTIONS"
        test_text = "You don't want to see her, do you? How can't you recognize him? Do you know him? Are you fine? Have you been there before? Who are those guys and what were they doing?"

        expected_debug = [
            "been",
            "you",
            "Have",
            "know",
            "before?",
            "him?",
            "there",
            "Do",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        # self.assertSequenceEqual(expected_debug, debug)

    def test_SY_EXCLAMATION(self):
        metric = "SY_EXCLAMATION"
        test_text = "Come back here! How can't you recognize him? Do you know him? I told you that was her! Have you been there before? Who are those guys and what were they doing?"

        expected_debug = [
            "Come",
            "I",
            "was",
            "back",
            "her!",
            "you",
            "that",
            "told",
            "here!",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        # self.assertSequenceEqual(expected_debug, debug)

    def test_SY_IMPERATIVE(self):
        metric = "SY_IMPERATIVE"
        test_text = "Come back here! How can't you recognize him? Do you know him? Look at the window!"

        expected_debug = ["Look", "window", "Come", "the", "here", "back", "at"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        # self.assertSequenceEqual(expected_debug, debug)

    def test_SY_SUBORD_SENT(self):
        metric = "SY_SUBORD_SENT"
        test_text = "I needed to see her because I missed her. Although she doesn't look sick, her voice is definitely hoarse. I know you're not a bad person."

        expected_debug = [
            "I",
            "needed",
            "to",
            "see",
            "her",
            "because",
            "I",
            "missed",
            "her.",
            "Although",
            "she",
            "doesn't",
            "look",
            "sick,",
            "her",
            "voice",
            "is",
            "definitely",
            "hoarse.",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_SUBORD_SENT_PUNCT(self):
        metric = "SY_SUBORD_SENT_PUNCT"
        test_text = "I needed to see her because I missed her. Although she doesn't look sick, her voice is definitely hoarse. I know you're not a bad person."

        expected_debug = [".", ",", "."]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_COORD_SENT(self):
        metric = "SY_COORD_SENT"
        test_text = "She was smart and beautiful. We can go to the restaurat or to the cinema. I like her, but she doesn't like me. We need to call her."

        expected_debug = [
            "She",
            "was",
            "smart",
            "and",
            "beautiful.",
            "We",
            "can",
            "go",
            "to",
            "the",
            "restaurat",
            "or",
            "to",
            "the",
            "cinema.",
            "I",
            "like",
            "her,",
            "but",
            "she",
            "doesn't",
            "like",
            "me.",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_COORD_SENT_PUNCT(self):
        metric = "SY_COORD_SENT_PUNCT"
        test_text = "She was smart and beautiful. We can go to the restaurat or to the cinema. I like her, but she doesn't like me."

        expected_debug = [".", ".", ",", "."]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_SIMPLE_SENT(self):
        metric = "SY_SIMPLE_SENT"
        test_text = "The weather is nice. I like her. Winter. I'm tired. I'm going to sleep. We can go to the restaurat or to the cinema. Although she doesn't look sick, her voice is definitely hoarse."

        expected_debug = [
            "The",
            "weather",
            "is",
            "nice.",
            "I",
            "like",
            "her.",
            "Winter.",
            "I'm",
            "tired.",
            "I'm",
            "going",
            "to",
            "sleep.",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_INVERSE_PATTERNS(self):
        metric = "SY_INVERSE_PATTERNS"
        test_text = "Never a day had she missed her lessons. Not only was Mary famous for helping escaped slaves, but she was also the first African Canadian woman to establish a newspaper. So high is Mount Everest that climbers can take only a couple of steps per minute as they near the summit. Hardly ever have there been so many choices for young people entering the work force as there are today."

        expected_debug = [
            "Never",
            "a",
            "day",
            "had",
            "she",
            "missed",
            "her",
            "lessons.",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_SIMILE(self):
        metric = "SY_SIMILE"
        test_text = (
            "She was as beautiful as ever. He looks like his father. We don't like him."
        )

        expected_debug = [
            "He",
            "looks",
            "like",
            "his",
            "father.",
            "She",
            "was",
            "as",
            "beautiful",
            "as",
            "ever.",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_FRONTING(self):
        metric = "SY_FRONTING"
        test_text = "In June came ponderous heat and mornings like eggshells, pale and smooth. Powerful you have become Dooku, the dark side I sense in you."

        expected_debug = [
            "In",
            "June",
            "came",
            "ponderous",
            "heat",
            "and",
            "mornings",
            "like",
            "eggshells,",
            "pale",
            "and",
            "smooth.",
            "Powerful",
            "you",
            "have",
            "become",
            "Dooku,",
            "the",
            "dark",
            "side",
            "I",
            "sense",
            "in",
            "you.",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_IRRITATION(self):
        metric = "SY_IRRITATION"
        test_text = "She is constantly being late. He was always losing his keys. She kept doing this all the time. I was every time annoying her about this."

        expected_debug = [
            "She",
            "is",
            "constantly",
            "being",
            "late.",
            "He",
            "was",
            "always",
            "losing",
            "his",
            "keys.",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_INTENSIFIER(self):
        metric = "SY_INTENSIFIER"
        test_text = "You do believe her. He did come to your birthday party. She loves him much."

        expected_debug = [
            "You",
            "do",
            "believe",
            "her.",
            "He",
            "did",
            "come",
            "to",
            "your",
            "birthday",
            "party.",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)


if __name__ == "__main__":
    unittest.main()
