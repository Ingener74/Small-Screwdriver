# encoding: utf8
from SmallScrewdriver.Size import Size


class Bin(object):
    def __init__(self, size=Size(256, 256)):
        self.size = size
        self.rects = []

    def append(self, rect):
        area = rect.area()
        for rect in self.rects:
            area += rect.area()

        if area <= self.size.area():
            self.rects.append(rect)
            return True
        else:
            return False

    def __str__(self):
        return ''
