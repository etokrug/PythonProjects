""" My very own unittest file"""
import unittest

def title(s):
    '''puts in title case'''
    return  s[0].upper()+s[1:]

class TestTitle(unittest.TestCase):
    
    def no_caps(self):
        self.assertEqual(title("some string"), "Some String", "Improper distribution of Capitals")
    
    def all_caps(self): 
        self.assertEqual(title("SOME STRING"), "Some String", "Improper distribution of capitals")

if __name__ == "__main__":
    unittest.main()