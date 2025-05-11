from abc import ABC

from hospital.adapters.repository.patients.abstract_repository import AbstractRepository
from hospital.domain.models.entities.patient import Patient
from hospital.domain.models.value_objects.people.people_id import People_ID
from hospital.tests.conftest import session

class FakePatientRepository(AbstractRepository, ABC):
    def __init__(self, session, patients=None):
        super().__init__()
        self.session = session
        self.patients = set(patients or [])

    def add(self, patient: Patient):
        self.patients.add(patient)

    def get(self, id: People_ID):
        return next((p for p in self.patients if p.id == id), None)

    def delete(self, patient_id) -> bool:
        patient = self.get(patient_id)
        if patient:
            self.patients.remove(patient)
            return True
        return False

    def get_by_national_id(self, national_id):
        return next((p for p in self.patients if p.national_id == national_id), None)

    def list(self):
        return list(self.patients)