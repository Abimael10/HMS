import pytest
from fastapi import FastAPI, Depends
from fastapi.testclient import TestClient

from hospital.adapters.repository.patients.sqlalchemy_respository import SqlAlchemyPatientRepository
from hospital.entrypoints.views.patients import create_patient
from hospital.service_layer.patients.commands import CreatePatientCommand
from hospital.service_layer.patients.messagebus import MessageBus
from hospital.tests.conftest import session

@pytest.fixture
def test_client(session):
    app = FastAPI()

    repo = SqlAlchemyPatientRepository(session)
    bus = MessageBus(repo=repo, session=session)

    def get_test_bus():
        return bus

    @app.post("/create_patient", status_code=201)
    def route_create_patient(
            cmd: CreatePatientCommand,
            test_bus: MessageBus = Depends(get_test_bus)
    ):
        return create_patient(cmd, test_bus)

    return TestClient(app)

def test_create_patient_e2e(test_client, session):
    response = test_client.post("/create_patient", json={
        "first_name": "Ana",
        "last_name": "Lopez",
        "birth_date": "1996-10-10",
        "national_id": "000-00000000-4",
        "address": "52 1st Street, New York, NY, USA"
    })

    print(response.status_code)
    print(response.json())
    assert response.status_code == 201
    assert response.json() == {"status": "Patient created"}