from MySQLdb import IntegrityError, Date
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from pyexpat.errors import messages

from .utils import check_data_for_registration
# Create your views here.
from .models import Zahtevzaregistraciju, Korisnik

def login_page(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        users = Korisnik.objects.all()
        print("users",users)

        # user= authenticate(request, username=username, sifra=password)
        # print(user, username, password)
        #
        # if user is not None:
        #     login(request, user)
        #     print("Logged in successfully")
        #     return redirect('home')  # Preusmeri korisnika na početnu stranicu nakon uspešnog logina
        # else:
        #     print("NOT Logged in successfully")
        #
        #     return redirect('register')

    return render(request, 'login.html')




    return render(request, 'login.html')


# Natalija
# Registracija - prikaz stranice za registraciju i pravljenje zahteva za registraciju
def register_page(request):

    if request.method == 'POST':
        try:
            print("post")
        # Submit dugme je pritisnuto : 1. Povuci podatke iz forme 2. Proveriti podatke iz forme 3.Poslati zahtev za registraciju ukoliko su validni
            username = request.POST['username']
            birthdate = request.POST['birthdate']
            birthplace= request.POST['birthplace']
            first_name = request.POST['name']
            last_name = request.POST['surname']
            phone_number = request.POST['phone']
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']
            email = request.POST['email']
            card= request.POST['card']
            user_type = request.POST['user_type']

            print("1")

            message = check_data_for_registration(username,birthdate, birthplace,first_name,last_name, phone_number, password, confirm_password, email, card)
            if message=="":
                print("2")
                new_request = Zahtevzaregistraciju(korime=username, ime= first_name, prezime=last_name, sifra=password,
                                                       email= email, brojtelefona=phone_number, brojkartice=card,
                                                       datumrodjenja=birthdate, mestorodjenja=birthplace, uloga=user_type)

                new_request.save()
                print("3")
                return redirect('index')

        except IntegrityError as e:
             message = "Greška pri unosu u bazu: " + str(e)

        return render(request, 'signin.html', {'error': message})



    return render(request, 'signin.html')


def registration_request(request):
    if request.method == 'POST':
        for key, value in request.POST.items():
            print(f"{key}: {value}")

        all_keys = list(request.POST.keys())  # Pretvaranje ključeva u listu
        action= ""
        id= ""
        if len(all_keys) > 1:
            second_key = all_keys[1]
            action, id= second_key.split('-')

        if action == 'accept':
            request_to_accept = Zahtevzaregistraciju.objects.get(idzah=id)
            # Implementirajte logiku za stvaranje korisnika s podacima iz request_to_accept objekta
            request_to_accept.delete()

        elif action == 'reject':
            # Logika za jednostavno brisanje zahtjeva
            Zahtevzaregistraciju.objects.filter(idzah=id).delete()

    requests = Zahtevzaregistraciju.objects.all()
    print(requests)

    return render(request, 'registration_request.html', {'zahtevi': requests})

