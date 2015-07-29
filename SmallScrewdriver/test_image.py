from unittest import TestCase
from SmallScrewdriver import BPImage, Rect, Size, Point


class TestImage(TestCase):
    def test_bg_image(self):
        image = BPImage('../resources/bg.png')

        assert image.size.width == 1024
        assert image.size.height == 1024

        assert image.area() == 1024*1024

        assert image.crop_region == Rect(Point(0, 0), Size(1024, 1024))

    def test_fire(self):
        fire = BPImage('../resources/fire.png')

        assert fire.size.width == 256
        assert fire.size.height == 256

        assert fire.area() == 256 * 256

        assert fire.crop_region == Rect(Point(16, 15), Size(226, 226))

    def test_cropImage(self):

        fire = BPImage('../resources/fire.png')

        assert fire.crop_region.size.width == 226
        assert fire.crop_region.size.height == 226