from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Movie
from carts.models import Cart, CartItem
# Create your views here.
def movie(request):
    movies = Movie.objects.all().filter(is_available=True)
    movies2 = Movie.objects.all().filter(is_available=False)
    page = request.GET.get('page')
    page = page or 1
    paginator = Paginator(movies, 4)
    paged_movies = paginator.get_page(page)
    if request.user.is_authenticated:
        check = True
        user = 'Hello ' + request.user.username
    else:
        check = False
        user = ""
    context = {
        "movies": paged_movies,
        "movies2": movies2,
        'check': check,
        'user': user,
    }
    return render(request, 'movie/movies.html', context)

def movie_detail(request, movie_slug=None):
    if request.user.is_authenticated:
        check = True
        user = 'Hello ' + request.user.username
    else:
        check = False
        user = ""
    single_movie = Movie.objects.get(slug=movie_slug)
    context = {
        'single_movie': single_movie,
        'check': check,
        'user': user,
    }
    return render(request, 'movie/single.html', context)

def search(request):
    if 'q' in request.GET:
        q = request.GET.get('q')
        # search = Movie.objects.order_by('-id').filter(Q(movie_name__icontains=q) | Q(description__icontains=q))
        search = Movie.objects.order_by('-id').filter(Q(movie_name__icontains=q))
        movies = Movie.objects.all().filter(is_available=True)
        movies2 = Movie.objects.all().filter(is_available=False)
    page = request.GET.get('page')
    page = page or 1
    paginator = Paginator(search, 4)
    paged_search = paginator.get_page(page)
    if request.user.is_authenticated:
        check = True
        user = 'Hello ' + request.user.username
    else:
        check = False
        user = ""
    context = {
        'search': paged_search,
        'movies': movies,
        'q': q,
        'movies2': movies2,
        'check': check,
        'user': user,
    }
    return render(request, 'movie/search.html', context)