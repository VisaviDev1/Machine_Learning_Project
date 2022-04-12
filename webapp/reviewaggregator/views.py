from django.shortcuts import render
from django.views.generic.base import View
from .models import MovieFull
from tmdbv3api import TMDb
import random

class Login(View):
    def get(request):
        return render(request, 'index.reg.html')

class Movie(View):
    def get(request, slug):
        movies = MovieFull.objects.get(url=slug)
        return render(request, 'index.description.html', {'movie': movies})

class Movies(View):
    def get(request):
        movies = MovieFull.objects.all().order_by('?')
        movies_new = MovieFull.objects.filter(year__gt=2020).order_by('?')
        movies_pop = MovieFull.objects.filter(fees__gt=200000000, year__gt=2020).order_by('?')
        movies_r = MovieFull.objects.filter(ratingimdb__gt=85).order_by('?')
        movies_fam = MovieFull.objects.filter(rating='PG').order_by('?')
        return render(request, 'index.movies.html', {'movies': movies, 'movies_new': movies_new, 'movies_r': movies_r, 'movies_pop': movies_pop, 'movies_fam': movies_fam})

class Series(View):
    def get(request):
        movies = MovieFull.objects.all()
        return render(request, 'index.series.html', {'movies': movies})

class Cartoons(View):
    def get(request):
        movies = MovieFull.objects.all()
        return render(request, 'index.cartoons.html', {'movies': movies})

class Home(View):
    def get(request):
        items = list(MovieFull.objects.all())
        movies = random.choice(items)
        return render(request, 'index.html', {'movie': movies})

def handler403(request, *args, **argv):
    return render(request, 'errs/403.html', status=403)

def handler404(request, *args, **argv):
    return render(request, 'errs/404.html', status=404)

def handler500(request, *args, **argv):
    return render(request, 'errs/500.html', status=500)