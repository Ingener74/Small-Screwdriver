# encoding: utf8
# Sunday's Iron
from PySide.QtCore import QDir, QDirIterator
import re

from termcolor import cprint
from click import command, option

from SmallScrewdriver import (FirstFitShelfBinPacking, Size, Image)


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
    cprint("Sunday's Iron command line texture packing tool", 'yellow')
    pack()
