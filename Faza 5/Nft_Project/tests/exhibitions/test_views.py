from django.test import TestCase, Client
from django.urls import reverse
from exhibitions.models import Izlozba, Listanft
from profiles.models import Registrovanikorisnik
from accounts.models import Korisnik
from django.utils import timezone


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = Korisnik.objects.create_user(username='testuser', password='123456', user_type='kreator')
        self.reg_user = Registrovanikorisnik.objects.create(
            idkor=self.user,
            datumrodjenja='2000-05-22 00:00:00.000000'
        )
        self.client.login(username='testuser', password='123456')
        self.exhibition_list = Listanft.objects.create(idlis=1, idvla=self.reg_user, ukupnavrednost=0, brojnft=0)
        self.exhibition = Izlozba.objects.create(idlis=self.exhibition_list, naziv='Test', opis='Opis',
                                                 datumkreiranja='2024-05-30', prosecnaocena=0)

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_index_POST(self):
        response = self.client.post(reverse('index'), {
            'sort': 'poImenu'
        })

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_create_exhibition_get(self):
        response = self.client.get(reverse('create_exhibition'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_exhibition.html')

    def test_create_exhibition_post(self):
        response = self.client.post(reverse('create_exhibition'), {
            'ime': 'Nova',
            'opis': 'Opis',
            # Add other necessary POST data here
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'operation_on_exhibition_success.html')
        self.assertTrue(Izlozba.objects.filter(naziv='Nova').exists())
        self.assertTrue(Listanft.objects.exists())

    def test_change_exhibition_get(self):
        response = self.client.get(reverse('change_exhibition', args=[1]))  # Pretpostavka da je exhibition_id = 1
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'change_exhibition.html')

    def test_change_exhibition_post(self):
        response = self.client.post(reverse('change_exhibition', args=[1]))
