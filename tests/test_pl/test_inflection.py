import unittest

from src.stylo_metrix.stylo_metrix import StyloMetrix


class TestInflectionPL(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        lang = "pl"
        cls.sm = StyloMetrix(lang, debug=True)

    def test_IN_N_1NOM(self):
        metric = "IN_N_1NOM"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = ["Księga", "Gospodarstwo", "Księga"]
        expected_out = 0.15

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_N_5INS(self):
        metric = "IN_N_5INS"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = ["inwokacją"]
        expected_out = 0.05

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_N_7VOC(self):
        metric = "IN_N_7VOC"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = ["Litwo", "Ojczyzno"]
        expected_out = 0.1

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_N_SG(self):
        metric = "IN_N_SG"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = [
            "Księga",
            "Gospodarstwo",
            "Księga",
            "inwokacją",
            "Litwo",
            "Ojczyzno",
        ]
        expected_out = 0.3

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_N_FS(self):
        metric = "IN_N_FS"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = ["Księga", "Księga", "inwokacją", "Litwo", "Ojczyzno"]
        expected_out = 0.25

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_N_NS(self):
        metric = "IN_N_NS"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = ["Gospodarstwo"]
        expected_out = 0.05

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_PRO_1NOM(self):
        metric = "IN_PRO_1NOM"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = ["ta"]
        expected_out = 0.05

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_PRO_7VOC(self):
        metric = "IN_PRO_7VOC"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = ["moja"]
        expected_out = 0.05

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_PRO_1S(self):
        metric = "IN_PRO_1S"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = ["moja"]
        expected_out = 0.05

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_3S(self):
        metric = "IN_V_3S"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = ["rozpoczyna"]
        expected_out = 0.05

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_FIN(self):
        metric = "IN_V_FIN"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = ["rozpoczyna"]
        expected_out = 0.05

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_IMPERF(self):
        metric = "IN_V_IMPERF"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = ["rozpoczyna"]
        expected_out = 0.05

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_ACT(self):
        metric = "IN_V_ACT"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = ["rozpoczyna"]
        expected_out = 0.05

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_PRES(self):
        metric = "IN_V_PRES"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = ["rozpoczyna"]
        expected_out = 0.05

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_ADJ_POS(self):
        metric = "IN_ADJ_POS"
        test_text = "Tadeusz po długiej nieobecności przybywa do rodzinnego domu."
        expected_debug = ["długiej", "rodzinnego"]
        expected_out = 0.2222222222222222

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_N_2GEN(self):
        metric = "IN_N_2GEN"
        test_text = "Tadeusz po długiej nieobecności przybywa do rodzinnego domu."
        expected_debug = ["domu"]
        expected_out = 0.1111111111111111

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_N_6LOC(self):
        metric = "IN_N_6LOC"
        test_text = "Tadeusz po długiej nieobecności przybywa do rodzinnego domu."
        expected_debug = ["nieobecności"]
        expected_out = 0.1111111111111111

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_N_MS(self):
        metric = "IN_N_MS"
        test_text = "Tadeusz po długiej nieobecności przybywa do rodzinnego domu."
        expected_debug = ["Tadeusz", "domu"]
        expected_out = 0.2222222222222222

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_PRO_2GEN(self):
        metric = "IN_PRO_2GEN"
        test_text = "Kieruje się do swego dawnego pokoju, ale ze zdziwieniem stwierdza, że komnata ta jest przez kogoś zamieszkiwana."
        expected_debug = ["swego"]
        expected_out = 0.05

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_PRO_4ACC(self):
        metric = "IN_PRO_4ACC"
        test_text = "Kieruje się do swego dawnego pokoju, ale ze zdziwieniem stwierdza, że komnata ta jest przez kogoś zamieszkiwana."
        expected_debug = ["kogoś"]
        expected_out = 0.05

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_PPAS(self):
        metric = "IN_V_PPAS"
        test_text = "Kieruje się do swego dawnego pokoju, ale ze zdziwieniem stwierdza, że komnata ta jest przez kogoś zamieszkiwana."
        expected_debug = ["zamieszkiwana"]
        expected_out = 0.05

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_PPAS_IMPERF(self):
        metric = "IN_V_PPAS_IMPERF"
        test_text = "Kieruje się do swego dawnego pokoju, ale ze zdziwieniem stwierdza, że komnata ta jest przez kogoś zamieszkiwana."
        expected_debug = ["zamieszkiwana"]
        expected_out = 0.05

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_N_4ACC(self):
        metric = "IN_N_4ACC"
        test_text = "Przez okno panicz dostrzega młodą dziewczynę, która podlewa w ogródku kwiaty."
        expected_debug = ["okno", "dziewczynę", "kwiaty"]
        expected_out = 0.23076923076923078

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_N_PL(self):
        metric = "IN_N_PL"
        test_text = "Przez okno panicz dostrzega młodą dziewczynę, która podlewa w ogródku kwiaty."
        expected_debug = ["kwiaty"]
        expected_out = 0.07692307692307693

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_N_NMP(self):
        metric = "IN_N_NMP"
        test_text = "Przez okno panicz dostrzega młodą dziewczynę, która podlewa w ogródku kwiaty."
        expected_debug = ["kwiaty"]
        expected_out = 0.07692307692307693

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_PANT(self):
        metric = "IN_V_PANT"
        test_text = (
            "Po chwili panienka wchodzi do pokoju, ale zobaczywszy Tadeusza ucieka."
        )
        expected_debug = ["zobaczywszy"]
        expected_out = 0.08333333333333333

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_PERF(self):
        metric = "IN_V_PERF"
        test_text = "Młodzieniec wita się z Wojskim, który opowiada o aktualnych wydarzeniach, zwłaszcza o sporze, jaki zaistniał pomiędzy Hrabią a Sędzią."
        expected_debug = ["zaistniał"]
        expected_out = 0.043478260869565216

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_PAST(self):
        metric = "IN_V_PAST"
        test_text = "Młodzieniec wita się z Wojskim, który opowiada o aktualnych wydarzeniach, zwłaszcza o sporze, jaki zaistniał pomiędzy Hrabią a Sędzią."
        expected_debug = ["zaistniał"]
        expected_out = 0.043478260869565216

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_N_MP(self):
        metric = "IN_N_MP"
        test_text = "Spór dotyczy starego zamku - spuścizny Horeszków."
        expected_debug = ["Horeszków"]
        expected_out = 0.125

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_3P(self):
        metric = "IN_V_3P"
        test_text = "Trwają przygotowania do uczty, w czasie której ma nastąpić zakończenie sporu."
        expected_debug = ["Trwają"]
        expected_out = 0.07692307692307693

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_INF(self):
        metric = "IN_V_INF"
        test_text = "Trwają przygotowania do uczty, w czasie której ma nastąpić zakończenie sporu."
        expected_debug = ["nastąpić"]
        expected_out = 0.07692307692307693

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_PRO_6LOC(self):
        metric = "IN_PRO_6LOC"
        test_text = "W tym czasie Protazy przenosi stoły z dworu do ruin zamku."
        expected_debug = ["tym"]
        expected_out = 0.08333333333333333

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_PCON(self):
        metric = "IN_V_PCON"
        test_text = "Sędzia - nawiązując do dziwnego roztargnienia młodzieńca - rozwodzi się nad grzecznością."
        expected_debug = ["nawiązując"]
        expected_out = 0.07692307692307693

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_PRO_3S(self):
        metric = "IN_PRO_3S"
        test_text = "Po nim zaś głos zabiera Podkomorzy, krytykując bezmyślne naśladowanie francuskiej mody i obyczajów."
        expected_debug = ["nim"]
        expected_out = 0.06666666666666667

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_GER(self):
        metric = "IN_V_GER"
        test_text = "Po nim zaś głos zabiera Podkomorzy, krytykując bezmyślne naśladowanie francuskiej mody i obyczajów."
        expected_debug = ["naśladowanie"]
        expected_out = 0.06666666666666667

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_ADV_POS(self):
        metric = "IN_ADV_POS"
        test_text = "Tadeusz uważa ją za dziewczynę spotkaną uprzednio przelotnie w dworku i z tego powodu nie pozostaje w zalotach dłużny."
        expected_debug = ["uprzednio", "przelotnie"]
        expected_out = 0.1

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_PPAS_PERF(self):
        metric = "IN_V_PPAS_PERF"
        test_text = "Tadeusz uważa ją za dziewczynę spotkaną uprzednio przelotnie w dworku i z tego powodu nie pozostaje w zalotach dłużny."
        expected_debug = ["spotkaną"]
        expected_out = 0.05

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_PACT(self):
        metric = "IN_V_PACT"
        test_text = "W tym czasie Rejent z Asesorem wszczynają spór dotyczący zalet Kusego i Sokoła - psów myśliwskich."
        expected_debug = ["dotyczący"]
        expected_out = 0.058823529411764705

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_N_3DAT(self):
        metric = "IN_N_3DAT"
        test_text = "Obaj zwracają się w końcu do Wojskiego z prośbą o rozstrzygnięcie, ale ten odmawia stwierdzając, że polowanie na zające uwłacza jego godności i dlatego nie będzie się zajmował tak błahym nieporozumieniem."
        expected_debug = ["godności"]
        expected_out = 0.029411764705882353

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_PRO_5INS(self):
        metric = "IN_PRO_5INS"
        test_text = (
            "W związku z tymi wydarzeniami na Litwę przedostają się liczni emisariusze."
        )
        expected_debug = ["tymi"]
        expected_out = 0.08333333333333333

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_PRO_3P(self):
        metric = "IN_PRO_3P"
        test_text = "Jednym z nich ma być ksiądz Robak - bernardyn, którego wygląd i zachowanie świadczą o jego żołnierskiej przeszłości, a który kwestuje po dworach szlacheckich i okolicznych karczmach. Księga II."
        expected_debug = ["nich"]
        expected_out = 0.030303030303030304

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_PRO_3DAT(self):
        metric = "IN_PRO_3DAT"
        test_text = "Hrabia jedzie do zamku, gdzie Gerwazy opowiada mu historię Stolnika - ostatniego członka rodu Horeszków"
        expected_debug = ["mu"]
        expected_out = 0.0625

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_IMPERS(self):
        metric = "IN_V_IMPERS"
        test_text = "Po pewnym jednak czasie podano mu czarną polewkę, co oznaczało, że został odprawiony."
        expected_debug = ["podano"]
        expected_out = 0.0625

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_IMPERS_PERF(self):
        metric = "IN_V_IMPERS_PERF"
        test_text = "Po pewnym jednak czasie podano mu czarną polewkę, co oznaczało, że został odprawiony."
        expected_debug = ["podano"]
        expected_out = 0.0625

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_PASS(self):
        metric = "IN_V_PASS"
        test_text = "Po pewnym jednak czasie podano mu czarną polewkę, co oznaczało, że został odprawiony."
        expected_debug = [("został", "odprawiony")]
        expected_out = 0.125

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_ADJ_SUP(self):
        metric = "IN_ADJ_SUP"
        test_text = "Tadeusz podąża za nią, natomiast Sędzia ogłasza konkurs: ten z mężczyzn, który znajdzie najwspanialszego rydza, będzie mógł usiąść do stołu przy wybranej przez siebie - najładniejszej jego zdaniem - pannie."
        expected_debug = ["najwspanialszego", "najładniejszej"]
        expected_out = 0.05714285714285714

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_FUTS(self):
        metric = "IN_V_FUTS"
        test_text = "Tadeusz podąża za nią, natomiast Sędzia ogłasza konkurs: ten z mężczyzn, który znajdzie najwspanialszego rydza, będzie mógł usiąść do stołu przy wybranej przez siebie - najładniejszej jego zdaniem - pannie."
        expected_debug = ["znajdzie"]
        expected_out = 0.02857142857142857

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_FUT(self):
        metric = "IN_V_FUT"
        test_text = "Tadeusz podąża za nią, natomiast Sędzia ogłasza konkurs: ten z mężczyzn, który znajdzie najwspanialszego rydza, będzie mógł usiąść do stołu przy wybranej przez siebie - najładniejszej jego zdaniem - pannie."
        expected_debug = ["znajdzie"]
        expected_out = 0.02857142857142857

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_COND(self):
        metric = "IN_V_COND"
        test_text = "Niewiasta krytykuje Sędziego za to, że chce pozostawić Tadeusza na wsi i proponuje, aby stryj wysłał młodzieńca do Warszawy lub Petersburga, gdzie mógłby on zrobić karierę."
        expected_debug = ["mógłby"]
        expected_out = 0.03333333333333333

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_ADV_COM(self):
        metric = "IN_ADV_COM"
        test_text = (
            "Później Telimena wsuwa w rękę Tadeusza klucz od swego pokoju i liścik."
        )
        expected_debug = ["Później"]
        expected_out = 0.07692307692307693

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_QUASI(self):
        metric = "IN_V_QUASI"
        test_text = "Po jego stronie opowiada się również Jankiel twierdząc, że u Sopliców w wiosce stoi rosyjskie wojsko, natomiast o Francuzach nic jeszcze nie słychać."
        expected_debug = ["słychać"]
        expected_out = 0.038461538461538464

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_ADJ_COM(self):
        metric = "IN_ADJ_COM"
        test_text = "Kwestarz wyznaje, że to on jest Jackiem Soplicą i opowiada swe dzieje: miłość do córki Stolnika - Ewy, zabójstwo Stolnika, swoje późniejsze pijaństwo, mające pozwolić mu zapomnieć o ukochanej, nieszczęśliwe małżeństwo i poświęcenie życia w walce o niepodległość Polski."
        expected_debug = ["późniejsze"]
        expected_out = 0.021739130434782608

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_1P(self):
        metric = "IN_V_1P"
        test_text = "Kochajmy się!"
        expected_debug = ["Kochajmy"]
        expected_out = 0.3333333333333333

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_IMP(self):
        metric = "IN_V_IMP"
        test_text = "Kochajmy się!"
        expected_debug = ["Kochajmy"]
        expected_out = 0.3333333333333333

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_2S(self):
        metric = "IN_V_2S"
        test_text = "Czytaj więcej na https://www.bryk.pl/lektury/adam-mickiewicz/pan-tadeusz.streszczenie-szczegolowe#utm_source=paste&utm_medium=paste&utm_campaign=other"
        expected_debug = ["Czytaj"]
        expected_out = 0.25

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_ADV_SUP(self):
        metric = "IN_ADV_SUP"
        test_text = "x"
        expected_debug = []  # TODO
        expected_out = 0

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_PRO_1P(self):
        metric = "IN_PRO_1P"
        test_text = "x"
        expected_debug = []  # TODO
        expected_out = 0

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_PRO_2P(self):
        metric = "IN_PRO_2P"
        test_text = "x"
        expected_debug = []  # TODO
        expected_out = 0

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_PRO_2S(self):
        metric = "IN_PRO_2S"
        test_text = "x"
        expected_debug = []  # TODO
        expected_out = 0

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_1S(self):
        metric = "IN_V_1S"
        test_text = "x"
        expected_debug = []  # TODO
        expected_out = 0

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_2P(self):
        metric = "IN_V_2P"
        test_text = "x"
        expected_debug = []  # TODO
        expected_out = 0

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_FUTC(self):
        metric = "IN_V_FUTC"
        test_text = "x"
        expected_debug = []  # TODO
        expected_out = 0

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_IMPERS_IMPERF(self):
        metric = "IN_V_IMPERS_IMPERF"
        test_text = "x"
        expected_debug = []  # TODO
        expected_out = 0

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)

    def test_IN_V_MOD(self):
        metric = "IN_V_MOD"
        test_text = "x"
        expected_debug = []  # TODO
        expected_out = 0

        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]

        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)


if __name__ == "__main__":
    unittest.main()
