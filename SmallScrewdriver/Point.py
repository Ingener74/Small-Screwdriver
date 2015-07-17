# encoding: utf8


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '{}{}'.format(self.__class__.__name__, {key: str(value) for key, value in self.__dict__.iteritems()})