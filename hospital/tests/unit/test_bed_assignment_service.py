from datetime import datetime

from hospital.domain.models.entities.bed import Bed
from hospital.domain.models.entities.patient import Patient
from hospital.domain.models.value_objects.bed_label import BedLabel
from hospital.domain.models.value_objects.patient.birth_date import BirthDate
from hospital.domain.models.value_objects.patient.national_id import NationalID
from hospital.domain.models.value_objects.patient.patient_address import PatientAddress
from hospital.domain.models.value_objects.patient.patient_id import PatientID
from hospital.domain.models.value_objects.patient.patient_name import PatientName
from hospital.service_layer.bed_assignment import BedAssignmentService


def test_bed_assignment_service_assigns_patient_to_bed():
    bed = Bed(BedLabel("ROOM-101", "A"), is_reserved=False)
    patient = Patient(PatientID(1), PatientName("Ana", "Lopez"), BirthDate(datetime(1996,10,10)), NationalID("000-00000000-1"), PatientAddress("52 1st Street, New York, NY, USA"))

    admission = BedAssignmentService.assign_patient_to_bed(
        patient=patient,
        bed=bed,
        admission_id="ADM-001"
    )

    assert bed.is_occupied is True
    assert admission.bed == bed
    assert admission.patient == patient