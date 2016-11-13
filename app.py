import os
import logging
import datetime

import webapp2
import jinja2

import queries
import constants
import filters
import forms

from google.appengine.api import users

JINJA = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
	extensions=['jinja2.ext.autoescape'],
	autoescape=True)

JINJA.filters.update(filters.custom_filters)

class MainPage(webapp2.RequestHandler):
	def get(self):
		user = users.get_current_user()

		if user:
			return webapp2.redirect('/home')

		template_values = {

		}

		template = JINJA.get_template('index.html')
		self.response.write(template.render(template_values))

class HomePage(webapp2.RequestHandler):
	def get(self):
		user = users.get_current_user()

		template_values = {
			"today": datetime.date.today().isoformat(),
			"logged": queries.period.last_thirty_days(user),
			"valid_ratings": constants.valid_ratings,
		}

		template = JINJA.get_template('home.html')
		self.response.write(template.render(template_values))

class LogPlay(webapp2.RequestHandler):
	def get(self):

		template_values = {
			"today": datetime.date.today().isoformat(),
			"valid_ratings": constants.valid_ratings,
		}

		template = JINJA.get_template('log.html')
		self.response.write(template.render(template_values))

	def post(self):
		#logging.info(self.request.POST)
		user = users.get_current_user()

		date_played = datetime.datetime.strptime(self.request.POST['date'], '%Y-%m-%d').date()

		tags = self.request.POST.get('tags', '').split(',')

		tags = filter(lambda tag: len(tag) > 0, tags)

		notes = self.request.POST.get('notes', None)

		category = self.request.POST.get('category', None)

		rating = self.request.POST.get('rating', None)

		rating = int(rating) if rating else None

		#logging.info(rating)

		url = self.request.POST.get('url', None)

		#logging.info(url)

		bechdel_test = forms.bechdel_test(self.request.POST)

		logging.info(bechdel_test)

		queries.log(user, self.request.POST['name'], date_played, tags=tags,
			rating=rating,
			notes=notes,
			category=category,
			url=url,
			bechdel_test=bechdel_test)
		return webapp2.redirect('/home')

class LogsPage(webapp2.RequestHandler):
	def get(self):
		user = users.get_current_user()

		template_values = {
			"logged": queries.all(user),
		}

		template = JINJA.get_template('logs.html')
		self.response.write(template.render(template_values))

class LogPage(webapp2.RequestHandler):
	def get(self, log_id):
		user = users.get_current_user()

		template_values = {
			"log": queries.read_log(user, log_id),
			"valid_ratings": constants.valid_ratings,
		}

		template = JINJA.get_template('log.html')
		self.response.write(template.render(template_values))

	def post(self, log_id):
		user = users.get_current_user()

		date_attended = datetime.datetime.strptime(self.request.POST['date'], '%Y-%m-%d').date()

		tags = self.request.POST.get('tags', '').split(',')

		tags = filter(lambda tag: len(tag) > 0, tags)

		notes = self.request.POST.get('notes', None)

		rating = self.request.POST.get('rating', None)

		category = self.request.POST.get('category', None)

		url = self.request.POST.get('url', None)

		if rating:
			rating = int(rating)

		bechdel_test = forms.bechdel_test(self.request.POST)

		queries.log(user, self.request.POST['name'], date_attended,
			tags=tags,
			rating=rating,
			notes=notes,
			log_id=log_id,
			category=category,
			url=url,
			bechdel_test=bechdel_test)

		return webapp2.redirect('/log/'+log_id)

class DeleteLogPage(webapp2.RequestHandler):
	def post(self, log_id):
		queries.delete_log(log_id)
		return webapp2.redirect('/logs')

app = webapp2.WSGIApplication([
	webapp2.Route(r'/', handler=MainPage),
	webapp2.Route(r'/home', handler=HomePage),
	webapp2.Route(r'/log', handler=LogPlay),
	webapp2.Route(r'/logs', handler=LogsPage),
	webapp2.Route(r'/log/<log_id>', handler=LogPage),
	webapp2.Route(r'/log/<log_id>/delete', handler=DeleteLogPage),
	], debug=True)
