from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.test import TestCase
from django.urls import reverse_lazy

User = get_user_model()


class LoginFormTest(TestCase):
    def test_valid_login(self):
        User.objects.create_user(username="testuser", password="testpassword")
        form_data = {"username": "testuser", "password": "testpassword"}
        form = AuthenticationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_login_form_empty_data(self):
        form_data = {}
        form = AuthenticationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("username", form.errors)
        self.assertIn("password", form.errors)


class URLTests(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse_lazy("index"))
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        response = self.client.get(reverse_lazy("login"))
        self.assertEqual(response.status_code, 200)

    def test_logout_view(self):
        response = self.client.get(reverse_lazy("logout"))
        print(response)
        self.assertEqual(response.status_code, 302)


class HomePageTest(TestCase):
    def setUp(self):
        self.response = self.client.get(reverse_lazy("index"))

    def test_home_page(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "index.html")
        self.assertContains(self.response, "Greetings from Hexlet!")
        self.assertNotContains(self.response, "This text shouldn't be here")
