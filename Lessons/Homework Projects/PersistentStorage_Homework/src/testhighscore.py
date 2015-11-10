
import highscore
import glob
import os
import unittest

class testHighScore(unittest.TestCase):

    def test_many_scores(self):
        HighScore = highscore.scoreTable
        self.assertEqual(50, HighScore('player1', 50))
        self.assertEqual(150, HighScore('player1', 150))
        self.assertEqual(150, HighScore('player1', 40))
        self.assertEqual(150, HighScore('player1', 95))
        #I'm not sure about the following line, shouldn't the function make that return value 180 not 150?
        self.assertTrue(HighScore('player1', 180) == 180, 'player1 should have 150 as a top score')
        
    def tearDown(self):
        for file in glob.glob("testshelf.shlf.*"):
            os.remove(file)

if __name__ == "__main__":
    unittest.main()
        