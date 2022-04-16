class UserData:
    """This class contains data about watched movies
        and preferred genres"""
    watchedMovies = []
    genresDict = {}
    otherInf = 0
    coefficient = 0
    id = 0

    def __init__(self, watchedMovies, genresDict, otherInf, id):
        self.watchedMovies = watchedMovies
        self.genresDict = genresDict
        self.otherInf = otherInf
        self.id = id
        pass


class Film:
    """Класс содержащий url фильма, количество рассматриваемых пользователей
    и среднюю оценку фильма среди рассматриваемых пользователей"""
    url = ""
    watched_count = 0
    summary_mark = 0
    mark = 0 if watched_count == 0 else summary_mark/watched_count

    def __init__(self, url):
        self.url = url
        pass


"""otherInf - доп информация; так как её нельзя использовать для формул, я её отделил"""
genreList = {"drama", "action", "comedy"}
sim_cef_adding = 0.5
const_count = 100
count_of_recommendation = 10
"""Список фильмов"""
similar_group = []
users = []
""" Genres: drama, action, comedy
    Others: favorite_director, favorite_actor"""

u1WM = {"fight-club": 5, "up": 4, "dune": 4, "dark-knight": 3, "godfather": 1, "godfather-second": 2}
u1GD = {"drama": 1, "action": 3, "comedy": 5}
u1OI = { "favorite_director": "Martin Scorcese", "favorite_actor": "Ryan Gosling"}
u1ID = 1
user1 = UserData(u1WM, u1GD, u1OI, u1ID)

u2WM = {"fight-club": 5, "up": 5, "dune": 3, "dark-knight": 1, "godfather-second": 2, "schindlers-list": 5}
u2GD = {"drama": 5, "action": 4, "comedy": 1}
u2OI = { "favorite_director": "Martin Scorcese", "favorite_actor": "Ryan Gosling"}
u2ID = 2
user2 = UserData(u2WM, u2GD, u2OI, u2ID)


def flat_dist(main_object, subject):
    """Нахождение расстояния на n-мерном пространстве"""
    distance = 0

    for genre in genreList:
        distance += abs(main_object.genresDict[genre] - subject.genresDict[genre])**2

    return distance


def sim_cef(main_object, subject):
    """Нахождение коэффициента схожести"""
    cef = 0
    k = 0
    subject_movies = subject.watchedMovies.keys()
    object_movies = main_object.watchedMovies.keys()

    for markedMovie in object_movies:
        k += 1
        if markedMovie in subject_movies:
            cef += 0.5**abs(main_object.watchedMovies[markedMovie] - subject.watchedMovies[markedMovie])

    return sim_cef_adding + cef/k


def add_to_group(main_object, subject, rec_group):
    """Присваивание неглавному пользователю итогового коэффициента
    и добавление неглавного пользователя в необработанный массив с пользователями"""
    subject.coefficient = flat_dist(main_object, subject) / sim_cef(main_object, subject)
    rec_group.append(subject)


def user_construct(id_of_user):
    """Тело для образования объекта по данным"""
    comp_user = UserData()
    return comp_user


def group_analysis(rec_group, count):
    """Обработка массива с пользователями:
    сортировка по уменьшению коэффциента и обрезание лишних пользователей"""
    rec_group = sorted(rec_group, key=lambda subject: subject.coefficient, reverse=True)
    if len(rec_group) > count:
        rec_group = rec_group[:count]

    return rec_group


def enumeration_of_users(main_object, subject_id_list):
    """Перебор пользователей для образования обработанной группы пользователей"""
    rec_group = []
    for id_of_subject in subject_id_list:
        subject = user_construct(id_of_subject)
        add_to_group(main_object, subject, rec_group)
    group_analysis(rec_group, const_count)
    return rec_group


def construct_film(url_of_film, subject):
    """Основа для объекта класса Film"""
    comp_film = Film(url_of_film)
    comp_film.summary_mark += subject.watchedMovies(url_of_film)
    comp_film.watched_count += 1
    return comp_film


def get_recommendation(main_object, rec_group):
    """Получение списка рекомандаций для пользователя на основе его рекомендационной группы"""
    recommendation_list = []
    list_of_films = []
    for subject in rec_group:
        for url_of_film in subject.watchedMovies.keys():
            if len(list(filter(lambda film: film.url == url_of_film, list_of_films))) != 0:
                next(film for film in list_of_films if film.url == url_of_film).watched_count += 1
                next(film for film in list_of_films if film.url == url_of_film).summary_mark += subject.watchedMovies(url_of_film)
            else:
                list_of_films.append(construct_film(url_of_film, subject))
    list_of_films = sorted(list_of_films, key=lambda film: film.mark)
    for film in list_of_films:
        if film.url not in main_object.watchedMovies.keys():
            recommendation_list.append(film.url)
    return recommendation_list[:count_of_recommendation]


def recommendation(id_object, list_of_id):
    """Функция рекомендации (финальная часть)"""
    main_object = user_construct(id_object)
    return get_recommendation(main_object, enumeration_of_users(main_object, list_of_id))


print()