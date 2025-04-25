from datetime import datetime

from hospital.domain.models.entities.patient import Patient
from hospital.domain.models.value_objects.patient.birth_date import BirthDate
from hospital.domain.models.value_objects.patient.national_id import NationalID
from hospital.domain.models.value_objects.patient.patient_address import PatientAddress
from hospital.domain.models.value_objects.patient.patient_id import PatientID
from hospital.domain.models.value_objects.patient.patient_name import PatientName
from hospital.tests.fakes.fake_patient_repository import FakePatientRepository
from hospital.tests.unit.test_services import FakeSession

def test_fake_repository_can_add_and_retrieve_patient():
    ana = Patient(PatientID(1), PatientName("Ana", "Lopez"), BirthDate(datetime(1996,10,10)), NationalID("000-00000000-1"), PatientAddress("52 1st Street, New York, NY, USA"))
    session = FakeSession()
    repo = FakePatientRepository(session, [ana])

    assert repo.get(PatientID(1)) == ana
    assert len(repo.list()) == 1