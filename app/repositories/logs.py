import datetime

from pony import orm

from . import models

def add_log(title, rating=None, category=None, event_date=None):
	if not category:
		category = ''

	if not event_date:
		event_date = datetime.date.utcnow()

	with orm.db_session:
		log = models.CultureLog(
			title = title,
			event_date = event_date,
			rating = rating,
			category = category,
			)
		return log

def update(id, **kwargs):

	with orm.db_session: 
		log = models.CultureLog[id]

		for key, value in kwargs.items():
			print(key)
			if hasattr(log, key):
				print(f'Setting {key}')
				setattr(log, key, value)

	return log