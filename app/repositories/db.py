import os

import psycopg

from pony.orm import Database

_db_url = os.environ["DATABASE_URL"]


def connect():
    db = Database()
    db.bind(provider="postgres", dsn=_db_url)
    return db


def pg_connect():
    return psycopg.connect(_db_url)
