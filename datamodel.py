
class Movie(object):
    def __init__(self,title,director,genre,score):
        self.title = title
        self.director = director
        self.genre = genre
        self.score = score

    def __iter__(self):
        #return self.__dict__.iteritems()
        return iter([('Title',self.title),('Director',self.director),('Genre',self.genre),('Score',self.score)])