from django.contrib import admin
from .models import Movie
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('movie_name', 'director', 'actor', 'category', 'description', 'rating', 'time', 'premiere_date', 'trailer', 'is_available','show_date', 'show_number', 'cinema_room', 'ticket_fare','seat_number')
    prepopulated_fields = {'slug': ('movie_name',)}
admin.site.register(Movie, MovieAdmin)