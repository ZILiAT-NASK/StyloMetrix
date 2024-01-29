import unittest

from src.stylo_metrix.stylo_metrix import StyloMetrix

TEXT_TEST = """Я люблю тебе, осінь! Багряні гаї та дібровки. Як ти вмієш різнобарвне, розмаїто одягати мій край!
Осінь! Шелестить під ногами листя. Розбурханий вітер кидає його додолу. Злий, непривітний, розлючений. Міцніше
й міцніше обіймає дерева. Ніяк не вгамується. Дедалі нові пригорщі жовто-червоного золота жбурляє на землю. Наче величезний килим навкруги.
Небо здається високим-високим. Он виникла цяточка, невеличка хмарка. 'Боязко так, наче соромиться, випливає
скрадливо.' Роздумує: чи принести дощ? І поступово лазурове небо набирає білястих тонів, а потім стає похмурим, сердитим.
Раптом воно прояснилось. Один, другий, третій сонячний промінь. Ласкаво так припали до землі.
Спасибі тобі, осінь, за те, що ти є. За те, що ти така неповторна. Мила. Замріяна. Щедра.
"""


class TestSyntacticUKR(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        lang = "ukr"
        cls.sm = StyloMetrix(lang, debug=True)

    def test_SY_NARRATIVE(self):
        metric = "SY_NARRATIVE"
        test_text = TEXT_TEST
        expected_debug = [
            "Багряні",
            "гаї",
            "та",
            "дібровки.",
            "Шелестить",
            "під",
            "ногами",
            "листя.",
            "Розбурханий",
            "вітер",
            "кидає",
            "його",
            "додолу.",
            "Злий,",
            "непривітний,",
            "розлючений.",
            "Міцніше",
            "й",
            "міцніше",
            "обіймає",
            "дерева.",
            "Ніяк",
            "не",
            "вгамується.",
            "Дедалі",
            "нові",
            "пригорщі",
            "жовто-червоного",
            "золота",
            "жбурляє",
            "на",
            "землю.",
            "Наче",
            "величезний",
            "килим",
            "навкруги.",
            "Небо",
            "здається",
            "високим-високим.",
            "Он",
            "виникла",
            "цяточка,",
            "невеличка",
            "хмарка.",
            "'Боязко",
            "так,",
            "наче",
            "соромиться,",
            "випливає",
            "скрадливо.",
            "І",
            "поступово",
            "лазурове",
            "небо",
            "набирає",
            "білястих",
            "тонів,",
            "а",
            "потім",
            "стає",
            "похмурим,",
            "сердитим.",
            "Раптом",
            "воно",
            "прояснилось.",
            "Один,",
            "другий,",
            "третій",
            "сонячний",
            "промінь.",
            "Ласкаво",
            "так",
            "припали",
            "до",
            "землі.",
            "Спасибі",
            "тобі,",
            "осінь,",
            "за",
            "те,",
            "що",
            "ти",
            "є.",
            "За",
            "те,",
            "що",
            "ти",
            "така",
            "неповторна.",
            "Мила.",
            "Замріяна.",
            "Щедра.",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_NEGATIVE(self):
        metric = "SY_NEGATIVE"
        test_text = TEXT_TEST
        expected_debug = ["Ніяк", "не", "вгамується."]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_PARATAXIS(self):
        metric = "SY_PARATAXIS"
        test_text = TEXT_TEST
        expected_debug = ["Роздумує", "чи", "принести", "дощ"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_NON_FINITE(self):
        metric = "SY_NON_FINITE"
        test_text = TEXT_TEST
        expected_debug = [
            "Багряні",
            "гаї",
            "та",
            "дібровки.",
            "Осінь!",
            "Злий,",
            "непривітний,",
            "розлючений.",
            "Наче",
            "величезний",
            "килим",
            "навкруги.",
            "Один,",
            "другий,",
            "третій",
            "сонячний",
            "промінь.",
            "За",
            "те,",
            "що",
            "ти",
            "така",
            "неповторна.",
            "Мила.",
            "Замріяна.",
            "Щедра.",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_QUOTATIONS(self):
        metric = "SY_QUOTATIONS"
        test_text = TEXT_TEST
        expected_debug = [
            "Боязко",
            "так",
            "наче",
            "соромиться",
            "випливає",
            "\n",
            "скрадливо",
            "Роздумує",
            "чи",
            "принести",
            "дощ",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_EXCLAMATION(self):
        metric = "SY_EXCLAMATION"
        test_text = TEXT_TEST
        expected_debug = [
            "Я",
            "люблю",
            "тебе,",
            "осінь!",
            "Як",
            "ти",
            "вмієш",
            "різнобарвне,",
            "розмаїто",
            "одягати",
            "мій",
            "край!",
            "Осінь!",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_QUESTION(self):
        metric = "SY_QUESTION"
        test_text = TEXT_TEST
        expected_debug = ["Роздумує", "чи", "принести", "дощ"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_ELLIPSES(self):
        metric = "SY_ELLIPSES"
        test_text = "Сім струн я торкаю, струна по струні."
        expected_debug = ["Сім", "струн", "я", "торкаю,", "струна", "по", "струні."]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_POSITIONING(self):
        metric = "SY_POSITIONING"
        test_text = (
            "Тому ще з давніх-давен, готуючись до зими, мешканці України шиють кожухи."
        )
        expected_debug = ["давніх-давен"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_CONDITIONAL(self):
        metric = "SY_CONDITIONAL"
        test_text = "Лягли б ви спочити!"
        expected_debug = ["б", "Лягли"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_IMPERATIVE(self):
        metric = "SY_IMPERATIVE"
        test_text = "Подай мені води."
        expected_debug = ["Подай", "мені", "води."]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_AMPLIFIED_SENT(self):
        metric = "SY_AMPLIFIED_SENT"
        test_text = (
            "Як зберегти оцю красу, нерідко отак ненароком і бездумно понищену?!"
        )
        expected_debug = [
            "Як",
            "зберегти",
            "оцю",
            "красу,",
            "нерідко",
            "отак",
            "ненароком",
            "і",
            "бездумно",
            "понищену?!",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_SY_NOUN_PHRASES(self):
        metric = "SY_NOUN_PHRASES"
        test_text = "Він зайнявся вивченням української мови."
        expected_debug = ["Він", "вивченням", "мови", "мови", "української"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)


if __name__ == "__main__":
    unittest.main()
