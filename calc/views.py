from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html', {'name':'M. A. MAMUN'})


def result(request):
    var1 = int(request.GET['num1'])
    var2 = int(request.GET['num2'])
    result = var1 + var2
    return render(request, 'result.html', {'result':result})
