# ORM model that SQLAlchemy can work with
from hospital.domain.models.entities.patient import Patient
from hospital.domain.models.value_objects.patient.birth_date import BirthDate
from hospital.domain.models.value_objects.patient.national_id import NationalID
from hospital.domain.models.value_objects.patient.patient_address import PatientAddress
from hospital.domain.models.value_objects.patient.patient_id import PatientID
from hospital.domain.models.value_objects.patient.patient_name import PatientName


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

    def __init__(self, id=None, first_name=None, last_name=None, birth_date=None, national_id=None, patient_address=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.national_id = national_id
        self.patient_address = patient_address

    # Convert ORM model to domain model
    def to_domain(self):
        return Patient(
            name=PatientName(self.first_name, self.last_name),
            birth_date=BirthDate(self.birth_date),
            national_id=NationalID(self.national_id),
            patient_address=PatientAddress(self.patient_address),
            id=PatientID(self.id)
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
            patient_address=patient.patient_address.value
        )