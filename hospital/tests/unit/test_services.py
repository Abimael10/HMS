from datetime import datetime

import pytest

#from hospital.adapters.repository.sqlalchemy_respository import SqlAlchemyPatientRepository
#from hospital.bootstrap import bootstrap
from hospital.domain.models.entities.patient import Patient
from hospital.domain.models.value_objects.people.birth_date import BirthDate
from hospital.domain.models.value_objects.people.national_id import NationalID
from hospital.domain.models.value_objects.people.address import Address
from hospital.domain.models.value_objects.people.people_id import People_ID
from hospital.domain.models.value_objects.people.people_name import Name
from hospital.service_layer.patient_services import register_new_patient, register_new_patient_staging
from hospital.tests.fakes.fake_patient_repository import FakePatientRepository
from hospital.tests.conftest import session
#from hospital.tests.test_utils import to_orm_patient

#from hospital.tests.test_utils import to_orm_patient

class FakeSession:
    committed = False
    def commit(self):
        self.committed = True

def test_registers_new_patient_successfully(session):
    session = FakeSession()
    repo = FakePatientRepository(session)
    #repo = SqlAlchemyPatientRepository(session)

    patient = register_new_patient_staging(
        id=1,
        first_name="Juan",
        last_name="Perez",
        birth_date=datetime(1996, 10, 10),
        national_id="000-00000000-1",
        address="52 1st Street, New York, NY, USA",
        repo=repo
    )

    assert session.committed is True
    patient_get = repo.get(patient.id)
    assert patient_get.name == Name("Juan", "Perez")

def test_raises_error_if_patient_exists():
    existing_patient = Patient(
        id=People_ID(1),
        name=Name("Ana", "Gomez"),
        birth_date=BirthDate(datetime(1996,10,10)),
        national_id=NationalID("000-0000000-1"),
        address=Address("52 1st Street, New York, NY, USA")
    )
    session = FakeSession()
    repo = FakePatientRepository(session, [existing_patient])

    with pytest.raises(ValueError, match="Patient ID already exists"):
        register_new_patient_staging(
            id=1,
            first_name="Ana",
            last_name="Gomez",
            birth_date=datetime(1996, 10, 10),
            national_id="000-00000000-1",
            address="52 1st Street, New York, NY, USA",
            repo=repo
        )

def test_delete_existing_patient(session):
    session = FakeSession()
    repo = FakePatientRepository(session)
    #repo = SqlAlchemyPatientRepository(session)

    new_patient = register_new_patient_staging(
        id=1,
        first_name="Juan",
        last_name="Pérez",
        birth_date=datetime(1996, 10, 10),
        national_id="000-00000000-1",
        address="52 1st Street, New York, NY, USA",
        repo=repo
    )

    assert session.committed is True

    assert repo.get(new_patient.id) is not None
    assert repo.delete(new_patient.id) is True
    assert repo.get(new_patient.id) is None

def test_delete_nonexistent_patient():
    session = FakeSession
    repo = FakePatientRepository(session)
    assert repo.delete(People_ID(99)) is False