import os
import plistlib
from Exporter import Exporter


class PListExporter(Exporter):
    def __init__(self):
        Exporter.__init__(self)

    def export(self, bin_name, bin_size, images):
        json_images = {}
        for i in images:
            image_dict = i.toJson()

            ow = image_dict['original_size']['width']
            oh = image_dict['original_size']['height']

            tw = image_dict['crop']['size']['width']
            th = image_dict['crop']['size']['height']

            tx = image_dict['crop']['origin']['x']
            ty = image_dict['original_size']['height'] - (image_dict['crop']['origin']['y'] + image_dict['crop']['size']['height'])

            offset_x = (tx + tw / 2) - ow / 2
            offset_y = (ty + th / 2) - oh / 2

            json_images[image_dict['filename']] = {
                'aliases': [],
                'spriteOffset': '{' + str(offset_x) + ',' + str(offset_y) + '}',
                'spriteSize': '{' +
                              str(image_dict['crop']['size']['width']) + ',' +
                              str(image_dict['crop']['size']['height']) +
                              '}',
                'spriteSourceSize': '{' +
                                    str(image_dict['original_size']['width']) + ',' +
                                    str(image_dict['original_size']['height']) +
                                    '}',
                'textureRect': '{{' +
                               str(image_dict['offset']['x']) + ',' +
                               str(image_dict['offset']['y']) +
                               '},{' +
                               str(image_dict['crop']['size']['width']) + ',' +
                               str(image_dict['crop']['size']['height']) +
                               '}}',
                'textureRotated': image_dict['rotated']
            }

        bin_name_png = os.path.basename(bin_name + '.png')
        frames = {
            'frames': json_images,
            'metadata': {
                'format': 3,
                'pixelFormat': 'RGBA8888',
                'premultiplyAlpha': False,
                'realTextureFileName': bin_name_png,
                'size': '{' + str(bin_size.width) + ',' + str(bin_size.height) + '}',
                'textureFileName': bin_name_png
            }
        }

        plistlib.writePlist(frames, bin_name + '.plist')
