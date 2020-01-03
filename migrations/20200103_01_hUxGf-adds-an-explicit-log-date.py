"""
Adds an explicit log date
"""

from yoyo import step

__depends__ = {'20191124_01_KUsDq-create-basic-log-table'}

steps = [
    step("ALTER TABLE culture_log ADD COLUMN event_date DATE NOT NULL DEFAULT current_date")
]
