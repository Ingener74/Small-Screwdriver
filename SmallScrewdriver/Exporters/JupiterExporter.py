# coding=utf-8
import json
from Exporter import Exporter


class JupiterExporter(Exporter):
    def __init__(self):
        Exporter.__init__(self)

    def export(self, bin_name, bin_size, images):
        # Собираем json файл для контейнера
        json_images = []
        for i in images:
            json_images.append(i.toJson())

        # Сохраняем json файл для контейнера
        with open(bin_name + '.json', mode='w') as outfile:
            json.dump(obj=json_images, fp=outfile, separators=(',', ':'), indent=4)
