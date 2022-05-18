from django.urls import path
from . import views
urlpatterns = [
    path('', views.movie, name='movie'),
    path('search/', views.search, name='search'),
    path('<slug:movie_slug>/', views.movie_detail, name='movie_detail'),
    path('search/<slug:movie_slug>/', views.movie_detail, name='movie_detail'),
]