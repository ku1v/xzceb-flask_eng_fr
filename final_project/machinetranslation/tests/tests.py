import unittest

from translator import frenchToEnglish, englishToFrench

class TestTranslator(unittest.TestCase):
    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertIsNone(frenchToEnglish(None))

    def test_englishToFranche(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertIsNone(englishToFrench(None))

if __name__ == '__main__':
    unittest.main()

