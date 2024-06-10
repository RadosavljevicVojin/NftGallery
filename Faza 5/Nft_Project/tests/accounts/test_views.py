from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import Korisnik, Zahtevzaregistraciju
from profiles.models import Registrovanikorisnik


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = Korisnik.objects.create_user(username=self.username, password=self.password)  # Koristite Korisnik model
        self.admin_user = Korisnik.objects.create_user(username='admin', password='adminpass', user_type='admin')
        self.reg_user = Registrovanikorisnik.objects.create(
            idkor=self.user,
            datumrodjenja='2000-05-22 00:00:00.000000'
        )

    def test_successful_login(self):
        # Testiraj uspešan login
        response = self.client.post(reverse('login'), {
            'username': self.username,
            'password': self.password
        })
        self.assertEqual(response.status_code, 302)  # Očekujemo redirekciju nakon uspešnog logina
        self.assertRedirects(response, reverse('index'))  # Pretpostavimo da je redirekcija na 'index'

    def test_failed_login(self):
        # Testiraj neuspešan login sa pogrešnim podacima
        response = self.client.post(reverse('login'), {
            'username': self.username,
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        messages_list = list(response.context['messages'])
        self.assertTrue(any("Uneli ste pogrešne kredencijale!" in str(message) for message in messages_list))

    def test_register_page(self):
        # Testiranje stranice za registraciju, treba da dobijemo status 200
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signin.html')

    def test_register_post(self):
        # Testiranje POST zahteva za registraciju, treba da dobijemo redirekciju na stranicu za prijavljivanje
        response = self.client.post(reverse('register'), {
            'username': 'novikorisnik',
            'birthdate': '1990-01-01',
            'birthplace': 'Novi Sad',
            'name': 'Marko',
            'surname': 'Markovic',
            'phone': '0643265474',
            'password': 'testpassword',
            'confirm_password': 'testpassword',
            'email': 'marko@gmail.com',
            'card': '123',
            'user_type': 'kreator'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signin.html')
        messages_list = list(response.context['messages'])
        self.assertTrue(any("Uspešno je poslat zahtev za registarciju." in str(message) for message in messages_list))
        self.assertTrue(Zahtevzaregistraciju.objects.filter(korime='novikorisnik').exists())

    def test_registration_request_view(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.get(reverse('reg_requests'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration_request.html')

    def test_accept_registration_request(self):
        self.client.login(username='admin', password='adminpass')
        request = Zahtevzaregistraciju.objects.create(
            korime='novikorisnik',
            uloga='kreator',
            ime='Marko',
            prezime='Markovic',
            sifra='testpassword',
            email='marko@gmail.com',
            brojtelefona='0643265474',
            datumrodjenja='1990-01-01',
            mestorodjenja='Belgrade'
        )

        response = self.client.post(reverse('reg_requests'), {
            f'accept-{request.idzah}': 'accept'
        })

        self.assertEqual(response.status_code, 200)
        # Dodajte provere za uspešno prihvatanje zahteva

    def test_reject_registration_request(self):
        self.client.login(username='admin', password='adminpass')
        request = Zahtevzaregistraciju.objects.create(
            korime='novikorisnik',
            uloga='kreator',
            ime='Marko',
            prezime='Markovic',
            sifra='testpassword',
            email='marko@gmail.com',
            brojtelefona='0643265474',
            datumrodjenja='1990-01-01',
            mestorodjenja='Belgrade'
        )

        response = self.client.post(reverse('reg_requests'), {
            f'reject-{request.idzah}': 'reject'
        })

        self.assertEqual(response.status_code, 200)

    def test_successful_logout(self):
        # Testiraj uspešan logout
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))

    def test_logout_without_login(self):
        # Testiraj logout bez prethodnog logina
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('error'))

    def test_delete_user(self):
        # Testiraj brisanje korisnika
        self.client.login(username='admin', password='adminpass')
        response = self.client.post(reverse('delete_user'), {
            'username': self.username
        })
        self.assertEqual(response.status_code, 302)  # Očekujemo redirekciju nakon uspešnog brisanja
        self.assertRedirects(response, reverse('reg_requests'))  # Pretpostavimo da je redirekcija na 'reg_requests'
        self.assertFalse(Korisnik.objects.filter(username=self.username).exists())  # Provera da li je korisnik obrisan

    def test_delete_user_without_login(self):
        # Testiraj brisanje korisnika bez logovanja
        response = self.client.post(reverse('delete_user'), {
            'username': self.username
        })
        self.assertEqual(response.status_code, 302)  # Očekujemo redirekciju na stranicu sa greškom
        self.assertRedirects(response, f"{reverse('error')}?next={reverse('delete_user')}")

    def test_error_view(self):
        response = self.client.get(reverse('error'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'error.html')
        self.assertContains(response, '403')
        self.assertContains(response, 'permission denied')