from dataclasses import dataclass

@dataclass(frozen=True)
class Address:
    value: str

    def __str__(self):
        return f"{self.value}"