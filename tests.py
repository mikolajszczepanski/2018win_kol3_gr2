#!/usr/bin/python3

#https://github.com/persja40/kol1_gr2


import unittest
from flight import Plane

class Tests(unittest.TestCase):

    def test_init_limit_rate_abs(self):
        p = Plane(10)
        self.assertEqual(p.limit_rate_abs, 10)

    def test_init_angle(self):
        p = Plane(10)
        self.assertTrue(p.angle != None)

if __name__ == '__main__':
    unittest.main()

