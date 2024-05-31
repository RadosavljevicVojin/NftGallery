from io import BytesIO
from django.core.files import File
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect
import requests
from common.decoraters import is_creator
from .utils import *
from urllib.parse import urlparse
from django.http import JsonResponse

# Obavezno se dodaje u Header Request-a
API_KEY = "e0d9ad00e95945918aec9ec56c057650"

# Ova funkcija ce mozda trebati da bi se od url koji se cuva u bazi mogla dobiti slika i podaci
# Pozove se ova funkcija sa zadatim url-om i koristi se na sledeci nacin:
# nft = Nft.object.get(idnft = ...)
# nft_url = nft.url
# data = get_nft_data(nft_url)
# data.nft.image_url -> url koji se stavlja u src atribut za slike u .html fajlovima

def get_nft_data(nft_url):
    parsed_url = urlparse(nft_url)
    path_parts = parsed_url.path.split('/')
    chain = path_parts[-3]
    nft_contract_address = path_parts[-2]
    nft_token_id = path_parts[-1]

    api_url = 'https://api.opensea.io/api/v2/chain/' + chain + '/contract/' + nft_contract_address + '/nfts/' + nft_token_id
    headers = {
        "Accept": "application/json",
        "X-API-KEY": "e0d9ad00e95945918aec9ec56c057650"
    }

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return None




def fetch_nft_image_url(nft_url):
    # Razbijte URL na delove
    parts = nft_url.split('/')
    token_id = parts.pop()  # Poslednji element u nizu
    contractAddress = parts.pop()  # Pretposlednji element u nizu
    chain = parts.pop()

    # OpenSea API Endpoint za preuzimanje NFT metapodataka
    api_url = f'https://api.opensea.io/api/v2/chain/{chain}/contract/{contractAddress}/nfts/{token_id}'
    if chain == "base":
        api_url = f'https://api.opensea.io/api/v2/chain/{chain}/contract/{contractAddress}/nfts/'


    # Postavite zaglavlja
    headers = {
        'X-API-KEY': 'e0d9ad00e95945918aec9ec56c057650',
        'Content-Type': 'application/json',
    }

    # Pošaljite GET zahtev
    response = requests.get(api_url, headers=headers)

    # Proverite da li je zahtev uspešan
    if response.status_code == 200:
        data = response.json()
        # Pretpostavimo da je struktura odgovora ista kao u vašem JS kodu
        if "nft" in data:
            return data['nft']['image_url']
        else:
            return None
    else:
        print("Greška prilikom preuzimanja podataka:", response.status_code)
        return None


def check_nft_param(file, nft_url, name, price, description, creator, owner):
    message = ""
    if file is None and nft_url =="":
        message += "Morate ucitati sliku Nft!\n"
    if not name or name.strip() == "":
        message += "Ime mora biti uneto!\n"
    if Nft.objects.filter(naziv=name).exists():
        message += "Ime vec postoji!\n"
    try:
        price = float(price)
        if price <= 0:
            message += "Cena mora biti veća od 0!\n"
    except ValueError:
        message += "Cena mora biti broj!\n"
    if description is None or len(description.strip()) == 0:
        message += "Opis mora biti unet!\n"
    if len(name) >= 20:
        message += "Ime mora biti manje od 20 karaktera!\n"
    if len(description) >=1024:
        message += "Opis mora biti manji od 1024 karaktera!\n"

    return message

