# encoding: utf8
# Sunday's Iron
from PySide.QtCore import QDir, QDirIterator
import sys
import re
import time

from termcolor import cprint
from click import command, option

from SmallScrewdriver import (FirstFitShelfBinPacking, Size, Image)


# noinspection PyPep8Naming
def packProgress(progress, max_progress=40):
    for i in xrange(0, progress):
        percent = float(i) / progress
        hashes = '#' * int(round(percent * max_progress))
        spaces = ' ' * (max_progress - len(hashes))
        sys.stdout.write("\rPercent: [{0}] {1}%".format(hashes + spaces, int(round(percent * 100))))
        sys.stdout.flush()


# noinspection PyPep8Naming
def verifyProgress(progress):
    pass


# noinspection PyPep8Naming
def savingProgress(progress):
    pass


@command()
@option('--directory', default='.', help='working directory')
@option('--quiet', default=False, help='pack atlases quietly')
@option('--algorithm', default='MaxRects', help='NextFitShelf, FirstFitShelf, Guillotine, MaxRects(default)')
def pack(directory, quiet, algorithm):
    cprint('working directory {}'.format(directory), color='green')
    cprint('quiet {}'.format(quiet), color='green')
    cprint('algorithm {}'.format(algorithm), color='green')

    folder = QDir(path=directory)
    folder.setNameFilters(['*.png'])
    folder.setFilter(QDir.Files or QDir.NoDotAndDotDot)

    dit = QDirIterator(folder, flags=QDirIterator.Subdirectories, filters=QDir.Files)

    filenames = []

    while dit.hasNext():
        im = folder.relativeFilePath(dit.next())
        if not re.search('atlas', im):
            filenames.append(im)

    images = [Image(directory, filename) for filename in filenames]

    bin_packer = FirstFitShelfBinPacking(Size(2048, 2048), images)
    bin_packer.saveAtlases(directory)

if __name__ == '__main__':

    for i in xrange(0, 100):
        time.sleep(1)
        packProgress(i)

    # cprint("Sunday's Iron command line texture packing tool", 'yellow')
    # pack()
