from hospital.adapters.orm.metadata import mapper_registry
from hospital.adapters.orm.patients.patient_orm import PatientORM
from hospital.adapters.orm.patients.patient_schema import patients_schema
from hospital.adapters.orm.patients.value_objects_adapters import register_adapters

already_mapped = False

def start_mappers():
    global already_mapped
    if already_mapped:
        return

    # Try to register psycopg2 adapters
    register_adapters()

    # Map the ORM model to the table
    mapper_registry.map_imperatively(PatientORM, patients_schema)
    already_mapped = True