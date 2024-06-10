from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from accounts.models import Korisnik
from nft.models import Nft, Ocena
from exhibitions.models import Pripada, Listanft, Kolekcija
from profiles.models import Registrovanikorisnik
import os
import json
class Nft_views_test(TestCase):
    def setUp(self):
        # Kreiranje korisnika i potrebnih objekata za testiranje
        self.client = Client()
        self.user = Korisnik.objects.create_user(username='cevu', password='12345678',user_type="kreator")
        self.registrovani_korisnik = Registrovanikorisnik.objects.create(
            idkor=self.user,
            brojkartice='1235567890123456',
            brojtelefona='123456789',
            ime='Vuk2',
            prezime='Petrovic',
            email='vukk@example.com',
            datumrodjenja='2000-01-01',
            mestorodjenja='Beograd',
            prodatihNFT = 0,
            kupljenihNFT = 0
        )
        self.client.login(username='cevu', password='12345678')

        self.client2 = Client()
        self.user2 = Korisnik.objects.create_user(username='cevu2', password='12345678', user_type="kreator")
        self.registrovani_korisnik2 = Registrovanikorisnik.objects.create(
            idkor=self.user2,
            brojkartice='1235547890123456',
            brojtelefona='123456789',
            ime='Vuk3',
            prezime='Petrovic',
            email='vuk3@example.com',
            datumrodjenja='2000-01-01',
            mestorodjenja='Beograd',
            prodatihNFT=0,
            kupljenihNFT=0
        )
        self.client2.login(username='cevu2', password='12345678')

        test_image_path = os.path.join(os.path.dirname(__file__), 'nft_project', 'media', 'nft_images', 'deveta2.PNG')
        self.nft = Nft.objects.create(naziv='Test NFT', vrednost=10.0, opis='Test NFT Description',
                                      prosecnaocena=0.0, slika="deveta2.PNG", idkre=self.registrovani_korisnik, idvla=self.registrovani_korisnik, url='')

    def test_nft_review(self):
        url = reverse('nft_review', args=[self.nft.idnft])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'nft_review.html')

    def test_grade_nft_without_rating(self):
        url = reverse('grade_nft')
        # Simulacija POST zahteva sa nedostajućom ocenom
        response = self.client.post(url, {'idnft_name': self.nft.idnft})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'nft_review.html')

        # Provera da li je ocena za NFT ostala nepromenjena
        self.assertEqual(Ocena.objects.filter(idnft=self.nft).count(), 0)

    def test_grade_nft_with_rating(self):
        url = reverse('grade_nft')
        # Simulacija POST zahteva sa ocenom 4
        response = self.client.post(url, {'idnft_name': self.nft.idnft, 'rating': 4})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'nft_review.html')

        # Provera da li je ocena za NFT uspešno dodata
        self.assertEqual(Ocena.objects.filter(idnft=self.nft).count(), 1)

    def test_change_price(self):
        # Simulacija POST zahteva za promenu cene NFT-a
        nova_cena = 15.0  # Nova cena NFT-a
        url = reverse('change_price')
        response = self.client.post(url, {'idnft_name': self.nft.idnft, 'new_price': nova_cena})

        # Provera da li je zahtev uspešno izvršen
        self.assertEqual(response.status_code, 200)

        # Provera da li se koristi odgovarajući template
        self.assertTemplateUsed(response, 'nft_review.html')

        # Provera da li je cena NFT-a uspešno promenjena u bazi podataka
        updated_nft = Nft.objects.get(idnft=self.nft.idnft)
        self.assertEqual(updated_nft.vrednost, nova_cena)

        # Provera da li je ukupna vrednost svih lista kojima pripada NFT promenjena
        pripadajuce_liste = Pripada.objects.filter(idnft=self.nft)
        for lista in pripadajuce_liste:
            self.assertEqual(lista.ukupnavrednost, lista.ukupnavrednost + nova_cena - self.nft.vrednost)

    def test_nft_view_ajax(self):
        url = reverse('updatePrice')
        response = self.client.post(url, {'idnft_name': self.nft.idnft})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIn('vrednost', data)
        self.assertIn('ocena', data)

    def test_buy_nft(self):
        # Simulacija POST zahteva za kupovinu NFT-a
        url = reverse('buy_nft')
        response = self.client2.post(url, {'idnft_name': self.nft.idnft})

        # Provera da li je zahtev uspeo
        self.assertEqual(response.status_code, 200)

        # Provera da li je korisnik povećao broj kupljenih NFT-ova
        platio = Registrovanikorisnik.objects.get(idkor=self.user2)

        self.assertEqual(platio.kupljenihNFT, 1)

        # Provera da li je prethodni vlasnik povećao broj prodatih NFT-ova
        prosli_vlasnik = Registrovanikorisnik.objects.get(idkor=self.user)
        self.assertEqual(prosli_vlasnik.prodatihNFT, 1)

        prosli_vlasnik_kolekcije = Listanft.objects.filter(idvla=prosli_vlasnik)
        for kol in prosli_vlasnik_kolekcije:
            # Očekujemo da NFT nije više u kolekciji prethodnog vlasnika
            self.assertFalse(Pripada.objects.filter(idlis=kol, idnft=self.nft).exists())
            # Provera smanjenja vrednosti i broja NFT-ova u kolekciji
            kol.refresh_from_db()
            self.assertEqual(kol.ukupnavrednost, 0)  # Pretpostavka da je vrednost početno 0
            self.assertEqual(kol.brojnft, 0)  # Pretpostavka da je broj NFT-ova početno 0

        # Provera da li je NFT dodat u kolekciju novog vlasnika ("cevu2")
        platio_kolekcija = Listanft.objects.filter(idvla=platio)
        for kol in platio_kolekcija:
            if Kolekcija.objects.filter(idlis=kol).exists():
                # Očekujemo da NFT bude dodat u kolekciju novog vlasnika
                self.assertTrue(Pripada.objects.filter(idlis=kol, idnft=self.nft).exists())
                # Provera povećanja vrednosti i broja NFT-ova u kolekciji
                kol.refresh_from_db()
                self.assertEqual(kol.ukupnavrednost, self.nft.vrednost)
                self.assertEqual(kol.brojnft, 1)



        # Provera da li je odgovarajući template korišćen za prikaz
        self.assertTemplateUsed(response, 'nft_review.html')