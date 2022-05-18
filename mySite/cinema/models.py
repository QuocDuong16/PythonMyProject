from django.db import models
# Create your models here.
class Movie(models.Model):
    movie_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    director = models.CharField(max_length=100, null=True)
    actor = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=1000, null=True)
    rating = models.FloatField(null=True)
    image = models.ImageField(upload_to='photos/movies')
    time = models.IntegerField(null=True)
    category = models.CharField(max_length=200)
    premiere_date = models.DateTimeField(null=True)
    is_available = models.BooleanField(default=True)
    trailer = models.URLField(max_length = 200, null=True)
    show_date = models.DateTimeField()
    show_number = models.IntegerField(default=0)
    cinema_room = models.IntegerField(default=0)
    ticket_fare = models.IntegerField(default=0)
    seat_number = models.IntegerField(default=0)

    def __str__(self):
        return self.movie_name
