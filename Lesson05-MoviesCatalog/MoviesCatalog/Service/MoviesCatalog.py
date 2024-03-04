from MoviesCatalog.Domain.Movie import Movie


class MoviesCatalog:
    """
    Do operations over movies.txt file
    """
    _file_path = 'movies.txt'

    @staticmethod
    def add_movie(movie: Movie):
        exists = False
        with open(MoviesCatalog._file_path, 'a+', encoding='utf8') as fileMovies:
            for movie in fileMovies.readlines():
                if movie.__str__() == movie:
                    exists = True
                    break
            if not exists:
                fileMovies.write(f'{movie.__str__()}\n')
                print('MOVIE ADDED'.center(30, '-'))
                print(f'{movie.__str__()}')
                print(''.center(30, '-'))

    @staticmethod
    def list_movies():
        with open(MoviesCatalog._file_path, 'r', encoding='utf8') as fileMovies:
            print('MOVIES LIST'.center(30, '-'))
            print(f'{fileMovies.read()}')
            print(''.center(30, '-'))

    @staticmethod
    def delete():
        # to remove file
        # os.remove(MoviesCatalog._file_path)
        with open(MoviesCatalog._file_path, 'w', encoding='utf8'):
            print('MOVIES FILE CLEARED'.center(30, '-'))
            print(''.center(30, '-'))
