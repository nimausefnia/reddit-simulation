from django.urls import reverse,resolve
from django.test import SimpleTestCase
from accounts.views import UserRegisteration,Dashboard




class TestUrls(SimpleTestCase):
    def test_register(self):
        url=reverse('accounts:register')
        self.assertEqual(resolve(url).func.view_class, UserRegisteration)
    

    def test_dashboard(self):
        url=reverse('accounts:dashboard', args=['nimajan'])
        self.assertEqual(resolve(url).func.view_class, Dashboard)




        