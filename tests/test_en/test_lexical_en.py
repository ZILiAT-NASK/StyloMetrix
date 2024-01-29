import unittest

from src.stylo_metrix.stylo_metrix import StyloMetrix


class TestLexicalEN(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        lang = "en"
        cls.sm = StyloMetrix(lang, debug=True)

    def test_L_TYPE_TOKEN_RATIO_LEMMAS(self):
        metric = "L_TYPE_TOKEN_RATIO_LEMMAS"
        test_text = """Text in the present passive is written when the subject of the sentence isn't the doer of the action, but the receiver. For example, "The cake is baked by John" is a present passive sentence, because the cake is not baking itself, but John is baking it."""

        expected_debug = [
            "in",
            "because",
            "not",
            "passive",
            "be",
            "by",
            "cake",
            "text",
            "bake",
            "example",
            "the",
            "subject",
            "sentence",
            "write",
            "for",
            "but",
            "doer",
            "when",
            "John",
            "action",
            "receiver",
            "of",
            "itself",
            "it",
            "a",
            "present",
        ]
        expected_out = 0.5531914893617021

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = {}

        self.assertEqual(expected_out, out)
        # self.assertSequenceEqual(expected_debug, debug)

    def test_HERDAN_TTR(self):
        metric = "HERDAN_TTR"
        test_text = """Text in the present passive is written when the subject of the sentence isn't the doer of the action, but the receiver. For example, "The cake is baked by John" is a present passive sentence, because the cake is not baking itself, but John is baking it.
To form the present passive, we use the verb to be in the present tense and the past participle of the main verb."""

        expected_debug = {}
        expected_out = 1.0

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = []

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_MASS_TTR(self):
        metric = "MASS_TTR"
        test_text = """Text in the present passive is written when the subject of the sentence isn't the doer of the action, but the receiver. For example, "The cake is baked by John" is a present passive sentence, because the cake is not baking itself, but John is baking it.
To form the present passive, we use the verb to be in the present tense and the past participle of the main verb."""

        expected_debug = {}
        expected_out = 0.0

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = {}

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_MENTION(self):
        metric = "L_MENTION"
        test_text = "@USER @USER @USER @USER @USER Any argument with liberals is same as forcing water through the steel."

        expected_debug = ["@USER", "@USER", "@USER", "@USER", "@USER"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_HASHTAG(self):
        metric = "L_HASHTAG"
        test_text = "#travel #winter #vibes http://example.org/#comments I love #stackoverflow because #people are very #helpful!"

        expected_debug = [
            "#travel",
            "#winter",
            "#vibes",
            "#comments",
            "#stackoverflow",
            "#people",
            "#helpful",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_RT(self):
        metric = "L_RT"
        test_text = "!!! RT @mayasolovely: As a woman you shouldn't complain about cleaning up your house."

        expected_debug = ["RT"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_LINKS(self):
        metric = "L_LINKS"
        test_text = "http://example.org/#comments I love #stackoverflow because #people are very #helpful!"

        expected_debug = ["http://example.org/#comments"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_CONT_A(self):
        metric = "L_CONT_A"
        test_text = (
            test_text
        ) = "Text in the present passive is written when the subject of the sentence isn't the doer of the action, but the receiver. For example, The cake is baked by John is a present passive sentence, because the cake is not baking itself, but John is baking it."

        expected_debug = [
            "Text",
            "present",
            "passive",
            "written",
            "subject",
            "sentence",
            "doer",
            "action",
            "receiver",
            "example",
            "cake",
            "baked",
            "John",
            "present",
            "passive",
            "sentence",
            "cake",
            "baking",
            "John",
            "baking",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_FUNC_A(self):
        metric = "L_FUNC_A"
        test_text = "Text in the present passive is written when the subject of the sentence isn't the doer of the action, but the receiver. For example, The cake is baked by John is a present passive sentence, because the cake is not baking itself, but John is baking it."

        expected_debug = [
            "in",
            "the",
            "is",
            "when",
            "the",
            "of",
            "the",
            "is",
            "n't",
            "the",
            "of",
            "the",
            "but",
            "the",
            "For",
            "The",
            "is",
            "by",
            "is",
            "a",
            "because",
            "the",
            "is",
            "not",
            "itself",
            "but",
            "is",
            "it",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_CONT_T(self):
        metric = "L_CONT_T"
        test_text = "Text in the present passive is written when the subject of the sentence isn't the doer of the action, but the receiver. For example, The cake is baked by John is a present passive sentence, because the cake is not baking itself, but John is baking it."

        expected_debug = [
            "Text",
            "present",
            "subject",
            "sentence",
            "passive",
            "example",
            "action",
            "receiver",
            "doer",
            "cake",
            "written",
            "baked",
            "baking",
            "John",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = {}

        self.assertEqual(expected_out, out)
        # self.assertSequenceEqual(expected_debug, debug)

    def test_L_FUNC_T(self):
        metric = "L_FUNC_T"
        test_text = "Text in the present passive is written when the subject of the sentence isn't the doer of the action, but the receiver. For example, The cake is baked by John is a present passive sentence, because the cake is not baking itself, but John is baking it."

        expected_debug = [
            "but",
            "The",
            "by",
            "because",
            "the",
            "of",
            "n't",
            "a",
            "not",
            "is",
            "in",
            "itself",
            "it",
            "For",
            "when",
        ]

        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = {}

        self.assertEqual(expected_out, out)
        # self.assertSequenceEqual(expected_debug, debug)

    def test_L_PLURAL_NOUNS(self):
        metric = "L_PLURAL_NOUNS"
        test_text = "They have many children. Play with mice and throw dice. How many people are there?"

        expected_debug = ["children", "mice", "dice", "people"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_SINGULAR_NOUNS(self):
        metric = "L_SINGULAR_NOUNS"
        test_text = "She was a beautiful girl. My friend is a doctor. A brother and a sister were playing in the garden."

        expected_debug = ["girl", "friend", "doctor", "brother", "sister", "garden"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_PROPER_NAME(self):
        metric = "L_PROPER_NAME"
        test_text = "Lisa was an amasing singer. The Eifel Tower is in Paris. I love the Beatles."

        expected_debug = ["Lisa", "Eifel", "Tower", "Paris", "Beatles"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_PERSONAL_NAME(self):
        metric = "L_PERSONAL_NAME"
        test_text = "Mary was never to be seen. Thomas found his way home. I loved watching small Lidia playing in the garden."

        expected_debug = ["Mary", "Thomas", "Lidia"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_NOUN_PHRASES(self):
        metric = "L_NOUN_PHRASES"
        test_text = "Mary was never to be seen. Thomas found his way home. I loved watching small Lidia playing in the garden."

        expected_debug = [
            "Mary",
            "Thomas",
            "his",
            "way",
            "I",
            "small",
            "Lidia",
            "the",
            "garden",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_PUNCT(self):
        metric = "L_PUNCT"
        test_text = "Mary was never to be seen. Thomas found his way home. I loved watching small Lidia playing in the garden."

        expected_debug = [".", ".", "."]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_PUNCT_DOT(self):
        metric = "L_PUNCT_DOT"
        test_text = "Mary was never to be seen. Thomas found his way home. I loved watching small Lidia playing in the garden."

        expected_debug = [".", ".", "."]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_PUNCT_COM(self):
        metric = "L_PUNCT_COM"
        test_text = "He was listening attentively, and trying not to intervene. They were fearless, cruel, and fanatical."

        expected_debug = [",", ",", ","]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_PUNCT_COL(self):
        metric = "L_PUNCT_COL"
        test_text = "Remember to get: milk, bread, and cheese. There are a few things to consider: cost, size, and color."

        expected_debug = [":", ":"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_PUNCT_SEMC(self):
        metric = "L_PUNCT_SEMC"
        test_text = "Don't forget to smile; people love happy faces. I love to eat; I eat all the time."

        expected_debug = [";", ";"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_PUNCT_DASH(self):
        metric = "L_PUNCT_DASH"
        test_text = "That was the best — and last — time I ever saw him. It was the beginning of a new era — for him, and for me."

        expected_debug = ["—", "—", "—"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_POSSESSIVES(self):
        metric = "L_POSSESSIVES"
        test_text = "Mary's home was not far from here. Thomas's car was parked outside. I saw them playing wy children's toys."

        expected_debug = ["'s", "'s", "'s"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_ADJ_POSITIVE(self):
        metric = "L_ADJ_POSITIVE"
        test_text = "Yesterday we watched an interesting movie. Her stories were brilliant. I love my new car."

        expected_debug = ["interesting", "brilliant", "new"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_ADJ_COMPARATIVE(self):
        metric = "L_ADJ_COMPARATIVE"
        test_text = "She was always better than me. I was more and more tired. The book was more interesting than the movie."

        expected_debug = ["better", "more", "more", "tired", "more", "interesting"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_ADJ_SUPERLATIVE(self):
        metric = "L_ADJ_SUPERLATIVE"
        test_text = "He was the smartest in the class. Our athlets are the best. He saw the most attractive woman in the world."

        expected_debug = ["smartest", "best", "most"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_ADV_POSITIVE(self):
        metric = "L_ADV_POSITIVE"
        test_text = "The play was brilliantly made. I started adjusting slowy. She needed to go home badly."

        expected_debug = ["brilliantly", "slowy", "home", "badly"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_ADV_COMPARATIVE(self):
        metric = "L_ADV_COMPARATIVE"
        test_text = "He arrived later than expected. She sings more beautifully than anyone I know. He spoke more loudly than necessary."

        expected_debug = ["later", "more", "beautifully", "more", "loudly"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_ADV_SUPERLATIVE(self):
        metric = "L_ADV_SUPERLATIVE"
        test_text = "They arrived the latest of all the guests. He plays the piano most beautifully in the class."

        expected_debug = ["latest", "most", "beautifully"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_PS_CONTRADICTION(self):
        metric = "PS_CONTRADICTION"
        test_text = "Although, she looked gorgeous, something was odd in her look. Otherwise, I would not be here."

        expected_debug = ["Although", "Otherwise"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_PS_AGREEMENT(self):
        metric = "PS_AGREEMENT"
        test_text = "She loves not only me, but also my dog. Additionaly, she was always right. Furthermore, she was always right."

        expected_debug = ["not", "but", "also", "Furthermore"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_PS_EXAMPLES(self):
        metric = "PS_EXAMPLES"
        test_text = "To put it differently, I never liked you. For instance, the world is round. Surprisingly, he was right."

        expected_debug = ["put", "it", "differently", "instance", "is", "Surprisingly"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_PS_CONSEQUENCE(self):
        metric = "PS_CONSEQUENCE"
        test_text = "They didn't want to talk to her because she was introvert. Therefore, they didn't want to talk to her."

        expected_debug = ["because", "Therefore"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_PS_CAUSE(self):
        metric = "PS_CAUSE"
        test_text = "Whenever you go, I'll follow you. Due to hash weather, we decided to stay at home."

        expected_debug = [
            "Whenever",
            "Due",
            "to",
            "to",
            "to",
            "to",
            "to",
            "to",
            "to",
            "to",
            "to",
            "to",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_PS_LOCATION(self):
        metric = "PS_LOCATION"
        test_text = (
            "In the middle was a large box. We saw the dog where he was standing"
        )

        expected_debug = ["middle", "where"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_PS_TIME(self):
        metric = "PS_TIME"
        test_text = (
            "Occasionally, I meet her at the office. As soon as you get there, call me."
        )

        expected_debug = ["Occasionally", "at", "the", "soon"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_PS_CONDITION(self):
        metric = "PS_CONDITION"
        test_text = "Assuming that she's not here, we start the meeting."

        expected_debug = ["Assuming", "that"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_PS_MANNER(self):
        metric = "PS_MANNER"
        test_text = "How could you even think about that? As if I didn't know."

        expected_debug = ["How", "As"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)


if __name__ == "__main__":
    unittest.main()
