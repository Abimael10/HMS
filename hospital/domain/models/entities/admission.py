from dataclasses import dataclass
from datetime import datetime
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from hospital.domain.models.entities.bed import Bed
    from hospital.domain.models.entities.patient import Patient

@dataclass
class Admission:
    id: str
    patient: "Patient"
    bed: "Bed"
    admitted_at: datetime = datetime.now()
    discharged_at: Optional[datetime] = None
    is_emergency: bool = False