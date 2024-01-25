import unittest

from src.stylo_metrix.stylo_metrix import StyloMetrix


class TestDetailedLexicalEN(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        lang = "en"
        cls.sm = StyloMetrix(lang, debug=True)

    def test_L_I_PRON(self):
        metric = "L_I_PRON"
        test_text = "I've just finished writing a short story for my creative writing class. It's about a girl who discovers a secret portal in her basement. I have always loved fantasy stories, so I decided to try my hand at one."
        expected_debug = ["I", "my", "I", "I", "my"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_HE_PRON(self):
        metric = "L_HE_PRON"
        test_text = "He was being chased and bitten by a dog when he fell down. I assume, he was a neglected child. His collection is the most elegant one. You gave him too much attention."
        expected_debug = ["He", "he", "he"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_SHE_PRON(self):
        metric = "L_SHE_PRON"
        test_text = "She hadn't been dreaming of becoming a doctor ever since she was a child. Had he been trying to call her for days, but she never answered. She'll go to the cinema tomorrow and meet Alex there."
        expected_debug = ["She", "she", "she", "She"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_IT_PRON(self):
        metric = "L_IT_PRON"
        test_text = "I've spent a lot of time on it, editing and revising until I was satisfied. It will always be with you. It's a great book."
        expected_debug = ["It", "It"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_YOU_PRON(self):
        metric = "L_YOU_PRON"
        test_text = "You should know, I'll stay with you. Your questions are incorrect. You are the best."
        expected_debug = ["You", "You"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_WE_PRON(self):
        metric = "L_WE_PRON"
        test_text = "We could be the heroes. Our room is occupied. You need to agree, we did that together."
        expected_debug = ["We", "we"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_THEY_PRON(self):
        metric = "L_THEY_PRON"
        test_text = "They’d never met each other before they started working together. You should tell them the truth. They are the best."
        expected_debug = ["They", "they", "They"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_ME_PRON(self):
        metric = "L_ME_PRON"
        test_text = "I want you to show me this place. You should tell me the truth. Me, myself and I are always together."
        expected_debug = ["me", "me", "Me"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_YOU_OBJ_PRON(self):
        metric = "L_YOU_OBJ_PRON"
        test_text = "I want to come with you. Alice called you yesterday. They invited you to the party."
        expected_debug = ["you", "you", "you"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_HIM_PRON(self):
        metric = "L_HIM_PRON"
        test_text = "I missed him a lot. I asked him how he was doing and what he had planned for the summer."
        expected_debug = ["him", "him"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_HER_OBJECT_PRON(self):
        metric = "L_HER_OBJECT_PRON"
        test_text = "It's about a girl who discovers a secret portal in her basement. Her voice was so beautiful. I missed her a lot. She will come back in a minute."
        expected_debug = ["her"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_IT_OBJECT_PRON(self):
        metric = "L_IT_OBJECT_PRON"
        test_text = "I've spent a lot of time on it, editing and revising until I was satisfied. We'll go for it. I'll do it for you."
        expected_debug = ["it", "it", "it"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_US_PRON(self):
        metric = "L_US_PRON"
        test_text = "You can find us on the website. Don't make us do that for you."
        expected_debug = ["us", "us"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_THEM_PRON(self):
        metric = "L_THEM_PRON"
        test_text = "I missed them a lot. I asked them how they were doing and what they had planned for the summer. I'll do it for them."
        expected_debug = ["them", "them", "them"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_MY_PRON(self):
        metric = "L_MY_PRON"
        test_text = "My name is not that important. My house is not that big. I love my friends."
        expected_debug = ["My", "My", "my"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_YOUR_PRON(self):
        metric = "L_YOUR_PRON"
        test_text = "Your questions are incorrect. Your house is not that big. I love your friends."
        expected_debug = ["Your", "Your", "your"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_HIS_PRON(self):
        metric = "L_HIS_PRON"
        test_text = "His collection is the most elegant one. This book is his. His arm has been broken by a fall."
        expected_debug = ["His", "his", "His"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_HER_PRON(self):
        metric = "L_HER_PRON"
        test_text = "As soon as she's done with her work, she'll head home. Her clothes are dirty. She has finished her task."
        expected_debug = ["her", "Her", "her"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_ITS_PRON(self):
        metric = "L_ITS_PRON"
        test_text = "The company announced its plans to expand its market share. The car had a dent in its door from the accident."
        expected_debug = ["its", "its", "its"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_OUR_PRON(self):
        metric = "L_OUR_PRON"
        test_text = "Our team won the championship yesterday. We should take care of our planet and its resources. This is our favorite restaurant in the city."
        expected_debug = ["Our", "our", "our"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_THEIR_PRON(self):
        metric = "L_THEIR_PRON"
        test_text = "They left their coats in the car. Their house was damaged by the storm. The birds built their nests in the trees."
        expected_debug = ["their", "Their", "their"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_YOURS_PRON(self):
        metric = "L_YOURS_PRON"
        test_text = "Sorry, that was yours. Yours faithfully. Yours sincerely."
        expected_debug = ["yours", "Yours", "Yours"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_THEIRS_PRON(self):
        metric = "L_THEIRS_PRON"
        test_text = " She likes to compare her grades with theirs, but she shouldn't worry so much. This book is mine, and that one is theirs. We have a dog, and so do they. Theirs is a golden retriever, and ours is a labrador."
        expected_debug = ["theirs", "theirs", "Theirs"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_HERS_PRON(self):
        metric = "L_HERS_PRON"
        test_text = "She has a lot of friends, but she is closest to hers. That bike is hers, she bought it yesterday. That coat is not hers, it belongs to someone else."
        expected_debug = ["hers", "hers", "hers"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_OURS_PRON(self):
        metric = "L_OURS_PRON"
        test_text = "They invited us to their party, but we already had plans of ours. The house next to ours is for sale."
        expected_debug = ["ours", "ours"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_MYSELF_PRON(self):
        metric = "L_MYSELF_PRON"
        test_text = "I am proud of myself for achieving my goals and overcoming obstacles. I taught myself how to play the guitar when I was 12 years old."
        expected_debug = ["myself", "myself"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_YOURSELF_PRON(self):
        metric = "L_YOURSELF_PRON"
        test_text = "Don't compare yourself to others, you are unique and valuable. You should be proud of yourself. You should take care of yourself."
        expected_debug = ["yourself", "yourself", "yourself"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_HIMSELF_PRON(self):
        metric = "L_HIMSELF_PRON"
        test_text = "He cut himself while shaving this morning. He bought himself a new car as a reward. He considers himself a good writer."
        expected_debug = ["himself", "himself", "himself"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_HERSELF_PRON(self):
        metric = "L_HERSELF_PRON"
        test_text = "She blamed herself for the mistake she made. She locked herself out of the house by accident."
        expected_debug = ["herself", "herself"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_ITSELF_PRON(self):
        metric = "L_ITSELF_PRON"
        test_text = "The cat licked itself clean after eating its meal. The building itself is not very old, but it has a lot of historical significance."
        expected_debug = ["itself", "itself"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_OURSELVES_PRON(self):
        metric = "L_OURSELVES_PRON"
        test_text = "We made this cake by ourselves. We can't blame anyone but ourselves for missing the bus. We need to take care of ourselves during the pandemic."
        expected_debug = ["ourselves", "ourselves", "ourselves"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_YOURSELVES_PRON(self):
        metric = "L_YOURSELVES_PRON"
        test_text = "Enjoy yourselves at the party, but don't drink too much. How do you motivate yourselves to exercise every day? Please make yourselves comfortable while I prepare some tea and cookies."
        expected_debug = ["yourselves", "yourselves", "yourselves"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_THEMSELVES_PRON(self):
        metric = "L_THEMSELVES_PRON"
        test_text = (
            "They saw themselves in the mirror. Some go crazy then kill themselves."
        )
        expected_debug = ["themselves", "themselves"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_SECOND_PERSON_PRON(self):
        metric = "L_SECOND_PERSON_PRON"
        test_text = "I need you to get me a new paintbrush. My shoes are black and yours are white. You are my best friend. I am impressed that you managed to teach yourself geometry."
        expected_debug = ["you", "yours", "You", "you", "yourself"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_THIRD_PERSON_SING_PRON(self):
        metric = "L_THIRD_PERSON_SING_PRON"
        test_text = "You should respect his opinion, even if you disagree with him. She loves to read books and learn new things. That is my favorite book. I have read it several times."
        expected_debug = ["his", "him", "She", "it"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_THIRD_PERSON_PLURAL_PRON(self):
        metric = "L_THIRD_PERSON_PLURAL_PRON"
        test_text = "They are very proud of their son, who is studying abroad. I have been listening to them since I was a teenager. The chimpanzees built a treehouse by themselves."
        expected_debug = ["They", "their", "them", "themselves"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)


if __name__ == "__main__":
    unittest.main()
