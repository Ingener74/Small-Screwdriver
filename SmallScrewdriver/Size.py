# encoding: utf8


class Size(object):
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return '{}({}, {})'.format(self.__class__.__name__, self.width, self.height)

    def __repr__(self):
        return self.__str__()
