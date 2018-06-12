from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		##user opens up the page
		self.browser.get('http://localhost:8000')

		##user sees that the title of the page mentions to-do lists
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		##user is invited to input a todo item
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
			) 

		##user enters the item into a text bok
		inputbox.send_keys('Buy peacock feathers')

		##user hits enter, the page updates, and lists "1:item"
		inputbox.send_keys(Keys.ENTER)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1: Buy peacock feathers' for row in rows),
			"New to-do item did not appear in table :("
			)

		##text bok remains, allowing the user to go again
		self.fail("Nailed it! Take a shot.")

		##page updates again if the user enters another item

		##user sees that the to-do list has been given its own URL, so that it can be accessed again

		##visit the URL, list exists

		#user exits

if __name__ == '__main__':
	unittest.main(warnings='ignore')