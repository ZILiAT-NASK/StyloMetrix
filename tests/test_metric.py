import unittest

from .test_en.test_detailed_grammar import TestDetailedGrammarEN
from .test_en.test_detailed_lexical import TestDetailedLexicalEN
from .test_en.test_grammar import TestGrammarEN
from .test_en.test_hurtlex import TestHurtlexEN
from .test_en.test_lexical_en import TestLexicalEN
from .test_en.test_pos import TestPosEN
from .test_en.test_syntax import TestSyntaxEN
from .test_en.test_text_stat import TestTextStatEN
from .test_ru.test_grammar import TestGrammarRU
from .test_ru.test_lexical import TestLexicalRU
from .test_ru.test_pos import TestPosRU
from .test_ru.test_syntactic import TestSyntacticRU
from .test_ukr.test_grammar import TestGrammarUKR
from .test_ukr.test_lexical import TestLexicalUKR
from .test_ukr.test_pos import TestPosUKR
from .test_ukr.test_syntactic import TestSyntacticUKR
from .test_ukr.test_text_stat import TestReadabilityUKR


def suite():
    test_suite = unittest.TestSuite()

    test_list_en = [
        TestDetailedGrammarEN,
        TestDetailedLexicalEN,
        TestGrammarEN,
        TestHurtlexEN,
        TestLexicalEN,
        TestPosEN,
        TestSyntaxEN,
        TestTextStatEN,
    ]

    test_list_ru = [TestGrammarRU, TestLexicalRU, TestPosRU, TestSyntacticRU]

    test_list_ukr = [
        TestGrammarUKR,
        TestLexicalUKR,
        TestPosUKR,
        TestSyntacticUKR,
        TestReadabilityUKR,
    ]

    test_list = test_list_en + test_list_ru + test_list_ukr

    for test in test_list:
        test_suite.addTest(unittest.makeSuite(test))

    return test_suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    test_suite = suite()
    result = runner.run(test_suite)
    if int(not result.wasSuccessful()):
        raise Exception("Tests failed")
