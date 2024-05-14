

# exhibitions/views.py

from django.shortcuts import render

def home_page(request):
    # Dohvati sve izložbe i sortiraj ih po željenom kriteriju (npr. po datumu)
   # exhibitions = Izloba.objects.all()

    # context = {
    #     'exhibitions': exhibitions
    # }

    return render(request, 'index.html')
