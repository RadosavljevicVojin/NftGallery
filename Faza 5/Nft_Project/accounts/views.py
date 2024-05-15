from MySQLdb import IntegrityError, Date
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from pyexpat.errors import messages

from .utils import check_data_for_registration
# Create your views here.
from .models import Zahtevzaregistraciju, Korisnik, CustomUserManager
from profiles.models import Registrovanikorisnik, Kupac, Kreator, Kolekcionar




def logout_view(request):

    logout(request)
    redirect('index')
def login_page(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']


        user= authenticate(request, username=username, password=password)
        print(user, username, password)

        if user is not None:
            login(request, user)
            print("Logged in successfully")
            return redirect('index')  # Preusmeri korisnika na početnu stranicu nakon uspešnog logina
        else:
            print("Nema korisnika sa tim usenamemom")
            return redirect('register')

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
            message = check_data_for_registration(username,birthdate, birthplace,first_name,last_name, phone_number, password, confirm_password, email, card)
            if message=="":
                new_request = Zahtevzaregistraciju(korime=username, ime= first_name, prezime=last_name, sifra=password,
                                                       email= email, brojtelefona=phone_number, brojkartice=card,
                                                       datumrodjenja=birthdate, mestorodjenja=birthplace, uloga=user_type)

                new_request.save()
                return redirect('index')

        except IntegrityError as e:
             message = "Greška pri unosu u bazu: " + str(e)
        return render(request, 'signin.html', {'error': message})

    return render(request, 'signin.html')


#Natalija
#Odobravanje zahteva - brisanje iz baze zahtevi, ukoliko je prijavljen pravljenje novog Korisnika
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
            # pravljenje korisnika- pa onda Regsitrovanog pa onda tip

            user= Korisnik(username=request_to_accept.korime, user_type=request_to_accept.uloga)
            user.set_password(request_to_accept.sifra)
            user.save()
            reg_user=  Registrovanikorisnik(ime=request_to_accept.ime,
                                            prezime=request_to_accept.prezime, brojkartice=request_to_accept.brojkartice,
                                            brojtelefona=request_to_accept.brojtelefona, datumrodjenja=request_to_accept.datumrodjenja,
                                            mestorodjenja=request_to_accept.mestorodjenja, email=request_to_accept.email, idkor=user, slika= "PUTANJA DO SLIKE PROMENITI")

            reg_user.save()

            if  request_to_accept.uloga=="kreator":
                role= Kreator(idkor=reg_user.idkor.idkor)
                role.save()

            elif request_to_accept.uloga=="kupac":
                role = Kupac(idkor=reg_user.idkor)
                role.save()
            elif request_to_accept.uloga=="kolekcionar":
                role = Kolekcionar(idkor=reg_user.idkor.idkor)
                role.save()
            request_to_accept.delete()

        elif action == 'reject':
            # Logika za jednostavno brisanje zahtjeva
            Zahtevzaregistraciju.objects.filter(idzah=id).delete()

    requests = Zahtevzaregistraciju.objects.all()
    print(requests)

    return render(request, 'registration_request.html', {'zahtevi': requests})

