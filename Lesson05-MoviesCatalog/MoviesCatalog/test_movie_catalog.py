from Domain.Movie import Movie
from Service.MoviesCatalog import MoviesCatalog


option: str = ''
while option != '0':
    print('1) Add movie')
    print('2) List movies')
    print('3) Delete movies catalog')
    print('0) Exit')
    option = input('> ')

    if option == '1':
        name = input('Insert the movie\'s name: ')
        movie = Movie(name)
        MoviesCatalog.add_movie(movie)
    elif option == '2':
        MoviesCatalog.list_movies()
    elif option == '3':
        MoviesCatalog.delete()
