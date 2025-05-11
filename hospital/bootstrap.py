import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from hospital.adapters.orm.main_adapter import start_mappers

#start_mappers()

from hospital.adapters.orm.metadata import mapper_metadata
from hospital.adapters.repository.patients.sqlalchemy_respository import SqlAlchemyPatientRepository
#from hospital.adapters.repository.sqlalchemy_respository import SqlAlchemyPatientRepository
from hospital.service_layer.patients.messagebus import MessageBus
#from hospital.tests.fakes.fake_patient_repository import FakePatientRepository
from hospital.config import get_postgres_uri

@pytest.fixture(scope="session", autouse=True)
def initialize_mappers():
    start_mappers()

def bootstrap():
    connection_string = get_postgres_uri()
    
    engine = create_engine(connection_string, echo=True)
    mapper_metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    #Fake repo, replace in prod
    #repo = FakePatientRepository(session)
    repo = SqlAlchemyPatientRepository(session)

    return MessageBus(repo=repo, session=session)