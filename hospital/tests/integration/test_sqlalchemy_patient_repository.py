from datetime import datetime

import pytest

from hospital.bootstrap import bootstrap
from hospital.domain.models.entities.patient import Patient
from hospital.domain.models.value_objects.people.birth_date import BirthDate
from hospital.domain.models.value_objects.people.national_id import NationalID
from hospital.domain.models.value_objects.people.address import Address
from hospital.domain.models.value_objects.people.people_id import People_ID
from hospital.adapters.repository.patients.sqlalchemy_respository import SqlAlchemyPatientRepository
from hospital.domain.models.value_objects.people.people_name import Name
from hospital.service_layer.patient_services import register_new_patient
from hospital.tests.conftest import session
#from hospital.adapters.orm.patients.patient_orm import PatientORM

def test_repository_can_add_and_retrieve_patient(session):

    session = bootstrap().session
    repo = SqlAlchemyPatientRepository(session)

    new_patient = register_new_patient(
        first_name="Annie",
        last_name="Leonhart",
        birth_date=datetime(1996, 10, 10),
        national_id="000-00000123-9",
        address="52 1st Street, New York, NY, USA",
        repo=repo,
        id=99
    )

    retrieved = repo.get_by_national_id(new_patient.national_id)

    assert isinstance(retrieved, Patient)
    assert retrieved.name.first_name == "Annie"
    assert retrieved.name.last_name == "Leonhart"

    # Verify we can list all patients
    all_patients = repo.list()
    assert len(all_patients) >= 1

    # Clean up after test
    repo.delete(retrieved.id)
    session.commit()

def test_repository_delete_patient(session):

    session = bootstrap().session
    repo = SqlAlchemyPatientRepository(session)

    new_patient = register_new_patient(
        id=99,
        first_name="Juan",
        last_name="Santos",
        birth_date=datetime(1996, 10, 10),
        national_id="000-12300000-2",
        address="52 1st Street, New York, NY, USA",
        repo=repo
    )

    retrieved = repo.get_by_national_id(new_patient.national_id)

    assert repo.get_by_national_id(retrieved.national_id) is not None
    repo.delete(retrieved.id)
    session.commit()
    assert repo.get(retrieved.id) is None

def test_repository_do_not_add_the_same_patient_more_than_once(session):

    existing_patient = Patient(
        id=People_ID(77),
        name=Name("Eren", "Jaeger"),
        birth_date=BirthDate(datetime(1996,10,10)),
        national_id=NationalID("000-1230000-6"),
        address=Address("52 1st Street, New York, NY, USA")
    )

    session = bootstrap().session
    repo = SqlAlchemyPatientRepository(session)

    repo.add(existing_patient)

    retrieved = repo.get_by_national_id(existing_patient.national_id)

    assert isinstance(retrieved, Patient)
    assert retrieved.name.first_name == "Eren"
    assert retrieved.name.last_name == "Jaeger"

    # Verify we can list all patients
    all_patients = repo.list()
    assert len(all_patients) >= 1

    with pytest.raises(ValueError, match="Patient ID already exists"):
        register_new_patient(
            id=77,
            first_name="Eren",
            last_name="Jaeger",
            birth_date=datetime(1996, 10, 10),
            national_id="000-12300000-6",
            address="52 1st Street, New York, NY, USA",
            repo=repo
        )