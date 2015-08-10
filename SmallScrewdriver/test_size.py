# encoding: utf8

from unittest import TestCase
from SmallScrewdriver import Size


class TestSize(TestCase):
    def test_area(self):
        size = Size(100, 100)
        self.assertEqual(size.area(), 10000)

        size = Size(10, 10)
        self.assertEqual(size.area(), 100)

        size = Size(20, 20)
        self.assertEqual(size.area(), 400)

    def test_eq(self):
        # TODO надо больше тестов !!!!
        s1 = Size(10, 10)
        s2 = Size(20, 20)
        s3 = Size(10, 20)
        s4 = Size(10, 10)

        self.assertEqual(s1, s4)
        self.assertNotEquals(s1, s2)
        self.assertNotEqual(s1, s3)

    def test_ne(self):
        s1 = Size(10, 10)
        s2 = Size(20, 20)
        s3 = Size(10, 20)
        s4 = Size(10, 10)

        self.assertNotEquals(s1, s2)
        self.assertNotEqual(s1, s3)

        self.assertNotEqual(s2, s3)
        self.assertNotEqual(s2, s4)

        self.assertNotEqual(s3, s4)

    def test_lt(self):
        s1 = Size(8, 6)
        s2 = Size(20, 20)
        s3 = Size(7, 20)
        s4 = Size(11, 9)

        self.assertLess(s1, s2)
        self.assertLess(s4, s2)
        self.assertFalse(s3 < s2)
