from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render

from accounts.models import Korisnik
from exhibitions.models import Listanft, Pripada
from nft.models import Nft
from nft.views import get_nft_data
from profiles.models import Registrovanikorisnik
from profiles.utils import create_main_context


# Create your views here.

#Natalija
# prikaz informacija o profilu, preko searcja, preko buttona moj ptofil- to je else deo - get zahtev
def view_profile_info(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        if username:
            if Korisnik.objects.filter(username=username).exclude(user_type='admin').exists():
                context = create_main_context(request, username)
                return render(request, 'profile_info.html', context)
            else:
                return render(request, "index.html", {"message": True})
    else:
        context = create_main_context(request, request.user.username)

        card = str(Registrovanikorisnik.objects.get(idkor=request.user).brojkartice)
        last_3_digits = card[-3:]
        new_card_view = '*' * (len(card) - 3) + last_3_digits
        context['phone']= Registrovanikorisnik.objects.get(idkor=request.user).brojtelefona
        context['card']= new_card_view
        context['name']= Registrovanikorisnik.objects.get(idkor=request.user).ime
        context['surname']= Registrovanikorisnik.objects.get(idkor=request.user).prezime
        context['birthplace']= Registrovanikorisnik.objects.get(idkor=request.user).mestorodjenja
        return render(request, 'profile_info.html', context)




def view_profile_portfolio(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        if username:
            if Korisnik.objects.filter(username=username).exclude(user_type='admin').exists():
                context = create_main_context(request, username)
                #  dopuniti kontekst ya informacije
                id = context["id"]
                listanft = Listanft.objects.filter(portfolio__isnull=False,idvla= id).first()
                print(listanft)
                pripada_ids = Pripada.objects.filter(idlis=listanft.idlis).values_list('idnft', flat=True)
                print(pripada_ids)
                nfts = Nft.objects.filter(idnft__in=pripada_ids)
                print(nfts)
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
                context["nfts"] = nft_list
                context["cena"] = cena
                return render(request, 'profile_portfolio.html', context)
        else:
            return HttpResponse("Molimo vas da unesete korisničko ime.")
    else:
        # deo za search treba staviti
        # Ukoliko nije POST zahtev, možemo prikazati formu za unos korisničkog imena ili redirectovati na drugu stranicu
        return HttpResponseNotAllowed(['POST'])




def view_profile_collection(request):
    if request.method == 'POST':
        print(request)
        username = request.POST.get('username', None)
        print(username)
        if username:
            if Korisnik.objects.filter(username=username).exclude(user_type='admin').exists():
                context = create_main_context(request, username)
                #  dopuniti kontekst ya informacije
                id = context["id"]
                print(id)
                nfts = Nft.objects.filter(idvla=id)
                print(nfts[0].naziv)
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
                context["nfts"] = nft_list
                context["cena"] = cena
                #context2 = {"nfts": nft_list,"image":context[]}
                return render(request, 'profile_collection.html', context)
        else:
            return HttpResponse("Molimo vas da unesete korisničko ime.")
    else:
        # deo za search treba staviti
        # Ukoliko nije POST zahtev, možemo prikazati formu za unos korisničkog imena ili redirectovati na drugu stranicu
        return HttpResponseNotAllowed(['POST'])
def view_profile_exhibitions(request):
    if request.method == 'POST':
        print(request)
        username = request.POST.get('username', None)
        print(username)
        if username:
            if Korisnik.objects.filter(username=username).exclude(user_type='admin').exists():
                context = create_main_context(request, username)
                #  dopuniti kontekst ya informacije

                return render(request, 'profile_exhibitions.html', context)
        else:
            return HttpResponse("Molimo vas da unesete korisničko ime.")
    else:
        # deo za search treba staviti
        # Ukoliko nije POST zahtev, možemo prikazati formu za unos korisničkog imena ili redirectovati na drugu stranicu
        return HttpResponseNotAllowed(['POST'])


def sort_profile_collection(request):
    if request.method == 'POST':
        print(request)
        username = request.POST.get('username', None)
        print(username)
        if username:
            if Korisnik.objects.filter(username=username).exclude(user_type='admin').exists():
                context = create_main_context(request, username)
                #  dopuniti kontekst ya informacije
                sort = request.POST.get('sort', None)
                id = context["id"]
                nfts = Nft.objects.filter(idvla=id)
                nft_list = []
                cena = request.POST.get('cena', None)
                if (sort == "poImenu"):
                    print("usao")
                    nfts = sorted(nfts, key=lambda nft: nft.naziv)
                elif (sort == "poOceni"):
                    nfts = sorted(nfts, key=lambda nft: nft.prosecnaocena)
                elif (sort == "poVelicini"):
                    pass
                elif (sort == "poVrednosti"):
                    nfts = sorted(nfts, key=lambda nft: nft.vrednost)
                for nft in nfts:
                    print(nft.naziv)
                    nft_data = {
                        'nft': nft,
                        'data': None
                    }
                    if nft.slika == "":
                        nft_data['data'] = get_nft_data(nft.url)
                    nft_list.append(nft_data)
                context["nfts"] = nft_list
                context["cena"] = cena
                pageType = request.POST.get('pageType', None)
                if pageType == "collection":
                  return render(request, 'profile_collection.html', context)
                else:
                  return render(request, 'profile_portfolio.html', context)
        else:
            return HttpResponse("Molimo vas da unesete korisničko ime.")
    else:
        # deo za search treba staviti
        # Ukoliko nije POST zahtev, možemo prikazati formu za unos korisničkog imena ili redirectovati na drugu stranicu
        return HttpResponseNotAllowed(['POST'])
