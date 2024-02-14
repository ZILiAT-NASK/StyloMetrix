import unittest

from src.stylo_metrix.stylo_metrix import StyloMetrix 


class TestPunctuationDE(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        lang = "de"
        cls.sm = StyloMetrix(lang, debug=True)
        


    def test_PUNCT_TOTAL(self):
        metric = "PUNCT_TOTAL"
        test_text = "Neue Gewohnheiten etablieren:"
        expected_debug = [':']
        expected_out = 0.25
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_PUNCT_BI_VERB(self):
        metric = "PUNCT_BI_VERB"
        test_text = "Neue Gewohnheiten etablieren:"
        expected_debug = ['etablieren:']
        expected_out = 0.5
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_PUNCT_BI_NOUN(self):
        metric = "PUNCT_BI_NOUN"
        test_text = "Gewohnheiten haben meist einen schlechten Ruf – assoziieren wir sie doch sofort mit negativen Dingen wie Junkfood, Rauchen oder zu wenig Bewegung."
        expected_debug = ['Ruf –', 'Junkfood,']
        expected_out = 0.16666666666666666
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        


if __name__ == "__main__":
    unittest.main()
