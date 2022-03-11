import os
from typing import Optional
from unittest.mock import MagicMock

import pytest

from app.dao.models import Director
from app.dao import DirectorDAO
from app.database import db
from app.services.director import DirectorService


@pytest.fixture()
def director_dao():
	director_dao = DirectorDAO(db.session)

	director_1 = Director(id=1, name="name1")
	director_2 = Director(id=2, name="name2")
	director_3 = Director(id=3, name="name3")

	director_dao.get_one = MagicMock(return_value=director_1)
	director_dao.get_all = MagicMock(return_value=[director_1, director_2, director_3])
	director_dao.create = MagicMock(return_value=Director(id=3))
	director_dao.db_update = MagicMock()
	director_dao.delete = MagicMock()

	return director_dao


class TestDirectorsService:
	@pytest.fixture(autouse=True)
	def director_service(self, director_dao):
		self.director_service = DirectorService(dao=director_dao)

	def test_get_one(self):
		director = self.director_service.get_one(1)
		assert director != None
		assert director.id != None

	def test_get_all(self):
		director = self.director_service.get_all()
		assert len(director) > 0

	def test_create(self):
		director_d = {"name": "name1"}
		director = self.director_service.create(director_d)
		assert director.id != None

	def test_delete(self):
		ret = self.director_service.delete(1)
		assert ret == None

	def test_update(self):
		director_d = {"id": "4", "name": "name1"}
		ret = self.director_service.get_update(director_d)
		assert ret == None


if __name__ =="__main__":
	os.system("pytest")
