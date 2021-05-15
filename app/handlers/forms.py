from copy import deepcopy

import flask

from app.repositories import logs

def create_log():
	data = deepcopy(flask.request.form.to_dict(flat=True))

	data.pop('title', None)

	new_log = logs.add(flask.request.form['title'], **data)

	return flask.redirect(flask.url_for('log', log_id=new_log.id))

def delete_log():
	return flask.redirect(flask.url_for('home'))

def edit_log():
	log_id = flask.request.form['log_id']
	data = deepcopy(flask.request.form.to_dict(flat=True))
	logs.update(log_id, **data)
	return flask.redirect(flask.url_for('log', log_id=log_id))