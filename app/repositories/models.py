from dataclasses import dataclass
import datetime
from typing import List

from pony import orm

from . import db

database = db.connect()

class CultureLog(database.Entity):
	_table_ = "culture_log"

	id = orm.PrimaryKey(int, auto=True)
	title = orm.Required(str)
	rating = orm.Optional(int)
	category = orm.Optional(str)
	event_date = orm.Required(datetime.date)
	content = orm.Optional(str)
	tags = orm.Optional(orm.StrArray)


@dataclass
class LogRecord:
	id: int()
	title: str
	rating: int
	category: str
	event_date: datetime.date
	content: str
	tags: List[str]

database.generate_mapping()