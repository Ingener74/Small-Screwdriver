# coding=utf-8
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
        r1 = Rect(Point(10, 10), Size(512, 512))
        r2 = Rect(Point(), Size(110, 70))
        r3 = Rect(Point(), Size(70, 90))
        r4 = Rect(Point(), Size(90, 50))
        r5 = Rect(Point(), Size(50, 70))

        # test SAS
        s, rs1, rs2 = r1.split(r2, Rect.RULE_SAS)
        self.assertTrue(s)
        # Верхний большой
        self.assertEqual(rs1, Rect(Point(r1.origin.x, r1.origin.y + r2.size.height),
                                   Size(r2.size.width, r1.size.height - r2.size.height)))

        # Левый маленький
        self.assertEqual(rs2, Rect(Point(r1.origin.x + r2.size.width, r1.origin.y),
                                   Size(r1.size.width - r2.size.width, r1.size.height)))

        s, rs3, rs4 = rs2.split(r3)
        self.assertTrue(s)
        self.assertEqual(rs3, Rect(Point(rs1), Size()))
        self.assertEqual(rs4, Rect(Point(), Size()))

        # test LAS
        r3 = Rect(Point(), Size(256, 256))
        s, rs1, rs2 = r1.split(r3.size, Rect.RULE_LAS)
        self.assertFalse(s)
