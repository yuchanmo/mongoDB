from datamodel import Movie
from moviedbmanager import MovieManager as mm
from mongocollection import MovieCollection

ismoviedbrunning = True
if __name__ == '__main__' :
    moviemongo = MovieCollection('movie')
    #c = moviemongo.moviecollection()
    while ismoviedbrunning:
        movies = mm.input_many_movie_info()
        moviemongo.insert_many(movies)




