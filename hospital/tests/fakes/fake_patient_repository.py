from hospital.adapters.repository.abstract_repository import AbstractRepository
from hospital.domain.models.entities.patient import Patient
from hospital.domain.models.value_objects.patient.patient_id import PatientID
from hospital.tests.conftest import session

class FakePatientRepository(AbstractRepository):
    def __init__(self, session, patients=None):
        super().__init__()
        self.session = session
        self.patients = set(patients or [])

    def add(self, patient: Patient):
        self.patients.add(patient)

    def get(self, id: PatientID):
        return next((p for p in self.patients if p.id == id), None)

    def delete(self, patient_id) -> bool:
        patient = self.get(patient_id)
        if patient:
            self.patients.remove(patient)
            return True
        return False

    def list(self):
        return list(self.patients)