from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_Other(self):
        # Rosie has heard about a cool new online to-do app. She goes to checkout
        #its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn("To-Do", header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types "Buy Will a present" into a text box
        inputbox.send_keys('Buy Will\'s present')

        # When she hits eneter, the page updates, and now the page lists
        # "#1: Buy Will a present" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy Will\'s present', [row.text for row in rows])

        # There is still a text box inviting her to add another item.
        # She enters "Buy Will another present"
        self.assertIn('2: Buy Will another present',
            [row.text for row in rows]
        )



        #The page updates again, and now shows both items on her lists

        # Rosie wonders whether the site will remember her list. Then she sees that the
        # site has generated a unique URL for her -- there is some explanatory text to
        # that effect.
        self.fail('Finish the test!')

        # She visits the URL - her to do list is still there.

if __name__ == '__main__':
    unittest.main()
