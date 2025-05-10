from datetime import date

from hospital.adapters.repository.abstract_repository import AbstractRepository
from hospital.adapters.repository.sqlalchemy_respository import SqlAlchemyPatientRepository
from hospital.domain.models.entities.patient import Patient
from hospital.domain.models.value_objects.patient.birth_date import BirthDate
from hospital.domain.models.value_objects.patient.national_id import NationalID
from hospital.domain.models.value_objects.patient.patient_address import PatientAddress
from hospital.domain.models.value_objects.patient.patient_id import PatientID
from hospital.domain.models.value_objects.patient.patient_name import PatientName


def register_new_patient(id: int, first_name: str, last_name: str, birth_date: date, national_id: str, patient_address: str, repo: AbstractRepository):

    if id is not None and repo.get(PatientID(id)):
        raise ValueError("Patient ID already exists")

    # Also check if the national ID exists
    if repo.get_by_national_id(NationalID(national_id)):
        raise ValueError("National ID already exists")

    new_patient = Patient(
        name=PatientName(first_name, last_name),
        birth_date=BirthDate(birth_date),
        national_id=NationalID(national_id),
        patient_address=PatientAddress(patient_address)
        #id=PatientID(id) if id is not None else None
    )

    repo.add(new_patient)
    repo.session.commit()
    return new_patient

def register_new_patient_staging(id: int, first_name: str, last_name: str, birth_date: date, national_id: str, patient_address: str, repo: AbstractRepository):
    if id is not None and repo.get(PatientID(id)):
        raise ValueError("Patient ID already exists")
        
    # Also check if the national ID exists
    if repo.get_by_national_id(NationalID(national_id)):
        raise ValueError("National ID already exists")

    new_patient = Patient(
        name=PatientName(first_name, last_name),
        birth_date=BirthDate(birth_date),
        national_id=NationalID(national_id),
        patient_address=PatientAddress(patient_address)
        #id=PatientID(id) if id is not None else None
    )

    repo.add(new_patient)
    repo.session.commit()
    return new_patient