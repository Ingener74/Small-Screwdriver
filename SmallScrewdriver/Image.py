# encoding: utf8

class Image(object):
    def __init__(self, filename):
        self.filename = filename

        self.size = None
        self.rect = None

    def __str__(self):
        print '{}({})'.format(self.__class__.__name__, self.filename)

    def __repr__(self):
        return self.__str__()
