import os
from typing import Optional
from unittest.mock import MagicMock

import pytest

from app.dao.models import Movie
from app.dao import MovieDAO
from app.database import db
from app.services.movie import MovieService


@pytest.fixture()
def movie_dao():
	movie_dao: Optional[MovieDAO] = MovieDAO(db.session)

	user_1 = Movie(id=1, title="title1", description="description1", trailer="trailer1", year=2015, rating="rating1",genre_id=1,director_id=1)
	user_2 = Movie(id=2, title="title2", description="description2", trailer="trailer2", year=2015, rating="rating2",genre_id=2,director_id=2)
	user_3 = Movie(id=3, title="title3", description="description3", trailer="trailer3", year=2015, rating="rating3",genre_id=3,director_id=3)

	movie_dao.get_one = MagicMock(return_value=user_1)
	movie_dao.get_all = MagicMock(return_value=[user_1, user_2, user_3])
	movie_dao.create = MagicMock(return_value=Movie(id=3))
	movie_dao.db_update = MagicMock()
	movie_dao.delete = MagicMock()
	movie_dao.found_film = MagicMock(return_value=user_1)

	return movie_dao


class TestMoviesService:
	@pytest.fixture(autouse=True)
	def movie_service(self, movie_dao):
		self.movie_service = MovieService(dao=movie_dao)

	def test_get_one(self):
		movie = self.movie_service.get_one(1)
		assert movie != None
		assert movie.id != None
		assert len(movie) == 1

	def test_get_all(self):
		movie = self.movie_service.get_all()
		assert len(movie) >0

	def test_create(self):
		movie_d = {
			"title": "title1",
			"description": "description1",
			"trailer": "trailer1",
			"year": 2015,
			"rating": "rating1",
			"genre_id": 1,
			"director_id": 1
		}
		movie = self.movie_service.create(movie_d)
		assert movie.id != None

	def test_delete(self):
		ret = self.movie_service.delete(1)
		assert ret == None

	def test_update(self):
		movie_d = {
			"id": "4",
			"title": "title4",
			"description": "description4",
			"trailer": "trailer4",
			"year": 2015,
			"rating": "rating4",
			"genre_id": 4,
			"director_id": 4
		}
		ret = self.movie_service.get_update(movie_d)
		assert ret == None


if __name__ =="__main__":
	os.system("pytest")
