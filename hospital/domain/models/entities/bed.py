from dataclasses import dataclass
from typing import Optional, TYPE_CHECKING

from hospital.domain.models.entities.admission import Admission
from hospital.domain.models.value_objects.bed_label import BedLabel

if TYPE_CHECKING:
    from hospital.domain.models.entities.admission import Admission

@dataclass
class Bed:

    def __init__(self, bed_label: BedLabel, is_reserved: bool, _current_admission: Optional["Admission"] = None):
        self.bedLabel = bed_label
        self.is_reserved = is_reserved
        self._current_admission = _current_admission


    def assign(self, admission: "Admission"):
        if self.is_reserved and not admission.is_emergency:
            raise ValueError("Cannot assign reserved bed to non-emergency")
        if self._current_admission is not None:
            raise ValueError("Bed is already occupied")
        self._current_admission = admission

    def discharge(self):
        if self._current_admission is None:
            raise ValueError("No patient to discharge")
        self._current_admission = None

    @property
    def is_occupied(self) -> bool:
        return self._current_admission is not None