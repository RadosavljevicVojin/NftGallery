from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import register_page, registration_request, logout_view, delete_user, error_view


class TestUrls(SimpleTestCase):

    def test_login_page_access(self):
        # Testiraj pristup login stranici
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_register_url_is_resolved(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, register_page)

    def test_registration_request_url_is_resolved(self):
        url = reverse('reg_requests')
        self.assertEqual(resolve(url).func, registration_request)

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, logout_view)

    def test_delete_user_url_is_resolved(self):
        url = reverse('delete_user')
        self.assertEqual(resolve(url).func, delete_user)

    def test_error_url_is_resolved(self):
        url = reverse('error')
        self.assertEqual(resolve(url).func, error_view)