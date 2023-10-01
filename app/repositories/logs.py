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

    if not tags:
        tags = []

    if not rating.strip():
        rating = None

    if not event_date:
        event_date = datetime.date.today()

    with orm.db_session:
        log = models.CultureLog(
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
        return log


def update(id, **kwargs):
    with orm.db_session:
        log = models.CultureLog[id]

        for key, value in kwargs.items():
            if hasattr(log, key):
                setattr(log, key, value)

    return log


def all():
    with orm.db_session:
        return [
            mappers.log(l)
            for l in models.CultureLog.select().sort_by(
                orm.desc(models.CultureLog.event_date)
            )
        ]


def category(category_name):
    with orm.db_session:
        query = models.CultureLog.select().sort_by(
            orm.desc(models.CultureLog.event_date)
        )

        return [
            mappers.log(l)
            for l in query
            if l.category and l.category.lower() == category_name
        ]


def log(log_id):
    with orm.db_session:
        return mappers.log(models.CultureLog[log_id])


def run_query(query, data, data_class):
    with db.pg_connect() as conn:
        with conn.cursor(row_factory=psycopg.rows.class_row(data_class)) as cursor:
            cursor.execute(query, data)
            rows = cursor.fetchall()
            return [row for row in rows]


def all():
    return run_query(sql.logs.ALL, {}, models.LogRecord)


def category(category_name):
    params = {"category": category_name.lower()}
    return run_query(sql.logs.ALL_FROM_CATEGORY, params, models.LogRecord)


def log(log_id):
    params = {"log_id": log_id}

    with db.pg_connect() as conn:
        with conn.cursor(
            row_factory=psycopg.rows.class_row(models.LogRecord)
        ) as cursor:
            cursor.execute(sql.logs.LOG, params)
            return cursor.fetchone()
