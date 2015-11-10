""" Demonstrates the unittest module in action."""
import unittest

def cube(x):
    '''Returns the cube of a passed value'''
    return x**3

class TestCube(unittest.TestCase):
    
    def test_small_number(self):
        self.assertEqual(cube(3), 27, "Cube of 3 is not 27")
        
    def test_large_number(self):
        self.assertEqual(cube(1000), 1000000000, "Cube of 1000 should be 1000000000")
        
    def test_bad_input(self):
        self.assertRaises(TypeError, cube, 'x')

if __name__ == "__main__":
    unittest.main()