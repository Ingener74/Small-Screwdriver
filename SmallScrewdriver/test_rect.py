from unittest import TestCase, expectedFailure
from SmallScrewdriver import Rect, Size, Point

__author__ = 'Pavel'


class TestRect(TestCase):
    def test_area(self):
        r = Rect(Point(0, 0), Size(10, 10))
        self.assertEqual(r.area(), 100)

        r = Rect(Point(10, 10), Size(20, 20))
        self.assertEqual(r.area(), 400)

        r = Rect(Point(20, 20), Size(50, 50))
        self.assertEqual(r.area(), 2500)

        r = Rect(Point(100, 100), Size(200, 300))
        self.assertEqual(r.area(), 60000)

    def test_eq(self):
        r1 = Rect(Point(0, 0), Size(10, 10))
        r2 = Rect(Point(10, 10), Size(20, 20))
        r3 = Rect(Point(20, 20), Size(50, 50))
        r4 = Rect(Point(100, 100), Size(200, 300))
        r5 = Rect(Point(0, 0), Size(10, 10))

        self.assertEqual(r1, r5)
        self.assertNotEqual(r1, r2)
        self.assertNotEqual(r1, r3)
        self.assertNotEqual(r1, r4)

        self.assertNotEqual(r2, r3)
        self.assertNotEqual(r2, r4)
        self.assertNotEqual(r2, r5)

        self.assertNotEqual(r3, r4)
        self.assertNotEqual(r3, r5)

        self.assertNotEqual(r4, r5)

    @expectedFailure
    def test_split(self):

        r1 = Rect(Point(), Size(256, 256))
        r2 = Rect(Point(), Size(10, 10))
        r3 = Rect(Point(), Size(256, 256))

        split, r11, r12 = r1.split(r2)
        self.assertTrue(split)

        self.assertFalse(r1.split(r3.size))