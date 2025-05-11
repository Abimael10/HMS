from datetime import datetime

from hospital.domain.models.entities.bed import Bed
from hospital.domain.models.entities.patient import Patient
from hospital.domain.models.value_objects.bed_label import BedLabel
from hospital.domain.models.entities.admission import Admission

import pytest

from hospital.domain.models.value_objects.people.birth_date import BirthDate
from hospital.domain.models.value_objects.people.national_id import NationalID
from hospital.domain.models.value_objects.people.address import Address
from hospital.domain.models.value_objects.people.people_name import Name


def test_admitting_patient_to_bed_marks_it_as_occupied():
    bed = Bed(BedLabel("ROOM-101", "A"), is_reserved=False)
    patient = Patient(Name("Ana", "Lopez"), BirthDate(datetime(1996,10,10)), NationalID("000-00000000-1"), Address("52 1st Street, New York, NY, USA"))
    admission = Admission("ADM-001", patient, bed)
    bed.assign(admission)

    assert bed.is_occupied is True

def test_discharge_patient_frees_bed():
    bed = Bed(BedLabel("ROOM-101", "A"), is_reserved=False)
    patient = Patient(Name("Ana", "Lopez"), BirthDate(datetime(1996,10,10)), NationalID("000-00000000-1"), Address("52 1st Street, New York, NY, USA"))
    admission = Admission("ADM-001", patient, bed)

    bed.assign(admission)
    assert bed.is_occupied is True

    bed.discharge()
    assert bed.is_occupied is False

def test_emergency_patient_can_override_reservation():
    bed = Bed(BedLabel("ROOM-101", "A"), is_reserved=True)
    patient = Patient(Name("Ana", "Lopez"), BirthDate(datetime(1996,10,10)), NationalID("000-00000000-1"), Address("52 1st Street, New York, NY, USA"))
    admission = Admission("ADM-001", patient, bed, is_emergency=True)

    bed.assign(admission)

    assert bed.is_occupied is True

def test_non_emergency_cannot_use_reserved_bed():
    bed = Bed(BedLabel("ROOM-202", "D"), is_reserved=True)
    patient = Patient(Name("Ana", "Lopez"), BirthDate(datetime(1996,10,10)), NationalID("000-00000000-1"), Address("52 1st Street, New York, NY, USA"))
    admission = Admission("ADM-002", patient, bed, is_emergency=False)

    with pytest.raises(ValueError, match="reserved bed to non-emergency"):
        bed.assign(admission)

def test_cannot_assign_two_patients_to_same_bed():
    bed = Bed(BedLabel("ROOM-202", "D"), is_reserved=False)

    patient1 = Patient(Name("Ana", "Lopez"), BirthDate(datetime(1996,10,10)), NationalID("000-00000000-1"), Address("52 1st Street, New York, NY, USA"))
    admission1 = Admission("ADM-001", patient1, bed)
    bed.assign(admission1)

    patient2 = Patient(Name("Billy", "Bob"), BirthDate(datetime(1996,10,10)), NationalID("000-00000000-2"), Address("53 1st Street, New York, NY, USA"))
    admission2 = Admission("ADM-002", patient2, bed)

    with pytest.raises(ValueError, match="already occupied"):
        bed.assign(admission2)

    assert bed.is_occupied is True