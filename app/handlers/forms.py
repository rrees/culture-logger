from copy import deepcopy

import flask

from app.repositories import logs

def create_log():
	print(flask.request.form.to_dict(flat=True))
	data = deepcopy(flask.request.form.to_dict(flat=True))

	data.pop('name', None)

	new_log = logs.add(flask.request.form['name'], **data)

	return flask.redirect(flask.url_for('log', log_id=new_log.id))