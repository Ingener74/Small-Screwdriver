from unittest import TestCase
import math
from SmallScrewdriver import Bin, Size, Point, Rect

__author__ = 'Pavel'


class TestBin(TestCase):
    def test_append1(self):
        b = Bin(Size(256, 256), Point(0, 0))

        assert b.append(Rect(Point(0, 0), Size(10, 10)))
        assert len(b.rects) == 1

        assert b.append(Rect(Point(10, 10), Size(100, 100)))
        assert len(b.rects) == 2

        assert b.append(Rect(Point(10, 10), Size(100, 100)))
        assert len(b.rects) == 3

        assert b.append(Rect(Point(10, 10), Size(100, 100)))
        assert len(b.rects) == 4

        assert b.append(Rect(Point(10, 10), Size(100, 100)))
        assert len(b.rects) == 5

        assert b.append(Rect(Point(10, 10), Size(50, 50)))
        assert len(b.rects) == 6

        assert b.append(Rect(Point(10, 10), Size(50, 50)))
        assert len(b.rects) == 7

        assert b.append(Rect(Point(10, 10), Size(50, 50)))
        assert len(b.rects) == 8

        assert b.append(Rect(Point(10, 10), Size(50, 50)))
        assert len(b.rects) == 9

        assert b.append(Rect(Point(10, 10), Size(100, 100)))
        assert len(b.rects) == 10

        assert not b.append(Rect(Point(0, 0), Size(512, 512)))
        assert len(b.rects) == 10

    def test_fillLevel(self):
        b = Bin(Size(256, 256), Point(0, 0))

        b.append(Rect(Point(0, 0), Size(10, 10)))
        assert math.fabs(b.fillLevel() - (10. * 10.) / (256. * 256.)) < 1e-6

        b.append(Rect(Point(0, 0), Size(20, 20)))
        assert math.fabs(b.fillLevel() - (10. * 10. + 20. * 20.) / (256. * 256.)) < 1e-6

        b.append(Rect(Point(0, 0), Size(40, 40)))
        assert math.fabs(b.fillLevel() - (10. * 10. + 20. * 20. + 40. * 40.) / (256. * 256.)) < 1e-6
