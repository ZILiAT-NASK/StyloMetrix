import unittest

from src.stylo_metrix.stylo_metrix import StyloMetrix 


class TestLexicalDE(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        lang = "de"
        cls.sm = StyloMetrix(lang, debug=True)
        


    def test_L_SYL_G1(self):
        metric = "L_SYL_G1"
        test_text = "Neue Gewohnheiten etablieren:"
        expected_debug = ['Neue']
        expected_out = 0.25
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_L_SYL_G3(self):
        metric = "L_SYL_G3"
        test_text = "Neue Gewohnheiten etablieren:"
        expected_debug = ['etablieren']
        expected_out = 0.25
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_L_SYL_G4(self):
        metric = "L_SYL_G4"
        test_text = "Neue Gewohnheiten etablieren:"
        expected_debug = ['Gewohnheiten']
        expected_out = 0.25
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_L_TTR_IA(self):
        metric = "L_TTR_IA"
        test_text = "Neue Gewohnheiten etablieren:"
        expected_debug = {'etablieren', 'gewohnheiten', 'neue'}
        expected_out = 0.75
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_L_TTR_LA(self):
        metric = "L_TTR_LA"
        test_text = "Neue Gewohnheiten etablieren:"
        expected_debug = {'neu', 'etablieren', 'gewohnheit'}
        expected_out = 0.75
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_L_CONT_A(self):
        metric = "L_CONT_A"
        test_text = "Neue Gewohnheiten etablieren:"
        expected_debug = ['Neue', 'Gewohnheiten', 'etablieren']
        expected_out = 0.75
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_L_CONT_T(self):
        metric = "L_CONT_T"
        test_text = "Neue Gewohnheiten etablieren:"
        expected_debug = {'Gewohnheiten', 'etablieren', 'Neue'}
        expected_out = 0.75
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_L_CONT_L(self):
        metric = "L_CONT_L"
        test_text = "Neue Gewohnheiten etablieren:"
        expected_debug = {'neu', 'etablieren', 'Gewohnheit'}
        expected_out = 0.75
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_L_STOP(self):
        metric = "L_STOP"
        test_text = "Neue Gewohnheiten etablieren:"
        expected_debug = ['Neue']
        expected_out = 0.25
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_L_TCCT1(self):
        metric = "L_TCCT1"
        test_text = "Neue Gewohnheiten etablieren:"
        expected_debug = ['neu']
        expected_out = 0.25
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_L_TCCT5(self):
        metric = "L_TCCT5"
        test_text = "Neue Gewohnheiten etablieren:"
        expected_debug = ['neu']
        expected_out = 0.25
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_L_SYL_G2(self):
        metric = "L_SYL_G2"
        test_text = "6 Tipps aus der Wissenschaft Neue Angewohnheiten etablieren und alte loswerden – wie funktioniert das?"
        expected_debug = ['alte']
        expected_out = 0.0625
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_L_SYL_G5(self):
        metric = "L_SYL_G5"
        test_text = "6 Tipps aus der Wissenschaft Neue Angewohnheiten etablieren und alte loswerden – wie funktioniert das?"
        expected_debug = ['Angewohnheiten']
        expected_out = 0.0625
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_L_FUNC_A(self):
        metric = "L_FUNC_A"
        test_text = "6 Tipps aus der Wissenschaft Neue Angewohnheiten etablieren und alte loswerden – wie funktioniert das?"
        expected_debug = ['6', 'aus', 'der', 'und', 'das']
        expected_out = 0.3125
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_L_FUNC_T(self):
        metric = "L_FUNC_T"
        test_text = "6 Tipps aus der Wissenschaft Neue Angewohnheiten etablieren und alte loswerden – wie funktioniert das?"
        expected_debug = {'der', 'aus', 'das', '6', 'und'}
        expected_out = 0.3125
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_L_FUNC_L(self):
        metric = "L_FUNC_L"
        test_text = "6 Tipps aus der Wissenschaft Neue Angewohnheiten etablieren und alte loswerden – wie funktioniert das?"
        expected_debug = {'aus', 'der', '6', 'und'}
        expected_out = 0.25
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_L_NAME(self):
        metric = "L_NAME"
        test_text = "Der Professor für Sozialpsychologie Bas Verplanken, der sich seit über 20 Jahren mit dem Einfluss von Angewohnheiten auf unser Leben und Wesen beschäftigt, geht allerdings von rund 30 bis 50 Prozent aus."
        expected_debug = ['Bas', 'Verplanken']
        expected_out = 0.05714285714285714
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_L_NAME_M(self):
        metric = "L_NAME_M"
        test_text = "Der Professor für Sozialpsychologie Bas Verplanken, der sich seit über 20 Jahren mit dem Einfluss von Angewohnheiten auf unser Leben und Wesen beschäftigt, geht allerdings von rund 30 bis 50 Prozent aus."
        expected_debug = ['Bas', 'Verplanken']
        expected_out = 0.05714285714285714
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_L_NAME_F(self):
        metric = "L_NAME_F"
        test_text = "Dan Ariely ist Professor für Psychologie und Verhaltensökonomik an der Duke University."
        expected_debug = ['University']
        expected_out = 0.07692307692307693
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_L_ORG(self):
        metric = "L_ORG"
        test_text = "Dan Ariely ist Professor für Psychologie und Verhaltensökonomik an der Duke University."
        expected_debug = ['Duke', 'University']
        expected_out = 0.15384615384615385
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_L_GEOG(self):
        metric = "L_GEOG"
        test_text = "Wenn man sich also gesünder ernähren will, um abzunehmen, dem Diätwahn innerlich aber längst abgeschworen hat, fällt es viel schwerer, dieses Ziel tatsächlich umzusetzen."
        expected_debug = ['Diätwahn']
        expected_out = 0.034482758620689655
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        


if __name__ == "__main__":
    unittest.main()
