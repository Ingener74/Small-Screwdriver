# coding: utf-8
from SmallScrewdriver import Bin, DEFAULT_BIN_SIZE, Point, Rect


class MaxRectsBin(Bin):
    """
    Контейнер для метода максимальных прямоугольников
    """

    # Эвристики выбора
    HEURISTIC_BL = 0
    HEURISTIC_BAF = 1
    HEURISTIC_BSSF = 2
    HEURISTIC_BLSF = 3

    def __init__(self, size=DEFAULT_BIN_SIZE, origin=Point(), bin_parameters=None):
        Bin.__init__(self, size=size, origin=origin, bin_parameters=bin_parameters)

        self.free_rect = [Rect(size=self.size)]

    def addImage(self, image):
        return False
