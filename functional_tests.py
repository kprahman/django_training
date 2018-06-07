from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		##user opens up the page
		self.browser.get('http://localhost:8000')

		##user sees that the title of the page mentions to-do lists
		self.assertIn('To-Do', self.browser.title)
		self.fail("Finish the test!")

		##user is invited to input a todo item 

		##user enters the item into a text bok

		##user hits enter, the page updates, and lists "1:item"

		##text bok remains, allowing the user to go again

		##page updates again if the user enters another item

		##user sees that the to-do list has been given its own URL, so that it can be accessed again

		##visit the URL, list exists

		#user exits

if __name__ == '__main__':
	unittest.main(warnings='ignore')