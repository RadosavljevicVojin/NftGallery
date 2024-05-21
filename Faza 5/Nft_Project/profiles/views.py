from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render

from accounts.models import Korisnik
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
                #  dopuniti kontekst ya informacije

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
                #  dopuniti kontekst ya informacije

                return render(request, 'profile_exhibitions.html', context)
        else:
            return HttpResponse("Molimo vas da unesete korisničko ime.")
    else:
        # deo za search treba staviti
        # Ukoliko nije POST zahtev, možemo prikazati formu za unos korisničkog imena ili redirectovati na drugu stranicu
        return HttpResponseNotAllowed(['POST'])