from datetime import datetime

from hospital.domain.models.entities.admission import Admission
from hospital.domain.models.entities.bed import Bed
from hospital.domain.models.entities.patient import Patient
from hospital.domain.models.value_objects.bed_label import BedLabel
from hospital.domain.models.value_objects.people.birth_date import BirthDate
from hospital.domain.models.value_objects.people.national_id import NationalID
from hospital.domain.models.value_objects.people.address import Address
#from hospital.domain.models.value_objects.people.people_id import People_ID
from hospital.domain.models.value_objects.people.people_name import Name

def test_patient_object_valid_creation():
    patient = Patient(Name("Ana", "Lopez"), BirthDate(datetime(1996,10,10)), NationalID("000-00000000-1"), Address("52 1st Street, New York, NY, USA"))

    assert patient.name == Name("Ana", "Lopez")

def test_locate_existing_patient_object():
    patient = Patient(Name("Ana", "Lopez"), BirthDate(datetime(1996,10,10)), NationalID("000-00000000-1"), Address("52 1st Street, New York, NY, USA"))
    bed = Bed(BedLabel("ROOM-303", "B"), is_reserved=False)
    admission = Admission("ADM-003", patient, bed)

    bed.assign(admission)

    assert bed._current_admission.patient == patient
    assert bed.bedLabel == BedLabel("ROOM-303", "B")

    location = f"{bed.bedLabel}"
    assert location == "ROOM-303 - B"