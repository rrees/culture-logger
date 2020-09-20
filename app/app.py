import os
import logging

import flask

from flask_sslify import SSLify

from . import handlers
from . import redis_utils
from . import filters

from .auth_password.routes import auth_routes 

ENV = os.environ.get("ENV", "PROD")

redis_url = os.environ.get("REDIS_URL", None)

redis = redis_utils.setup_redis(redis_url) if redis_url else None

app = flask.Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", os.urandom(24))

if not ENV == "DEV":
    sslify = SSLify(app)

logger = app.logger

routes = [
	('/', 'index', handlers.pages.front_page, ['GET']),
	('/home', 'home', handlers.pages.home_page, ['GET']),
	('/logs', 'logs', handlers.pages.all_logs, ['GET']),
	('/logs/category/<category_name>', 'category_logs', handlers.pages.all_category_logs, ['GET']),
	('/log/<log_id>', 'log', handlers.pages.log, ['GET']),
	('/log/<log_id>/edit', 'log_edit', handlers.pages.edit_log, ['GET']),
	('/log/create', 'log_create', handlers.pages.create_log, ['GET']),
	('/forms/logs/create', 'forms_log_create', handlers.forms.create_log, ['POST']),
	('/log/<log_id>/delete', 'log_delete', handlers.pages.delete_log, ['GET']),
	('/forms/logs/delete', 'forms_log_delete', handlers.forms.delete_log, ['POST']),
]

routes.extend(auth_routes)

for path, endpoint, handler, methods in routes:
	app.add_url_rule(path, endpoint, handler, methods=methods)

for filter_name, filter in filters.custom_filters.items():
	app.add_template_filter(filter, name=filter_name)

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500

@app.before_request
def check_authentication():
	if 'email' not in flask.session and flask.request.endpoint not in ['index', 'login_form']:
		return flask.redirect(flask.url_for('index'))
