from app.config import DevelopmentConfig
from app.dao import Genre, Director, User, Movie
from main import create_app, db


app = create_app(DevelopmentConfig)


@app.shell_context_processor
def shell():
	try:
		return {
			"db": db,
			"Genre": Genre,
			"Director": Director,
			"User": User,
			"Movie": Movie,
		}
	except ImportError as e:
		print(e)
