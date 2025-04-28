from pydantic import BaseModel
from datetime import date

class CreatePatientCommand(BaseModel):
    first_name: str
    last_name: str
    birth_date: date
    national_id: str
    patient_address: str

class FindPatientCommand(BaseModel):
    national_id: str

class UpdatePatientInfoCommand(BaseModel):
    id: int
    first_name: str
    last_name: str
    birth_date: date
    national_id: str
    patient_address: str

class DeletePatientCommand(BaseModel):
    id: int