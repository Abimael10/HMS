from hospital.domain.models.value_objects.people.birth_date import BirthDate
from hospital.domain.models.value_objects.people.national_id import NationalID
from hospital.domain.models.value_objects.people.address import Address
from hospital.domain.models.value_objects.people.people_id import People_ID

from psycopg2.extensions import register_adapter, AsIs

# Create SQLAlchemy type adapters for our domain value objects
class PatientIDAdapter:
    @classmethod
    def adapt(cls, obj):
        if isinstance(obj, People_ID):
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
        if isinstance(obj, Address):
            return obj.value
        return obj

def register_adapters():
    try:
        # Register adapter for PatientID
        register_adapter(People_ID, lambda x: AsIs(str(x.value)))
        register_adapter(BirthDate, lambda x: x.value)
        register_adapter(NationalID, lambda x: x.value)
        register_adapter(Address, lambda x: x.value)
    except Exception as e:
        # Log the error but continue - likely we'll need to handle this in the mapper
        print(f"Error registering adapters: {e}")