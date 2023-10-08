ALL = """SELECT *
FROM culture_log
ORDER BY event_date DESC
"""

ALL_FROM_CATEGORY = """SELECT *
FROM culture_log
WHERE LOWER(category) = %(category)s
ORDER BY event_date DESC"""

LOG = """SELECT *
FROM culture_log
WHERE id = %(log_id)s
"""

DELETE = """DELETE FROM culture_log
WHERE id = %(log_id)s"""

CREATE = """INSERT INTO culture_log (
	title,
	content,
	tags,
	category,
	rating,
	url,
	bechdel_test,
	violence_against_women
) VALUES (
	%(title)s,
	%(content)s,
	%(tags)s,
	%(category)s,
	%(rating)s,
	%(url)s,
	%(bechdel_test)s,
	%(violence_against_women)s
) RETURNING id"""

UPDATE = """UPDATE culture_log
SET ({}) = ({})
WHERE id = %(log_id)s
RETURNING id"""
