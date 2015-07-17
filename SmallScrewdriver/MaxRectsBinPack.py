# encoding: utf8
import sys
from SmallScrewdriver import Rect, Point


"""
https://github.com/juj/RectangleBinPack
http://clb.demon.fi/
"""

# noinspection PyPep8Naming
class MaxRectsBinPack(object):

    RECT_BEST_SHORT_SIDE_FIT = 1
    RECT_BEST_LONG_SIDE_FIT = 2
    RECT_BEST_AREA_FIT = 3
    RECT_BOTTOM_LEFT_RULE = 4
    RECT_CONTACT_POINT_RULE = 5

    def __init__(self, width, height):
        self.bin_width = width
        self.bin_height = height

        used_rectangles = []
        free_rectangles = [Rect(Point(0, 0), self.bin_width, self.bin_height)]

    def insert(self, rects, heurictic):
        """
        Решает разложение прямоугольников
        :param rects: входные прямоугольники
        :param heurictic: евристика для решения
        :return: Вернёт разложенные прямоугольники
        """
        result = []

        while len(rects):

            bestScore1 = sys.maxint
            bestScore2 = sys.maxint


            for rect in rects:
                newRect, score1, score2 = self._scoreRect(rect.width, rect.height, heurictic)

                if score1 < bestScore1 or (score1 == bestScore1 and score2 < bestScore2):
                    bestScore1 = score1
                    bestScore2 = score2
                    bestNode = newRect

            if bestNode is None:
                return

            self._placeRect(bestNode)
            rects.remove(newRect)

        return result

    def Occupancy(self):
        """
        Считает отношение занятой площади к полной
        :return:отношение площадей
        """
        pass

    def _scoreRect(self, width, height, heuristic):
        return Rect(Point(0, 0), 0, 0), 0, 0

    def _placeRect(self, node):
        pass

    def _contactPointScoreNode(self, x, y, width, height):
        return 0

    def _findPositionForNewNodeBottomLeft(self, width, height):
        return 0, 0

    def _findPositionForNewNodeBestShortSideFit(self, width, height):
        return 0, 0

    def _findPositionFowNewNodeBestLongSideFit(self, width, height):

        return 0, 0

    def _findPositionFowNewNodeBestAreaFit(self, width, height):
        return 0, 0

    def _findPositionForNewNodeBestContactPoint(self, width, height):
        return 0, 0

    def _splitFreeNode(self, free_node, used_node):
        pass

    def _pruneFreeList(self):
        pass

