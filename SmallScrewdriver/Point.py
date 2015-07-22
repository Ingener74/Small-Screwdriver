# encoding: utf8


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __str__(self):
        return '{}({}, {})'.format(self.__class__.__name__, self.x, self.y)

    def __repr__(self):
        return self.__str__()
