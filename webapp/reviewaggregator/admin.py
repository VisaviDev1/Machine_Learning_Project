from django.contrib import admin
from .models import Category, Actor, Genre, MovieFull, MovieShort, Reviews, Selfdata

admin.site.register(Category)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(MovieFull)
admin.site.register(MovieShort)
admin.site.register(Reviews)
admin.site.register(Selfdata)

