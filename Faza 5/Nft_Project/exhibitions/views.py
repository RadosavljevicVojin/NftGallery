from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect
from common.decoraters import is_creator_or_collector
from profiles.models import Registrovanikorisnik
from .utils import *
from datetime import datetime
from profiles.utils import sort_user_exhibitions,sort_nfts


# Create your views here.
def index(request):
    izlozbe = getRandomExhibitions()
    if request.method == 'POST':
        sort = request.POST.get('sort', None)
        izlozbe = sort_user_exhibitions(-1,sort)
    context = dict()
    context["izlozbe"] = izlozbe
    return render(request, 'index.html', context)


@login_required(login_url='/accounts/error')
@user_passes_test(is_creator_or_collector, login_url='/accounts/error')
def create_exhibition(request):
    user = Registrovanikorisnik.objects.get(idkor=request.user)

    if request.method == 'POST':
        exhibition_name = request.POST['ime']
        description = request.POST['opis']

        nfts_objects, exhibition_size, exhibition_value, exhibition_avg_grades = get_updated_exhibition_attr(request)

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

        return render(request, 'operation_on_exhibition_success.html')

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
    if exhibition_list.idvla.idkor != request.user:
        return redirect("error")

    belong = Pripada.objects.filter(idlis=exhibition_list)
    exhibition_nfts = [b.idnft for b in belong]

    if request.method == "POST":

        nfts_objects, exhibition_size, exhibition_value, exhibition_avg_grades = get_updated_exhibition_attr(request)

        exhibition_list.brojnft = exhibition_size
        exhibition_list.ukupnavrednost = exhibition_value
        exhibition_list.save()

        exhibition = Izlozba.objects.get(idlis=exhibition_list)
        exhibition.prosecnaocena = exhibition_avg_grades
        exhibition.save()

        [belong_obj.delete() for belong_obj in belong if belong_obj.idnft not in nfts_objects]

        belong = [
            Pripada(idlis=exhibition_list, idnft=nft_object) for nft_object in nfts_objects if
            nft_object not in exhibition_nfts
        ]

        for belong_obj in belong:
            belong_obj.save()
        return render(request, 'operation_on_exhibition_success.html')

    else:

        user = Registrovanikorisnik.objects.get(idkor=request.user)

        collection_user = get_user_collection(user)

        collection_nfts = get_nfts_from_collection(collection_user)

        context = create_context_for_nfts(collection_nfts)

        nft_list = context['nfts']
        for nft in nft_list:
            if nft['nft'] in exhibition_nfts:
                nft['select'] = True
            else:
                nft['select'] = False

        return render(request, 'change_exhibition.html', context)


def exhibition_review(request, exhibition_id):
    if request.method == 'POST':
        sort = request.POST.get('sort', None)
        exhibition_id = request.POST.get('id', None)
    exhibition_dict = dict()

    exhibition_list = Listanft.objects.get(idlis=exhibition_id)
    exhibition = Izlozba.objects.get(idlis=exhibition_list)

    #exhibition_dict["owner_image"] = user.slika.url
    exhibition_dict["name"] = exhibition.naziv
    exhibition_dict["value"] = exhibition_list.ukupnavrednost
    exhibition_dict["avg_grade"] = exhibition.prosecnaocena
    exhibition_dict["date"] = exhibition.datumkreiranja
    exhibition_dict["id"] = exhibition_id
    nfts = get_nfts_from_exhibition(exhibition)
    if request.method == 'POST':
           nfts = sort_nfts(nfts,sort)
    context = create_context_for_nfts(nfts)

    context["exhibition"] = exhibition_dict

    context["owner"] = exhibition_list.idvla.idkor

    return render(request, "exhibition_review.html", context)

def sort_exhibition(request):
    print("sortiraaaj")
    sort = request.POST.get('sort', None)
    exhibition_id = request.POST.get('id', None)
    exhibition_dict = dict()
    exhibition_list = Listanft.objects.get(idlis=exhibition_id)
    exhibition = Izlozba.objects.get(idlis=exhibition_list)

    #exhibition_dict["owner_image"] = user.slika.url
    exhibition_dict["name"] = exhibition.naziv
    exhibition_dict["value"] = exhibition_list.ukupnavrednost
    exhibition_dict["avg_grade"] = exhibition.prosecnaocena
    exhibition_dict["date"] = exhibition.datumkreiranja
    exhibition_dict["id"] = exhibition_id
    nfts = get_nfts_from_exhibition(exhibition)
    nfts = sort_nfts(nfts,sort)
    context = create_context_for_nfts(nfts)
    context["exhibition"] = exhibition_dict
    context["owner"] = exhibition_list.idvla.idkor
    return render(request, "exhibition_review.html", context)

@login_required(login_url='/accounts/error')
@user_passes_test(is_creator_or_collector, login_url='/accounts/error')
def remove_exhibition(request):
    if request.method == "POST":
        exhibition_id = request.POST["exhibition_id"]
        exhibition_list = Listanft.objects.get(idlis=exhibition_id)

        exhibition = Izlozba.objects.get(idlis=exhibition_list)
        belong = Pripada.objects.filter(idlis=exhibition_list)
        belong.delete()
        exhibition.delete()
        exhibition_list.delete()

        return render(request, 'operation_on_exhibition_success.html')

    else:
        return HttpResponseNotAllowed(['POST'])
