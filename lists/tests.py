from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page

class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page(self):
		found = resolve('/') ##when we refer to this url (the root of the site)
		self.assertEqual(found.func, home_page) ##we're looking for the home_page function
		##because when we navigate to the root url, we want the home page to appear.

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		expected_html = render_to_string('home.html', request=request)
		self.assertEqual(response.content.decode(), expected_html)

	def test_home_page_can_save_a_POST_request(self):
		request = HttpRequest()
		request.method = 'POST'
		request.POST['item_text'] = 'A new list item' ##item text is the NAME (attribute) of our INPUT FORM

		response = home_page(request)
		self.assertIn("A new list item", response.content.decode())
		expected_html = render_to_string('home.html',
			{'new_item_text' : 'A new list item'}
			)
		self.assertEqual(expected_html,response.content.decode())