from hospital.domain.models.entities.patient import Patient
from hospital.adapters.repository.patients.abstract_repository import AbstractRepository
from hospital.adapters.orm.main_adapter import PatientORM, start_mappers


class SqlAlchemyPatientRepository(AbstractRepository):
    def __init__(self, session):
        super().__init__()
        #Start the mapping before any query is ran to avoid runtime errors
        start_mappers()
        self.session = session

    def add(self, patient):
        # Convert domain model to ORM model
        patient_orm = PatientORM.from_domain(patient)
        self.session.add(patient_orm)

    def get_by_national_id(self, national_id):
        # Get ORM model by national_id
        patient_orm = self.session.query(PatientORM).filter_by(national_id=national_id.value).first()
        if patient_orm is None:
            return None
        # Convert ORM model to domain model
        return patient_orm.to_domain()
        
    def get(self, patient_id):
        # Get ORM model by ID
        patient_orm = self.session.query(PatientORM).filter_by(id=patient_id.value).first()
        if patient_orm is None:
            return None
        # Convert ORM model to domain model
        return patient_orm.to_domain()

    def update(self, patient: Patient):
        orm_patient = self.session.query(PatientORM).filter_by(id=patient.id.value).first()
        if not orm_patient:
            raise ValueError(f"Patient with ID {patient.id.value} not found")

        orm_patient.first_name = patient.name.first_name
        orm_patient.last_name = patient.name.last_name
        orm_patient.birth_date = patient.birth_date.value
        orm_patient.national_id = patient.national_id.value
        orm_patient.address = patient.address.value

    def delete(self, patient_id) -> bool:
        patient_orm = self.session.query(PatientORM).filter_by(id=patient_id.value).first()
        if patient_orm:
            self.session.delete(patient_orm)
            return True
        return False

    def list(self):
        patient_orms = self.session.query(PatientORM).all()
        # Convert ORM models to domain models
        return [patient_orm.to_domain() for patient_orm in patient_orms]
        
    def commit(self):
        self.session.commit()