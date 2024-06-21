import flask


def import_page():
    return flask.render_template("migrations/import.html")


def import_logs():
    return flask.redirect(flask.url_for("logs"))