@login_required(login_url='/accounts/error')
@user_passes_test(is_creator, login_url='/accounts/error')
def create_nft(request):
    if request.method == 'POST':
        if "fileUpload" in request.FILES:
            file = request.FILES["fileUpload"]
        else:
            file = None
        if "nft_url" in request.POST:
            nft_url = request.POST["nft_url"]
        else:
            nft_url = None

        name = request.POST["nftName"]
        price = request.POST["nftPrice"]
        description = request.POST["nftDescription"]

        creator = Registrovanikorisnik.objects.get(idkor=request.user)
        owner = creator

        # Provera da li su dobro uneti parametri
        message = check_nft_param(file, nft_url, name, price, description, creator, owner)
        if message == "":
            # Napravi objekat nft sa datim parametrima i sacuva ga u bazi
            price = float(price)
            if file is not None:
                nft = Nft(naziv=name, vrednost=price, opis=description, prosecnaocena=0, slika=file, idkre=creator, idvla=owner, url="")
            else:

                image_url = fetch_nft_image_url(nft_url)
                response = requests.get(image_url)
                if response.status_code == 200:
                    # Otvaranje slike u memoriji
                    img_temp = BytesIO(response.content)
                    img_temp.seek(0)
                    max_idnft = Nft.objects.all().aggregate(Max('idnft'))['idnft__max']
                    next_id = (max_idnft or 0) + 1
                    image_file = File(img_temp, name=str(name)+str(next_id)+".jpg")
                    nft = Nft(naziv=name, vrednost=price, opis=description, prosecnaocena=0, slika=File(image_file), idkre=creator, idvla=owner,
                              url="")

            nft.save()

            creator_lists = Listanft.objects.filter(idvla=creator)
            all_collections = Kolekcija.objects.all()
            for creator_list in creator_lists:
                for collection in all_collections:
                    if creator_list == collection.idlis:

                        belong = Pripada(idlis=creator_list, idnft=nft)
                        belong.save()

                        creator_list.ukupnavrednost += nft.vrednost
                        creator_list.brojnft += 1
                        creator_list.save()

            if request.user.user_type == 'kreator':
                all_portfolios = Portfolio.objects.all()
                for creator_list in creator_lists:
                    for portfolio in all_portfolios:
                        if creator_list == portfolio.idlis:

                            belong = Pripada(idlis=creator_list, idnft=nft)
                            belong.save()

                            creator_list.ukupnavrednost += nft.vrednost
                            creator_list.brojnft += 1
                            creator_list.save()

            return redirect('index')

        else:
            messages.error(request, message)
            return render(request, 'create_nft.html', {})

    return render(request, 'create_nft.html')


def nft_review(request, idnft):
    nft = Nft.objects.get(idnft=idnft)

    if denied_access_to_the_nft(request, nft):
        return redirect("error")

    nft_data = {
        'nft': nft,
        'data': None
    }

    context = {"nft": nft_data}
    context["owner"] = nft.idvla.idkor
    context["creator"] = nft.idkre.idkor

    return render(request, 'nft_review.html', context)


from django.db.models import Avg, Max


@login_required(login_url='/accounts/error')
def grade_nft(request):
    if request.method == 'POST':
        if 'rating' in request.POST:
            rating = int(request.POST['rating'])
        else:
            rating = None
        idnft = int(request.POST['idnft_name'])
        nft = Nft.objects.get(idnft=idnft)
        ocenio = Registrovanikorisnik.objects.get(idkor=request.user)

        context = dict()

        nft_data = {
            'nft': nft,
            'data': None
        }
        ##if nft.slika == "":
            ##nft_data['data'] = get_nft_data(nft.url)

        context = {"nft": nft_data}
        context["owner"] = nft.idvla.idkor
        context["creator"] = nft.idkre.idkor


        #provera rejtinga
        if first_time_grading(idnft, ocenio):

            if rating is not None and 0 < rating < 6:

                ocena = Ocena(ocena=rating, idnft=nft, idkor=ocenio)

                ocena.save()

                prosecna_ocena = Ocena.objects.filter(idnft=nft).aggregate(avg_rating=Avg('ocena'))['avg_rating']

                nft.prosecnaocena = prosecna_ocena
                nft.save()

                update_nft_all_exhibitions_with_grades(nft)

                messages.success(request, "Uspešno ste ocenili NFT!")
                return render(request, 'nft_review.html', context)

            else:
                messages.error(request, "Morate izabrati ocenu!")
                return render(request, 'nft_review.html', context)

        else:
            # Logika kako da obavestim korisnika da je vec ocenio
            messages.error(request, "Vec ste ocenili ovaj NFT!")
            return render(request, 'nft_review.html', context)


    else:
        return HttpResponseNotAllowed(['POST'])

    #return render(request, 'nft_review.html', {'idnft': request.GET.get('idnft')})


