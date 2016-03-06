import datetime

from google.appengine.ext import ndb

import models

def last(user, datetime_limit):
	return models.LogEntry.query(models.LogEntry.user == user).filter(models.LogEntry.date >= datetime_limit).order(-models.LogEntry.date)

def last_thirty_days(user):
	return last(user, datetime.datetime.now() - datetime.timedelta(days=30))

def last_year(user):
	now = datetime.datetime.now()
	return last(user, now - datetime.timedelta(year=1))

def year(user, year):
	start_date = datetime.datetime(year, 1, 1, 0, 0, 0)
	end_date = datetime.datetime(year + 1, 1, 1, 0, 0, 0)
	return (models.LogEntry.query(models.LogEntry.user == user)
		.filter(models.LogEntry.date >= start_date)
		.filter(models.LogEntry.date < end_date)
		.order(-models.LogEntry.date))
