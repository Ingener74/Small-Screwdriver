# from SmallScrewdriver.Size import (Size)
# from SmallScrewdriver.Rect import (Rect)
# from SmallScrewdriver.Exporters import (PListExporter, JupiterExporter)
# from SmallScrewdriver.Shelf import (NextFitShelfBinPacking, FirstFitShelfBinPacking, FirstFitShelfBin)
# from SmallScrewdriver.Guillotine import (GuillotineBinPacking, GuillotineBin)
# from SmallScrewdriver.MaxRects import (MaxRectsBinPacking)
#
#
# class SmallScrewdriver(object):
#     Sizes = (
#         Size(256, 256),
#         Size(512, 512),
#         Size(1024, 1024),
#         Size(2048, 2048),
#         Size(4096, 4096),
#         Size(8192, 8192),
#         Size(16384, 16384),
#     )
#
#     Exporters = (
#         JupiterExporter,
#         PListExporter
#     )
#
#     Methods = (
#         NextFitShelfBinPacking,
#         FirstFitShelfBinPacking,
#         GuillotineBinPacking,
#         MaxRectsBinPacking
#     )
#
#     BinParameter = {
#         'next_fit_shelf': {
#         },
#         'first_fit_shelf': {
#             'selection_variant': FirstFitShelfBin.BEST_VARIANTS,
#             'selection_heuristic': FirstFitShelfBin.SHORT_SIDE_FIT,
#         },
#         'guillotine': {
#             'selection_variant': GuillotineBin.BEST_VARIANTS,
#             'selection_heuristic': GuillotineBin.SHORT_SIDE_FIT,
#             'split_rule': Rect.RULE_SAS
#         },
#         'max_rects': {
#         }
#     }
#
#     def __init__(self):
#         pass
#
#     def pack_images(self, images, output_directory):
#         pass
#
#     def pack_directory(self, input_directory, output_directory):
#         pass
