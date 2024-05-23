from nft.views import get_nft_data
from .models import Listanft, Kolekcija, Pripada, Portfolio
from exhibitions.models import Listanft, Pripada, Izlozba
from nft.models import Nft
def create_context_for_nfts(nfts):
    nft_list = []
    for nft in nfts:
        print("slika: " + str(nft.slika))
        print("url: " + str(nft.url))
        nft_data = {
            'nft': nft,
            'data': None
        }
        if nft.slika == "":
            nft_data['data'] = get_nft_data(nft.url)
        print("data: " + str(nft_data['data']))
        nft_list.append(nft_data)

    context = {"nfts": nft_list}

    return context


def get_user_collection(user):
    lists_nft = Listanft.objects.filter(idvla=user)

    collection_user = None
    collections = Kolekcija.objects.all()
    for list_nft in lists_nft:
        for collection in collections:
            if list_nft == collection.idlis:
                collection_user = collection
                break

    return collection_user


def get_user_portfolio(user):
    lists_nft = Listanft.objects.filter(idvla=user)

    portfolio_user = None
    portfolios = Portfolio.objects.all()
    for list_nft in lists_nft:
        for portfolio in portfolios:
            if list_nft == portfolio.idlis:
                portfolio_user = portfolio
                break

    return portfolio_user


def get_nfts_from_collection(collection_user):
    nfts = []
    if collection_user:
        belong = Pripada.objects.filter(idlis=collection_user.idlis)
        for belon in belong:
            nfts.append(belon.idnft)
            print(str(belon.idlis))
            print(str(belon.idnft))

        print(nfts)

    return nfts


def get_nfts_from_portfolio(portfolio_user):
    return get_nfts_from_collection(portfolio_user)

def getRandomExhibitions():
    izlozba_ids = Izlozba.objects.values_list('idlis', flat=True)[:3]
    izlozbe = []
    for id in izlozba_ids:
        nft_list = []
        pripada_ids = Pripada.objects.filter(idlis=id).values_list('idnft', flat=True)
        izloz = Izlozba.objects.get(idlis=id)
        print(pripada_ids)
        nfts = Nft.objects.filter(idnft__in=pripada_ids)
        cena = 0
        velicina = 0
        ocena = 0
        for nft in nfts:
            print(nft.naziv)
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
        prosOc = float(ocena) / velicina
        izlozba = {
            'nfts': nft_list,
            'cena': cena,
            'naziv': izloz.naziv,
            'velicina': velicina,
            'prosecnaOcena': prosOc
        }
        izlozbe.append(izlozba)
    return izlozbe

