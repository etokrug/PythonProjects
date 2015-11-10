import unittest
import os
import lookin
import shutil



class TestLookinDir(unittest.TestCase):
    """Tests to verify proper directory and names"""

    def setUp(self):
        os.mkdir(r"v:\tmpz") #Creates tmpz dir
        f_path = r'v:\tmpz'
        for i in range(1, 4):
            f = open(f_path + '\\test' + str(i) + '.txt', 'w')
            f.close()
        for i in range(1, 5):
            f = open(f_path + '\\test' + str(i) + '.doc', 'w')
            f.close()
        for i in range(1, 2):
            f = open(f_path + '\\test' + str(i) + '.bin', 'wb')
            f.close()
        os.chdir(r"v:\tmpz")
 
    def test_times(self):
        test_dct = {".txt": 3, ".doc": 4, ".bin": 1}
        self.assertEqual(test_dct, lookin.print_lst(), "Dicts are not equivalent")
    
    def tearDown(self):
        os.chdir("v:\\")
        shutil.rmtree("tmpz")

if __name__ == "__main__":
    unittest.main()
        
        
        