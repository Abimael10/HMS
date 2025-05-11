#import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
from hospital.adapters.orm.main_adapter import start_mappers

#start_mappers()

from hospital.adapters.orm.metadata import mapper_metadata

#TEST_DB_PATH = "./test.db"

"""
@pytest.fixture
def engine():
    
    # Si existe de antes, elimínala para un test limpio
    if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)
    
    engine = create_engine(f"sqlite:///:memory:", future=True)
    mapper_metadata.create_all(engine)
    start_mappers()
    return engine
"""

@pytest.fixture(scope="session", autouse=True)
def initialize_mappers():
    start_mappers()

@pytest.fixture
def session():
    engine = create_engine(f"sqlite:///:memory:", future=True)
    mapper_metadata.create_all(engine)

    Session = sessionmaker(bind=engine, future=True)
    sess = Session()
    yield sess
    sess.close()
    clear_mappers()

    """
        if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)  # borra al final para tests limpios
    """