import unittest

from .test_en.test_detailed_grammar import TestDetailedGrammar
from .test_en.test_detailed_lexical import TestDetailedLexical
from .test_en.test_grammar import TestGrammar
from .test_en.test_hurtlex import TestHurtlex
from .test_en.test_lexical_en import TestLexicalEN
from .test_en.test_pos import TestPos
from .test_en.test_syntax import TestSyntax
from .test_en.test_text_stat import TestTextStat


def suite():
    test_suite = unittest.TestSuite()

    test_list_en = [
        TestDetailedGrammar,
        TestDetailedLexical,
        TestGrammar,
        TestHurtlex,
        TestLexicalEN,
        TestPos,
        TestSyntax,
        TestTextStat,
    ]

    for test in test_list_en:
        test_suite.addTest(unittest.makeSuite(test))

    return test_suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    test_suite = suite()
    result = runner.run(test_suite)
    if int(not result.wasSuccessful()):
        raise Exception("Tests failed")
