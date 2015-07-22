# encoding: utf8
from PIL import Image
from Rect import Rect

class Image(Rect):
    def __init__(self, filename):
        self.filename = filename

        self.image = Image.open(self.filename)

        self.crop_region = Rect(self.origin, self.size)

    def __str__(self):
        print '{}({}, {})'.format(self.__class__.__name__, self.filename, self.image)

    def __repr__(self):
        return self.__str__()
