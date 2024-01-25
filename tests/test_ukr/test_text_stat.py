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


class TestReadabilityUKR(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        lang = "ukr"
        cls.sm = StyloMetrix(lang, debug=True)

    def test_FKR(self):
        metric = "FKR"
        test_text = TEXT_TEST
        expected_debug = {}
        expected_out = 73.19253968253966

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = {}

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_FKGL(self):
        metric = "FKGL"
        test_text = TEXT_TEST
        expected_debug = {}
        expected_out = 5.317063492063493

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = {}

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)


if __name__ == "__main__":
    unittest.main()
