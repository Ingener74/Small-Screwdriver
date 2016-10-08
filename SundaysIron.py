# encoding: utf8
# Sunday's Iron
import re
import time

from PySide.QtCore import QDir, QDirIterator

from SundaysIron import ProgressBar
from termcolor import cprint
from click import command, option
from SmallScrewdriver import (BinPacking, BinPackingProgress, FirstFitShelfBinPacking, NextFitShelfBinPacking,
                              GuillotineBinPacking, MaxRectsBinPacking, Size, Image)

METHODS = (
    {
        'name': 'next_fit_shelf',
        'type': NextFitShelfBinPacking
    }, {
        'name': 'first_fit_shelf',
        'type': FirstFitShelfBinPacking
    }, {
        'name': 'guillotine',
        'type': GuillotineBinPacking
    }, {
        'name': 'max_rects',
        'type': MaxRectsBinPacking
    }
)

prepare_progress = ProgressBar("Prepare : ", max_value=80)
pack_progress = ProgressBar("Packing : ", max_value=80)
verify_progress = ProgressBar("Verify  : ", max_value=80)
saving_progress = ProgressBar("Saving  : ", max_value=80)

class MyBinPackingProgress(BinPackingProgress):
    def packing_progress(self, percent):
        pack_progress.update(progress=percent)

    def verify_progress(self, percent):
        pack_progress.end()
        verify_progress.update(progress=percent)

    def saving_progress(self, percent):
        verify_progress.end()
        saving_progress.update(progress=percent)


@command()
@option('--directory', default='.', help='working directory')
@option('--quiet', default=False, help='pack atlases quietly')
@option('--algorithm', default='MaxRects', help='NextFitShelf, FirstFitShelf, Guillotine, MaxRects(default)')
@option('--size', default='2048x2048', help='256x256, 512x512, 1024x1024, 2048x2048, 4096x4096, 8192x8192')
def pack(directory, quiet, algorithm, size):
    cprint('working directory {}'.format(directory), color='green')
    cprint('quiet {}'.format(quiet), color='green')
    cprint('algorithm {}'.format(algorithm), color='green')
    cprint('size {}'.format(size))

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

    BinPacking.bin_packing_progress = MyBinPackingProgress()

    bin_packer = FirstFitShelfBinPacking(Size(2048, 2048), images, bin_parameters={})
    bin_packer.saveAtlases(directory)

    print ''


if __name__ == '__main__':

    cprint("Sunday's Iron command line texture packing tool", 'yellow')
    pack()
