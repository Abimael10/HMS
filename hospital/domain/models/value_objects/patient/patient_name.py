from dataclasses import dataclass

@dataclass(frozen=True)
class PatientName:
    first_name: str
    last_name: str

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"