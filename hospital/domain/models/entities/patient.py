from dataclasses import dataclass

from hospital.domain.models.value_objects.patient.patient_address import PatientAddress
from hospital.domain.models.value_objects.patient.birth_date import BirthDate
from hospital.domain.models.value_objects.patient.national_id import NationalID
from hospital.domain.models.value_objects.patient.patient_id import PatientID
from hospital.domain.models.value_objects.patient.patient_name import PatientName


@dataclass
class Patient:
    name: PatientName
    birth_date: BirthDate
    national_id: NationalID
    patient_address: PatientAddress
    id: PatientID = None

    def __eq__(self, other):
        return isinstance(other, Patient) and self.national_id == other.national_id

    def __hash__(self):
        return hash(self.national_id)