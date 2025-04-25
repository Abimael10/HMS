from hospital.domain.models.value_objects.patient.birth_date import BirthDate
from hospital.domain.models.value_objects.patient.national_id import NationalID
from hospital.domain.models.value_objects.patient.patient_address import PatientAddress
from hospital.domain.models.value_objects.patient.patient_id import PatientID

from psycopg2.extensions import register_adapter, AsIs

# Create SQLAlchemy type adapters for our domain value objects
class PatientIDAdapter:
    @classmethod
    def adapt(cls, obj):
        if isinstance(obj, PatientID):
            return obj.value
        return obj

class BirthDateAdapter:
    @classmethod
    def adapt(cls, obj):
        if isinstance(obj, BirthDate):
            return obj.value
        return obj

class NationalIDAdapter:
    @classmethod
    def adapt(cls, obj):
        if isinstance(obj, NationalID):
            return obj.value
        return obj

class PatientAddressAdapter:
    @classmethod
    def adapt(cls, obj):
        if isinstance(obj, PatientAddress):
            return obj.value
        return obj

def register_adapters():
    try:
        # Register adapter for PatientID
        register_adapter(PatientID, lambda x: AsIs(str(x.value)))
        register_adapter(BirthDate, lambda x: x.value)
        register_adapter(NationalID, lambda x: x.value)
        register_adapter(PatientAddress, lambda x: x.value)
    except Exception as e:
        # Log the error but continue - likely we'll need to handle this in the mapper
        print(f"Error registering adapters: {e}")