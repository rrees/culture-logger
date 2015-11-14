import period


import logging
import datetime

from google.appengine.ext import ndb

import models

def read_log(user, log_id):
    return ndb.Key(urlsafe=log_id).get()

def create_new_log(user, name, date, tags=None, rating=None, notes=None):
    log_entry = models.LogEntry(user=user, name=name, date=date)

    if tags:
        log_entry.tags = tags

    if notes:
        log_entry.notes = notes

    if rating:
        log_entry.rating = rating

    log_entry.put()
    return log_entry

def update_log(user, log_id, name, played, tags=None, rating=None, notes=None):
    log_entry = read_log(user, log_id)

    if game_name:
        log_entry.name = name

    if date_played:
        log_entry.date = date

    if tags:
        log_entry.tags = tags

    if notes:
        log_entry.notes = notes

    if rating:
        log_entry.rating = rating

    log_entry.put()

    return log_entry

def log(user, name, date, tags=None, notes=None, rating=None, log_id=None):
    if not log_id:
        return create_new_log(user, name, date, tags, rating, notes)

    return update_log(user, log_id, name, date, tags, rating, notes)


def all(user):
    return models.LogEntry.query(models.LogEntry.user == user).order(-models.LogEntry.date)

def delete_log(log_id):
    return ndb.Key(urlsafe=log_id).delete()
