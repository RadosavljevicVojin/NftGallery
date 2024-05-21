from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

from common.decoraters import is_creator_or_collector

from profiles.models import Registrovanikorisnik
from exhibitions.models import Listanft, Kolekcija, Pripada
from nft.models import Nft


# Create your views here.
def index(request):
    return render(request, "index.html")




@login_required(login_url='/accounts/error')
@user_passes_test(is_creator_or_collector, login_url='/accounts/error')
def create_exhibition(request):

    user = Registrovanikorisnik.objects.get(idkor = request.user)

    lists_nft = Listanft.objects.filter(idvla=user)

    collection_user = None
    collections = Kolekcija.objects.all()
    for list_nft in lists_nft:
        for collection in collections:
            if(list_nft.idlis == collection.idlis):
                collection_user = collection
                break

    nfts = []
    if collection_user:
        belong = Pripada.objects.filter(idlis=collection_user.idlis)
        nfts = [b.idnft for b in belong]

    return render(request, 'create_exhibition.html', {"nfts": nfts})


    return render(request, 'create_exhibition.html')
