from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect

from common.decoraters import is_creator_or_collector

from profiles.models import Registrovanikorisnik
from exhibitions.models import Listanft, Kolekcija, Pripada, Izlozba
from nft.models import Nft
from nft.views import get_nft_data
from datetime import datetime


# Create your views here.
def index(request):
    return render(request, "index.html")




@login_required(login_url='/accounts/error')
@user_passes_test(is_creator_or_collector, login_url='/accounts/error')
def create_exhibition(request):
    user = Registrovanikorisnik.objects.get(idkor=request.user)

    if request.method == 'POST':
        exhibition_name = request.POST['ime']
        description = request.POST['opis']
        selected_nfts = list(map(int, request.POST.get('selected_nfts').split(',')))
        nfts_objects = Nft.objects.filter(idnft__in=selected_nfts)
        exhibition_size = len(selected_nfts)

        grades = 0
        exhibition_value = 0
        for nft_object in nfts_objects:
            grades += nft_object.prosecnaocena
            exhibition_value += nft_object.vrednost

        exhibition_avg_grades = grades / exhibition_size
        date = datetime.now().strftime('%Y-%m-%d')

        print(exhibition_name)
        print(description)
        print(str(selected_nfts))
        print(str(nfts_objects))
        print(exhibition_size)

        exhibition_list = Listanft(idvla=user, ukupnavrednost=exhibition_value, brojnft=exhibition_size)
        exhibition_list.save()

        # Креирање и чување новог Kolekcija објекта
        exhibition = Izlozba(idlis=exhibition_list, naziv=exhibition_name, opis=description,
                             datumkreiranja=date, prosecnaocena=exhibition_avg_grades)
        exhibition.save()

        for nft_object in nfts_objects:
            belong = Pripada(idlis=exhibition_list, idnft=nft_object)
            belong.save()

        return redirect("profile_info")

    else:

        user = Registrovanikorisnik.objects.get(idkor=request.user)
        print(str(user))

        lists_nft = Listanft.objects.filter(idvla=user)

        collection_user = None
        collections = Kolekcija.objects.all()
        for list_nft in lists_nft:
            for collection in collections:
                if list_nft == collection.idlis:
                    collection_user = collection
                    break

        print(str(collection_user))

        nfts = []
        if collection_user:
            belong = Pripada.objects.filter(idlis=collection_user.idlis)
            nfts = [b.idnft for b in belong]

        print(str(nfts))

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

        return render(request, 'create_exhibition.html', context)
