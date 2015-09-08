# encoding: utf8
from SmallScrewdriver import Bin, Size, Point, DEFAULT_BIN_SIZE
from SmallScrewdriver.Shelf import Shelf


class BinFirstFitShelf(Bin):
    def __init__(self, size=DEFAULT_BIN_SIZE, origin=Point()):
        Bin.__init__(self, size=size, origin=origin)

        self.shelfs = [Shelf(self.size)]

    def addImage(self, image):

        # Проходим по каждой полке ...
        for shelf in self.shelfs:

            # ... и пробуем добавить изображение ...
            if shelf.addImage(image):

                # ... если получается добавляем изображение в контейнер ...
                return Bin.addImage(self, image)
        else:
            shelf = self.shelfs[-1]

            # Если не в одну полку изображение не вошло ...
            max_size = Size(self.size.width, self.size.height - (shelf.origin.y + shelf.size.height))

            # ... создаём новую полку ...
            shelf = Shelf(max_size, Point(0, shelf.origin.y + shelf.size.height))

            # ... добавляем её к полками ...
            self.shelfs.append(shelf)

            # ... добавляем изображение в контейнер если изображение входит в эту полку в противном случае, оно не
            # входит в контейнер
            return Bin.addImage(self, image) if shelf.addImage(image) else False
