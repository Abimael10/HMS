from abc import ABC, abstractmethod

class AbstractRepository(ABC):
    def __init__(self):
        self.session = None

    @abstractmethod
    def add(self, patient):
        raise NotImplemented

    @abstractmethod
    def get(self, patient_id):
        raise NotImplemented

    @abstractmethod
    def delete(self, patient_id) -> bool:
        raise NotImplemented

    @abstractmethod
    def list(self):
        raise NotImplemented

    def get_by_national_id(self, national_id):
        raise NotImplemented