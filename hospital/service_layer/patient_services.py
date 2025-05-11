from datetime import date

from hospital.adapters.repository.patients.abstract_repository import AbstractRepository
from hospital.domain.models.entities.patient import Patient
from hospital.domain.models.value_objects.people.birth_date import BirthDate
from hospital.domain.models.value_objects.people.national_id import NationalID
from hospital.domain.models.value_objects.people.address import Address
from hospital.domain.models.value_objects.people.people_id import People_ID
from hospital.domain.models.value_objects.people.people_name import Name

def register_new_patient(id: int, first_name: str, last_name: str, birth_date: date, national_id: str, address: str, repo: AbstractRepository):

    if id is not None and repo.get(People_ID(id)):
        raise ValueError("Patient ID already exists")

    # Also check if the national ID exists
    if repo.get_by_national_id(NationalID(national_id)):
        raise ValueError("National ID already exists")

    new_patient = Patient(
        name=Name(first_name, last_name),
        birth_date=BirthDate(birth_date),
        national_id=NationalID(national_id),
        address=Address(address)
        #id=PatientID(id) if id is not None else None
    )

    repo.add(new_patient)
    repo.session.commit()
    return new_patient

def register_new_patient_staging(id: int, first_name: str, last_name: str, birth_date: date, national_id: str, address: str, repo: AbstractRepository):
    if id is not None and repo.get(People_ID(id)):
        raise ValueError("Patient ID already exists")
        
    # Also check if the national ID exists
    if repo.get_by_national_id(NationalID(national_id)):
        raise ValueError("National ID already exists")

    new_patient = Patient(
        name=Name(first_name, last_name),
        birth_date=BirthDate(birth_date),
        national_id=NationalID(national_id),
        address=Address(address)
        #id=PatientID(id) if id is not None else None
    )

    repo.add(new_patient)
    repo.session.commit()
    return new_patient