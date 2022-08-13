from django.test import TestCase


# Create your tests here.

class HomePageTest(TestCase):
    '''Тест домашней страницы'''

    def test_home_page_returns_correct_html(self):
        '''Тест: используется home.html'''
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
