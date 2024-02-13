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


class TestLexicalRU(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        lang = "ru"
        cls.sm = StyloMetrix(lang, debug=True)

    def test_L_PLURAL_NOUNS(self):
        metric = "L_PLURAL_NOUNS"
        test_text = TEXT_TEST
        expected_debug = [
            "Студенты",
            "Студенты",
            "занятиях",
            "студенты",
            "гости",
            "-",
            "людей",
            "глаза",
            "слез",
            "людьми",
            "людьми",
            "людьми",
            "Стены",
            "тайн",
            "овощи",
            "стихах",
            "врачами",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_SINGULAR_NOUNS(self):
        metric = "L_SINGULAR_NOUNS"
        test_text = "Студенты учатся русскому языку каждый день. Студенты учатся. На занятиях студенты изучают русский язык. Зима пришла."
        expected_debug = ["языку", "день", "язык", "Зима"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_PROPER_NAMES(self):
        metric = "L_PROPER_NAME"
        test_text = TEXT_TEST
        expected_debug = ["России", "России", "Евгений", "Онегин", "Пушкиным"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_PERSONAL_NAME(self):
        metric = "L_PERSONAL_NAME"
        test_text = TEXT_TEST
        expected_debug = ["Евгений Онегин", "Пушкиным"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_ANIM_NOUN(self):
        metric = "L_ANIM_NOUN"
        test_text = TEXT_TEST
        expected_debug = [
            "Студенты",
            "Студенты",
            "студенты",
            "гости",
            "-",
            "людей",
            "женщина",
            "людьми",
            "людьми",
            "людьми",
            "блондинка",
            "студент",
            "учителем",
            "собака",
            "девушка",
            "Человек",
            "Человек",
            "подруга",
            "художником",
            "врачами",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_INANIM_NOUN(self):
        metric = "L_INANIM_NOUN"
        test_text = "Студенты учатся русскому языку каждый день. Студенты учатся. На занятиях студенты изучают русский язык. Зима пришла."
        expected_debug = ["языку", "день", "занятиях", "язык", "Зима"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_NOUN_NEUTRAL(self):
        metric = "L_NOUN_NEUTRAL"
        test_text = TEXT_TEST
        expected_debug = [
            "занятиях",
            "Слово",
            "-",
            "серебро",
            "молчание",
            "-",
            "золото",
            "путешествие",
            "путешествие",
            "Лекарство",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_NOUN_FAMININE(self):
        metric = "L_NOUN_FAMININE"
        test_text = TEXT_TEST
        expected_debug = [
            "Зима",
            "работу",
            "работу",
            "работу",
            "работу",
            "работу",
            "работу",
            "лекцию",
            "Книга",
            "полке",
            "причине",
            "-",
            "погода",
            "женщина",
            "слез",
            "Стены",
            "блондинка",
            "Машина",
            "Машина",
            "встречу",
            "собака",
            "лавочке",
            "девушка",
            "тайн",
            "гибель",
            "подруга",
            "работу",
            "Картина",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_NOUN_MASCULINE(self):
        metric = "L_NOUN_MASCULINE"
        test_text = "Студенты учатся русскому языку каждый день. Студенты учатся. На занятиях студенты изучают русский язык. Зима пришла."
        expected_debug = ["Студенты", "языку", "день", "Студенты", "студенты", "язык"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_FEMININE_NAMES(self):
        metric = "L_FEMININE_NAMES"
        test_text = TEXT_TEST
        expected_debug = []
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_SURNAMES(self):
        metric = "L_SURNAMES"
        test_text = TEXT_TEST
        expected_debug = []
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_GIVEN_NAMES(self):
        metric = "L_GIVEN_NAMES"
        test_text = TEXT_TEST
        expected_debug = []
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_FLAT_MULTIWORD(self):
        metric = "L_FLAT_MULTIWORD"
        test_text = TEXT_TEST
        expected_debug = ["Евгений", "Онегин"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_DIRECT_OBJ(self):
        metric = "L_DIRECT_OBJ"
        test_text = TEXT_TEST
        expected_debug = [
            "язык",
            "работу",
            "работу",
            "работу",
            "работу",
            "работу",
            "Чего",
            "их",
            "работу",
            "лекцию",
            "его",
            "-",
            "людей",
            "глаза",
            "слез",
            "тайн",
            "овощи",
            "работу",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_INDIRECT_OBJ(self):
        metric = "L_INDIRECT_OBJ"
        test_text = "Студенты учатся русскому языку каждый день. Студенты учатся. На занятиях студенты изучают русский язык. Зима пришла."
        expected_debug = ["языку", "день", "занятиях"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_NOM_CASE(self):
        metric = "L_NOM_CASE"
        test_text = "Студенты учатся русскому языку каждый день. Студенты учатся. На занятиях студенты изучают русский язык. Зима пришла."
        expected_debug = ["Студенты", "Студенты", "студенты", "Зима"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_GEN_CASE(self):
        metric = "L_GEN_CASE"
        test_text = TEXT_TEST
        expected_debug = ["слез", "тайн"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_DAT_CASE(self):
        metric = "L_DAT_CASE"
        test_text = TEXT_TEST
        expected_debug = ["языку", "причине", "-", "городу"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_ACC_CASE(self):
        metric = "L_ACC_CASE"
        test_text = TEXT_TEST
        expected_debug = [
            "день",
            "язык",
            "работу",
            "работу",
            "работу",
            "работу",
            "срок",
            "работу",
            "работу",
            "лекцию",
            "молчание",
            "-",
            "людей",
            "путешествие",
            "год",
            "путешествие",
            "цвет",
            "встречу",
            "гибель",
            "овощи",
            "работу",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_INS_CASE(self):
        metric = "L_INS_CASE"
        test_text = TEXT_TEST
        expected_debug = [
            "людьми",
            "людьми",
            "людьми",
            "шагом",
            "учителем",
            "хвостом",
            "призраком",
            "художником",
            "врачами",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_LOC_CASE(self):
        metric = "L_LOC_CASE"
        test_text = TEXT_TEST
        expected_debug = ["занятиях", "полке", "лавочке", "стихах"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_QULITATIVE_ADJ_P(self):
        metric = "L_QULITATIVE_ADJ_P"
        test_text = TEXT_TEST
        expected_debug = [
            "русскому",
            "русский",
            "Странно",
            "нужна",
            "замечательная",
            "готовы",
            "зеленый",
            "Окрашенная",
            "медленным",
            "Бывший",
            "первым",
            "свежие",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_RELATIVE_ADJ(self):
        metric = "L_RELATIVE_ADJ"
        test_text = TEXT_TEST
        expected_debug = ["2014"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_QUALITATIVE_ADJ_CMP(self):
        metric = "L_QUALITATIVE_ADJ_CMP"
        test_text = TEXT_TEST
        expected_debug = []
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_QUALITATIVE_ADJ_SUP(self):
        metric = "L_QUALITATIVE_ADJ_SUP"
        test_text = TEXT_TEST
        expected_debug = []
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_DIRECT_ADJ(self):
        metric = "L_DIRECT_ADJ"
        test_text = TEXT_TEST
        expected_debug = [
            "русскому",
            "русский",
            "зеленый",
            "Окрашенная",
            "медленным",
            "Бывший",
            "первым",
            "свежие",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_INDIRECT_ADJ(self):
        metric = "L_INDIRECT_ADJ"
        test_text = TEXT_TEST
        expected_debug = ["Странно", "нужна", "2014"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_PUNCT(self):
        metric = "L_PUNCT"
        test_text = TEXT_TEST
        expected_debug = [
            ".",
            ".",
            ".",
            ".",
            ".",
            "?",
            "!",
            "?",
            "!",
            ",",
            ".",
            ",",
            "?",
            "?",
            "?",
            "?",
            "?",
            "?",
            ",",
            "?",
            ",",
            "?",
            "?",
            "?",
            ",",
            ",",
            ".",
            ",",
            ".",
            ".",
            "?",
            ".",
            ",",
            ".",
            ".",
            ",",
            ".",
            ".",
            ".",
            ".",
            ".",
            ".",
            ".",
            ",",
            ".",
            ",",
            ".",
            ".",
            ".",
            ",",
            ",",
            ".",
            ",",
            ".",
            ",",
            ",",
            ".",
            "«",
            "»",
            ".",
            ".",
            ".",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_PUNCT_DOT(self):
        metric = "L_PUNCT_DOT"
        test_text = TEXT_TEST
        expected_debug = [
            ".",
            ".",
            ".",
            ".",
            ".",
            ".",
            ".",
            ".",
            ".",
            ".",
            ".",
            ".",
            ".",
            ".",
            ".",
            ".",
            ".",
            ".",
            ".",
            ".",
            ".",
            ".",
            ".",
            ".",
            ".",
            ".",
            ".",
            ".",
            ".",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_PUNCT_COM(self):
        metric = "L_PUNCT_COM"
        test_text = TEXT_TEST
        expected_debug = [
            ",",
            ",",
            ",",
            ",",
            ",",
            ",",
            ",",
            ",",
            ",",
            ",",
            ",",
            ",",
            ",",
            ",",
            ",",
            ",",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_PUNCT_SEMC(self):
        metric = "L_PUNCT_SEMC"
        test_text = TEXT_TEST
        expected_debug = []
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_PUNCT_COL(self):
        metric = "L_PUNCT_COL"
        test_text = TEXT_TEST
        expected_debug = []
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_PUNCT_DASH(self):
        metric = "L_PUNCT_DASH"
        test_text = TEXT_TEST
        expected_debug = []
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_NUM(self):
        metric = "L_NUM"
        test_text = "Картина была продана за 5 рублей."
        expected_debug = ["5"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_ADV_POS(self):
        metric = "L_ADV_POS"
        test_text = TEXT_TEST
        expected_debug = [
            "сегодня",
            "Сколько",
            "можно",
            "правда",
            "так",
            "завтра",
            "скоро",
            "куда",
            "снова",
            "медленно",
            "домой",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_ADV_CMP(self):
        metric = "L_ADV_CMP"
        test_text = TEXT_TEST
        expected_debug = ["раньше", "больше"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_ADV_SUP(self):
        metric = "L_ADV_SUP"
        test_text = TEXT_TEST
        expected_debug = []
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)


if __name__ == "__main__":
    unittest.main()
