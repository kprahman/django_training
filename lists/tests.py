from django.urls import resolve
from django.test import TestCase
from lists.views import home_page

class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page(self):
		found = resolve('/') ##when we refer to this url (the root of the site)
		self.assertEqual(found.func, home_page) ##we're looking for the home_page function
		##because when we navigate to the root url, we want the home page to appear.


