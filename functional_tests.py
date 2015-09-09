from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Kara heard about a new top-notch online to-do app. She goes to the website to check it out.
        self.browser.get('http://localhost:8000')

        # She sees that the website's title and header do indeed talk about to-dos, so she can guess she has the right link.
        self.assertIn('To-do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('to-do', header_text)

        # Kara is immediately given the option to enter a to-do item
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                input_box.get_attribute('placeholder'),
                'Enter a to-do item'
        )

        # She types in "Buy a telescope"
        input_box.send_keys('Buy a telescope')

        # When she hits enter, the page updates, and now displays an item in a to-do list listing "1: Buy a telescope".
        input_box.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table('1: Buy a telescope')

        # There is a box inviting her to add another item, so she types in "Use telescope to view stars" (Kara is very
        # methodical).
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                input_box.get_attribute('placeholder'),
                'Enter a to-do item'
        )
        input_box.send_keys('Use telescope to view stars')
        input_box.send_keys(Keys.ENTER)

        # The page updates again and now lists both items.
        self.check_for_row_in_list_table('1: Buy a telescope')
        self.check_for_row_in_list_table('2: Use telescope to view stars')

        # Kara is wonders if the site will remember her list, and then sees that the site has generated a unique URL for her.
        # At least, there's some explanatory text to that effect.
        self.fail('Finish the test!')

        # She visits the url and her list is still there.

        # For the moment, Kara's skeptism about the site is quelled, and she goes back to sleep.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
