from . import models

def log(a_log: models.CultureLog) -> models.LogRecord:
	return models.LogRecord(
		id=a_log.id,
		title=a_log.title,
		rating=a_log.rating,
		content=a_log.content,
		category=a_log.category,
		tags=a_log.tags,
		event_date=a_log.event_date,
		bechdel_test=a_log.bechdel_test,
		url=a_log.url,
	)

