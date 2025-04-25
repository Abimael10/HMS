from dataclasses import dataclass


@dataclass(frozen=True)
class BedLabel:
    room_number: str
    position: str

    def __str__(self):
        if not self.room_number or not self.position:
            raise ValueError("Bed label must not be empty")
        if " " in self.room_number or " " in self.position:
            raise ValueError("Bed label cannot contain spaces")
        return f"{self.room_number} - {self.position}"