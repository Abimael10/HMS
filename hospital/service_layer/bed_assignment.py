from hospital.domain.models.entities.admission import Admission
from hospital.domain.models.entities.bed import Bed
from hospital.domain.models.entities.patient import Patient

class BedAssignmentService:
    @staticmethod
    def assign_patient_to_bed(patient: Patient, bed: Bed, admission_id: str, is_emergency: bool = False) -> Admission:
        if bed.is_occupied:
            raise ValueError(f"Bed {bed.bedLabel} is already occupied")

        admission = Admission(
            id=admission_id,
            patient=patient,
            bed=bed,
            is_emergency=is_emergency
        )

        bed.assign(admission)
        return admission