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


class TestGrammarRU(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        lang = "ru"
        cls.sm = StyloMetrix(lang, debug=True)

    def test_G_ROOT_VERB_IMPERFECT(self):
        metric = "G_ROOT_VERB_IMPERFECT"
        test_text = TEXT_TEST
        expected_debug = [
            "учатся",
            "учатся",
            "изучают",
            "делает",
            "делает",
            "Слушай",
            "заключается",
            "Сделает",
            "делает",
            "хочешь",
            "слушали",
            "работаешь",
            "встречала",
            "лежит",
            "Поспешишь",
            "предугадает",
            "исследуется",
            "исследовался",
            "исследоваться",
            "шагала",
            "качал",
            "казалась",
            "учишься",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_ALL_VERB_IMPERFECT(self):
        metric = "G_ALL_VERB_IMPERFECT"
        test_text = TEXT_TEST
        expected_debug = [
            "учатся",
            "учатся",
            "изучают",
            "делает",
            "делает",
            "Слушай",
            "заключается",
            "Сделает",
            "делает",
            "хочешь",
            "слушать",
            "слушали",
            "работаешь",
            "учишься",
            "встречала",
            "лежит",
            "Поспешишь",
            "насмешишь",
            "предугадает",
            "бежать",
            "глядели",
            "сдерживать",
            "исследуется",
            "исследовался",
            "исследоваться",
            "шагала",
            "производимая",
            "Идущий",
            "качал",
            "Сидящая",
            "казалась",
            "знающий",
            "покупающий",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_ROOT_VERB_PERFECT(self):
        metric = "G_ROOT_VERB_PERFECT"
        test_text = TEXT_TEST
        expected_debug = [
            "пришла",
            "Сделай",
            "придет",
            "успеет",
            "сможешь",
            "отправится",
            "согласились",
            "смогла",
            "выкрашены",
            "встретился",
            "обречен",
            "ушла",
            "написан",
            "написана",
            "использовано",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_ALL_VERB_PERFECT(self):
        metric = "G_ALL_VERB_PERFECT"
        test_text = TEXT_TEST
        expected_debug = [
            "пришла",
            "Сделай",
            "отказались",
            "помочь",
            "придет",
            "придет",
            "успеет",
            "сделать",
            "познакомилась",
            "сможешь",
            "прийти",
            "отправится",
            "согласились",
            "Познакомившись",
            "смогла",
            "выкрашены",
            "встретился",
            "произведённая",
            "обречен",
            "закончившая",
            "ушла",
            "написан",
            "написана",
            "использовано",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_PRESENT_IND_IMPERFECT(self):
        metric = "G_PRESENT_IND_IMPERFECT"
        test_text = TEXT_TEST
        expected_debug = [
            "учатся",
            "учатся",
            "изучают",
            "делает",
            "делает",
            "заключается",
            "Сделает",
            "делает",
            "хочешь",
            "работаешь",
            "лежит",
            "Поспешишь",
            "насмешишь",
            "будет",
            "предугадает",
            "исследуется",
            "будет",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_PAST_IND_IMPERFECT(self):
        metric = "G_PAST_IND_IMPERFECT"
        test_text = TEXT_TEST
        expected_debug = [
            "слушали",
            "встречала",
            "была",
            "были",
            "глядели",
            "исследовался",
            "шагала",
            "качал",
            "казалась",
            "был",
            "была",
            "было",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_PAST_IND_PERFECT(self):
        metric = "G_PAST_IND_PERFECT"
        test_text = TEXT_TEST
        expected_debug = [
            "пришла",
            "Сделай",
            "отказались",
            "познакомилась",
            "согласились",
            "смогла",
            "встретился",
            "ушла",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_FUT_IND_PERFECT(self):
        metric = "G_FUT_IND_PERFECT"
        test_text = TEXT_TEST
        expected_debug = ["придет", "придет", "успеет", "сможешь", "отправится"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_FUT_IND_IMPERFECT_SIMPLE(self):
        metric = "G_FUT_IND_IMPERFECT_SIMPLE"
        test_text = TEXT_TEST
        expected_debug = []
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_FUT_IND_COMPLEX(self):
        metric = "G_FUT_IND_COMPLEX"
        test_text = TEXT_TEST
        expected_debug = [
            "будет",
            "была",
            "год",
            "замечательная",
            "исследоваться",
            "написана",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_INFINITIVE(self):
        metric = "G_INFINITIVE"
        test_text = TEXT_TEST
        expected_debug = [
            "помочь",
            "слушать",
            "сделать",
            "учишься",
            "прийти",
            "бежать",
            "сдерживать",
            "исследоваться",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_PASSIVE(self):
        metric = "G_PASSIVE"
        test_text = TEXT_TEST
        expected_debug = [
            "выкрашены",
            "Машина",
            "обречен",
            "написан",
            "написана",
            "использовано",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_TRANSITIVE(self):
        metric = "G_TRANSITIVE"
        test_text = TEXT_TEST
        expected_debug = [
            "учатся",
            "учатся",
            "изучают",
            "пришла",
            "делает",
            "делает",
            "Сделай",
            "отказались",
            "заключается",
            "придет",
            "Сделает",
            "делает",
            "придет",
            "хочешь",
            "успеет",
            "слушали",
            "работаешь",
            "встречала",
            "лежит",
            "Поспешишь",
            "насмешишь",
            "сможешь",
            "отправится",
            "предугадает",
            "согласились",
            "Познакомившись",
            "смогла",
            "исследуется",
            "исследовался",
            "выкрашены",
            "шагала",
            "встретился",
            "производимая",
            "произведённая",
            "Идущий",
            "качал",
            "Сидящая",
            "казалась",
            "знающий",
            "обречен",
            "покупающий",
            "закончившая",
            "ушла",
            "написан",
            "написана",
            "использовано",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_INTRANSITIVE(self):
        metric = "G_INTRANSITIVE"
        test_text = TEXT_TEST
        expected_debug = [
            "Слушай",
            "учишься",
            "познакомилась",
            "прийти",
            "глядели",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_IMPERSONAL_VERBS(self):
        metric = "G_IMPERSONAL_VERBS"
        test_text = TEXT_TEST
        expected_debug = [
            "изучают",
            "заключается",
            "хочешь",
            "отправится",
            "согласились",
            "использовано",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_G_ADV_PRF_PART(self):
        metric = "G_ADV_PRF_PART"
        test_text = TEXT_TEST
        expected_debug = ["Познакомившись"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)


if __name__ == "__main__":
    unittest.main()
