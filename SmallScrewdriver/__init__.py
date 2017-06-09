# encoding: utf8
import re
from PySide.QtCore import (QDir, QDirIterator)
from Point import (Point)
from Rect import (Rect)
from Size import (Size)
from Bin import (Bin, DEFAULT_BIN_SIZE)
from Image import (Image)
from BinPacking import (BinPacking, BinPackingProgress)
from Shelf import (Shelf, FirstFitShelfBin, NextFitShelfBin, FirstFitShelfBinPacking, NextFitShelfBinPacking)
from Guillotine import (GuillotineBin, GuillotineBinPacking)
from MaxRects import (MaxRectsBin, MaxRectsBinPacking)
from Exporters import (Exporter, JupiterExporter, PListExporter)


class SmallScrewdriver(object):
    Sizes = (
        Size(256, 256),
        Size(512, 512),
        Size(1024, 1024),
        Size(2048, 2048),
        Size(4096, 4096),
        Size(8192, 8192),
        Size(16384, 16384),
    )

    Exporters = (
        JupiterExporter,
        PListExporter
    )

    # Algorithms
    NextShelf = 0
    FirstShelf = 1
    Guillotine = 2
    MaxRects = 3

    Algorithms = (
        NextFitShelfBinPacking,
        FirstFitShelfBinPacking,
        GuillotineBinPacking,
        MaxRectsBinPacking
    )

    @staticmethod
    def pack_images(images_filenames,
                    input_directory,
                    output_directory,
                    exporter,
                    max_bin_size,
                    algorithm,
                    algorithm_parameters,
                    progress):

        # TODO arguments asserts

        images = []
        for index, image in enumerate(images_filenames):
            images.append(Image(input_directory, image))
            progress.prepare_progress(int(100 * (index + 1) / float(len(images_filenames))))

        bin_packing = SmallScrewdriver.Algorithms[algorithm](SmallScrewdriver.Sizes[max_bin_size],
                                                             images,
                                                             [exporter] + algorithm_parameters,
                                                             progress)
        bin_packing.saveAtlases(output_directory + QDir.separator())
        return bin_packing.bins

    @staticmethod
    def pack_directory(input_directory,
                       output_directory,
                       exporter,
                       max_bin_size,
                       algorithm,
                       algorithm_parameters,
                       progress):

        image_filenames = []
        folder = QDir(input_directory)
        folder.setNameFilters(['*.png'])
        folder.setFilter(QDir.Files or QDir.NoDotAndDotDot)
        dit = QDirIterator(folder, flags=QDirIterator.Subdirectories, filters=QDir.Files)
        while dit.hasNext():
            im = folder.relativeFilePath(dit.next())
            if not re.search('atlas', im):
                image_filenames.append(im)

        SmallScrewdriver.pack_images(image_filenames, input_directory, output_directory, exporter, max_bin_size,
                                     algorithm, algorithm_parameters, progress)