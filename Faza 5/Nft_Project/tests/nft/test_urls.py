from django.test import SimpleTestCase
from django.urls import reverse, resolve
from nft.views import create_nft, nft_review, grade_nft,change_price, buy_nft, nft_view_ajax

class NftUrlsTest(SimpleTestCase):

    def test_create_nft_url_is_resolved(self):
        url = reverse('create_nft')
        self.assertEqual(resolve(url).func, create_nft)

    def test_nft_review_url_is_resolved(self):
        url = reverse('nft_review', args=[1])
        self.assertEqual(resolve(url).func, nft_review)

    def test_grade_nft_url_is_resolved(self):
        url = reverse('grade_nft')
        self.assertEqual(resolve(url).func, grade_nft)

    def test_change_price_url_is_resolved(self):
        url = reverse('change_price')
        self.assertEqual(resolve(url).func, change_price)

    def test_buy_nft_url_is_resolved(self):
        url = reverse('buy_nft')
        self.assertEqual(resolve(url).func, buy_nft)

    def test_updatePrice_url_is_resolved(self):
        url = reverse('updatePrice')
        self.assertEqual(resolve(url).func, nft_view_ajax)