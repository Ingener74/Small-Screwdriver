# encoding: utf8


class Size(object):
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.width == other.width and self.height == other.height

    def __ne__(self, other):
        return self.width != other.width or self.height != other.height

    def __lt__(self, other):
        return self.width < other.width and self.height < other.height

    def __le__(self, other):
        return self.width <= other.width and self.height <= other.height

    def __gt__(self, other):
        return self.width > other.width and self.height > other.height

    def __ge__(self, other):
        return self.width >= other.width and self.height >= other.height

    def __str__(self):
        return '{}({}, {})'.format(self.__class__.__name__, self.width, self.height)

    def __repr__(self):
        return self.__str__()
