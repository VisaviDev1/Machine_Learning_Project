from django.db import models
from datetime import date

class Category(models.Model):
    name = models.CharField('Категория', max_length = 150)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Actor(models.Model):
    name = models.CharField('Имя', max_length = 100)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Актеры и режиссеры'
        verbose_name_plural = 'Актеры и режиссеры'

class Genre(models.Model):
    name = models.CharField('Имя', max_length = 100)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

class MovieFull(models.Model):
    title = models.CharField('Название', max_length = 100)
    tagline = models.CharField('Слоган', max_length = 100, default = '')
    year = models.PositiveIntegerField('Дата выхода', default = 1900)
    country = models.CharField('Страна', max_length = 100)
    genres = models.ManyToManyField(Genre, verbose_name = 'жанры')
    directors = models.ManyToManyField(Actor, verbose_name = 'режиссёр', related_name = 'film_director')
    screenwriters = models.ManyToManyField(Actor, verbose_name = 'сценарист', related_name = 'film_screenwriter')
    producer = models.ManyToManyField(Actor, verbose_name = 'продюсер', related_name = 'film_producer')
    actors = models.ManyToManyField(Actor, verbose_name = 'актёры', related_name = 'film_actor')
    budget = models.PositiveIntegerField('Бюджет', default = 0)
    fees = models.PositiveIntegerField('Сборы в мире', default = 0)
    category = models.ForeignKey(Category, verbose_name = 'Категория', on_delete = models.SET_NULL, null = True)
    discription = models.TextField('Описание')
    hours = models.PositiveIntegerField('Часы', default = 0)
    minutes = models.PositiveIntegerField('Минуты', default = 0)
    rating = models.CharField('Рейтинг', max_length = 3, default = '')
    ratingimdb = models.PositiveIntegerField('Рейтинг IMDb', default = 0)
    age = models.PositiveIntegerField('Возраст', default = 0)
    poster = models.ImageField('Постер', upload_to = 'movies/')
    url = models.SlugField(max_length = 150, unique = True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

class MovieShort(models.Model):
    title = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to = 'movie_shorts/')
    movie = models.ForeignKey(MovieFull, verbose_name = 'Фильм', on_delete = models.SET_NULL, null = True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Краткое описание фильма'
        verbose_name_plural = 'Краткое описание фильмов'  

class Reviews(models.Model):
    email = models.EmailField('Почта')
    movie = models.CharField('Фильм', max_length = 100)
    mark = models.PositiveIntegerField('Оценка', default = 0)
    def __str__(self):
        return f'{self.mark} - {self.movie} - {self.email}'
    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'

class Selfdata(models.Model):
    email = models.EmailField('Почта')
    login = models.CharField('Логин', max_length = 50)
    password = models.CharField('Пароль', max_length = 5000)
    def __str__(self):
        return self.login
    class Meta:
        verbose_name = 'Личные данные'
        verbose_name_plural = 'Личные данные'