import datetime

import flask

from app.data.categories import categories
from app.data.ratings import valid_ratings

from app.repositories import logs


def front_page():
    return flask.render_template('index.html')


def home_page():
    return flask.render_template('home.html')


def all_logs():
    log_entries = logs.all()
    return flask.render_template('logs.html', logged=log_entries)


def all_category_logs(category_name):
    normalised_category_name = category_name.lower()
    log_entries = logs.category(normalised_category_name)
    return flask.render_template(
        'logs.html', logged=log_entries, category_name=category_name.capitalize()
    )


def log(log_id):
    return flask.render_template('log.html', log_entry=logs.log(log_id))


def edit_log(log_id):
    return flask.render_template(
        'logs/edit.html',
        log=logs.log(log_id),
        categories=categories,
        valid_ratings=valid_ratings,
    )


def create_log():
    return flask.render_template(
        'logs/create.html',
        categories=categories,
        valid_ratings=valid_ratings,
        today=datetime.date.today().isoformat(),
    )


def delete_log(log_id):
    return flask.render_template('logs/delete.html', log_entry=logs.log(log_id))
