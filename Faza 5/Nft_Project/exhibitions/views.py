from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect

from common.decoraters import is_creator_or_collector

from profiles.models import Registrovanikorisnik
from exhibitions.models import Listanft, Kolekcija, Pripada, Izlozba
from nft.models import Nft

from .utils import create_context_for_nfts, get_user_collection, get_nfts_from_collection
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

        collection_user = get_user_collection(user)

        nfts = get_nfts_from_collection(collection_user)

        context = create_context_for_nfts(nfts)

        return render(request, 'create_exhibition.html', context)

@login_required(login_url='/accounts/error')
@user_passes_test(is_creator_or_collector, login_url='/accounts/error')
def change_exhibition(request, exhibition_id):

    exhibition_list = Listanft.objects.get(idlis=exhibition_id)
    belong = Pripada.objects.filter(idlis=exhibition_list)
    exhibition_nfts = [b.idnft for b in belong]



    if request.method == "POST":

        selected_nfts = list(map(int, request.POST.get('selected_nfts').split(',')))
        nfts_objects = Nft.objects.filter(idnft__in=selected_nfts)

        [belong_obj.delete() for belong_obj in belong if belong_obj.idnft not in nfts_objects]

        belong = [
            Pripada(idlis=exhibition_list, idnft=nft_object) for nft_object in nfts_objects if nft_object not in exhibition_nfts
        ]

        for belong_obj in belong:
            belong_obj.save()
        return redirect("profile_info")

    else:

        user = Registrovanikorisnik.objects.get(idkor=request.user)

        collection_user = get_user_collection(user)

        collection_nfts = get_nfts_from_collection(collection_user)

        context = create_context_for_nfts(collection_nfts)

        nft_list = context['nfts']
        for nft in nft_list:
            if nft['nft'] in exhibition_nfts:
                print("Selektovani nft sam ja " + str(nft['nft']))
                nft['select'] = True
            else:
                nft['select'] = False

        return render(request, 'change_exhibition.html', context)