#import datetime
from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class BirthDate:
    value: date

    def __str__(self):
        return f"{self.value}"