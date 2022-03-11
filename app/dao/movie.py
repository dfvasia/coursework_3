from app.dao.models.movie import Movie


# CRUD
class MovieDAO:
    def __init__(self, session):
        self.session = session

    def found_film(self, movie):
        if 'director_id' in movie and 'genre_id' in movie:
            director_id = movie['director_id']
            genre_id = movie['genre_id']
            return self.session.query(Movie).filter(Movie.director_id == director_id, Movie.genre_id == genre_id).all()
        if 'director_id' in movie:
            director_id = movie['director_id']
            return self.session.query(Movie).filter(Movie.director_id == director_id).all()
        if 'genre_id' in movie:
            genre_id = movie['genre_id']
            return self.session.query(Movie).filter(Movie.genre_id == genre_id).all()

    def db_update(self, movie):
        self.session.add(movie)
        self.session.commit()
        self.session.refresh(movie)
        return movie.id

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_all(self):
        return self.session.query(Movie).all()

    def create(self, data):
        movie = Movie(**data)
        return self.db_update(movie)  # self.session.add(movie) self.session.commit()

    def delete(self, mid):
        movie = self.get_one(mid)
        self.db_update(movie)  # self.session.add(movie) self.session.commit()
