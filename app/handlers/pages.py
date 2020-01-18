import flask

from app.repositories import logs

def front_page():
	return flask.render_template('index.html')

def all_logs():
	log_entries = logs.all()
	return flask.render_template('logs.html', logged=log_entries)


def all_category_logs(category_name):
	log_entries = logs.category(category_name)
	return flask.render_template('logs.html', logged=log_entries)

def log(log_id):
	return flask.render_template('log.html', log_entry=logs.log(log_id))