@login_required(login_url='/accounts/error')
def change_price(request):
    if request.method == 'POST':
        nova_cena = float(request.POST['new_price'])
        idnft = int(request.POST['idnft_name'])
        nft = Nft.objects.get(idnft=idnft)

        nft_data = {
            'nft': nft,
            'data': None
        }
        #if nft.slika == "":
           #nft_data['data'] = get_nft_data(nft.url)

        context = {"nft": nft_data}
        context["owner"] = nft.idvla.idkor
        context["creator"] = nft.idkre.idkor

        if nova_cena is not None and nova_cena != '':
            stara_cena = nft.vrednost
            nft.vrednost = nova_cena
            nft.save()

            nft_se_nalazi = Pripada.objects.filter(idnft=nft)
            liste = [l.idlis for l in nft_se_nalazi]
            for l in liste:
                l.ukupnavrednost += nova_cena - stara_cena
                l.save()

        return render(request, 'nft_review.html', context)

    else:
        return HttpResponseNotAllowed(['POST'])

    #return render(request, 'nft_review.html', {'idnft': request.GET.get('idnft')})
def buy_nft(request):
    if request.method == 'POST':
        idnft = int(request.POST['idnft_name'])
        nft = Nft.objects.get(idnft=idnft)

        platio = Registrovanikorisnik.objects.get(idkor=request.user)

        platio.kupljenihNFT += 1

        platio.save()

        prosli_vlasnik = nft.idvla

        prosli_vlasnik.prodatihNFT += 1

        prosli_vlasnik.save()
        nft.idvla = platio

        nft.save()

        prosli_vlasnik_kolekcije = Listanft.objects.filter(idvla=prosli_vlasnik)

        for kol in prosli_vlasnik_kolekcije:

            # Nista ne radi ako je portfolio u pitanju
            if not Portfolio.objects.filter(idlis=kol).exists():

                # Ako je kolekcija ili izlozba kojoj nft pripada
                if (Kolekcija.objects.filter(idlis=kol).exists() or
                        (Izlozba.objects.filter(idlis=kol).exists() and Pripada.objects.filter(idlis=kol,
                                                                                               idnft=nft).exists())):

                    # Obrisi nft iz liste
                    Pripada.objects.filter(idlis=kol, idnft=nft).delete()

                    if Izlozba.objects.filter(idlis=kol).exists():
                        izlozba = Izlozba.objects.get(idlis=kol)

                        # Dodato za brisanje izlozbe ako se kupi poslednji nft iz izlozbe
                        if kol.brojnft == 1:
                            izlozba.delete()
                            kol.delete()
                            continue

                        else:
                            nft_izlozbe = get_nfts_from_exhibition(izlozba)
                            update_exhibition_grade(izlozba, nft_izlozbe)

                    kol.ukupnavrednost -= nft.vrednost
                    kol.brojnft -= 1
                    kol.save()


        platio_kolekcija = Listanft.objects.filter(idvla=platio)
        for kol in platio_kolekcija:
            if Kolekcija.objects.filter(idlis=kol).exists():
                Pripada.objects.create(idlis=kol, idnft=nft)
                kol.ukupnavrednost += nft.vrednost
                kol.brojnft += 1
                kol.save()


        # Treba da se doda da se u svakoj izlozbi promeni atributi
        nft_data = {
            'nft': nft,
            'data': None
        }
        #if nft.slika == "":
         #   nft_data['data'] = get_nft_data(nft.url)

        context = {"nft": nft_data}
        context["owner"] = nft.idvla.idkor
        context["creator"] = nft.idkre.idkor

        return render(request, 'nft_review.html', context)

    else:
        return HttpResponseNotAllowed(['POST'])


def nft_view_ajax(request):
    if request.method == 'POST':
        idnft = int(request.POST['idnft_name'])
        nft = Nft.objects.get(idnft=idnft)
        print("update nft price")
        response_data = {
            'vrednost': nft.vrednost,
            'ocena':nft.prosecnaocena
        }
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


