from pony import orm

from . import models

def add_log(title, rating=None, category=None):
	with orm.db_session:
		log = models.CultureLog(
			title = title,
			rating = rating,
			category = category,
			)
		return log
