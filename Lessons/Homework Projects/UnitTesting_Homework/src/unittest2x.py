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
    
    def test_caps(self):
        for s in ["some string", "SomE sTRiNG", "SOME STRING"]:
            self.assertEqual(title(s), str.title(s), "Improper distribution of Capitals")

if __name__ == "__main__":
    unittest.main()