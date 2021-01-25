from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.views import classes,login,registration,createdclass,joinclass

class TestUrls(SimpleTestCase):
    def test_urls_login(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, login)

    def test_urls_registration(self):
        url = reverse('registration')
        self.assertEqual(resolve(url).func, registration)

    def test_urls_joinclass(self):
        url = reverse('joinclass')
        self.assertEqual(resolve(url).func, joinclass)

    def test_urls_createdclass(self):
        url = reverse('createdclass')
        self.assertEquals(resolve(url).func, createdclass)