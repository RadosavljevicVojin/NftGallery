from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from accounts.models import Korisnik
from profiles.models import Registrovanikorisnik

class ProfileInfoViewTest(TestCase):
    def setUp(self):
        # Kreiranje korisnika i potrebnih objekata za testiranje
        self.client = Client()
        self.user = Korisnik.objects.create_user(username='vojin2', password='12345678',user_type="kreator")
        self.registrovani_korisnik = Registrovanikorisnik.objects.create(
            idkor=self.user,
            brojkartice='1234567890123456',
            brojtelefona='123456789',
            ime='Vojin2',
            prezime='Petrovic',
            email='vojin@example.com',
            datumrodjenja='2000-01-01',
            mestorodjenja='Beograd'
        )
        self.client.login(username='vojin2', password='12345678')

    def test_view_profile_info_post_ajax_request(self):
        # Testiranje POST zahteva sa validnim korisničkim imenom
        response = self.client.post(reverse('profile_info'), {'username': 'Vojin2'},
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ajaxProfileInfo.html')
        self.assertContains(response, 'Vojin2')
        self.assertContains(response, 'Petrovic')
        self.assertContains(response, '123456789')

    def test_view_profile_info_post_request(self):
        # Testiranje POST zahteva sa validnim korisničkim imenom
        response = self.client.post(reverse('profile_info'), {'username': 'vojin2'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile_info.html')
        self.assertContains(response, 'Vojin2')
        self.assertContains(response, 'Petrovic')
        self.assertContains(response, '123456789')

    def test_view_profile_info_post_request_invalid_user(self):
        # Testiranje POST zahteva sa nevalidnim korisničkim imenom
        response = self.client.post(reverse('profile_info'), {'username': 'invaliduser'})
        self.assertRedirects(response, reverse('index') + '?exists=false')

    def test_view_profile_collection_post_request_valid_username(self):
        response = self.client.post(reverse('profile_collection'), {'username': 'vojin2'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile_collection.html')

    def test_view_profile_collection_post_request_no_username(self):
        response = self.client.post(reverse('profile_collection'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Molimo vas da unesete korisničko ime.")


    def test_view_profile_portfolio_post_request_no_username(self):
        response = self.client.post(reverse('profile_portfolio'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Molimo vas da unesete korisničko ime.")

    def test_view_profile_exhibitions_post_request_valid_username(self):
        response = self.client.post(reverse('profile_exhibitions'), {'username': 'vojin2'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile_exhibitions.html')

    def test_view_profile_exhibitions_post_request_no_username(self):
        response = self.client.post(reverse('profile_exhibitions'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Molimo vas da unesete korisničko ime.")

    def test_sort_profile_collection_post_request_valid_username(self):
        response = self.client.post(reverse('collection_sort'),
                                    {'username': 'vojin2', 'sort': 'po Imenu', 'pageType': 'collection'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile_collection.html')

    def test_sort_profile_collection_post_request_invalid_username(self):
        response = self.client.post(reverse('collection_sort'),
                                    {'sort': 'name', 'pageType': 'collection'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Molimo vas da unesete korisničko ime.")
    def test_sort_profile_exhibition_post_request_valid_username(self):
        response = self.client.post(reverse('exhibition_sort'), {'username': 'vojin2', 'sort': 'po Imenu'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile_exhibitions.html')

    def test_sort_profile_exhibition_post_request_invalid_username(self):
        response = self.client.post(reverse('exhibition_sort'), { 'sort': 'po Imenu'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Molimo vas da unesete korisničko ime.")

    def test_change_info_post_request(self):
        response = self.client.post(reverse('change_info'),
                                    {'stara-lozinka': '12345678', 'nova-lozinka': '87654321',
                                     'potvrda-lozinke': '87654321'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'change_profile_info.html')


