ALL = """SELECT *
FROM culture_log
ORDER BY event_date DESC
"""

ALL_FROM_CATEGORY = """SELECT *
FROM culture_log
WHERE LOWER(category) = %(category)s
ORDER BY event_date DESC"""
