# ORM model that SQLAlchemy can work with
from hospital.domain.models.entities.patient import Patient
from hospital.domain.models.value_objects.people.birth_date import BirthDate
from hospital.domain.models.value_objects.people.national_id import NationalID
from hospital.domain.models.value_objects.people.address import Address
from hospital.domain.models.value_objects.people.people_id import People_ID
from hospital.domain.models.value_objects.people.people_name import Name


class PatientORM:
    # These columns match the table definition
    """
    id = None
    first_name = None
    last_name = None
    birth_date = None
    national_id = None
    patient_address = None
    """

    def __init__(self, id=None, first_name=None, last_name=None, birth_date=None, national_id=None, address=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.national_id = national_id
        self.address = address

    # Convert ORM model to domain model
    def to_domain(self):
        return Patient(
            name=Name(self.first_name, self.last_name),
            birth_date=BirthDate(self.birth_date),
            national_id=NationalID(self.national_id),
            address=Address(self.address),
            id=People_ID(self.id)
        )

    # Convert domain model to ORM model
    @classmethod
    def from_domain(cls, patient):
        return cls(
            id=patient.id.value if patient.id else None,
            first_name=patient.name.first_name,
            last_name=patient.name.last_name,
            birth_date=patient.birth_date.value,
            national_id=patient.national_id.value,
            address=patient.address.value
        )