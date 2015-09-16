from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Kara heard about a new top-notch online to-do app. She goes to the website to check it out.
        self.browser.get(self.server_url)

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

        # When she hits enter, shes taken to a new URL, which now displays an item in a to-do list listing "1: Buy a telescope".
        input_box.send_keys(Keys.ENTER)
        karas_list_url = self.browser.current_url
        self.assertRegex(karas_list_url, '/lists/.+')
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

        # Now a new user, Sophia, takes a look at the website.

        ## We use a new browser to make sure no cookies are kept from Kara's browser.
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Sophia visits the homepage, and does not see Kara's list.
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy a telescope', page_text)
        self.assertNotIn('Use telescope to view stars', page_text)

        # Sophia starts a new list by entering a new item, which by chance is also science based.
        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys('Buy a Bunsen burner')
        input_box.send_keys(Keys.ENTER)

        # Sophia gets her own unique URL.
        sophias_list_url = self.browser.current_url
        self.assertRegex(sophias_list_url, '/lists/.+')
        self.assertNotEqual(karas_list_url, sophias_list_url)

        # Sophia sees only her list.
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn('Bunsen burner', page_text)
        self.assertNotIn('Buy a telescope', page_text)

        # For the moment, both Kara and Sophia's skeptism about the site is quelled, and both go back to sleep.

