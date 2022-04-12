from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from reviewaggregator.views import Login, Movie, Home, Movies, Series, Cartoons

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', Login.get),
    path('home/', Home.get),
    path('movies/', Movies.get),
    path('series/', Series.get),
    path('cartoons/', Cartoons.get),
    path('<slug:slug>/', Movie.get)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


handler403 = 'reviewaggregator.views.handler403'
handler404 = 'reviewaggregator.views.handler404'
handler500 = 'reviewaggregator.views.handler500'
