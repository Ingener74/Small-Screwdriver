# encoding: utf8


class BinPacking(object):
    def __init__(self, bin_size):
        self.bins = []
        self.bin_size = bin_size

    def save_atlases(self, directory):
        for i, b in enumerate(self.bins):
            b.save(directory + '/atlas' + str(i))
