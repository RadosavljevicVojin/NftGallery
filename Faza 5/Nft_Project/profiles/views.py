from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.hashers import check_password
from pyexpat.errors import messages
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render

from accounts.models import Korisnik
from common.decoraters import is_not_admin
from exhibitions.models import Listanft, Pripada,Izlozba
from nft.models import Nft
from nft.views import get_nft_data
from profiles.models import Registrovanikorisnik
from profiles.utils import create_main_context
from django.contrib import messages
from profiles.utils import create_main_context,pack_nfts,pack_nfts_exhibitions,get_user_exhibitions,get_user_portfolio,get_user_collection,sort_user_exhibitions,sort_user_nfts



# Create your views here.

#Natalija
# prikaz informacija o profilu, preko searcja, preko buttona moj ptofil- to je else deo - get zahtev
def view_profile_info(request):
    print("usao u profil info")
    if request.method == 'POST':
        if 'username' in request.POST:

            username = request.POST.get('username', None)
            print(username)
            if username:
                if Korisnik.objects.filter(username=username).exclude(user_type='admin').exists():
                    context = create_main_context(request, username)
                    user = Korisnik.objects.get(username=username)

                    card = str(Registrovanikorisnik.objects.get(idkor=user).brojkartice)
                    last_3_digits = card[-3:]
                    new_card_view = '*' * (len(card) - 3) + last_3_digits
                    context['phone'] = Registrovanikorisnik.objects.get(idkor=user).brojtelefona
                    context['card'] = new_card_view
                    context['name'] = Registrovanikorisnik.objects.get(idkor=user).ime
                    context['surname'] = Registrovanikorisnik.objects.get(idkor=user).prezime
                    context['birthplace'] = Registrovanikorisnik.objects.get(idkor=user).mestorodjenja


                    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                        print("ajaxx")
                        return render(request, 'ajaxProfileInfo.html', context)
                    else:
                        print("vracam profil info")
                        return render(request, 'profile_info.html', context)
                else:
                    return render(request, "index.html", {"message": True})

        else:
            context = create_main_context(request, request.user.username)

            card = str(Registrovanikorisnik.objects.get(idkor=request.user).brojkartice)
            last_3_digits = card[-3:]
            new_card_view = '*' * (len(card) - 3) + last_3_digits
            context['phone'] = Registrovanikorisnik.objects.get(idkor=request.user).brojtelefona
            context['card'] = new_card_view
            context['name'] = Registrovanikorisnik.objects.get(idkor=request.user).ime
            context['surname'] = Registrovanikorisnik.objects.get(idkor=request.user).prezime
            context['birthplace'] = Registrovanikorisnik.objects.get(idkor=request.user).mestorodjenja

            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                print("ajaxxxxxx")
                return render(request, 'ajaxProfileInfo.html.html', context)
            else:
                return render(request, 'profile_info.html', context)

    else:
        # deo za search treba staviti
        # Ukoliko nije POST zahtev, možemo prikazati formu za unos korisničkog imena ili redirectovati na drugu stranicu
        return HttpResponseNotAllowed(['POST'])




