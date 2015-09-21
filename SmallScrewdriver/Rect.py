# encoding: utf8

import random

from PySide.QtGui import QPen, QColor

from Size import Size
from Point import Point


# noinspection PyPep8Naming
class Rect(object):
    """
    Правила разделения ...
    """
    # ... для гильотины
    RULE_SAS = 0
    RULE_LAS = 1
    RULE_SLAS = 2
    RULE_LLAS = 3
    RULE_MAXAS = 4
    RULE_MINAS = 5

    # ... для максимальных прямоугольников
    RULE_PICK_BOTH = 6

    def __init__(self, *args, **kwargs):
        self.origin = args[0] if len(args) > 0 else kwargs['origin'] if 'origin' in kwargs else Point()
        self.size = args[1] if len(args) > 1 else kwargs['size'] if 'size' in kwargs else Size()
        self.pen = args[2] if len(args) > 2 else kwargs['pen'] if 'pen' in kwargs else QPen()

        if 'rect' in kwargs:
            self.origin, self.size, self.pen = kwargs['rect'].origin, kwargs['rect'].size, kwargs['rect'].pen

    def area(self):
        return self.size.area()

    def draw(self, painter, offset=Point()):
        painter.setPen(self.pen)
        color = QColor(self.pen.color())
        color.setAlpha(50)
        painter.setBrush(QColor(color))
        painter.drawRect(self.origin.x + offset.x, self.origin.y + offset.y, self.size.width, self.size.height)

    def split(self, rect, rule):
        """
        Разделить прямоугольник
        :param rect: разделяющий прямоугольник
        rule - правило для разделения
        :return: первое поле возвращает число прямоугольников после деления, возможны варианты: 0, 1 и 2
         второе поле возвращает первый прямоугольник
         третье поле возврящает второй прямоугольник
         четвёрное поле возврящает True если прямоугольник пришлось повернуть для того чтобы он влез,
         False если поворачивать не прилось
        """

        rect_r = Rect(rect.origin, rect.size.rotate(), rect.pen)

        less = rect.size.less(self.size)
        less_r = rect_r.size.less(self.size)

        equal = rect.size.equal(self.size)
        equal_r = rect_r.size.equal(self.size)

        # Случай когда разделяющий и разделяемый одинаковые
        if equal == (True, True) or equal_r == (True, True):
            return 0, Rect(), Rect(), False

        # Одна сторона одинаковая, другая меньше
        elif equal == (True, False) and less == (False, True):
            return self.__splitOne(rect, True, False)

        elif equal_r == (True, False) and less_r == (False, True):
            return self.__splitOne(rect_r, True, True)

        elif equal == (False, True) and less == (True, False):
            return self.__splitOne(rect, False, False)

        elif equal_r == (False, True) and less_r == (True, False):
            return self.__splitOne(rect_r, False, True)

        # Обе стороны меньше
        elif less == (True, True):
            return self.__splitTwoPickBoth(rect, False) if rule == self.RULE_PICK_BOTH else \
                self.__splitTwo(rect, rule, False)

        elif less_r == (True, True):
            return self.__splitTwoPickBoth(rect, True) if rule == self.RULE_PICK_BOTH else \
                self.__splitTwo(rect_r, rule, True)

        # Остальные случаи
        else:
            return 0, Rect(), Rect(), False

    def __splitOne(self, rect, horizontal, rotate):
        if horizontal:
            return 1, \
                   Rect(self.origin + Point(0, rect.size.height),
                        Size(self.size.width, self.size.height - rect.size.height)), \
                   Rect(), \
                   rotate
        else:
            return 1, \
                   Rect(self.origin + Point(rect.size.width, 0),
                        Size(self.size.width - rect.size.width, self.size.height)), \
                   Rect(), \
                   rotate

    def __splitTwo(self, rect, rule, rotate):
        x1 = 0
        x2 = 0
        if rule is Rect.RULE_SAS or rule is Rect.RULE_LAS:
            x1 = self.size.width
            x2 = self.size.height
        elif rule is Rect.RULE_SLAS or rule is Rect.RULE_LLAS:
            x1 = self.size.width - rect.size.width
            x2 = self.size.height - rect.size.height
        elif rule is Rect.RULE_MAXAS or rule is Rect.RULE_MINAS:

            # TODO здесь надо сделать по другому

            x1 = self.area()
            x2 = rect.area()

        less_rule = rule is Rect.RULE_SAS or rule is Rect.RULE_SLAS or rule is Rect.RULE_MINAS
        greater_rule = rule is Rect.RULE_LAS or rule is Rect.RULE_LLAS or rule is Rect.RULE_MAXAS

        if (less_rule and x1 < x2) or (greater_rule and x1 >= x2):
            # Делим горизонтально
            r1 = Rect(self.origin + Point(rect.size.width, 0),
                      Size(self.size.width - rect.size.width, rect.size.height))

            r2 = Rect(self.origin + Point(0, rect.size.height),
                      Size(self.size.width, self.size.height - rect.size.height))
        else:
            # Делим вертикально
            r1 = Rect(self.origin + Point(rect.size.width, 0),
                      Size(self.size.width - rect.size.width, self.size.height))

            r2 = Rect(self.origin + Point(0, rect.size.height),
                      Size(rect.size.width, self.size.height - rect.size.height))
        return 2, r1, r2, rotate

    def __splitTwoPickBoth(self, rect, rotate):
        h = self.size.height
        w = self.size.width
        rh = rect.size.height
        rw = rect.size.width

        r1 = Rect(self.origin + Point(rh, 0), Size(w - rh, h)) if rotate else \
            Rect(self.origin + Point(rw, 0), Size(w - rw, h))

        r2 = Rect(self.origin + Point(0, rw), Size(w, h - rw)) if rotate else \
            Rect(self.origin + Point(0, rh), Size(w, h - rh))

        return 2, r1, r2, rotate

    def intersection(self, rect):
        x1 = self.origin.x
        y1 = self.origin.y
        x2 = self.origin.x + self.size.width
        y2 = self.origin.y + self.size.height
        rx1 = rect.origin.x
        ry1 = rect.origin.y
        rx2 = rect.origin.x + rect.size.width
        ry2 = rect.origin.y + rect.size.height

        x1x2_min = min(x1, x2)
        x1x2_max = max(x1, x2)
        rx1rx2_min = min(rx1, rx2)
        rx1rx2_max = max(rx1, rx2)

        nx = 0
        nw = 0

        # if x1x2_max > rx1rx2_min:
        #     pass
        # elif x

        y1y2_min = min(y1, y2)
        y1y2_max = max(y1, y2)
        ry1ry2_min = min(ry1, ry2)
        ry1ry2_max = max(ry1, ry2)

        ny = 0
        nh = 0

        return Rect(Point(nx, ny), Size(nw, nh))

    def __eq__(self, other):
        return self.origin == other.origin and self.size == other.size

    def __ne__(self, other):
        return self.origin != other.origin or self.size != other.size

    def __str__(self):
        return '{}({}, {})'.format(self.__class__.__name__, str(self.origin), str(self.size))

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def random():
        pen = QPen()
        pen.setColor(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        point = Point(100. * random.random(), 100. * random.random())
        size = Size(5 + 100. * random.random(), 5 + 100. * random.random())
        return Rect(point, size, pen)

    def randomColor(self):
        self.pen.setColor(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
