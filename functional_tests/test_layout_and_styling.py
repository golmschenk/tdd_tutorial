from .base import FunctionalTest


class LayoutAndStylingTest(FunctionalTest):

    def test_layout_and_styling(self):
        # Kara goes to the homepage.
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)

        # She notices a nicely centered box.
        input_box = self.get_item_input_box()
        self.assertAlmostEqual(
            input_box.location['x'] + input_box.size['width'] / 2,
            512,
            delta=5
        )

        # She starts a new list and sees that the box is centered on that page as well.
        input_box.send_keys('Just checking\n')
        input_box = self.get_item_input_box()
        self.assertAlmostEqual(
            input_box.location['x'] + input_box.size['width'] / 2,
            512,
            delta=5
        )

