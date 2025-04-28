from hospital.domain.models.entities.patient import Patient
from hospital.domain.models.value_objects.patient.birth_date import BirthDate
from hospital.domain.models.value_objects.patient.national_id import NationalID
from hospital.domain.models.value_objects.patient.patient_address import PatientAddress
from hospital.domain.models.value_objects.patient.patient_id import PatientID
from hospital.domain.models.value_objects.patient.patient_name import PatientName
from hospital.service_layer.patients.commands import DeletePatientCommand, CreatePatientCommand, FindPatientCommand, \
    UpdatePatientInfoCommand


def handle_create_patient(cmd: CreatePatientCommand, repo):

    patient = Patient(
        #id=None,  # Let SQL auto-generate the ID
        name=PatientName(cmd.first_name, cmd.last_name),
        birth_date=BirthDate(cmd.birth_date),
        national_id=NationalID(cmd.national_id),
        patient_address=PatientAddress(cmd.patient_address)
    )

    repo.add(patient)
    repo.commit()

def handle_find_patient(cmd: FindPatientCommand, repo):
    # Create a proper NationalID value object from the string
    national_id = NationalID(cmd.national_id)
    patient = repo.get_by_national_id(national_id)
    if not patient:
        raise ValueError("Patient not found")
    return patient

def handle_update_patient_info(cmd: UpdatePatientInfoCommand, repo):

    patient = Patient(
        id=PatientID(cmd.id),
        name=PatientName(cmd.first_name, cmd.last_name),
        birth_date=BirthDate(cmd.birth_date),
        national_id=NationalID(cmd.national_id),
        patient_address=PatientAddress(cmd.patient_address)
    )

    repo.update(patient)

def handle_delete_patient(cmd: DeletePatientCommand, repo):
    # Create a proper PatientID value object from the integer
    patient_id = PatientID(cmd.id)
    deleted = repo.delete(patient_id)
    if not deleted:
        raise ValueError("Patient not found")