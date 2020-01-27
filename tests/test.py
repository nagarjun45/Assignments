import unittest
from unittest.mock import patch
from src.Q3 import sets
from src.Q4 import array
from src.Q10 import Reverselter
# from src.Q4 import array
from io import StringIO


class Test(unittest.TestCase):
    def setUp(self):
        pass
    def test_set(self):
        li= [12,24,35,24,88,120,155,88,120,155]
        expected = [12, 24, 35, 88, 120, 155]
        actual = sets(li)
        self.assertEqual(expected, actual)
    def test_squareMap(self):
        expected = [i*i for i in range(1, 21)]
        actual = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
        self.assertEqual(expected, actual)
    def test_array(self):
        expected = [[['0' for i in range(8)]for i in range(5)]for i in range(3)]
        actual = array()
        self.assertEqual(expected,actual)
    def test_reverse(self):
        lis = [1,2,3,4,5,6,7,8,9,10]
        expected = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        actual = Reverselter(lis)
        self.assertEqual(expected,actual)
    def tearDown(self):
        pass
