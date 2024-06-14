import flask


def import_logs():
    return flask.render_template("migrations/import.html")
