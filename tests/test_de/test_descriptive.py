import unittest

from src.stylo_metrix.stylo_metrix import StyloMetrix 


class TestDescriptiveDE(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        lang = "de"
        cls.sm = StyloMetrix(lang, debug=True)
        


    def test_DESC_PRON_VOC(self):
        metric = "DESC_PRON_VOC"
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
