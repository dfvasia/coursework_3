import os
from typing import Optional
from unittest.mock import MagicMock

import pytest

from app.dao.models import Genre
from app.dao import GenreDAO
from app.database import db
from app.services.genre import GenreService


@pytest.fixture()
def genre_dao():
	genre_dao: Optional[GenreDAO] = GenreDAO(db.session)

	genre_1 = Genre(id=1, name="name1")
	genre_2 = Genre(id=2, name="name2")
	genre_3 = Genre(id=3, name="name3")

	genre_dao.get_one = MagicMock(return_value=genre_1)
	genre_dao.get_all = MagicMock(return_value=[genre_1, genre_2, genre_3])
	genre_dao.create = MagicMock(return_value=Genre(id=3))
	genre_dao.db_update = MagicMock()
	genre_dao.delete = MagicMock()
	genre_dao.found_film = MagicMock(return_value=genre_1)

	return genre_dao


class TestGenresService:
	@pytest.fixture(autouse=True)
	def genre_service(self, genre_dao):
		self.genre_service = GenreService(dao=genre_dao)

	def test_get_one(self):
		genre = self.genre_service.get_one(1)
		assert genre != None
		assert genre.id != None

	def test_get_all(self):
		genre = self.genre_service.get_all()
		assert len(genre) >0

	def test_create(self):
		genre_d = {"name": "name1"}
		genre = self.genre_service.create(genre_d)
		assert genre.id != None

	def test_delete(self):
		ret = self.genre_service.delete(1)
		assert ret == None

	def test_update(self):
		genre_d = {"id": "4", "name": "name4"}
		ret = self.genre_service.get_update(genre_d)
		assert ret == None


if __name__ =="__main__":
	os.system("pytest")
