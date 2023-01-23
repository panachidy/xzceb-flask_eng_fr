import unittest

from translator import english_to_french, french_to_english

class TestFrenchToEnglish(unittest.TestCase):
    "This class contains the test function for testing the fr-eng translation"
    def test_english_to_french(self):
        "This is test for eng-fr"
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        
    def test_null_english_to_french(self):
        "This is going to test for null input, i.e when there is no word entered."
        self.assertNotEqual(english_to_french("Hello"), "")
   
class Testenglish_to_french(unittest.TestCase):
    "This class contains the test function for testing the eng-fr translation"
    def test_french_to_english(self):
        "This is test for fr-eng"
        self.assertEqual(french_to_english("Bonjour"), "Hello")
    def test_null_french_to_english(self):
        "This is going to test for null input, i.e when there is no word entered."
        self.assertNotEqual(french_to_english("Bonjour"), "")   

if __name__ =='__main__':
         unittest.main()