from anagram import isAnagram
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(isAnagram("claimed", "decimal"), True)
    
    def test2(self):
        self.assertEqual(isAnagram("Heart", "Earth"), True)
    
    def test3(self):
        self.assertEqual(isAnagram("Race", "Care"), True)
    
    def test4(self):
        self.assertEqual(isAnagram("something", "Algo"), False)

if __name__ == '__main__':
    unittest.main()