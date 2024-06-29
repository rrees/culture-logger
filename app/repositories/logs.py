import datetime

import psycopg

from . import db, models, sql


def process_tags(tag_value: str) -> list[str]:
    if not tag_value:
        return []

    return [t.strip() for t in tag_value.lower().split(",")]


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

    tags = process_tags(tags)

    if rating != None and len(rating.strip()) < 1:
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

    with db.connect() as conn:
        with conn.cursor() as cursor:
            with conn.transaction():
                result = cursor.execute(sql.logs.CREATE, data)
                return cursor.fetchone()[0]


def update(id, **kwargs):
    params = dict(kwargs)

    params["tags"] = process_tags(params["tags"])

    column_names = [n for n in kwargs.keys() if n != "log_id"]

    with db.connect() as conn:
        with conn.cursor() as cursor:
            with conn.transaction():
                update = db.format_placeholders(sql.logs.UPDATE, column_names)

                cursor.execute(update, params)

    return id


def read(query, data, data_class, read_one=False):
    with db.connect() as conn:
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
    with db.connect() as conn:
        with conn.cursor() as cursor:
            with conn.transaction():
                cursor.execute(sql.logs.DELETE, {"log_id": log_id})
