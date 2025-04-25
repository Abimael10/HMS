from sqlalchemy import Table, Column, Integer, String, Date

from hospital.adapters.orm.metadata import mapper_metadata

patients_schema = Table(
    "patients", mapper_metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("first_name", String(255)),
    Column("last_name", String(255)),
    Column("birth_date", Date),
    Column("national_id", String(50), unique=True),
    Column("patient_address", String(255))
)