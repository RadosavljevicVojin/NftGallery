from nft.views import get_nft_data
from .models import Listanft, Kolekcija, Pripada, Portfolio


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
        nfts = [b.idnft for b in belong]

    return nfts


def get_nfts_from_portfolio(portfolio_user):
    return get_nfts_from_collection(portfolio_user)
