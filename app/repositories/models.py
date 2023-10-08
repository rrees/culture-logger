from dataclasses import dataclass
import datetime


@dataclass
class LogRecord:
    id: int()
    title: str
    rating: int
    category: str
    event_date: datetime.date
    created: datetime.date
    updated: datetime.date
    content: str
    tags: list[str]
    bechdel_test: bool
    violence_against_women: bool
    url: str
