from django.shortcuts import render

# Create your views here.


def login_page(request):
    # Dohvati sve izložbe i sortiraj ih po željenom kriteriju (npr. po datumu)
   # exhibitions = Izloba.objects.all()

    # context = {
    #     'exhibitions': exhibitions
    # }

    return render(request, 'login.html')