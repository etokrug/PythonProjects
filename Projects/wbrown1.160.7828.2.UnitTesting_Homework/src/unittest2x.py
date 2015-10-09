""" My very own unittest file"""
import unittest

def title(s):
    '''puts in title case'''
    new_str = ""
    cnt = 0
    for word in s.strip().split(' '):
        word = word[0].upper() + word[1:].lower()
        if cnt >= 1:
            new_str = new_str + ' ' + word
        else:
            new_str = new_str + word
        cnt += 1
    return new_str

class TestTitle(unittest.TestCase):
    
    def test_no_caps(self):
        self.assertEqual(title("some string"), "Some String", "Improper distribution of Capitals")
    
    def test_all_caps(self): 
        self.assertEqual(title("SOME STRING"), "Some String", "Incorrect lower casting")
        
if __name__ == "__main__":
    unittest.main()