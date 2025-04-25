from hospital.domain.models.entities.patient import Patient

def to_orm_patient(domain_patient):
    return Patient(
        id=domain_patient.id.value,
        name=domain_patient.name.full_name(),
        birth_date=domain_patient.birth_date.value,
        national_id=domain_patient.national_id.value,
        patient_address=domain_patient.patient_address.value
    )