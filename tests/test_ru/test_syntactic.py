import unittest

from src.stylo_metrix.stylo_metrix import StyloMetrix

TEXT_TEST = """Студенты учатся русскому языку каждый день. Студенты учатся. На занятиях студенты изучают русский язык. Зима пришла.
Он делает работу. Кто делает эту работу? Сделай работу! Что? Слушай! Странно, что они отказались нам помочь. Вопрос заключается в том, придет ли он?
Сделает ли он работу в срок? Он делает работу? Кто придет сегодня в гости? Чего ты хочешь? Сколько можно их слушать? Она успеет сделать эту работу, правда?
Они слушали лекцию, не так ли? Ты работаешь или учишься? Она встречала его раньше или только познакомилась? Книга, которая вам нужна, лежит на полке. Слово - серебро, молчание - золото. Поспешишь - людей насмешишь. 
Ты сможешь прийти завтра? Она скоро отправится в путешествие. Что будет через год, никто не предугадает.
Мы согласились на это путешествие по одной причине - погода была замечательная и мы были готовы бежать куда глаза глядели. Познакомившись с ней, женщина не смогла больше сдерживать слез. 
Космос исследуется людьми. Космос исследовался людьми. Космос будет исследоваться людьми. Стены выкрашены в зеленый цвет.
Окрашенная блондинка шагала медленным шагом по городу. Бывший студент снова встретился со своим первым учителем. Машина, производимая в России. Машина, произведённая в России.
Идущий на встречу собака медленно качал хвостом. Сидящая на лавочке девушка казалась призраком. Человек, знающий много тайн, обречен на гибель. Человек, покупающий только свежие овощи. Моя подруга, только что закончившая работу, ушла домой.
Роман в стихах «Евгений Онегин» был написан Пушкиным. Картина была написана художником в 2014. Лекарство было использовано врачами."""


class TestSyntacticRU(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        lang = "ru"
        cls.sm = StyloMetrix(lang, debug=True)

    def test_SY_NARRATIVE(self):
        metric = "SY_NARRATIVE"
        test_text = "Что будет через год, никто не предугадает."
        expected_debug = [
            "Что",
            "будет",
            "через",
            "год",
            "никто",
            "не",
            "предугадает",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_NEGATIVE(self):
        metric = "SY_NEGATIVE"
        test_text = TEXT_TEST
        expected_debug = [
            "Они",
            "слушали",
            "лекцию",
            "не",
            "так",
            "ли",
            "Что",
            "будет",
            "через",
            "год",
            "никто",
            "не",
            "предугадает",
            "\n",
            "Познакомившись",
            "с",
            "ней",
            "женщина",
            "не",
            "смогла",
            "больше",
            "сдерживать",
            "слез",
            "\n",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_PARATAXIS(self):
        metric = "SY_PARATAXIS"
        test_text = TEXT_TEST
        expected_debug = ["Она", "успеет", "сделать", "эту", "работу", "правда", "\n"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_NON_FINITE(self):
        metric = "SY_NON_FINITE"
        test_text = TEXT_TEST
        expected_debug = ["Что", "Слово", "серебро", "молчание", "золото"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_QUOTATIONS(self):
        metric = "SY_QUOTATIONS"
        test_text = "Он делает работу. 'Кто делает эту работу?'"
        expected_debug = [
            "Кто",
            "делает",
            "эту",
            "работу",
            "Кто",
            "делает",
            "эту",
            "работу",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_EXCLAMATION(self):
        metric = "SY_EXCLAMATION"
        test_text = TEXT_TEST
        expected_debug = ["Сделай", "работу", "Слушай"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_QUESTION(self):
        metric = "SY_QUESTION"
        test_text = TEXT_TEST
        expected_debug = [
            "Кто",
            "делает",
            "эту",
            "работу",
            "Что",
            "Сделает",
            "ли",
            "он",
            "работу",
            "в",
            "срок",
            "Он",
            "делает",
            "работу",
            "Кто",
            "придет",
            "сегодня",
            "в",
            "гости",
            "Чего",
            "ты",
            "хочешь",
            "Сколько",
            "можно",
            "их",
            "слушать",
            "Они",
            "слушали",
            "лекцию",
            "не",
            "так",
            "ли",
            "Ты",
            "работаешь",
            "или",
            "учишься",
            "Она",
            "встречала",
            "его",
            "раньше",
            "или",
            "только",
            "познакомилась",
            "Ты",
            "сможешь",
            "прийти",
            "завтра",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_ELLIPSES(self):
        metric = "SY_ELLIPSES"
        test_text = TEXT_TEST
        expected_debug = []
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_POSITIONING(self):
        metric = "SY_POSITIONING"
        test_text = TEXT_TEST
        expected_debug = ["2014. Лекарство"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token.text for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_CONDITIONAL(self):
        metric = "SY_CONDITIONAL"
        test_text = "Если бы я был богат, я бы купил дом на берегу моря."
        expected_debug = ["бы", "богат", "бы", "купил"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_IMPERATIVE(self):
        metric = "SY_IMPERATIVE"
        test_text = TEXT_TEST
        expected_debug = ["Слушай"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_AMPLIFIED_SENT(self):
        metric = "SY_AMPLIFIED_SENT"
        test_text = "Чего ты хочешь?!"
        expected_debug = ["Чего", "ты", "хочешь"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_QUESTION_GENERAL(self):
        metric = "SY_QUESTION_GENERAL"
        test_text = TEXT_TEST
        expected_debug = [
            "Сделает",
            "ли",
            "он",
            "работу",
            "в",
            "срок",
            "Он",
            "делает",
            "работу",
            "Они",
            "слушали",
            "лекцию",
            "не",
            "так",
            "ли",
            "Ты",
            "сможешь",
            "прийти",
            "завтра",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_QUESTION_SPECIAL(self):
        metric = "SY_QUESTION_SPECIAL"
        test_text = TEXT_TEST
        expected_debug = [
            "Кто",
            "делает",
            "эту",
            "работу",
            "Что",
            "Кто",
            "придет",
            "сегодня",
            "в",
            "гости",
            "Чего",
            "ты",
            "хочешь",
            "Сколько",
            "можно",
            "их",
            "слушать",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_QUESTION_ALTERNATIVE(self):
        metric = "SY_QUESTION_ALTERNATIVE"
        test_text = TEXT_TEST
        expected_debug = [
            "Ты",
            "работаешь",
            "или",
            "учишься",
            "Она",
            "встречала",
            "его",
            "раньше",
            "или",
            "только",
            "познакомилась",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_QUESTION_TAG(self):
        metric = "SY_QUESTION_TAG"
        test_text = "Она успеет сделать эту работу, правда?"
        expected_debug = ["Она", "успеет", "сделать", "эту", "работу", "правда"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)


if __name__ == "__main__":
    unittest.main()
