from app.dao.models.director import Director


# CRUD
class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def db_update(self, director):
        self.session.add(director)
        self.session.commit()
        self.session.refresh(director)
        return director.id

    def get_one(self, did):
        return self.session.query(Director).get(did)

    def get_all(self):
        return self.session.query(Director).all()

    def create(self, data):
        director = Director(**data)
        return self.db_update(director)

    def delete(self, did):
        director = self.get_one(did)
        self.db_update(director)
