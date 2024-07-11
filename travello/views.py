from django.shortcuts import render
from .models import Destination
# Create your views here.

def index(request):
    # dest3 = Destination()
    # dest3.name = 'Rajshahi'
    # dest3.desc = 'Rajshahi is a historic center of silk production And Clean City'
    # dest3.img = 'destination_3.jpg'
    # dest3.price = 120
    # dest3.offer = True
    # dests = [dest1, dest2, dest3]

    dests = Destination.objects.all()

    return render(request, 'index.html', {'dests':dests})
