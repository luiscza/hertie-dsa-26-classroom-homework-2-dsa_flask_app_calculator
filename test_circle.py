import math
import unittest
 
from circle import make_circle
 
 
class TestCircle(unittest.TestCase):
 
    def test_perimeter(self):
        result = make_circle(5, 'perimeter')
        self.assertAlmostEqual(result, 2 * 5 * math.pi)
 
    def test_area(self):
        result = make_circle(5, 'area')
        self.assertAlmostEqual(result, math.pi * 25)
 
 
if __name__ == '__main__':
    unittest.main()