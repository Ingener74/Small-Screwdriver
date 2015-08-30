# encoding: utf8
from unittest import TestCase, expectedFailure
from SmallScrewdriver import Rect, Size, Point


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

    def test_split(self):

        r1 = Rect(Point(10, 10), Size(512, 512))
        r2 = Rect(Point(), Size(110, 75))
        r3 = Rect(Point(), Size(70, 95))
        r4 = Rect(Point(), Size(90, 55))
        r5 = Rect(Point(), Size(50, 75))

        r6 = Rect(Point(), Size(110, 50))
        r7 = Rect(Point(), Size(70, 75))

        # Плохие примеры
        r8 = Rect(Point(), Size(512, 512))
        s, rs1_, rs2_ = r1.split(r8, Rect.RULE_SAS)
        self.assertEqual(s, 0)
        self.assertEqual(rs1_, Rect())
        self.assertEqual(rs2_, Rect())

        r9 = Rect(Point(), Size(200, 70))
        s, rs1_, rs2_ = r2.split(r9, Rect.RULE_SAS)
        self.assertEqual(s, 0)
        self.assertEqual(rs1_, Rect())
        self.assertEqual(rs2_, Rect())

        r10 = Rect(Point(), Size(50, 80))
        s, rs1_, rs2_ = r2.split(r10, Rect.RULE_SAS)
        self.assertEqual(s, 0)
        self.assertEqual(rs1_, Rect())
        self.assertEqual(rs2_, Rect())

        # 1
        s, ro1, ro2 = r2.split(r6, Rect.RULE_SAS)
        self.assertEqual(s, 1)
        self.assertEqual(ro1, Rect(Point(r2.origin.x,
                                    r2.origin.y + r6.size.height),
                              Size(r2.size.width,
                                   r2.size.height - r6.size.height)))
        self.assertEqual(ro2, Rect())

        s, ro1, ro2 = r2.split(r7, Rect.RULE_SAS)
        self.assertEqual(s, 1)
        self.assertEqual(ro1, Rect(Point(r2.origin.x + r7.size.width,
                                         r2.origin.y),
                                   Size(r2.size.width - r7.size.width,
                                        r2.size.height)))
        self.assertEqual(ro2, Rect())

        # test SAS
        s, rs1, rs2 = r1.split(r2, Rect.RULE_SAS)
        self.assertEqual(s, 2)
        self.assertEqual(rs1, Rect(Point(r1.origin.x + r2.size.width,
                                         r1.origin.y),
                                   Size(r1.size.width - r2.size.width,
                                        r1.size.height)))

        self.assertEqual(rs2, Rect(Point(r1.origin.x,
                                         r1.origin.y + r2.size.height),
                                   Size(r2.size.width,
                                        r1.size.height - r2.size.height)))

        s, rs3, rs4 = rs1.split(r3, Rect.RULE_SAS)
        self.assertEqual(s, 2)
        self.assertEqual(rs3, Rect(Point(rs1.origin.x + r3.size.width,
                                         rs1.origin.y),
                                   Size(rs1.size.width - r3.size.width,
                                        r3.size.height)))

        self.assertEqual(rs4, Rect(Point(rs1.origin.x,
                                         rs1.origin.y + r3.size.height),
                                   Size(rs1.size.width,
                                        rs1.size.height - r3.size.height)))

        s, rs5, rs6 = rs3.split(r4, Rect.RULE_SAS)
        self.assertEqual(s, 2)
        self.assertEqual(rs5, Rect(Point(rs3.origin.x + r4.size.width,
                                         rs3.origin.y),
                                   Size(rs3.size.width - r4.size.width,
                                        rs3.size.height)))

        self.assertEqual(rs6, Rect(Point(rs3.origin.x,
                                         rs3.origin.y + r4.size.height),
                                   Size(r4.size.width,
                                        rs3.size.height - r4.size.height)))

        # # test LAS
        # r3 = Rect(Point(), Size(256, 256))
        # s, rs1, rs2 = r1.split(r3.size, Rect.RULE_LAS)
        # self.assertFalse(s)
