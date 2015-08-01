from unittest import TestCase
from SmallScrewdriver import Size

__author__ = 'Pavel'


class TestSize(TestCase):
    def test_area(self):
        size = Size(100, 100)
        assert size.area() == 10000

        size = Size(10, 10)
        assert size.area() == 100

        size = Size(20, 20)
        assert size.area() == 400

    def test_eq(self):
        s1 = Size(10, 10)
        s2 = Size(20, 20)
        s3 = Size(10, 20)
        s4 = Size(10, 10)

        assert s1 == s4
        assert s1 != s2
        assert s1 != s3

        assert s2 != s3
        assert s2 != s4

        assert s3 != s4

        assert s1 < s2
        assert s4 < s2
        assert not s1 < s3

        assert s2 > s1
        assert s2 > s4
        assert not s3 > s1

        assert s1 <= s4
        assert s1 <= s2
        assert s1 <= s3

        assert s2 >= s1
        assert s1 >= s4
        assert s3 >= s1
