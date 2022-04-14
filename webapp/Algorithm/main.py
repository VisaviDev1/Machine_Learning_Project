class UserData:
    """This class contains data about watched movies
        and preferred genres"""
    watchedMovies = []
    genresDict = {}
    otherInf = 0

    def __init__(self, watchedMovies, genresDict, otherInf):
        self.watchedMovies = watchedMovies
        self.genresDict = genresDict
        self.otherInf = otherInf
        pass


"""otherInf - доп информация; так как её нельзя использовать для формул, я её отделил"""
genreList = {"drama", "action", "comedy"}
"""Список фильмов"""

users = []
""" Genres: drama, action, comedy
    Others: favorite_director, favorite_actor"""

u1WM = {"fight-club": 5, "up": 4, "dune": 4, "dark-knight": 3, "godfather": 1, "godfather-second": 2}
u1GD = {"drama": 1, "action": 3, "comedy": 5}
u1OI = { "favorite_director": "Martin Scorcese", "favorite_actor": "Ryan Gosling"}
user1 = UserData(u1WM, u1GD, u1OI)

u2WM = {"fight-club": 5, "up": 5, "dune": 3, "dark-knight": 1, "godfather-second": 2, "schindlers-list": 5}
u2GD = {"drama": 5, "action": 4, "comedy": 1}
u2OI = { "favorite_director": "Martin Scorcese", "favorite_actor": "Ryan Gosling"}
user2 = UserData(u2WM, u2GD, u2OI)


def coefficient_of_similarity(object, subject):
    R = 0
    for i in genreList:
        R += abs(object.genresDict[i] - subject.genresDict[i])






