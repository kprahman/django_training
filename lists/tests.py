from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page

class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page(self):
		found = resolve('/') ##when we refer to this url (the root of the site)
		self.assertEqual(found.func, home_page) ##we're looking for the home_page function
		##because when we navigate to the root url, we want the home page to appear.

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		html = response.content.decode('utf8')
		self.assertTrue(html.startswith('<html>'))
		self.assertTrue(html.endswith('</html>'))
		self.assertIn('<title>To-Do lists</title>', html)

