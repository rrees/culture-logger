import period


import logging
import datetime

from google.appengine.ext import ndb

import models

def read_log(user, log_id):
	return ndb.Key(urlsafe=log_id).get()

def create_new_log(user, name, date, tags=None, rating=None, notes=None, category=None, url=None,
	bechdel_test=None, violence_against_women=False):
	log_entry = models.LogEntry(user=user, name=name, date=date)

	if tags:
		log_entry.tags = tags

	if notes:
		log_entry.notes = notes

	if rating:
		log_entry.rating = rating

	if category:
		log_entry.category = category

	if url:
		log_entry.url = url

	if bechdel_test:
		log_entry.bechdel_test = bechdel_test

	log_entry.violence_against_women = violence_against_women

	log_entry.put()
	return log_entry

def update_log(user, log_id, name, date, tags=None, rating=None, notes=None, category=None, url=None,
	bechdel_test=None,
	violence_against_women=None):
	log_entry = read_log(user, log_id)

	if name:
		log_entry.name = name

	if date:
		log_entry.date = date

	if tags:
		log_entry.tags = tags

	if rating:
		log_entry.rating = rating

	if notes:
		log_entry.notes = notes

	if category:
		log_entry.category = category

	if url:
		log_entry.url = url

	if bechdel_test:
		log_entry.bechdel_test = bechdel_test

	if log_entry.bechdel_test  == True and not bechdel_test:
		log_entry.bechdel_test = False

	if violence_against_women:
		log_entry.violence_against_women = violence_against_women

	if log_entry.violence_against_women == True and not violence_against_women:
		log_entry.violence_against_women = False

	log_entry.put()

	return log_entry

def log(user, name, date, tags=None, rating=None, notes=None, log_id=None, category=None, url=None,
		bechdel_test=None,
		violence_against_women=None):
	if not log_id:
		return create_new_log(user, name, date, tags, rating, notes, category, url=url,
			bechdel_test=bechdel_test,
			violence_against_women=violence_against_women)

	return update_log(user, log_id, name, date, tags, rating, notes, category, url=url,
		bechdel_test=bechdel_test,
		violence_against_women=violence_against_women)


def all(user):
    return models.LogEntry.query(models.LogEntry.user == user).order(-models.LogEntry.date)

def delete_log(log_id):
    return ndb.Key(urlsafe=log_id).delete()
