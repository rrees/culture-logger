import os
from pony.orm import Database


def connect():
	db = Database()
	db.bind(provider='postgres', dsn=os.environ['DATABASE_URL'])
	return db