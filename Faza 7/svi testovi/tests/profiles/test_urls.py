from django.test import SimpleTestCase
from django.urls import reverse, resolve
from profiles.views import (view_profile_info, view_profile_collection,
                            view_profile_portfolio, view_profile_exhibitions,
                            sort_profile_collection, sort_profile_exhibition, view_change_info,exhibition_view_ajax, collection_view_ajax,change_info)

class UrlsTest(SimpleTestCase):
    def test_profile_info_url_resolves(self):
        url = reverse('profile_info')
        self.assertEqual(resolve(url).func, view_profile_info)

    def test_profile_collection_url_resolves(self):
        url = reverse('profile_collection')
        self.assertEqual(resolve(url).func, view_profile_collection)

    def test_profile_portfolio_url_resolves(self):
        url = reverse('profile_portfolio')
        self.assertEqual(resolve(url).func, view_profile_portfolio)

    def test_profile_exhibitions_url_resolves(self):
        url = reverse('profile_exhibitions')
        self.assertEqual(resolve(url).func, view_profile_exhibitions)

    def test_collection_sort_url_resolves(self):
        url = reverse('collection_sort')
        self.assertEqual(resolve(url).func, sort_profile_collection)
    def test_portfolio_sort_url_resolves(self):
        url = reverse('portfolio_sort')
        self.assertEqual(resolve(url).func, sort_profile_collection)

    def test_exhibition_sort_url_resolves(self):
        url = reverse('exhibition_sort')
        self.assertEqual(resolve(url).func, sort_profile_exhibition)

    def test_change_info_url_resolves(self):
        url = reverse('change_info')
        self.assertEqual(resolve(url).func, view_change_info)

    def test_change_info_submit_url_resolves(self):
        url = reverse('submit_change_info')
        self.assertEqual(resolve(url).func, change_info)

    def test_exhibition_view_ajax_url_resolves(self):
        url = reverse('exhibition_view_ajax')
        self.assertEqual(resolve(url).func, exhibition_view_ajax)

    def test_collection_view_ajax_url_resolves(self):
        url = reverse('collection_view_ajax')
        self.assertEqual(resolve(url).func, collection_view_ajax)