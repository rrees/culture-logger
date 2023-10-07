import datetime

import psycopg

from pony import orm

from . import db, mappers, models, sql


def add(
    title,
    rating=None,
    category=None,
    event_date=None,
    content=None,
    tags=None,
    url=None,
    bechdel_test=None,
    violence_against_women=None,
):
    if not category:
        category = ""

    if not content:
        content = ""

    if tags:
        tags = [t.strip() for t in tags.split(",")]
    if not tags:
        tags = []

    if not rating.strip():
        rating = None

    if not event_date:
        event_date = datetime.date.today()

    data = dict(
        title=title,
        event_date=event_date,
        rating=rating,
        category=category,
        content=content,
        tags=tags,
        url=url,
        bechdel_test=bechdel_test,
        violence_against_women=violence_against_women,
    )

    with db.pg_connect() as conn:
        with conn.cursor() as cursor:
            with conn.transaction():
                result = cursor.execute(sql.logs.CREATE, data)
                return cursor.fetchone()[0]


def update(id, **kwargs):
    with orm.db_session:
        log = models.CultureLog[id]

        for key, value in kwargs.items():
            if hasattr(log, key):
                setattr(log, key, value)

    return log


def read(query, data, data_class, read_one=False):
    with db.pg_connect() as conn:
        with conn.cursor(row_factory=psycopg.rows.class_row(data_class)) as cursor:
            cursor.execute(query, data)
            if read_one:
                return cursor.fetchone()

            rows = cursor.fetchall()
            return [row for row in rows]


def all():
    return read(sql.logs.ALL, {}, models.LogRecord)


def category(category_name):
    params = {"category": category_name.lower()}
    return read(sql.logs.ALL_FROM_CATEGORY, params, models.LogRecord)


def log(log_id):
    params = {"log_id": log_id}

    return read(sql.logs.LOG, params, models.LogRecord, read_one=True)


def delete(log_id):
    with db.pg_connect() as conn:
        with conn.cursor() as cursor:
            with conn.transaction():
                cursor.execute(sql.logs.DELETE, {"log_id": log_id})
