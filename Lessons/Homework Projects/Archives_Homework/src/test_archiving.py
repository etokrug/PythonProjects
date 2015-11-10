import unittest
import archiving
import os
import shutil

class TestArchiving(unittest.TestCase):
    
    def setUp(self):
        self.home = os.getcwd()
        self.path = r"v:\\workspace\\archiving_test"
        os.mkdir(self.path)
        self.parent = os.path.split(self.path)[-1]
        self.zip_fn = os.path.join(self.path, "zarchiver.zip")
        os.chdir(self.path)
        self.file_names = ["archiving_test/groucho.txt", "archiving_test/harpo.txt", "archiving_test/chico.txt"]
        for fn in self.file_names:
            f = open(os.path.join(self.path, os.path.basename(fn)), "w")
            f.close()
    
    def test_zarchive(self):
        observed = archiving.zarchive(self.zip_fn, self.path)
        expected = set(self.file_names)
        self.assertEqual(observed, expected)
    
    def tearDown(self):
        os.remove(self.zip_fn)
        os.chdir(self.home)
        try:
            shutil.rmtree(self.path, ignore_errors=True)
        except IOError:
            pass
        os.chdir(self.home)

if __name__ == "__main__":
    unittest.main()