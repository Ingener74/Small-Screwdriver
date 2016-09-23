import plistlib
from Exporter import Exporter


class PListExporter(Exporter):
    def __init__(self):
        Exporter.__init__(self)

    def export(self, bin_name, bin_size, images):
        json_images = {}
        for i in images:
            image_dict = i.toJson()

            json_images[image_dict['filename']] = {
                'aliases': [],
                'spriteOffset': '{0, 0}',
                'spriteSize': '{' + str(image_dict['crop']['size']['width']) + ',' + str(image_dict['crop']['size']['height']) + '}',
                'spriteSourceSize': '{' + str(image_dict['original_size']['width']) + ',' + str(image_dict['original_size']['height']) + '}',
                'textureRect': '{{' + str(image_dict['offset']['x']) + ',' + str(image_dict['offset']['x']) + '},{' +
                               str(image_dict['crop']['size']['width']) + ',' + str(image_dict['crop']['size']['height']) + '}}',
                'textureRotated': image_dict['rotated']
            }

        frames = {
            'frames': json_images,
            'metadata': {
                'format': 3,
                'pixelFormat': 'RGBA8888',
                'premultiplyAlpha': False,
                'realTextureFileName': bin_name + '.png',
                'size': '{' + str(bin_size.width) + ',' + str(bin_size.height) + '}',
                'smartupdate': '',
                'textureFileName': bin_name + '.png'
            }
        }

        plistlib.writePlist(frames, bin_name + '.plist')
