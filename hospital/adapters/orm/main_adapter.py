from hospital.adapters.orm.metadata import mapper_registry
from hospital.adapters.orm.patients.patient_orm import PatientORM
from hospital.adapters.orm.patients.patient_schema import patients_schema
from hospital.adapters.orm.patients.value_objects_adapters import register_adapters

_already_mapped = False

def start_mappers():
    global _already_mapped
    if _already_mapped:
        return

    # Try to register psycopg2 adapters
    register_adapters()

    # Map the ORM model to the table
    mapper_registry.map_imperatively(PatientORM, patients_schema)
    _already_mapped = True