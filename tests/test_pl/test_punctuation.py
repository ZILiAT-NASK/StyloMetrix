import unittest

from src.stylo_metrix.stylo_metrix import StyloMetrix 


class TestPunctuationPL(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        lang = "pl"
        cls.sm = StyloMetrix(lang, debug=True)
        


    def test_PUNCT_TOTAL(self):
        metric = "PUNCT_TOTAL"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = ['.', ':', '“', ',', '.', '.', '.', '”', '.']
        expected_out = 0.45
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_PUNCT_BI_NOUN(self):
        metric = "PUNCT_BI_NOUN"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = ['inwokacją:']
        expected_out = 0.1
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_PUNCT_BI_VERB(self):
        metric = "PUNCT_BI_VERB"
        test_text = "Kieruje się do swego dawnego pokoju, ale ze zdziwieniem stwierdza, że komnata ta jest przez kogoś zamieszkiwana."
        expected_debug = ['stwierdza', ',']
        expected_out = 0.1
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        


if __name__ == "__main__":
    unittest.main()
