from datamodel import Movie

class MovieManager():
    @staticmethod
    def input_movie_info():
        title = input('Movie Title : ')
        director = input('Director : ')#.split(',')
        genre = input('Genre : ')#.split(',')
        score = float(input('score : '))
        return Movie(title,director,genre,score)
    
    @staticmethod
    def input_many_movie_info():
        inputpredicate = True
        movies = []
        try:
            while inputpredicate:
                amovie = MovieManager.input_movie_info()
                movies.append(amovie)
                inputpredicate = True if input('Try to type more movies?[Y/N]').lower() == 'y' else False
            return movies
        except:
            return 'Fail to get information'
    

            