from pony import orm

from . import db

database = db.connect()

class CultureLog(database.Entity):
	_table_ = "culture_log"

	id = orm.PrimaryKey(int, auto=True)
	title = orm.Required(str)
	rating = orm.Optional(int)
	category = orm.Optional(str)


database.generate_mapping()