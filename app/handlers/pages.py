import flask

from app.repositories import logs

def front_page():
	return flask.render_template('index.html')

def all_logs():
	log_entries = logs.all()
	return flask.render_template('logs.html', logged=log_entries)
