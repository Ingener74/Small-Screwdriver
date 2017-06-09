# encoding: utf8

import sys
import argparse

from SmallScrewdriver import (BinPackingProgress, SmallScrewdriver)


class MyBinPackingProgress(BinPackingProgress):
    def prepare_progress(self, progress_in_percent):
        pass

    def packing_progress(self, percent):
        pass

    def verify_progress(self, percent):
        pass

    def saving_progress(self, percent):
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sunday's Iron arguments")
    parser.add_argument("-i", "--input_directory",
                        default=".",
                        nargs="+")
    parser.add_argument('-o', "--output_directory",
                        default=".",
                        nargs="+")
    parser.add_argument("-S", "--max_size",
                        default=3,
                        help="0 - 256x256, 1 - 512x512, 2 - 1024x1024, 3 - 2048x2048(default), "
                             "4 - 4096x4096, 5 - 8192x8192, 6 - 16384, 16384")
    parser.add_argument("-e", "--exporter",
                        default=1,
                        help="0 - Jupiter exporter or 1 - Plist(default)")
    parser.add_argument("-a", "--algorithm",
                        default=2,
                        help="0 - NextShelfFit, 1 - FirstShelfFit, 2 - Guillotine(default), 3 - MaxRects")

    args = parser.parse_args()

    try:
        for input_dir, output_dir in zip(args.input_directory, args.output_directory):
            SmallScrewdriver.pack_directory(
                input_dir,
                output_dir,
                args.exporter,
                args.max_size,
                args.algorithm,
                [],
                MyBinPackingProgress()
            )

    except RuntimeError as e:
        print e.message
