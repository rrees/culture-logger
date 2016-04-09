import logging
import datetime

from google.appengine.ext import ndb

import models

def all_played(user):
	return models.LogEntry.query(models.LogEntry.user == user).order(-models.LogEntry.date_played)

def delete_log(log_id):
	return ndb.Key(urlsafe=log_id).delete()
