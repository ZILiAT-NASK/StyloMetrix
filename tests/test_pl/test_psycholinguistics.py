import unittest

from src.stylo_metrix.stylo_metrix import StyloMetrix 


class TestPsycholinguisticsPL(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        lang = "pl"
        cls.sm = StyloMetrix(lang, debug=True)
        


    def test_PS_M_POSb(self):
        metric = "PS_M_POSb"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = ['Gospodarstwo']
        expected_out = 0.05
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_PS_M_NEGb(self):
        metric = "PS_M_NEGb"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = ['Gospodarstwo']
        expected_out = 0.05
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_PS_M_REFa(self):
        metric = "PS_M_REFa"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = ['Gospodarstwo']
        expected_out = 0.05
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_PS_M_AUTb(self):
        metric = "PS_M_AUTb"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = ['Gospodarstwo']
        expected_out = 0.05
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_PS_M_AROa(self):
        metric = "PS_M_AROa"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = ['Gospodarstwo']
        expected_out = 0.05
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_PS_M_SIGa(self):
        metric = "PS_M_SIGa"
        test_text = "Księga I. Gospodarstwo Księga ta rozpoczyna się inwokacją: “Litwo, Ojczyzno moja...”."
        expected_debug = ['Gospodarstwo']
        expected_out = 0.05
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_PS_M_POSa(self):
        metric = "PS_M_POSa"
        test_text = "Tadeusz po długiej nieobecności przybywa do rodzinnego domu."
        expected_debug = ['domu']
        expected_out = 0.1111111111111111
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_PS_M_REFb(self):
        metric = "PS_M_REFb"
        test_text = "Tadeusz po długiej nieobecności przybywa do rodzinnego domu."
        expected_debug = ['domu']
        expected_out = 0.1111111111111111
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_PS_M_AUTa(self):
        metric = "PS_M_AUTa"
        test_text = "Tadeusz po długiej nieobecności przybywa do rodzinnego domu."
        expected_debug = ['domu']
        expected_out = 0.1111111111111111
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_PS_M_AROb(self):
        metric = "PS_M_AROb"
        test_text = "Tadeusz po długiej nieobecności przybywa do rodzinnego domu."
        expected_debug = ['domu']
        expected_out = 0.1111111111111111
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_PS_M_NEGa(self):
        metric = "PS_M_NEGa"
        test_text = "Kieruje się do swego dawnego pokoju, ale ze zdziwieniem stwierdza, że komnata ta jest przez kogoś zamieszkiwana."
        expected_debug = ['zdziwieniem']
        expected_out = 0.05
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        
    def test_PS_M_SIGb(self):
        metric = "PS_M_SIGb"
        test_text = "Przez okno panicz dostrzega młodą dziewczynę, która podlewa w ogródku kwiaty."
        expected_debug = ['okno', 'kwiaty']
        expected_out = 0.15384615384615385
    
        out, debug = self.sm.transform([test_text])
        out = out[metric][0]
        debug = debug[metric][0]
    
        self.assertEqual(expected_out, out)
        self.assertSequenceEqual(expected_debug, debug)
    
                
        


if __name__ == "__main__":
    unittest.main()
