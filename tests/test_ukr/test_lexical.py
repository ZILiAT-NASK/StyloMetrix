import unittest

from src.stylo_metrix.stylo_metrix import StyloMetrix

TEXT_TEST = """Я люблю тебе, осінь! Багряні гаї; та дібровки. Як ти вмієш різнобарвне, розмаїто одягати мій край!
Осінь! Шелестить під ногами листя. Розбурханий вітер кидає його додолу. Злий, непривітний, розлючений. Міцніше
й міцніше обіймає дерева. Ніяк — не вгамується. Дедалі нові пригорщі: жовто-червоного золота жбурляє на землю. Наче величезний килим навкруги.
Небо здається високим-високим. Он виникла цяточка, невеличка хмарка. 'Боязко так, наче соромиться, випливає
скрадливо.' Роздумує: чи принести дощ? І поступово лазурове небо набирає білястих тонів, а потім стає похмурим, сердитим.
Раптом воно прояснилось. Один, другий, третій сонячний промінь. Ласкаво так припали до землі.
Спасибі тобі, осінь, за те, що ти є. За те, що ти така неповторна. Мила. Замріяна. Щедра.
"""


class TestLexicalUKR(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        lang = "ukr"
        cls.sm = StyloMetrix(lang, debug=True)

    def test_L_TYPE_TOKEN_RATIO_LEMMAS(self):
        metric = "L_TYPE_TOKEN_RATIO_LEMMAS"
        test_text = TEXT_TEST
        expected_debug = [
            "неповторний",
            "лазуровий",
            "мій",
            "прояснитися",
            "принести",
            "тон",
            "воно",
            "дощ",
            "край",
            "сердитий",
            "небо",
            "другий",
            "наче",
            "кидати",
            "пригорщі",
            "дерева",
            "міцніше",
            "дібровка",
            "здаватися",
            "хмарка",
            "високий",
            "замріяний",
            "боязко",
            "й",
            "бути",
            "одягати",
            "вміти",
            "нога",
            "такий",
            "цяточка",
            "до",
            "земля",
            "роздумувати",
            "під",
            "Міцніше",
            "скрадливо",
            "червоний",
            "що",
            "вітер",
            "так",
            "не",
            "та",
            "осінь",
            "ставати",
            "додолу",
            "за",
            "чи",
            "жовто",
            "промінь",
            "поступово",
            "ласкаво",
            "сонячний",
            "непривітний",
            "розлючений",
            "виникнути",
            "величезний",
            "і",
            "як",
            "жбурляти",
            "спасибі",
            "щедрий",
            "листя",
            "випливати",
            "гай",
            "раптом",
            "а",
            "ніяк",
            "розбурханий",
            "шелестіти",
            "багряний",
            "он",
            "навкруги",
            "я",
            "новий",
            "припасти",
            "обіймати",
            "вгамується",
            "білястий",
            "милий",
            "похмурий",
            "на",
            "ти",
            "золото",
            "третій",
            "розмаїто",
            "дедал",
            "набирати",
            "той",
            "потім",
            "один",
            "соромитися",
            "невеличкий",
            "любити",
            "злий",
            "різнобарвне",
            "килим",
            "він",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)

    def test_L_CONT_A(self):
        metric = "L_CONT_A"
        test_text = TEXT_TEST
        expected_debug = [
            "Я",
            "люблю",
            "тебе",
            "осінь",
            "!",
            "Багряні",
            "гаї",
            "дібровки",
            "Як",
            "ти",
            "вмієш",
            "різнобарвне",
            "розмаїто",
            "одягати",
            "край",
            "\n",
            "Осінь",
            "!",
            "Шелестить",
            "ногами",
            "листя",
            "Розбурханий",
            "вітер",
            "кидає",
            "його",
            "додолу",
            "Злий",
            "непривітний",
            "розлючений",
            "Міцніше",
            "\n",
            "міцніше",
            "обіймає",
            "дерева",
            "Ніяк",
            "вгамується",
            "Дедалі",
            "нові",
            "пригорщі",
            "жовто",
            "червоного",
            "золота",
            "жбурляє",
            "землю",
            "величезний",
            "килим",
            "навкруги",
            "\n",
            "Небо",
            "здається",
            "високим",
            "високим",
            "виникла",
            "цяточка",
            "невеличка",
            "хмарка",
            "Боязко",
            "так",
            "соромиться",
            "випливає",
            "\n",
            "скрадливо",
            "Роздумує",
            "принести",
            "дощ",
            "поступово",
            "лазурове",
            "небо",
            "набирає",
            "білястих",
            "тонів",
            "потім",
            "стає",
            "похмурим",
            "сердитим",
            "\n",
            "Раптом",
            "воно",
            "прояснилось",
            "другий",
            "третій",
            "сонячний",
            "промінь",
            "Ласкаво",
            "так",
            "припали",
            "землі",
            "\n",
            "тобі",
            "осінь",
            "те",
            "ти",
            "є",
            "те",
            "ти",
            "неповторна",
            "Мила",
            "Замріяна",
            "Щедра",
            "\n",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)

    def test_L_FUNC_A(self):
        metric = "L_FUNC_A"
        test_text = TEXT_TEST
        expected_debug = [
            ",",
            ";",
            "та",
            ".",
            ",",
            "мій",
            "!",
            "під",
            ".",
            ".",
            ",",
            ",",
            ".",
            "й",
            ".",
            "—",
            "не",
            ".",
            ":",
            "-",
            "на",
            ".",
            "Наче",
            ".",
            "-",
            ".",
            "Он",
            ",",
            ".",
            "'",
            ",",
            "наче",
            ",",
            ".",
            "'",
            ":",
            "чи",
            "?",
            "І",
            ",",
            "а",
            ",",
            ".",
            ".",
            "Один",
            ",",
            ",",
            ".",
            "до",
            ".",
            "Спасибі",
            ",",
            ",",
            "за",
            ",",
            "що",
            ".",
            "За",
            ",",
            "що",
            "така",
            ".",
            ".",
            ".",
            ".",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)

    def test_L_CONT_T(self):
        metric = "L_CONT_T"
        test_text = TEXT_TEST
        expected_debug = [
            "білястих",
            "обіймає",
            "дощ",
            "дібровки",
            "воно",
            "набирає",
            "додолу",
            "Багряні",
            "\n",
            "дерева",
            "прояснилось",
            "лазурове",
            "стає",
            "потім",
            "розлючений",
            "тобі",
            "другий",
            "небо",
            "червоного",
            "кидає",
            "різнобарвне",
            "високим",
            "цяточка",
            "Злий",
            "Боязко",
            "сердитим",
            "похмурим",
            "Як",
            "міцніше",
            "виникла",
            "Міцніше",
            "одягати",
            "його",
            "землі",
            "гаї",
            "розмаїто",
            "землю",
            "килим",
            "Щедра",
            "Шелестить",
            "сонячний",
            "тебе",
            "листя",
            "Осінь",
            "навкруги",
            "!",
            "тонів",
            "пригорщі",
            "скрадливо",
            "третій",
            "Небо",
            "величезний",
            "вітер",
            "Раптом",
            "поступово",
            "ногами",
            "золота",
            "Роздумує",
            "припали",
            "здається",
            "невеличка",
            "вмієш",
            "Розбурханий",
            "неповторна",
            "Ласкаво",
            "соромиться",
            "те",
            "ти",
            "осінь",
            "так",
            "вгамується",
            "Мила",
            "випливає",
            "край",
            "нові",
            "промінь",
            "жовто",
            "Ніяк",
            "хмарка",
            "є",
            "Замріяна",
            "непривітний",
            "Дедалі",
            "люблю",
            "жбурляє",
            "Я",
            "принести",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)

    def test_L_FUNC_T(self):
        metric = "L_FUNC_T"
        test_text = TEXT_TEST
        expected_debug = [
            "наче",
            "не",
            "?",
            "до",
            "Он",
            "а",
            "що",
            "за",
            "мій",
            "Спасибі",
            "-",
            "та",
            "Наче",
            ",",
            "й",
            ":",
            "І",
            "За",
            "'",
            "—",
            ";",
            "Один",
            "!",
            ".",
            "під",
            "така",
            "чи",
            "на",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)

    def test_L_PLURAL_NOUNS(self):
        metric = "L_PLURAL_NOUNS"
        test_text = TEXT_TEST
        expected_debug = ["гаї", "дібровки", "ногами", "тонів"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_SINGULAR_NOUNS(self):
        metric = "L_SINGULAR_NOUNS"
        test_text = TEXT_TEST
        expected_debug = [
            "осінь",
            "!",
            "різнобарвне",
            "край",
            "Осінь",
            "!",
            "листя",
            "вітер",
            "дерева",
            "золота",
            "землю",
            "килим",
            "Небо",
            "цяточка",
            "хмарка",
            "дощ",
            "небо",
            "промінь",
            "землі",
            "осінь",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_PROPER_NAMES(self):
        metric = "L_PROPER_NAME"
        test_text = """Дівчиною з легенди називають Марусю Чурай. 
За існуючими переказами, народна поетеса народилася у 1625 р. у Полтаві, в козацькій родині. 
Маруся мала чудовий голос і майстерно співала пісні, які складала сама. Друже суддя, я не буду працювати завтра."""
        expected_debug = ["Марусю", "Чурай", "Полтаві", "Маруся"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_PERSONAL_NAME(self):
        metric = "L_PERSONAL_NAME"
        test_text = "Дівчиною з легенди називають Марусю Чурай."
        expected_debug = ["Марусю Чурай"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_ANIM_NOUN(self):
        metric = "L_ANIM_NOUN"
        test_text = """Дівчиною з легенди називають Марусю Чурай. 
За існуючими переказами, народна поетеса народилася у 1625 р. у Полтаві, в козацькій родині. 
Маруся мала чудовий голос і майстерно співала пісні, які складала сама. Друже суддя, я не буду працювати завтра."""
        expected_debug = ["Дівчиною", "поетеса", "Друже", "суддя"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_INANIM_NOUN(self):
        metric = "L_INANIM_NOUN"
        test_text = TEXT_TEST
        expected_debug = [
            "осінь",
            "!",
            "гаї",
            "дібровки",
            "різнобарвне",
            "край",
            "Осінь",
            "!",
            "ногами",
            "листя",
            "вітер",
            "дерева",
            "пригорщі",
            "золота",
            "землю",
            "килим",
            "Небо",
            "цяточка",
            "хмарка",
            "дощ",
            "небо",
            "тонів",
            "промінь",
            "землі",
            "осінь",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_NOUN_NEUTRAL(self):
        metric = "L_NOUN_NEUTRAL"
        test_text = TEXT_TEST
        expected_debug = ["різнобарвне", "листя", "дерева", "золота", "Небо", "небо"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_NOUN_FAMININE(self):
        metric = "L_NOUN_FAMININE"
        test_text = TEXT_TEST
        expected_debug = [
            "осінь",
            "!",
            "дібровки",
            "Осінь",
            "!",
            "ногами",
            "землю",
            "цяточка",
            "хмарка",
            "землі",
            "осінь",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_NOUN_MASCULINE(self):
        metric = "L_NOUN_MASCULINE"
        test_text = TEXT_TEST
        expected_debug = ["гаї", "край", "вітер", "килим", "дощ", "тонів", "промінь"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_FEMININE_NAMES(self):
        metric = "L_FEMININE_NAMES"
        test_text = """Дівчиною з легенди називають Марусю Чурай. 
За існуючими переказами, народна поетеса народилася у 1625 р. у Полтаві, в козацькій родині. 
Маруся мала чудовий голос і майстерно співала пісні, які складала сама. Друже суддя, я не буду працювати завтра."""
        expected_debug = ["Марусю", "Чурай", "Маруся"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_SURNAMES(self):
        metric = "L_SURNAMES"
        test_text = "Дівчиною з легенди називають Марусю Чурай."
        expected_debug = ["Чурай"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_GIVEN_NAMES(self):
        metric = "L_GIVEN_NAMES"
        test_text = """Дівчиною з легенди називають Марусю Чурай. 
За існуючими переказами, народна поетеса народилася у 1625 р. у Полтаві, в козацькій родині. 
Маруся мала чудовий голос і майстерно співала пісні, які складала сама. Друже суддя, я не буду працювати завтра."""
        expected_debug = ["Марусю", "Маруся"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_FLAT_MULTIWORD(self):
        metric = "L_FLAT_MULTIWORD"
        test_text = """Дівчиною з легенди називають Марусю Чурай. 
За існуючими переказами, народна поетеса народилася у 1625 р. у Полтаві, в козацькій родині. 
Маруся мала чудовий голос і майстерно співала пісні, які складала сама. Друже суддя, я не буду працювати завтра."""
        expected_debug = ["Марусю", "Чурай", "Друже", "суддя"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_DIMINUTIVES(self):
        metric = "L_DIMINUTIVES"
        test_text = "То був малюсінький струмочок."
        expected_debug = ["малюсінький"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_DIRECT_OBJ(self):
        metric = "L_DIRECT_OBJ"
        test_text = TEXT_TEST
        expected_debug = [
            "тебе",
            "край",
            "листя",
            "його",
            "дерева",
            "дощ",
            "тонів",
            "тобі",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_INDIRECT_OBJ(self):
        metric = "L_INDIRECT_OBJ"
        test_text = TEXT_TEST
        expected_debug = ["ногами", "землю", "землі", "те"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_NOM_CASE(self):
        metric = "L_NOM_CASE"
        test_text = TEXT_TEST
        expected_debug = [
            "осінь",
            "!",
            "гаї",
            "дібровки",
            "Осінь",
            "!",
            "вітер",
            "пригорщі",
            "килим",
            "Небо",
            "цяточка",
            "хмарка",
            "небо",
            "промінь",
            "осінь",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_GEN_CASE(self):
        metric = "L_GEN_CASE"
        test_text = TEXT_TEST
        expected_debug = ["золота", "тонів", "землі"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_DAT_CASE(self):
        metric = "L_DAT_CASE"
        test_text = "Я не буду працювати завтра. Ви працюватимете завтра. Проект буде представлений наступного вівторка. Завдання буде зроблено. Але, добре подумавши, він вирішив, що на волі зайчику буде краще, хоч і небезпечно."
        expected_debug = ["зайчику"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_ACC_CASE(self):
        metric = "L_ACC_CASE"
        test_text = TEXT_TEST
        expected_debug = ["різнобарвне", "край", "листя", "дерева", "землю", "дощ"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_INS_CASE(self):
        metric = "L_INS_CASE"
        test_text = TEXT_TEST
        expected_debug = ["ногами"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_LOC_CASE(self):
        metric = "L_LOC_CASE"
        test_text = "Я не буду працювати завтра. Ви працюватимете завтра. Проект буде представлений наступного вівторка. Завдання буде зроблено. Але, добре подумавши, він вирішив, що на волі зайчику буде краще, хоч і небезпечно."
        expected_debug = ["волі"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_VOC_CASE(self):
        metric = "L_VOC_CASE"
        test_text = "Друже Вікторе, я не буду працювати завтра!"
        expected_debug = ["Друже", "Вікторе"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_QULITATIVE_ADJ_P(self):
        metric = "L_QULITATIVE_ADJ_P"
        test_text = TEXT_TEST
        expected_debug = [
            "Злий",
            "нові",
            "червоного",
            "високим",
            "високим",
            "похмурим",
            "Мила",
            "Щедра",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_RELATIVE_ADJ(self):
        metric = "L_RELATIVE_ADJ"
        test_text = TEXT_TEST
        expected_debug = [
            "Багряні",
            "Розбурханий",
            "непривітний",
            "розлючений",
            "жовто",
            "величезний",
            "невеличка",
            "лазурове",
            "білястих",
            "сердитим",
            "другий",
            "третій",
            "сонячний",
            "неповторна",
            "Замріяна",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_QUALITATIVE_ADJ_CMP(self):
        metric = "L_QUALITATIVE_ADJ_CMP"
        test_text = """Найсправжнісінький білий зовсім маленький грибок несміливо виглянув з-під великого дубового листочка. 
Трохи похилився до сходу, підставляючи теплому і ніжному сонцю свою гарну коричневу голівку. 
Велика краплина роси блиснула в косих променях світла і розтеклась веселими сестрами-намистинками по його капелюшку. 
Чисто вимитий грибок став зовсім симпатичний і навіть веселий.
Грибок швиденько накрився своїм листочком і навіть присів від страху.
Дівчиного жаху було достатньо.
Він вважав себе кращим за інших."""
        expected_debug = ["кращим"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_QUALITATIVE_ADJ_SUP(self):
        metric = "L_QUALITATIVE_ADJ_SUP"
        test_text = """Найсправжнісінький білий зовсім маленький грибок несміливо виглянув з-під великого дубового листочка. 
Трохи похилився до сходу, підставляючи теплому і ніжному сонцю свою гарну коричневу голівку. 
Велика краплина роси блиснула в косих променях світла і розтеклась веселими сестрами-намистинками по його капелюшку. 
Чисто вимитий грибок став зовсім симпатичний і навіть веселий.
Грибок швиденько накрився своїм листочком і навіть присів від страху.
Дівчиного жаху було достатньо.
Він вважав себе кращим за інших."""
        expected_debug = ["Найсправжнісінький"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_DIRECT_ADJ(self):
        metric = "L_DIRECT_ADJ"
        test_text = """Найсправжнісінький білий зовсім маленький грибок несміливо виглянув з-під великого дубового листочка. 
Трохи похилився до сходу, підставляючи теплому і ніжному сонцю свою гарну коричневу голівку. 
Велика краплина роси блиснула в косих променях світла і розтеклась веселими сестрами-намистинками по його капелюшку. 
Чисто вимитий грибок став зовсім симпатичний і навіть веселий.
Грибок швиденько накрився своїм листочком і навіть присів від страху.
Дівчиного жаху було достатньо.
Він вважав себе кращим за інших."""
        expected_debug = [
            "Найсправжнісінький",
            "білий",
            "маленький",
            "великого",
            "дубового",
            "теплому",
            "гарну",
            "коричневу",
            "Велика",
            "косих",
            "веселими",
            "вимитий",
            "Дівчиного",
            "ніжному",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_INDIRECT_ADJ(self):
        metric = "L_INDIRECT_ADJ"
        test_text = """Найсправжнісінький білий зовсім маленький грибок несміливо виглянув з-під великого дубового листочка. 
Трохи похилився до сходу, підставляючи теплому і ніжному сонцю свою гарну коричневу голівку. 
Велика краплина роси блиснула в косих променях світла і розтеклась веселими сестрами-намистинками по його капелюшку. 
Чисто вимитий грибок став зовсім симпатичний і навіть веселий.
Грибок швиденько накрився своїм листочком і навіть присів від страху.
Дівчиного жаху було достатньо.
Він вважав себе кращим за інших."""
        expected_debug = ["симпатичний", "кращим", "веселий"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_PUNCT(self):
        metric = "L_PUNCT"
        test_text = TEXT_TEST
        expected_debug = [
            ",",
            ";",
            ".",
            ",",
            "!",
            ".",
            ".",
            ",",
            ",",
            ".",
            ".",
            "—",
            ".",
            ":",
            "-",
            ".",
            ".",
            "-",
            ".",
            ",",
            ".",
            "'",
            ",",
            ",",
            ".",
            "'",
            ":",
            "?",
            ",",
            ",",
            ".",
            ".",
            ",",
            ",",
            ".",
            ".",
            ",",
            ",",
            ",",
            ".",
            ",",
            ".",
            ".",
            ".",
            ".",
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

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
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

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
        ]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_PUNCT_SEMC(self):
        metric = "L_PUNCT_SEMC"
        test_text = TEXT_TEST
        expected_debug = [";"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_PUNCT_COL(self):
        metric = "L_PUNCT_COL"
        test_text = TEXT_TEST
        expected_debug = [":", ":"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_PUNCT_DASH(self):
        metric = "L_PUNCT_DASH"
        test_text = TEXT_TEST
        expected_debug = ["—"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_NUM_CARD(self):
        metric = "L_NUM_CARD"
        test_text = "Минуло з часів козаччини більш як два століття."
        expected_debug = ["два"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_NUM_ORD(self):
        metric = "L_NUM_ORD"
        test_text = "Це був п'ятий день тижня"
        expected_debug = ["п'ятий"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_PRON_DEM(self):
        metric = "L_PRON_DEM"
        test_text = TEXT_TEST
        expected_debug = ["так", "потім", "так", "те", "те", "така"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_PRON_PRS(self):
        metric = "L_PRON_PRS"
        test_text = TEXT_TEST
        expected_debug = ["Я", "тебе", "ти", "мій", "його", "воно", "тобі", "ти", "ти"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_PRON_TOT(self):
        metric = "L_PRON_TOT"
        test_text = "П’єр Шевальє пише: “Мешканці України всі називають себе козаками і з гордістю носять це ім’я."
        expected_debug = ["всі"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_PRON_REL(self):
        metric = "L_PRON_REL"
        test_text = (
            "Він повинен попросити те, чого не можна ані побачити, ані попросити."
        )
        expected_debug = ["чого"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_PRON_INT(self):
        metric = "L_PRON_INT"
        test_text = "Де дім твій, скажи нам?"
        expected_debug = ["Де"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_PRON_RELATIVE(self):
        metric = "L_PRON_RELATIVE"
        test_text = "Ідеш і слухаєш і чуєш рідну землю, що годує тебе не тільки хлібом і медом, а й думками, піснями і звичаями."
        expected_debug = ["що"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_PRON_RFL(self):
        metric = "L_PRON_RFL"
        test_text = "П’єр Шевальє пише: “Мешканці України всі називають себе козаками і з гордістю носять це ім’я."
        expected_debug = ["себе"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_PRON_POS(self):
        metric = "L_PRON_POS"
        test_text = "Пишеться це не з бажання виставити свій рід перед світом, а в ім’я реалізму, з чим усі, хто співає, згодяться одностайно."
        expected_debug = ["свій"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_PRON_NEG(self):
        metric = "L_PRON_NEG"
        test_text = "Він купив його тільки через те, щоб ніхто не зарізав."
        expected_debug = ["ніхто"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_ADV_POS(self):
        metric = "L_ADV_POS"
        test_text = "Скрипливе колесо більше витримає, ніж добре."
        expected_debug = ["добре"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_ADV_CMP(self):
        metric = "L_ADV_CMP"
        test_text = "Скрипливе колесо більше витримає, ніж добре."
        expected_debug = ["більше"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_L_ADV_SUP(self):
        metric = "L_ADV_SUP"
        test_text = "Найтяжче хворому терпіти, а ще тяжче над хворим сидіти."
        expected_debug = ["Найтяжче"]
        expected_out = len(expected_debug) / len(test_text.split())

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = [token for token in debug[metric][0]["TOKENS"]]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)


if __name__ == "__main__":
    unittest.main()
