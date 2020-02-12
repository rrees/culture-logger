import os
import logging

import flask

from flask_sslify import SSLify

from . import handlers
from . import redis_utils
from . import filters

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
	('/logs', 'logs', handlers.pages.all_logs, ['GET']),
	('/logs/category/<category_name>', 'category_logs', handlers.pages.all_category_logs, ['GET']),
	('/log/<log_id>', 'log', handlers.pages.log, ['GET']),
	('/log/create', 'log_create', handlers.pages.create_log, ['GET']),
	('/forms/logs/create', 'forms_log_create', handlers.forms.create_log, ['POST']),
]

for path, endpoint, handler, methods in routes:
	app.add_url_rule(path, endpoint, handler, methods=methods)

for filter_name, filter in filters.custom_filters.items():
	app.add_template_filter(filter, name=filter_name)

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500