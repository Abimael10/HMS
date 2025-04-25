from dataclasses import dataclass

@dataclass(frozen=True)
class PatientAddress:
    value: str

    def __str__(self):
        return f"{self.value}"