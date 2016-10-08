from ScreamingMercury import ScreamingMercury


class ScreamingMercuryController(object):
    def __init__(self):
        self._view = ScreamingMercury(self)

    def view(self):
        return self._view

    def on_run_button(self):
        pass

    def on_settings_button_click(self):
        pass

    def on_remove_image(self, index):
        pass

    def on_remove_all_images(self):
        self._view.resetDirectory()

    def on_change_image_size(self, index):
        pass
