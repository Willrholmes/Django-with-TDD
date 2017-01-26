from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Rosie has heard about a cool new online to-do app. She goes to checkout
        #its homepage
        self.browser.get(self.server_url)

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn("To-Do", header_text)

        # She is invited to enter a to-do item straight away
        # She types "Buy Will a present" into a text box
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy Will\'s present')
        inputbox.send_keys(Keys.ENTER)

        # When she hits enter, the page updates, and now the page lists
        # "#1: Buy Will a present" as an item in a to-do list
        self.check_for_row_in_list_table('1: Buy Will\'s present')

        # There is still a text box inviting her to add another item.
        # She enters "Buy Will another present"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy Will another present')
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy Will\'s present')
        self.check_for_row_in_list_table('2: Buy Will another present')

        #The page updates again, and now shows both items on her lists

        # Rosie wonders whether the site will remember her list. Then she sees that the
        # site has generated a unique URL for her -- there is some explanatory text to
        # that effect.
        # She visits the URL - her to do list is still there.

    def test_multiple_users_can_start_lists_at_different_urls(self):
        #Rosie starts a new todo list
        self.browser.get(self.server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy Will\'s present')
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy Will\'s present')

        # she notices that her list has a unique URL
        rosie_list_url = self.browser.current_url
        self.assertRegex(rosie_list_url, '/lists/.+')

        # New user, Ned, comes along to the site

        ## We use a new browser sesseion to make sure that no information
        ## of Rosie's is coming from cookies etc.
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Ned visit the home page. There is no sign of Rosie's list
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy Will\'s present', page_text)
        self.assertNotIn('Buy Will another present', page_text)

        # Ned starts a new list by entering a new item. He
        # is less interesting than Rosie...
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy milk')

        # Ned gets his own unique URL
        ned_list_url = self.browser.current_url
        self.assertRegex(ned_list_url, '/lists/.+')
        self.assertNotEqual(ned_list_url, rosie_list_url)


        # Again there is no trace of Rosie's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy Will\'s present', page_text)
        self.assertIn('Buy milk', page_text)
