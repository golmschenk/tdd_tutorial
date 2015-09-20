from .base import FunctionalTest
from unittest import skip


class ItemValidationTest(FunctionalTest):

    def get_error_element(self):
        return self.browser.find_element_by_css_selector('.has-error')

    def test_cannot_add_empty_list_items(self):
        # Kara goes to the home page and accidentally tries to submit
        # an empty list item. She hits Enter on the empty input box
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')

        # The home page refreshes, and there is an error message saying
        # that list items cannot be blank
        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item")

        # She tries again with some text for the item, which now works
        self.get_item_input_box().send_keys('Buy telescope\n')
        self.check_for_row_in_list_table('1: Buy telescope') #

        # Perversely, she now decides to submit a second blank list item
        self.get_item_input_box().send_keys('\n')

        # She receives a similar warning on the list page
        self.check_for_row_in_list_table('1: Buy telescope')
        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item")

        # And she can correct it by filling some text in
        self.get_item_input_box().send_keys('View stars\n')
        self.check_for_row_in_list_table('1: Buy telescope')
        self.check_for_row_in_list_table('2: View stars')

    def test_cannot_add_duplicate_items(self):
        # Kara goes to the home page and starts a new list
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Buy lenses\n')
        self.check_for_row_in_list_table('1: Buy lenses')

        # She accidentally tries to enter a duplicate item
        self.get_item_input_box().send_keys('Buy lenses\n')
        # She sees a helpful error message
        self.check_for_row_in_list_table('1: Buy lenses')
        error = self.get_error_element()
        self.assertEqual(error.text, "You already have this item in this list")

    def test_error_messages_are_cleared_on_input(self):
        # Kara starts a new list in a way that causes a validation error:
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')
        error = self.get_error_element()
        self.assertTrue(error.is_displayed())

        # She starts typing in the input box to fix the error
        self.get_item_input_box().send_keys('a')

        # She is overjoyed to see that the mean error message disappears when she starts typing
        error = self.get_error_element()
        self.assertFalse(error.is_displayed())


