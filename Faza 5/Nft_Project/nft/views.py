from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, redirect

from common.decoraters import is_creator

from .models import Nft
from profiles.models import Registrovanikorisnik

import requests

from urllib.parse import urlparse

# Obavezno se dodaje u Header Request-a
API_KEY = "e0d9ad00e95945918aec9ec56c057650"

# Ova funkcija ce mozda trebati da bi se od url koji se cuva u bazi mogla dobiti slika i podaci
# Pozove se ova funkcija sa zadatim url-om i koristi se na sledeci nacin:
    # nft = Nft.object.get(idnft = ...)
    # nft_url = nft.url
    # data = get_nft_data(nft_url)
    # data.nft.image_url -> url koji se stavlja u src atribut za slike u .html fajlovima
"""
def get_nft_data(nft_url):
    parsed_url = urlparse(nft_url)
    path_parts = parsed_url.path.split('/')
    nft_contract_address = path_parts[-2]
    nft_token_id = path_parts[-1]

    api_url = 'https://api.opensea.io/api/v2/chain/ethereum/contract/' + nft_contract_address + '/nfts/' + nft_token_id
    headers = {
        "Accept": "application/json",
        "X-API-KEY": "e0d9ad00e95945918aec9ec56c057650"
    }

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return None

"""

def check_nft_param(file, name, price, description, creator, owner):
    # TODO
    return True;

@login_required(login_url='/accounts/error')
@user_passes_test(is_creator, login_url='/accounts/error')
def create_nft(request):

    if request.method == 'POST':
        if "fileUpload" in request.FILES:
            file = request.FILES["fileUpload"]
        else:
            file=None

        if "nft_url" in request.POST:
            nft_url = request.POST["nft_url"]
        else:
            nft_url=None


        name = request.POST["nftName"]
        price = request.POST["nftPrice"]
        description = request.POST["nftDescription"]

        creator = Registrovanikorisnik.objects.get(idkor=request.user)
        owner = creator

        #print("File: " + file)
        print("Name: " + name)
        print("Price: " + price)
        print("Description: " + description)

        # Provera da li su dobro uneti parametri
        if check_nft_param(file, name, price, description, creator, owner):

            # Napravi objekat nft sa datim parametrima i sacuva ga u bazi
            if file is not None:
                nft = Nft(naziv=name, vrednost=price, opis=description, slika=file, idkre=creator, idvla=owner,prosecnaocena=3.0, url="")
            else:
                nft = Nft(naziv=name, vrednost=price, opis=description, slika="", idkre=creator, idvla=owner,
                          prosecnaocena=3.0, url=nft_url)

            nft.save()

            # Display svih nft-ova u bazi
            """
            nfts = Nft.objects.all())
            return render(request,'preview.html', {'nfts':nfts})"""

            return redirect('index')

        else:
            #TODO
            print("Error")

    return render(request, 'create_nft.html')

