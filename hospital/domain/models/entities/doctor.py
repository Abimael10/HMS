from dataclasses import dataclass

from hospital.domain.models.value_objects.people.birth_date import BirthDate
from hospital.domain.models.value_objects.people.national_id import NationalID
from hospital.domain.models.value_objects.people.address import Address
from hospital.domain.models.value_objects.people.people_name import Name
from hospital.domain.models.value_objects.people.people_id import People_ID


@dataclass
class Doctor:
    name: Name
    birth_date: BirthDate
    national_id: NationalID
    address: Address
    specialty: DoctorSpecialty
    supervisor: DoctorSupervisor
    schedule: DoctorSchedule
    status: DoctorStatus

    id: People_ID = None

    def __eq__(self, other):
        return isinstance(other, Doctor) and self.national_id == other.national_id

    def __hash__(self):
        return hash(self.national_id)
