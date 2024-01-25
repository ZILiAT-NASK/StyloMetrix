import unittest

from src.stylo_metrix.stylo_metrix import StyloMetrix

TEXT_TEST = """Text in the present passive is written when the subject of the sentence isn't the doer of the action, but the receiver. For example, "The cake is baked by John" is a present passive sentence, because the cake is not baking itself, but John is baking it.
To form the present passive, we use the verb to be in the present tense and the past participle of the main verb. 
For example, "The book is bought and read by many people" is another present passive sentence, because the book is not reading itself, but many people are reading it.
I've just finished writing a short story for my creative writing class. It's about a girl who discovers a secret portal in her basement. I have always loved fantasy stories, so I decided to try my hand at one.
I hope my teacher and classmates will like it. As soon as she's done with her work, she'll head home. Have you figured out the way to solve this riddle? This work has been done already.
I have never shared or recited my writing to anyone before, so I'm a bit nervous. The house is being painted by the workers. The cake is being baked by my sister.
The window has been fixed. His arm has been broken by a fall. The dishes have been washed by my sister. Yesterday I wrote a letter to my friend. I had been meaning to do it for a long time, but I always procrastinated.
I told him about what I did last weekend, when I went to the beach with my family. We had a lot of fun there, swimming, playing volleyball and building sandcastles.
We also saw some dolphins jumping in the water. It was amazing! I asked him how he was doing and what he had planned for the summer. The house that he built was furnished amazingly weel.
I told him that I was going to visit him soon. I hoped he would write back soon. I missed him a lot.
Did you go for a ride? Was she a good daughter. They didn't do particularly well on the exams. I didn't go and meet with him that day.
He was being chased and bitten by a dog when he fell down. Were they being interviewed by a reporter when the fire alarm rang.
I had never seen such a beautiful sunset before I visited Hawaii. Does she come home every day? Do I care about what you think? I don't know what to do.
I had been aiming to visit Hawaii for a long time, but I never had the chance. She has finished her task. The task was really difficult.
They’d never met each other before they started working together. Had he already finished his homework and cleaned when his mother came home? 
She was happy because her novel had been published by a famous company. He felt guilty because he'd been caught cheating on the exam.
We’d been waiting for you since 10 o'clock and talking about weather, but you didn't show up.
She hadn't been dreaming of becoming a doctor ever since she was a child. Had he been trying to call her for days, but she never answered.
She'll go to the cinema tomorrow and meet Alex there. I’ll be waiting for you at the station.
They’ll come as soon as they finish their work. We won't be able to go to the party. Will you be okay?
The tickets will be sold online and distributed at the tickets offices. She'll be finished with the task by tomorrow. We'll be going to the party and staying there till the dawn.
She will be being interviewed by the manager at 10 a.m. tomorrow. They will be being taught by a native speaker in the next semester. 
The new bridge will be being built next year. By next week, I will have finished my project. They will have moved to a new house by the end of the year.
We will have seen all the movies by tomorrow night. I will have been working here for 10 years by the end of next year.
The cake will have been cooked and eaten by the time you come home. I've spent a lot of time on it, editing and revising until I was satisfied.
He has been working on his project since Monday. She has been studying for the exam all week.
"""


class TestTextStatEN(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        lang = "en"
        cls.sm = StyloMetrix(lang, debug=True)

    def test_SENT_ST_WRDSPERSENT(self):
        metric = "SENT_ST_WRDSPERSENT"
        test_text = TEXT_TEST
        expected_debug = {}
        expected_out = 0.9080590238365494

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SENT_ST_DIFFERENCE(self):
        metric = "SENT_ST_DIFFERENCE"
        test_text = TEXT_TEST
        expected_debug = {}
        expected_out = 0.10767160161507403

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_ST_REPETITIONS_WORDS(self):
        metric = "ST_REPETITIONS_WORDS"
        test_text = TEXT_TEST
        expected_debug = {}
        expected_out = 0.7200538358008075

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_ST_REPETITIONS_SENT(self):
        metric = "ST_REPETITIONS_SENT"
        test_text = TEXT_TEST
        expected_debug = {}
        expected_out = 0.0

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SENT_D_VP(self):
        metric = "SENT_D_VP"
        test_text = TEXT_TEST
        expected_debug = {}
        expected_out = 0.7935655751359041

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SENT_D_NP(self):
        metric = "SENT_D_NP"
        test_text = TEXT_TEST
        expected_debug = {}
        expected_out = 0.3172088049810066

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SENT_D_PP(self):
        metric = "SENT_D_PP"
        test_text = TEXT_TEST
        expected_debug = {}
        expected_out = 0.16747947517445322

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SENT_D_ADJP(self):
        metric = "SENT_D_ADJP"
        test_text = TEXT_TEST
        expected_debug = {}
        expected_out = 0.0  # TODO: Find example where expected_out > 0.0

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SENT_D_ADVP(self):
        metric = "SENT_D_ADVP"
        test_text = TEXT_TEST
        expected_debug = {}
        expected_out = 0.04839827359652514

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)


if __name__ == "__main__":
    unittest.main()
