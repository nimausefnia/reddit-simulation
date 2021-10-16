from django.test import SimpleTestCase
from accounts.forms import UserRegistrationForm


class TestForm(SimpleTestCase):

    def test_valid_data(self):
        
        form=UserRegistrationForm(data={'username':'amir','email':'email@email.com','password':'1234'})
        self.assertTrue(form.is_valid())



    def test_invalid_data(self):
        form=UserRegistrationForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)    