def view_profile_portfolio(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        if username:
            if Korisnik.objects.filter(username=username).exclude(user_type='admin').exists():
                context = create_main_context(request, username)
                id = context["id"]
                nft_list,novaCena = get_user_portfolio(id)
                context["nfts"] = nft_list
                context["cena"] = novaCena
                return render(request, 'profile_portfolio.html', context)
        else:
            return HttpResponse("Molimo vas da unesete korisničko ime.")
    else:
        # deo za search treba staviti
        # Ukoliko nije POST zahtev, možemo prikazati formu za unos korisničkog imena ili redirectovati na drugu stranicu
        return HttpResponseNotAllowed(['POST'])




def view_profile_collection(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        if username:
            if Korisnik.objects.filter(username=username).exclude(user_type='admin').exists():
                context = create_main_context(request, username)
                id = context["id"]
                nft_list,novaCena = get_user_collection(id)
                context["nfts"] = nft_list
                context["cena"] = novaCena
                return render(request, 'profile_collection.html', context)
        else:
            return HttpResponse("Molimo vas da unesete korisničko ime.")
    else:
        # deo za search treba staviti
        # Ukoliko nije POST zahtev, možemo prikazati formu za unos korisničkog imena ili redirectovati na drugu stranicu
        return HttpResponseNotAllowed(['POST'])
def view_profile_exhibitions(request):
    if request.method == 'POST':

        username = request.POST.get('username', None)

        if username:
            if Korisnik.objects.filter(username=username).exclude(user_type='admin').exists():
                context = create_main_context(request, username)
                id = context["id"]
                izlozbe = get_user_exhibitions(id)
                context["izlozbe"] = izlozbe
                # context["typeOfSort"] = "poImenu"
                return render(request, 'profile_exhibitions.html', context)
        else:
            return HttpResponse("Molimo vas da unesete korisničko ime.")
    else:
        # deo za search treba staviti
        # Ukoliko nije POST zahtev, možemo prikazati formu za unos korisničkog imena ili redirectovati na drugu stranicu
        return HttpResponseNotAllowed(['POST'])


def sort_profile_collection(request):
    if request.method == 'POST':

        username = request.POST.get('username', None)

        if username:
            if Korisnik.objects.filter(username=username).exclude(user_type='admin').exists():
                context = create_main_context(request, username)
                sort = request.POST.get('sort', None)
                id = context["id"]
                cena = request.POST.get('cena', None)
                pageType = request.POST.get('pageType', None)
                if pageType == "collection":
                   nfts = sort_user_nfts(id,sort,"collection")
                else:
                    nfts = sort_user_nfts(id,sort,"portfolio")
                nft_list,novaCena = pack_nfts(nfts)
                context["nfts"] = nft_list
                context["cena"] = cena
                context["typeOfSort"] = sort
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

def sort_profile_exhibition(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        if username:
            if Korisnik.objects.filter(username=username).exclude(user_type='admin').exists():
                context = create_main_context(request, username)
                sort = request.POST.get('sort', None)
                id = context["id"]
                izlozbe = sort_user_exhibitions(id,sort)
                context["izlozbe"] = izlozbe
                for izlozba in izlozbe:
                    for nft in izlozba["nfts"]:
                        if nft["data"] == None:
                            print(nft["nft"].url)
                            print(nft["nft"].slika)
                            print("nije okej")
                        else:
                            print(nft["nft"].slika)
                            print(nft["nft"].url)
                            print("okej")
                context["typeOfSort"] = sort
                return render(request, 'profile_exhibitions.html', context)
        else:
            return HttpResponse("Molimo vas da unesete korisničko ime.")
    else:
        # deo za search treba staviti
        # Ukoliko nije POST zahtev, možemo prikazati formu za unos korisničkog imena ili redirectovati na drugu stranicu
        return HttpResponseNotAllowed(['POST'])
def exhibition_view_ajax(request):
    print("AJAAXX")
    username = request.POST.get('username', None)
    print(username)
    if username:
        if Korisnik.objects.filter(username=username).exclude(user_type='admin').exists():
            context = create_main_context(request, username)
            sort = request.POST.get('sort', None)
            print(sort)
            id = context["id"]
            izlozbe = sort_user_exhibitions(id,sort)
            context["izlozbe"] = izlozbe
            return render(request,'ajaxExhibition.html',context)
def collection_view_ajax(request):
    print("AJAAXX")
    username = request.POST.get('username', None)
    print(username)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        print("jeste ajax")
    else:
        print("nije ajax")
    if username:
        if Korisnik.objects.filter(username=username).exclude(user_type='admin').exists():
            context = create_main_context(request, username)
            sort = request.POST.get('sort', None)
            pageType = request.POST.get('pageType', None)
            print(sort)
            id = context["id"]
            if pageType == "collection":
               nfts = sort_user_nfts(id,sort,"collection")
            elif pageType == "portfolio":
                nfts = sort_user_nfts(id,sort,"portfolio")
            print(pageType)
            nft_list, novaCena = pack_nfts(nfts)
            context["nfts"] = nft_list
            context["cena"] = novaCena
            if pageType == "collection":
              return render(request,'ajaxCollection.html',context)
            elif pageType == "portfolio":
              return render(request, 'ajaxPortfolio.html', context)



@login_required( login_url='/accounts/error')
def view_change_info(request):
    if request.method == 'POST':
        context = dict()
        user= request.user
        reguser= Registrovanikorisnik.objects.get(idkor=user)
        context["img"]= reguser.slika.url
    context = dict()
    user = request.user
    reguser = Registrovanikorisnik.objects.get(idkor=user)
    context["img"] = reguser.slika.url
    return render(request, 'change_profile_info.html', context)




@login_required( login_url='/accounts/error')
@user_passes_test(is_not_admin, login_url='/accounts/error')
def change_info(request):
    if request.method == 'POST':
        user = request.user
        old_password = request.POST['stara-lozinka']
        new_password = request.POST['nova-lozinka']
        confirm_password = request.POST['potvrda-lozinke']
        context={}
        if "fileUpload" in request.FILES:
            file = request.FILES["fileUpload"]
            reguser= Registrovanikorisnik.objects.get(idkor=user)
            if(reguser.slika!=file):
                reguser.slika= file
                reguser.save()
                messages.success(request, 'Slika je uspešno promenjena!')

        reguser = Registrovanikorisnik.objects.get(idkor=user)
        context["img"] = reguser.slika.url
        if old_password==""  and new_password=="" and confirm_password=="":
            return render(request, 'change_profile_info.html', context)

        if not check_password(old_password, user.password):
            messages.error(request, 'Stara lozinka nije ispravna!')


        elif new_password != confirm_password:
            messages.error(request, 'Lozinke se ne podudaraju. Molimo Vas unesite istu lozinku u oba polja!')

        else:
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Lozinka je uspešno promenjena!')
        return render(request, 'change_profile_info.html', context)

    return render(request, 'change_profile_info.html')
