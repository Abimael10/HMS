from datetime import datetime

from hospital.domain.models.entities.bed import Bed
from hospital.domain.models.entities.patient import Patient
from hospital.domain.models.value_objects.bed_label import BedLabel
from hospital.domain.models.value_objects.people.birth_date import BirthDate
from hospital.domain.models.value_objects.people.national_id import NationalID
from hospital.domain.models.value_objects.people.address import Address
from hospital.domain.models.value_objects.people.people_name import Name
from hospital.service_layer.bed_assignment import BedAssignmentService


def test_bed_assignment_service_assigns_patient_to_bed():
    bed = Bed(BedLabel("ROOM-101", "A"), is_reserved=False)
    patient = Patient(Name("Ana", "Lopez"), BirthDate(datetime(1996,10,10)), NationalID("000-00000000-1"), Address("52 1st Street, New York, NY, USA"))

    admission = BedAssignmentService.assign_patient_to_bed(
        patient=patient,
        bed=bed,
        admission_id="ADM-001"
    )

    assert bed.is_occupied is True
    assert admission.bed == bed
    assert admission.patient == patient