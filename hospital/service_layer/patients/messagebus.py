from hospital.service_layer.patients.commands import CreatePatientCommand, DeletePatientCommand, FindPatientCommand, \
    UpdatePatientInfoCommand
from hospital.service_layer.patients.handlers import handle_create_patient, handle_delete_patient, handle_find_patient, \
    handle_update_patient_info

class MessageBus:
    def __init__(self, repo, session):
        self.repo = repo
        self.session = session
        self.handlers = {
            CreatePatientCommand: handle_create_patient,
            DeletePatientCommand: handle_delete_patient,
            FindPatientCommand: handle_find_patient,
            UpdatePatientInfoCommand: handle_update_patient_info
        }

    def handle(self, command):
        handler = self.handlers[type(command)]

        try:
            result = handler(command, self.repo)
            self.session.commit()
            return result
        except Exception:
            self.session.rollback()
            raise