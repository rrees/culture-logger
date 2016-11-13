from google.appengine.ext import ndb

class Configuration(ndb.Model):
	value = ndb.StringProperty(required=True)

class LogEntry(ndb.Model):
	user = ndb.UserProperty(required=True)
	name = ndb.StringProperty(required=True)
	date = ndb.DateProperty(required=True, auto_now_add=True)
	tags = ndb.StringProperty(repeated=True)
	rating = ndb.IntegerProperty()
	notes= ndb.TextProperty()
	category = ndb.StringProperty()
	url = ndb.StringProperty()
	bechdel_test = ndb.BooleanProperty()
