import unittest

from src.stylo_metrix.stylo_metrix import StyloMetrix 


class TestPartsOfSpeechDE(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        lang = "de"
        cls.sm = StyloMetrix(lang, debug=True)
        


    def test_G_N(self):
        metric = "G_N"
        test_text = "Neue Gewohnheiten etablieren:"
        expected_debug = ['Gewohnheiten']
        expected_out = 0.25
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_G_ADJ(self):
        metric = "G_ADJ"
        test_text = "Neue Gewohnheiten etablieren:"
        expected_debug = ['Neue']
        expected_out = 0.25
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_G_V(self):
        metric = "G_V"
        test_text = "Neue Gewohnheiten etablieren:"
        expected_debug = ['etablieren']
        expected_out = 0.25
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_G_ADV(self):
        metric = "G_ADV"
        test_text = "6 Tipps aus der Wissenschaft Neue Angewohnheiten etablieren und alte loswerden – wie funktioniert das?"
        expected_debug = ['wie']
        expected_out = 0.0625
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_G_NUM(self):
        metric = "G_NUM"
        test_text = "6 Tipps aus der Wissenschaft Neue Angewohnheiten etablieren und alte loswerden – wie funktioniert das?"
        expected_debug = ['6']
        expected_out = 0.0625
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_G_ADP(self):
        metric = "G_ADP"
        test_text = "6 Tipps aus der Wissenschaft Neue Angewohnheiten etablieren und alte loswerden – wie funktioniert das?"
        expected_debug = ['aus']
        expected_out = 0.0625
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_G_CONJ(self):
        metric = "G_CONJ"
        test_text = "6 Tipps aus der Wissenschaft Neue Angewohnheiten etablieren und alte loswerden – wie funktioniert das?"
        expected_debug = ['und']
        expected_out = 0.0625
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_G_CCONJ(self):
        metric = "G_CCONJ"
        test_text = "6 Tipps aus der Wissenschaft Neue Angewohnheiten etablieren und alte loswerden – wie funktioniert das?"
        expected_debug = ['und']
        expected_out = 0.0625
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_G_PRO(self):
        metric = "G_PRO"
        test_text = "6 Tipps aus der Wissenschaft Neue Angewohnheiten etablieren und alte loswerden – wie funktioniert das?"
        expected_debug = ['wie', 'das']
        expected_out = 0.125
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_G_PRO_DEM(self):
        metric = "G_PRO_DEM"
        test_text = "6 Tipps aus der Wissenschaft Neue Angewohnheiten etablieren und alte loswerden – wie funktioniert das?"
        expected_debug = ['das']
        expected_out = 0.0625
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_G_PRO_INT(self):
        metric = "G_PRO_INT"
        test_text = "6 Tipps aus der Wissenschaft Neue Angewohnheiten etablieren und alte loswerden – wie funktioniert das?"
        expected_debug = ['wie']
        expected_out = 0.0625
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_G_ART(self):
        metric = "G_ART"
        test_text = "6 Tipps aus der Wissenschaft Neue Angewohnheiten etablieren und alte loswerden – wie funktioniert das?"
        expected_debug = ['der']
        expected_out = 0.0625
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_G_ART_DEF(self):
        metric = "G_ART_DEF"
        test_text = "6 Tipps aus der Wissenschaft Neue Angewohnheiten etablieren und alte loswerden – wie funktioniert das?"
        expected_debug = ['der']
        expected_out = 0.0625
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_G_SCONJ(self):
        metric = "G_SCONJ"
        test_text = "Und stimmt es tatsächlich, dass man dafür nur 21 Tage braucht?"
        expected_debug = ['dass']
        expected_out = 0.07692307692307693
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_G_PRO_PRS(self):
        metric = "G_PRO_PRS"
        test_text = "Und stimmt es tatsächlich, dass man dafür nur 21 Tage braucht?"
        expected_debug = ['es']
        expected_out = 0.07692307692307693
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_G_PRO_IND(self):
        metric = "G_PRO_IND"
        test_text = "Und stimmt es tatsächlich, dass man dafür nur 21 Tage braucht?"
        expected_debug = ['man']
        expected_out = 0.07692307692307693
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_G_PRO_PIS(self):
        metric = "G_PRO_PIS"
        test_text = "Und stimmt es tatsächlich, dass man dafür nur 21 Tage braucht?"
        expected_debug = ['man']
        expected_out = 0.07692307692307693
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_G_PRO_UNPERS(self):
        metric = "G_PRO_UNPERS"
        test_text = "Und stimmt es tatsächlich, dass man dafür nur 21 Tage braucht?"
        expected_debug = ['es']
        expected_out = 0.07692307692307693
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_G_PRO_ADV(self):
        metric = "G_PRO_ADV"
        test_text = "Und stimmt es tatsächlich, dass man dafür nur 21 Tage braucht?"
        expected_debug = ['dafür']
        expected_out = 0.07692307692307693
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_G_PART(self):
        metric = "G_PART"
        test_text = "Die Macht der Gewohnheit...ist nicht per se etwas Schlechtes"
        expected_debug = ['nicht']
        expected_out = 0.09090909090909091
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_G_PRO_PIAT(self):
        metric = "G_PRO_PIAT"
        test_text = "Die Macht der Gewohnheit...ist nicht per se etwas Schlechtes"
        expected_debug = ['etwas']
        expected_out = 0.09090909090909091
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_G_OTHER(self):
        metric = "G_OTHER"
        test_text = "Die Macht der Gewohnheit...ist nicht per se etwas Schlechtes"
        expected_debug = ['se']
        expected_out = 0.09090909090909091
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_G_PRO_POS(self):
        metric = "G_PRO_POS"
        test_text = "Wie viele von unseren täglichen Handlungen von Gewohnheiten beeinflusst werden, lässt sich nur schwer schätzen, weil das individuell unterschiedlich ist."
        expected_debug = ['unseren']
        expected_out = 0.043478260869565216
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_G_PRO_REFL(self):
        metric = "G_PRO_REFL"
        test_text = "Wie viele von unseren täglichen Handlungen von Gewohnheiten beeinflusst werden, lässt sich nur schwer schätzen, weil das individuell unterschiedlich ist."
        expected_debug = ['sich']
        expected_out = 0.043478260869565216
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_G_PRO_REL(self):
        metric = "G_PRO_REL"
        test_text = "Der Professor für Sozialpsychologie Bas Verplanken, der sich seit über 20 Jahren mit dem Einfluss von Angewohnheiten auf unser Leben und Wesen beschäftigt, geht allerdings von rund 30 bis 50 Prozent aus."
        expected_debug = ['der']
        expected_out = 0.02857142857142857
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_G_ART_IND(self):
        metric = "G_ART_IND"
        test_text = "Gewohnheiten haben meist einen schlechten Ruf – assoziieren wir sie doch sofort mit negativen Dingen wie Junkfood, Rauchen oder zu wenig Bewegung."
        expected_debug = ['einen']
        expected_out = 0.041666666666666664
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_G_VMOD(self):
        metric = "G_VMOD"
        test_text = "Denn unser Gehirn wäre maßlos überfordert, wenn es jede kleine Handlung bewusst steuern müsste."
        expected_debug = ['müsste']
        expected_out = 0.0625
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_G_INTJ(self):
        metric = "G_INTJ"
        test_text = "x"
        expected_debug = [] # TODO
        expected_out = 0
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
            
    
    def test_G_PRO_REZ(self):
        metric = "G_PRO_REZ"
        test_text = "x"
        expected_debug = [] # TODO
        expected_out = 0
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
            
    


if __name__ == "__main__":
    unittest.main()
