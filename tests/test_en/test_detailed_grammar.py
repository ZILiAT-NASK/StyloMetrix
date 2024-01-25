import unittest

from src.stylo_metrix.stylo_metrix import StyloMetrix


class TestDetailedGrammarEN(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        lang = "en"
        cls.sm = StyloMetrix(lang, debug=True)

    def test_VT_PRESENT_SIMPLE(self):
        metric = "VT_PRESENT_SIMPLE"
        test_text = "She loves vacation. They don't know where to go. He reads and cooks every day. Do you like my new dress? What do you attend in the evenings?"
        expected_debug = [
            "loves",
            "do",
            "know",
            "reads",
            "cooks",
            "Do",
            "like",
            "do",
            "attend",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_PRESENT_PROGRESSIVE(self):
        metric = "VT_PRESENT_PROGRESSIVE"
        test_text = "Is she doing her homework. When are you going to leave? What are you doing? I am not going to the party. She's not coming to the party."
        expected_debug = [
            "Is",
            "doing",
            "are",
            "going",
            "are",
            "doing",
            "am",
            "going",
            "'s",
            "coming",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_PRESENT_PERFECT(self):
        metric = "VT_PRESENT_PERFECT"
        test_text = (
            "What have you done? Has she been there? I've never been to the USA."
        )
        expected_debug = ["have", "done", "Has", "been", "'ve", "been"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_PRESENT_PERFECT_PROGR(self):
        metric = "VT_PRESENT_PERFECT_PROGR"
        test_text = "They have been doing great so far. Has she been staying there for a while? I've been listening this for ages. What have you been doing?"
        expected_debug = [
            "have",
            "been",
            "doing",
            "Has",
            "been",
            "staying",
            "'ve",
            "been",
            "listening",
            "have",
            "been",
            "doing",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_PRESENT_SIMPLE_PASSIVE(self):
        metric = "VT_PRESENT_SIMPLE_PASSIVE"
        test_text = "The project is completed. It's not done yet."
        expected_debug = ["is", "completed", "'s", "done"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_PRESENT_PROGR_PASSIVE(self):
        metric = "VT_PRESENT_PROGR_PASSIVE"
        test_text = "The house is being built. The flowers are being watered by the gardener. The documents are being scanned and delivered."
        expected_debug = [
            "is",
            "being",
            "built",
            "are",
            "being",
            "watered",
            "are",
            "being",
            "scanned",
            "delivered",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_PRESENT_PERFECT_PASSIVE(self):
        metric = "VT_PRESENT_PERFECT_PASSIVE"
        test_text = "The cake has been baked by my sister. The window has been broken by the storm. The book has been read by many people."
        expected_debug = [
            "has",
            "been",
            "baked",
            "has",
            "been",
            "broken",
            "has",
            "been",
            "read",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_PAST_SIMPLE(self):
        metric = "VT_PAST_SIMPLE"
        test_text = "She did that on purpose. We got your back. Did you see her? Was she there? I didn't know that."
        expected_debug = ["did", "got", "Did", "see", "did", "know"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_PAST_SIMPLE_BE(self):
        metric = "VT_PAST_SIMPLE_BE"
        test_text = "She did that on purpose. That wasn't here before. Were they happy? They weren't sure. Where were you?"
        expected_debug = ["was", "Were", "were", "were"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_PAST_PROGR(self):
        metric = "VT_PAST_PROGR"
        test_text = "Were they going to the cinema yestreday. She was backing a cake and singing before you came. What were you doing yesterday? I wasn't going to the party."
        expected_debug = [
            "Were",
            "going",
            "was",
            "backing",
            "singing",
            "were",
            "doing",
            "was",
            "going",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_PAST_PERFECT(self):
        metric = "VT_PAST_PERFECT"
        test_text = "Had you attended that event before you got to know her? I had never visited to the USA before. Before I knew it, he'd already finished the entire project. "
        expected_debug = ["Had", "attended", "had", "visited", "'d", "finished"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_PAST_PERFECT_PROGRT(self):
        metric = "VT_PAST_PERFECT_PROGR"
        test_text = "She had been working for hours when you called her. They had been waiting for you for ages. I'd been listening to this song for a while."
        expected_debug = [
            "had",
            "been",
            "working",
            "had",
            "been",
            "waiting",
            "'d",
            "been",
            "listening",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_PAST_SIMPLE_PASSIVET(self):
        metric = "VT_PAST_SIMPLE_PASSIVE"
        test_text = "They were invited to the party. The house was built in 1990. The book was read and advised by many people."
        expected_debug = ["were", "invited", "was", "built", "was", "read", "advised"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_PAST_POGR_PASSIVE(self):
        metric = "VT_PAST_POGR_PASSIVE"
        test_text = "The house was being built. The flowers were being watered by the gardener. The documents were being scanned and delivered."
        expected_debug = [
            "was",
            "being",
            "built",
            "were",
            "being",
            "watered",
            "were",
            "being",
            "scanned",
            "delivered",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_PAST_PERFECT_PASSIVE(self):
        metric = "VT_PAST_PERFECT_PASSIVE"
        test_text = "The cake had been baked by my sister. The window had been broken by the storm. The book had been read by many people."
        expected_debug = [
            "had",
            "been",
            "baked",
            "had",
            "been",
            "broken",
            "had",
            "been",
            "read",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_FUTURE_SIMPLE(self):
        metric = "VT_FUTURE_SIMPLE"
        test_text = "Will you come to the lesson today? She will be home late. I'll call you later."
        expected_debug = ["Will", "come", "will", "be", "'ll", "call"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_FUTURE_PROGRESSIVE(self):
        metric = "VT_FUTURE_PROGRESSIVE"
        test_text = "Will you be calling her later? She'll be waiting for you at the station. Will you be okay?"
        expected_debug = ["Will", "be", "calling", "'ll", "be", "waiting"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_FUTURE_PERFECT(self):
        metric = "VT_FUTURE_PERFECT"
        test_text = "We will have reached our destination before sunset. They will have learned a lot from this experience. She will have left by the time you arrive."
        expected_debug = [
            "will",
            "have",
            "reached",
            "will",
            "have",
            "learned",
            "will",
            "have",
            "left",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_FUTURE_PERFECT_PROGR(self):
        metric = "VT_FUTURE_PERFECT_PROGR"
        test_text = "By next year, she will have been working at this company for 10 years. They will have been traveling around the world for six months by the time they come back home."
        expected_debug = [
            "will",
            "have",
            "been",
            "working",
            "will",
            "have",
            "been",
            "traveling",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_FUTURE_SIMPLE_PASSIVE(self):
        metric = "VT_FUTURE_SIMPLE_PASSIVE"
        test_text = "The house will be built till next year. The book will be read by many people. Will you be invited to the party?"
        expected_debug = [
            "will",
            "be",
            "built",
            "will",
            "be",
            "read",
            "Will",
            "be",
            "invited",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_FUTURE_PROGR_PASSIVE(self):
        metric = "VT_FUTURE_PROGR_PASSIVE"
        test_text = "The car will be being repaired by the mechanic at noon. The cake will be being baked and eaten by my sister tomorrow."
        expected_debug = [
            "will",
            "be",
            "being",
            "repaired",
            "will",
            "be",
            "being",
            "baked",
            "eaten",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_FUTURE_PERFECT_PASSIVE(self):
        metric = "VT_FUTURE_PERFECT_PASSIVE"
        test_text = "The report will have been written by him by tomorrow morning. The cake will have been baked by her before the guests arrive."
        expected_debug = [
            "will",
            "have",
            "been",
            "written",
            "will",
            "have",
            "been",
            "baked",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_WOULD(self):
        metric = "VT_WOULD"
        test_text = "I'd like to ask you a question. Would you like to go to the cinema? Would you like to have a cup of tea? We'd like to thank you for your help."
        expected_debug = ["'d", "like", "Would", "like", "Would", "like", "'d", "like"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_WOULD_PASSIVE(self):
        metric = "VT_WOULD_PASSIVE"
        test_text = "The painting would be sold for a lot of money. The house would be built by the end of the year. The book would be read by many people."
        expected_debug = ["be", "sold", "be", "built", "be", "read"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_WOULD_PROGRESSIVEE(self):
        metric = "VT_WOULD_PROGRESSIVE"
        test_text = "She'd be watching TV now. I'd be working if I were you. I'd be waiting for you at the station."
        expected_debug = [
            "'d",
            "be",
            "watching",
            "'d",
            "be",
            "working",
            "'d",
            "be",
            "waiting",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_WOULD_PERFECT(self):
        metric = "VT_WOULD_PERFECT"
        test_text = "She would have done that earlier if he hadn't stopped her. I would have visited you if I had had time. They would have been happy if they had won the competition."
        expected_debug = ["have", "done", "have", "visited", "had", "have", "been"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_WOULD_PERFECT_PASSIVE(self):
        metric = "VT_WOULD_PERFECT_PASSIVE"
        test_text = "We would have been disappointed if you had not come to our party. They would have been arrested if they had tried to escape."
        expected_debug = ["would", "been", "disappointed", "would", "been", "arrested"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_SHOULD(self):
        metric = "VT_SHOULD"
        test_text = "Should I go first? You should go to the doctor. You should be more careful."
        expected_debug = ["Should", "go", "should", "go", "should", "be"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_SHOULD_PASSIVE(self):
        metric = "VT_SHOULD_PASSIVE"
        test_text = "The project should be completed by the end of the month. The house should be built by the end of the year."
        expected_debug = ["should", "be", "completed", "should", "be", "built"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_SHALL(self):
        metric = "VT_SHALL"
        test_text = "I shall see what to do next. Shall we go to the cinema?"
        expected_debug = ["shall", "see", "Shall", "go"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_SHALL_PASSIVE(self):
        metric = "VT_SHALL_PASSIVE"
        test_text = "The project shall be completed by the end of the month. The house shall be built by the end of the year."
        expected_debug = ["shall", "be", "completed", "shall", "be", "built"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_SHOULD_PROGRESSIVE(self):
        metric = "VT_SHOULD_PROGRESSIVE"
        test_text = "She should be watching TV now. I should be working if I were you."
        expected_debug = ["should", "be", "watching", "should", "be", "working"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_SHOULD_PERFECT(self):
        metric = "VT_SHOULD_PERFECT"
        test_text = "I should have done that earlier. They should have been happy if they had won the competition."
        expected_debug = ["should", "have", "done", "should", "have", "been"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_SHOULD_PERFECT_PASSIVE(self):
        metric = "VT_SHOULD_PERFECT_PASSIVE"
        test_text = "We should have been disappointed if you had not come to our party. They should have been arrested if they had tried to escape."
        expected_debug = [
            "should",
            "been",
            "disappointed",
            "should",
            "been",
            "arrested",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_MUST(self):
        metric = "VT_MUST"
        test_text = "She must be at home now. You must be more careful."
        expected_debug = ["must", "be", "must", "be"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_MUST_PASSIVE(self):
        metric = "VT_MUST_PASSIVE"
        test_text = "The project must be completed by the end of the month. The house must be built by the end of the year."
        expected_debug = ["completed", "must", "be", "built", "must", "be"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_MUST_PROGRESSIVE(self):
        metric = "VT_MUST_PROGRESSIVE"
        test_text = "She must be watching TV now. I must be working if I were you."
        expected_debug = ["must", "be", "watching", "must", "be", "working"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_MUST_PERFECT(self):
        metric = "VT_MUST_PERFECT"
        test_text = "I must have done that earlier. They must have been happy if they had won the competition."
        expected_debug = ["must", "have", "done", "must", "have", "been"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_MST_PERFECT_PASSIVE(self):
        metric = "VT_MST_PERFECT_PASSIVE"
        test_text = "The operation must have been completed a few hours ago. They must have been arrested if they had tried to escape."
        expected_debug = [
            "must",
            "have",
            "been",
            "completed",
            "must",
            "have",
            "been",
            "arrested",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_MST_PERFECT_PASSIVE(self):
        metric = "VT_MST_PERFECT_PASSIVE"
        test_text = "The operation must have been completed a few hours ago. They must have been arrested if they had tried to escape."
        expected_debug = [
            "must",
            "have",
            "been",
            "completed",
            "must",
            "have",
            "been",
            "arrested",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_CAN(self):
        metric = "VT_CAN"
        test_text = "Can you help me? Can I ask you a question? You can't do that."
        expected_debug = ["Can", "help", "Can", "ask", "ca", "do"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_CAN_PASSIVE(self):
        metric = "VT_CAN_PASSIVE"
        test_text = "The project can be completed by the end of the month. The house can be built by the end of the year."
        expected_debug = ["can", "be", "completed", "can", "be", "built"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_COULD(self):
        metric = "VT_COULD"
        test_text = (
            "Could you help me? Could I ask you a question? You couldn't do that."
        )
        expected_debug = ["Could", "help", "Could", "ask", "could", "do"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_COULD_PASSIVE(self):
        metric = "VT_COULD_PASSIVE"
        test_text = "The project could be completed by the end of the month. The house could be built by the end of the year."
        expected_debug = ["could", "be", "completed", "could", "be", "built"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_CAN_PROGRESSIVE(self):
        metric = "VT_CAN_PROGRESSIVE"
        test_text = "She can be watching TV now. I can be working if I were you."
        expected_debug = ["can", "be", "watching", "can", "be", "working"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_COULD_PROGRESSIVE(self):
        metric = "VT_COULD_PROGRESSIVE"
        test_text = "She could be watching TV now. I could be working if I were you."
        expected_debug = ["could", "be", "watching", "could", "be", "working"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_COULD_PERFECT(self):
        metric = "VT_COULD_PERFECT"
        test_text = "I could have done that earlier. They could have been happy if they had won the competition."
        expected_debug = ["could", "have", "done", "could", "have", "been"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_COULD_PERFECT_PASSIVE(self):
        metric = "VT_COULD_PERFECT_PASSIVE"
        test_text = "We could have been disappointed if you had not come to our party. They could have been arrested if they had tried to escape."
        expected_debug = [
            "could",
            "have",
            "been",
            "disappointed",
            "could",
            "have",
            "been",
            "arrested",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_MAY(self):
        metric = "VT_MAY"
        test_text = "May I ask you a question? You may not do that."
        expected_debug = ["May", "ask", "may", "do"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_MAY_PASSIVE(self):
        metric = "VT_MAY_PASSIVE"
        test_text = "The project may be completed by the end of the month. The house may be built by the end of the year."
        expected_debug = ["may", "be", "completed", "may", "be", "built"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_MIGHT(self):
        metric = "VT_MIGHT"
        test_text = "I might join you later. You might not do that."
        expected_debug = ["might", "join", "might", "do"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_MIGHT_PASSIVE(self):
        metric = "VT_MIGHT_PASSIVE"
        test_text = "The project might be completed by the end of the month. The house might be built by the end of the year."
        expected_debug = ["might", "be", "completed", "might", "be", "built"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_MAY_PROGRESSIVE(self):
        metric = "VT_MAY_PROGRESSIVE"
        test_text = "She may be watching TV now. I may be working if I were you."
        expected_debug = ["may", "be", "watching", "may", "be", "working"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_MIGTH_PERFECT(self):
        metric = "VT_MIGTH_PERFECT"
        test_text = "I might have done that earlier. They might have been happy if they had won the competition."
        expected_debug = ["might", "have", "done", "might", "have", "been"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_MIGHT_PERFECT_PASSIVE(self):
        metric = "VT_MIGHT_PERFECT_PASSIVE"
        test_text = "We might have been disappointed if you had not come to our party. They might have been arrested if they had tried to escape"
        expected_debug = [
            "might",
            "have",
            "been",
            "disappointed",
            "might",
            "have",
            "been",
            "arrested",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_VT_MAY_PERFECT_PASSIVE(self):
        metric = "VT_MAY_PERFECT_PASSIVE"
        test_text = "The project may have been completed by the end of the month. The house may have been built by the end of the year."
        expected_debug = [
            "may",
            "have",
            "been",
            "completed",
            "may",
            "have",
            "been",
            "built",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)


if __name__ == "__main__":
    unittest.main()
