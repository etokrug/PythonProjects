"""
Demonstration of setUp and tearDown.
The tests do not actually test anything = this is a demo.
"""
import unittest
import tempfile
import shutil
import glob
import os

class FileTest(unittest.TestCase):
    
    def setUp(self):
        self.origdir = os.getcwd()
        self.dirname = tempfile.mkdtemp("testdir")
        os.chdir(self.dirname)
    
    def test_1(self):
        "Verify creation of files is possible"
        actual_names = set({})
        valid_names = set({"this.txt", "that.txt", "the_other.txt"})
        for filename in valid_names:
            f = open(filename, "w")
            f.write("Some text\n")
            f.close()
            self.assertTrue(f.closed)
        for file in os.listdir('.'):
            actual_names.add(file)
        actual_names = sorted(actual_names)
        valid_names = sorted(valid_names)
        self.assertSameElements(valid_names, actual_names, "Elements are not the same")
            
        
    def test_2(self):
        "Verify that the current directory is empty"
        self.assertEqual(glob.glob("*"), [], "Directory not empy")
    
    def test_3(self):
        "Creates a 1,000,000 byte file then checks length"
        fb = open("size_test.bin", "wb")
        fb.write(b'\0' * 1000000)
        fb.close()
        fb_stat = os.stat("size_test.bin")
        self.assertEqual(fb_stat.st_size, 1000000, "Incorrect file size")
    
    def tearDown(self):
        os.chdir(self.origdir)
        shutil.rmtree(self.dirname)

if __name__ == "__main__":
    unittest.main()