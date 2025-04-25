from datetime import datetime

import pytest

#from hospital.adapters.repository.sqlalchemy_respository import SqlAlchemyPatientRepository
#from hospital.bootstrap import bootstrap
from hospital.domain.models.entities.patient import Patient
from hospital.domain.models.value_objects.patient.birth_date import BirthDate
from hospital.domain.models.value_objects.patient.national_id import NationalID
from hospital.domain.models.value_objects.patient.patient_address import PatientAddress
from hospital.domain.models.value_objects.patient.patient_id import PatientID
from hospital.domain.models.value_objects.patient.patient_name import PatientName
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
        patient_address="52 1st Street, New York, NY, USA",
        repo=repo,
        session=session
    )

    assert session.committed is True
    patient_get = repo.get(patient.id)
    assert patient_get.name == PatientName("Juan", "Perez")

def test_raises_error_if_patient_exists():
    existing_patient = Patient(
        id=PatientID(1),
        name=PatientName("Ana", "Gomez"),
        birth_date=BirthDate(datetime(1996,10,10)),
        national_id=NationalID("000-0000000-1"),
        patient_address=PatientAddress("52 1st Street, New York, NY, USA")
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
            patient_address="52 1st Street, New York, NY, USA",
            repo=repo,
            session=session
        )

def test_delete_existing_patient(session):
    session = FakeSession()
    repo = FakePatientRepository(session)
    #repo = SqlAlchemyPatientRepository(session)

    register_new_patient_staging(
        id=1,
        first_name="Juan",
        last_name="Pérez",
        birth_date=datetime(1996, 10, 10),
        national_id="000-00000000-1",
        patient_address="52 1st Street, New York, NY, USA",
        repo=repo,
        session=session
    )

    assert repo.get(PatientID(1)) is not None
    assert repo.delete(PatientID(1)) is True
    assert repo.get(PatientID(1)) is None

def test_delete_nonexistent_patient():
    session = FakeSession
    repo = FakePatientRepository(session)
    assert repo.delete(PatientID(99)) is False