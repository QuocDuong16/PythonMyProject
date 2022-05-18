from django.shortcuts import render
from django.http import HttpResponse
from cinema.models import Movie
# Create your views here.
def home(request):
    movies = Movie.objects.all().filter(is_available=True)
    movies2 = Movie.objects.all().filter(is_available=False)
    if request.user.is_authenticated:
        check = True
        user = 'Hello ' + request.user.username
    else:
        check = False
        user = ""
    context = {
        "movies": movies,
        "movies2": movies2,
        'check': check,
        'user': user,
    }
    return render(request, 'index.html', context)

def error(request):
    if request.user.is_authenticated:
        check = True
        user = 'Hello ' + request.user.username
    else:
        check = False
        user = ""
    context = {
        'check': check,
        'user': user,
    }
    return render(request, '404.html', context)

def contact(request):
    if request.user.is_authenticated:
        check = True
        user = 'Hello ' + request.user.username
    else:
        check = False
        user = ""
    context = {
        'check': check,
        'user': user,
    }
    return render(request, 'contact.html', context)

