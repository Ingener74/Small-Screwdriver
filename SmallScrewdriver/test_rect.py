from unittest import TestCase
from SmallScrewdriver import Rect, Size, Point

__author__ = 'Pavel'


class TestRect(TestCase):
    def test_area(self):
        r = Rect(Point(0, 0), Size(10, 10))
        assert r.area() == 100

        r = Rect(Point(10, 10), Size(20, 20))
        assert r.area() == 400

        r = Rect(Point(20, 20), Size(50, 50))
        assert r.area() == 2500

        r = Rect(Point(100, 100), Size(200, 300))
        assert r.area() == 60000

    def test_eq(self):
        r1 = Rect(Point(0, 0), Size(10, 10))
        r2 = Rect(Point(10, 10), Size(20, 20))
        r3 = Rect(Point(20, 20), Size(50, 50))
        r4 = Rect(Point(100, 100), Size(200, 300))
        r5 = Rect(Point(0, 0), Size(10, 10))

        assert r1 != r2
        assert r1 != r3
        assert r1 != r4
        assert r1 == r5

        assert r2 != r3
        assert r2 != r4
        assert r2 != r5

        assert r3 != r4
        assert r3 != r5

        assert r4 != r5
