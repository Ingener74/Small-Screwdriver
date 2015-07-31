from unittest import TestCase
import math
from SmallScrewdriver import Bin, Size, Point, Rect

__author__ = 'Pavel'


class TestBin(TestCase):
    def test_append1(self):
        b = Bin(Size(256, 256), Point(0, 0))

        assert b.append(Rect(Point(0, 0), Size(10, 10)))
        assert len(b.images) == 1
        # area = 100

        assert b.append(Rect(Point(10, 10), Size(100, 100)))
        assert len(b.images) == 2
        # area == 10100

        assert b.append(Rect(Point(10, 10), Size(100, 100)))
        assert len(b.images) == 3
        # area == 20100

        assert b.append(Rect(Point(10, 10), Size(100, 100)))
        assert len(b.images) == 4
        # area == 30100

        assert b.append(Rect(Point(10, 10), Size(100, 100)))
        assert len(b.images) == 5
        # area == 40100

        assert b.append(Rect(Point(10, 10), Size(50, 50)))
        assert len(b.images) == 6
        # area == 42600

        assert b.append(Rect(Point(10, 10), Size(50, 50)))
        assert len(b.images) == 7
        # area == 45100

        assert b.append(Rect(Point(10, 10), Size(50, 50)))
        assert len(b.images) == 8
        # area == 47600

        assert b.append(Rect(Point(10, 10), Size(50, 50)))
        assert len(b.images) == 9
        # area == 50100

        # assert b.append(Rect(Point(10, 10), Size(100, 100)))
        # assert len(b.images) == 10

        assert not b.append(Rect(Point(0, 0), Size(512, 512)))
        assert len(b.images) == 9

    def test_fillLevel(self):
        b = Bin(Size(256, 256), Point(0, 0))

        b.append(Rect(Point(0, 0), Size(10, 10)))
        assert math.fabs(b.fillLevel() - (10. * 10.) / (256. * 256.)) < 1e-6

        b.append(Rect(Point(0, 0), Size(20, 20)))
        assert math.fabs(b.fillLevel() - (10. * 10. + 20. * 20.) / (256. * 256.)) < 1e-6

        b.append(Rect(Point(0, 0), Size(40, 40)))
        assert math.fabs(b.fillLevel() - (10. * 10. + 20. * 20. + 40. * 40.) / (256. * 256.)) < 1e-6
