import unittest

from src.stylo_metrix.stylo_metrix import StyloMetrix

TEXT_TEST = """Про засилля вульгарного гумору про дебілізацію за посередництва багатьох програм
З урахуванням вкрай напруженої ситуації у фінансовому секторі нашої країни неотримання кредиту МВФ може мати вельми негативні наслідки
Однією з ймовірних причин нападу на співробітника МВС є його професійна діяльність зазначили в ДЗГ МВС
А метроритмічна організація музики передбачала велику свободу темпових відхилень
Наука вже давно встановила що курець скорочує своє життя на 10 років а той хто регулярно випиває я думаю скорочує своє життя значно більше
Адміністративно ця територія до 1471 року входила у склад Київського князівства згодом Київського воєводства Литовсько-Польської держави з 1782 року київського намісництва
**Віктор Гіржов головний редактор інформаційно-аналітичного порталу ОУР і журналу Український огляд співголова РГО Українці Москви
"""


class TestGrammarUKR(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        lang = "ukr"
        cls.sm = StyloMetrix(lang, debug=True)

    def test_G_ROOT_VERB_IMPERFECT(self):
        metric = "G_ROOT_VERB_IMPERFECT"
        test_text = TEXT_TEST
        expected_debug = ["може", "передбачала", "входила"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_ALL_VERB_IMPERFECT(self):
        metric = "G_ALL_VERB_IMPERFECT"
        test_text = TEXT_TEST
        expected_debug = [
            "може",
            "мати",
            "передбачала",
            "скорочує",
            "випиває",
            "думаю",
            "скорочує",
            "входила",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_ROOT_VERB_PERFECT(self):
        metric = "G_ROOT_VERB_PERFECT"
        test_text = TEXT_TEST
        expected_debug = ["зазначили", "встановила"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_ALL_VERB_PERFECT(self):
        metric = "G_ALL_VERB_PERFECT"
        test_text = TEXT_TEST
        expected_debug = ["зазначили", "встановила"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_PRESENT_IND_IMPERFECT(self):
        metric = "G_PRESENT_IND_IMPERFECT"
        test_text = TEXT_TEST
        expected_debug = ["може", "є", "скорочує", "випиває", "думаю", "скорочує"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_PAST_IND_IMPERFECT(self):
        metric = "G_PAST_IND_IMPERFECT"
        test_text = TEXT_TEST
        expected_debug = ["передбачала", "входила"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_PAST_IND_PERFECT(self):
        metric = "G_PAST_IND_PERFECT"
        test_text = TEXT_TEST
        expected_debug = ["зазначили", "встановила"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_FUT_IND_PERFECT(self):
        metric = "G_FUT_IND_PERFECT"
        test_text = "Завтра я піду на прогулянку. Мій чоловік придбає для мене цю каблучку. Я напушу листа."
        expected_debug = ["піду", "придбає", "напушу"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_FUT_IND_IMPERFECT_SIMPLE(self):
        metric = "G_FUT_IND_IMPERFECT_SIMPLE"
        test_text = "Я не буду працювати завтра. Ви працюватимете завтра. Проект буде представлений наступного вівторка. Завдання буде зроблено. Але, добре подумавши, він вирішив, що на волі зайчику буде краще, хоч і небезпечно."
        expected_debug = ["працюватимете"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_FUT_IND_COMPLEX(self):
        metric = "G_FUT_IND_COMPLEX"
        test_text = "Я не буду працювати завтра. Ви працюватимете завтра. Проект буде представлений наступного вівторка. Завдання буде зроблено. Але, добре подумавши, він вирішив, що на волі зайчику буде краще, хоч і небезпечно."
        expected_debug = [
            "буду",
            "буде",
            "буде",
            "буде",
            "працювати",
            "представлений",
            "зроблено",
            "краще",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_FIRST_CONJ(self):
        metric = "G_FIRST_CONJ"
        test_text = TEXT_TEST
        expected_debug = [
            "дебілізацію",
            "програм",
            "ситуації",
            "країни",
            "причин",
            "організація",
            "музики",
            "свободу",
            "Наука",
            "територія",
            "держави",
            "співголова",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_SECOND_CONJ(self):
        metric = "G_SECOND_CONJ"
        test_text = TEXT_TEST
        expected_debug = [
            "засилля",
            "гумору",
            "урахуванням",
            "секторі",
            "неотримання",
            "кредиту",
            "наслідки",
            "нападу",
            "співробітника",
            "МВС",
            "ДЗГ",
            "МВС",
            "відхилень",
            "курець",
            "життя",
            "років",
            "життя",
            "року",
            "склад",
            "князівства",
            "воєводства",
            "року",
            "намісництва",
            "редактор",
            "порталу",
            "журналу",
            "огляд",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_THIRD_CONJ(self):
        metric = "G_THIRD_CONJ"
        test_text = TEXT_TEST
        expected_debug = ["мати", "діяльність"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_FOURTH_CONJ(self):
        metric = "G_FOURTH_CONJ"
        test_text = TEXT_TEST
        expected_debug = ["відхилень"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_INFINITIVE(self):
        metric = "G_INFINITIVE"
        test_text = TEXT_TEST
        expected_debug = ["мати"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_PASSIVE(self):
        metric = "G_PASSIVE"
        test_text = "Товар виготовлено з натуральних інгредієнтів."
        expected_debug = ["виготовлено"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_TRANSITIVE(self):
        metric = "G_TRANSITIVE"
        test_text = TEXT_TEST
        expected_debug = [
            "може",
            "зазначили",
            "передбачала",
            "встановила",
            "скорочує",
            "випиває",
            "думаю",
            "скорочує",
            "входила",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_INTRANSITIVE(self):
        metric = "G_INTRANSITIVE"
        test_text = (
            "Вже веснянки заспівали. Із стріх закрапало, а з гір струмочки покотилися."
        )
        expected_debug = []  # TODO: poprawić ten test, żeby coś zwracało
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_IMPERSONAL_VERBS(self):
        metric = "G_IMPERSONAL_VERBS"
        test_text = TEXT_TEST
        expected_debug = ["може", "скорочує", "скорочує", "входила"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_PARTICIPLE_PASSIVE(self):
        metric = "G_PARTICIPLE_PASSIVE"
        test_text = TEXT_TEST
        expected_debug = ["напруженої"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_PARTICIPLE_ACTIVE(self):
        metric = "G_PARTICIPLE_ACTIVE"
        test_text = "За існуючими переказами, народна поетеса народилася у 1625 р. у Полтаві, в козацькій родині."
        expected_debug = ["існуючими"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_ADV_PRF_PART(self):
        metric = "G_ADV_PRF_PART"
        test_text = "Проект буде представлений наступного вівторка. Завдання буде зроблено. Але, добре подумавши, він вирішив, що на волі зайчику буде краще, хоч і небезпечно."
        expected_debug = ["подумавши"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_ADV_IMPRF_PART(self):
        metric = "G_ADV_IMPRF_PART"
        test_text = "Працюючи в ночну змину він захворів."
        expected_debug = ["Працюючи"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)


if __name__ == "__main__":
    unittest.main()
