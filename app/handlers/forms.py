from copy import deepcopy

import flask

from app.repositories import logs


def create_log():
    data = deepcopy(flask.request.form.to_dict(flat=True))

    data.pop("title", None)

    new_log_id = logs.add(flask.request.form["title"], **data)

    return flask.redirect(flask.url_for("log", log_id=new_log_id))


def delete_log():
    log_id = flask.request.form["log_id"]
    logs.delete(log_id)
    return flask.redirect(flask.url_for("logs"))


def edit_log():
    log_id = flask.request.form["log_id"]
    data = deepcopy(flask.request.form.to_dict(flat=True))

    if data["rating"] == "":
        del data["rating"]

    logs.update(log_id, **data)
    return flask.redirect(flask.url_for("log", log_id=log_id))
