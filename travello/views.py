from django.shortcuts import render
from .models import Destination
# Create your views here.

def index(request):

    dest1 = Destination()
    dest1.name = 'Dhaka'
    dest1.desc = 'The City That Naver Sleeds'
    dest1.img = 'destination_1.jpg'
    dest1.price = 100
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Chattogram'
    dest2.desc = 'Chittagong is large port city on the southeastern coast of Bangladesh'
    dest2.img = 'destination_2.jpg'
    dest2.price = 150
    dest2.offer = False

    dest3 = Destination()
    dest3.name = 'Rajshahi'
    dest3.desc = 'Rajshahi is a historic center of silk production And Clean City'
    dest3.img = 'destination_3.jpg'
    dest3.price = 120
    dest3.offer = True

    dests = [dest1, dest2, dest3]

    return render(request, 'index.html', {'dests':dests})
