import webapp2
import json

from google.appengine.api import users

import queries

class LogsForYear(webapp2.RequestHandler):
	def get(self, year):
		user = users.get_current_user()
		logs = queries.period.year(user, int(year))

		self.response.write(json.dumps([l for l in logs]))


app = webapp2.WSGIApplication([
	webapp2.Route(r'/api/logs/year/<year>', handler=LogsForYear),
	], debug=True)
