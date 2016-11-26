from selenium import webdriver
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
        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away

        # She types "Buy Will a present" into a text box

        # When she hits eneter, the page updates, and now the page lists
        # "#1: Buy Will a present" as an item in a to-do list

        # There is still a text box inviting her to add another item.
        # She enters "Buy Will another present"

        #The page updates again, and now shows both items on her lists

        # Rosie wonders whether the site will remember her list. Then she sees that the
        # site has generated a unique URL for her -- there is some explanatory text to
        # that effect.

        # She visits the URL - her to do list is still there.

if __name__ == '__main__':
    unittest.main()
