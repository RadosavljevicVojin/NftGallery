from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render

from accounts.models import Korisnik
from exhibitions.models import Listanft, Pripada,Izlozba
from nft.models import Nft
from nft.views import get_nft_data
from profiles.models import Registrovanikorisnik
def create_main_context(request, username):

    user = Korisnik.objects.get(username=username)
    context = dict()
    context["id"] = user.idkor
    context["username"] = user.username
    context["image"] = Registrovanikorisnik.objects.get(idkor=user).slika.url
    context["type"] = user.user_type
    context["myprofile"] = False
    context["joined"]= Registrovanikorisnik.objects.get(idkor=user).datumkreiranja
    context["email"]=Registrovanikorisnik.objects.get(idkor=user).email
    context["buy_number"]=Registrovanikorisnik.objects.get(idkor=user).kupljenihNFT
    context["sell_number"]=Registrovanikorisnik.objects.get(idkor=user).prodatihNFT
    context["birthdate"]= Registrovanikorisnik.objects.get(idkor=user).datumrodjenja.strftime("%d/%m/%Y")
    context["num_of_nft"]=  Nft.objects.filter(idvla=user.idkor).count()

    if user.username == request.user.username:
        context["myprofile"] = True

    return context

def pack_nfts(nfts):
    nft_list = []
    cena = 0
    for nft in nfts:
        nft_data = {
            'nft': nft,
            'data': None
        }
        if nft.slika == "":
            nft_data['data'] = get_nft_data(nft.url)
        nft_list.append(nft_data)
        cena += nft.vrednost
    return nft_list, cena

def pack_nfts_exhibitions(nfts):
    nft_list = []
    cena = 0
    velicina = 0
    ocena = 0
    for nft in nfts:
        nft_data = {
            'nft': nft,
            'data': None
        }
        if nft.slika == "":
            nft_data['data'] = get_nft_data(nft.url)
        nft_list.append(nft_data)
        cena += nft.vrednost
        velicina += 1
        ocena += nft.prosecnaocena
    return nft_list, cena, velicina, ocena

def get_user_exhibitions(idUser):
    listanfts = Listanft.objects.filter(izlozba__isnull=False, idvla=idUser)
    izlozbe = []
    for listanft in listanfts:
        pripada_ids = Pripada.objects.filter(idlis=listanft.idlis).values_list('idnft', flat=True)
        izloz = Izlozba.objects.get(idlis=listanft.idlis)
        nfts = Nft.objects.filter(idnft__in=pripada_ids)
        nft_list, cena, velicina, ocena = pack_nfts_exhibitions(nfts)
        prosOc = float(ocena) / velicina
        izlozba = {
            'id': listanft.idlis,
            'nfts': nft_list,
            'cena': cena,
            'naziv': izloz.naziv,
            'velicina': velicina,
            'prosecnaOcena': prosOc
        }
        izlozbe.append(izlozba)
    return izlozbe
def get_user_portfolio(idUser):
    listanft = Listanft.objects.filter(portfolio__isnull=False, idvla=idUser).first()
    pripada_ids = Pripada.objects.filter(idlis=listanft.idlis).values_list('idnft', flat=True)
    nfts = Nft.objects.filter(idnft__in=pripada_ids)
    nft_list, novaCena = pack_nfts(nfts)
    return nft_list, novaCena
def get_user_collection(idUser):
    nfts = Nft.objects.filter(idvla=idUser)
    nft_list, novaCena = pack_nfts(nfts)
    return nft_list,novaCena

