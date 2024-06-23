import json

import flask

from app.repositories import logs


def import_page():
    return flask.render_template("migrations/import.html")


def import_logs():
    data = flask.request.form.get("import_data", "[]")
    parsed_data = json.loads(data)

    for log in parsed_data:
        if not "title" in log:
            flask.abort(400, "A log exists without a title")
        title = log.pop("title")

        logs.add(title, **log)
    return flask.redirect(flask.url_for("logs"))
