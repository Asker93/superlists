from django.test import TestCase
from django.urls import resolve
from lists.views import home_page

# Create your tests here.

class HomePageTest(TestCase):
    '''Тест домашней страницы'''

    def test_root_url_resolves_to_home_page_view(self):
        '''Тест корневой URL преобразуется в представление домашней страницы'''
        found = resolve('/')
        self.assertEqual(found.func, home_page)

