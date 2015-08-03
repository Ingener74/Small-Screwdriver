from unittest import TestCase
from SmallScrewdriver import Point

__author__ = 'Pavel'


class TestPoint(TestCase):
    def test_point(self):
        p1 = Point(10, 10)
        p2 = Point(20, 20)
        p3 = Point(10, 10)
        p4 = Point(10, 20)
        p5 = Point(20, 10)

        self.assertEqual(p1, p3)
        self.assertNotEqual(p1, p2)
        self.assertNotEqual(p1, p4)
        self.assertNotEqual(p1, p5)
        self.assertNotEqual(p2, p3)
        self.assertNotEqual(p3, p4)
        self.assertNotEqual(p4, p5)

        self.assertEqual(p1 + p2, Point(30, 30))
        self.assertEqual(p1 + p3, Point(20, 20))
        self.assertEqual(p2 + p3, Point(30, 30))
