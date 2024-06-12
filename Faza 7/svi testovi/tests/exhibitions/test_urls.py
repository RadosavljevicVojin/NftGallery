from django.test import SimpleTestCase
from django.urls import reverse, resolve
from exhibitions.views import index, create_exhibition, change_exhibition, exhibition_review, remove_exhibition, sort_exhibition

class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)

    def test_create_exhibition_url_is_resolved(self):
        url = reverse('create_exhibition')
        self.assertEqual(resolve(url).func, create_exhibition)

    def test_change_exhibition_url_is_resolved(self):
        url = reverse('change_exhibition', args=[1])  # Pretpostavka da je exhibition_id = 1
        self.assertEqual(resolve(url).func, change_exhibition)

    def test_exhibition_review_url_is_resolved(self):
        url = reverse('exhibition_review', args=[1])  # Pretpostavka da je exhibition_id = 1
        self.assertEqual(resolve(url).func, exhibition_review)

    def test_remove_exhibition_url_is_resolved(self):
        url = reverse('remove_exhibition')
        self.assertEqual(resolve(url).func, remove_exhibition)

    def test_sort_exhibition_url_is_resolved(self):
        url = reverse('sort_exhibition')
        self.assertEqual(resolve(url).func, sort_exhibition)