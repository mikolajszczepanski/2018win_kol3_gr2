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

    def test_init_limit_rate_abs_not_none(self):
        p = Plane(20)
        self.assertTrue(p.limit_rate_abs != None)

    def test_init_limit_rate_abs_throws_when_none(self):
        with self.assertRaises(TypeError):
            p = Plane(None)

    def test_set_angle_less_than_limit(self):
        p = Plane(10)
        p.set_angle(5)
        self.assertEqual(p.angle, 5)

    def test_set_angle_greater_than_limit(self):
        p = Plane(10)
        p.set_angle(15)
        self.assertNotEqual(p.angle, 15)

    def test_str(self):
        p = Plane(5)
        s = str(p)
        self.assertTrue(isinstance(s, str))

    def test_angle_is_float(self):
        p = Plane(5)
        self.assertTrue(isinstance(p.angle, float))

    def test_limit_is_float(self):
        p = Plane(5.2)
        self.assertTrue(isinstance(p.limit_rate_abs, float))

    def test_limit_is_int(self):
        p = Plane(5)
        self.assertTrue(isinstance(p.limit_rate_abs, int))
        

if __name__ == '__main__':
    unittest.main()

