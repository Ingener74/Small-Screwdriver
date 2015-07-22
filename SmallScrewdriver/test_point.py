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

        assert p1 != p2
        assert p1 == p3
        assert p1 != p4
        assert p1 != p5
        assert p2 != p3
        assert p3 != p4
        assert p4 != p5

        assert p1 + p2 == Point(30, 30)
        assert p1 + p3 == Point(20, 20)
        assert p2 + p3 == Point(30, 30)


