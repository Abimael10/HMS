from dataclasses import dataclass

@dataclass(frozen=True)
class PatientID:
    value: int = None