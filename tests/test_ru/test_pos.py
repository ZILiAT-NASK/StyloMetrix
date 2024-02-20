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


class TestPosRU(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        lang = "ukr"
        cls.sm = StyloMetrix(lang, debug=True)

    def test_POS_VERB(self):
        metric = "POS_VERB"
        test_text = TEXT_TEST
        expected_debug = [
            "учатся",
            "учатся",
            "изучают",
            "пришла",
            "делает",
            "делает",
            "Сделай",
            "Слушай",
            "отказались",
            "заключается",
            "придет",
            "Сделает",
            "делает",
            "придет",
            "хочешь",
            "слушать",
            "успеет",
            "сделать",
            "слушали",
            "работаешь",
            "учишься",
            "встречала",
            "познакомилась",
            "лежит",
            "Поспешишь",
            "насмешишь",
            "сможешь",
            "прийти",
            "отправится",
            "предугадает",
            "согласились",
            "бежать",
            "глядели",
            "Познакомившись",
            "смогла",
            "сдерживать",
            "исследуется",
            "исследовался",
            "исследоваться",
            "шагала",
            "встретился",
            "качал",
            "казалась",
            "знающий",
            "покупающий",
            "закончившая",
            "ушла",
            "использовано",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_POS_NOUN(self):
        metric = "POS_NOUN"
        test_text = TEXT_TEST
        expected_debug = [
            "Студенты",
            "языку",
            "день",
            "Студенты",
            "занятиях",
            "студенты",
            "язык",
            "Зима",
            "работу",
            "работу",
            "работу",
            "Вопрос",
            "работу",
            "срок",
            "работу",
            "гости",
            "работу",
            "правда",
            "лекцию",
            "?",
            "Книга",
            "полке",
            "Слово",
            "серебро",
            "молчание",
            "золото",
            "людей",
            "путешествие",
            "год",
            "путешествие",
            "причине",
            "погода",
            "глаза",
            "женщина",
            "слез",
            "Космос",
            "людьми",
            "Космос",
            "людьми",
            "Космос",
            "людьми",
            "Стены",
            "цвет",
            "блондинка",
            "шагом",
            "городу",
            "студент",
            "учителем",
            "Машина",
            "Машина",
            "встречу",
            "собака",
            "хвостом",
            "лавочке",
            "девушка",
            "призраком",
            "Человек",
            "тайн",
            "гибель",
            "Человек",
            "овощи",
            "подруга",
            "работу",
            "Роман",
            "стихах",
            "Картина",
            "художником",
            "Лекарство",
            "врачами",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_POS_ADJ(self):
        metric = "POS_ADJ"
        test_text = TEXT_TEST
        expected_debug = [
            "русскому",
            "русский",
            "нужна",
            "замечательная",
            "готовы",
            "выкрашены",
            "зеленый",
            "Окрашенная",
            "медленным",
            "Бывший",
            "первым",
            "производимая",
            "произведённая",
            "Идущий",
            "Сидящая",
            "обречен",
            "свежие",
            "написан",
            "написана",
            "2014",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_POS_ADV(self):
        metric = "POS_ADV"
        test_text = TEXT_TEST
        expected_debug = [
            "Странно",
            "помочь",
            "сегодня",
            "Сколько",
            "можно",
            "так",
            "раньше",
            "завтра",
            "скоро",
            "куда",
            "больше",
            "снова",
            "медленно",
            "только",
            "домой",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_POS_DET(self):
        metric = "POS_DET"
        test_text = TEXT_TEST
        expected_debug = [
            "каждый",
            "эту",
            "эту",
            "которая",
            "это",
            "одной",
            "своим",
            "много",
            "Моя",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_POS_INTJ(self):
        metric = "POS_INTJ"
        test_text = "Эй! Слушай сюда!"
        expected_debug = ["Эй"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_POS_CONJ(self):
        metric = "POS_CONJ"
        test_text = TEXT_TEST
        expected_debug = ["что", "или", "или", "и"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_POS_PART(self):
        metric = "POS_PART"
        test_text = TEXT_TEST
        expected_debug = ["ли", "ли", "не", "ли", "только", "не", "не", "только", "что"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_POS_NUM(self):
        metric = "POS_NUM"
        test_text = TEXT_TEST
        expected_debug = []  # TODO
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_POS_PREP(self):
        metric = "POS_PREP"
        test_text = TEXT_TEST
        expected_debug = [
            "На",
            "в",
            "в",
            "в",
            "на",
            "в",
            "через",
            "на",
            "по",
            "с",
            "в",
            "по",
            "со",
            "в",
            "в",
            "на",
            "на",
            "на",
            "в",
            "в",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_POS_PRO(self):
        metric = "POS_PRO"
        test_text = TEXT_TEST
        expected_debug = [
            "Он",
            "Кто",
            "Что",
            "они",
            "нам",
            "том",
            "он",
            "он",
            "Он",
            "Кто",
            "Чего",
            "ты",
            "их",
            "Она",
            "Они",
            "Ты",
            "Она",
            "его",
            "вам",
            "Ты",
            "Она",
            "Что",
            "никто",
            "Мы",
            "мы",
            "ней",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_POS_OTHER(self):
        metric = "POS_OTHER"
        test_text = "Что это за xfgh pdl jklw?"
        expected_debug = ["xfgh", "pdl", "jklw"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)


if __name__ == "__main__":
    unittest.main()
