import unittest
from translator import englishToFrench, frenchToEnglish

class TestenglishToFrench(unittest.TestCase): 
    
    def test1(self): 
        self.assertEqual(englishToFrench('Hello'), 'Bonjour') # test when 'Hello'' is given as input the output is 'Bonjour'.
        self.assertEqual(englishToFrench(None), IOError)  # test when None is given as input the output is None.
        

class TestfrenchToEnglish(unittest.TestCase): 
   
    def test1(self): 
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello') # test when 'Bonjour' is given as input the output is 'Hello'
        self.assertEqual(frenchToEnglish(None), IOError) # test when None is given as input the output is None.

if __name__ == '__main__':
    unittest.main()
