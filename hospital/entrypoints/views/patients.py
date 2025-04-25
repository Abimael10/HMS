from fastapi import APIRouter, Depends, HTTPException
from hospital.service_layer.commands import CreatePatientCommand, DeletePatientCommand, FindPatientCommand, \
    UpdatePatientInfoCommand
from hospital.service_layer.messagebus import MessageBus
from hospital.bootstrap import bootstrap

router = APIRouter()

# Simple injection
def get_bus() -> MessageBus:
    return bootstrap()

@router.get("/{national_id}", status_code=200)
def get_patient(
        national_id: str,
        bus: MessageBus = Depends(get_bus)
):
    try:
        cmd = FindPatientCommand(national_id=national_id)
        patient = bus.handle(cmd)
        return patient
    except ValueError as e:
        # Cover scenarios like "Patient not found"
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/create_patient", status_code=201)
def create_patient(
    cmd: CreatePatientCommand,
    bus: MessageBus = Depends(get_bus)
):
    try:
        bus.handle(cmd)
        return {"status": "Patient created"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/{id}", status_code=200)
def update_patient(
        cmd: UpdatePatientInfoCommand,
        bus: MessageBus = Depends(get_bus)
):
    try:
        bus.handle(cmd)
        return {"status": "Patient info updated"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{id}", status_code=200)
def delete_patient_by_id(
        id: int,
        bus: MessageBus = Depends(get_bus)
):
    try:
        cmd = DeletePatientCommand(id=id)
        bus.handle(cmd)
        return {"status": "Patient deleted"}
    except ValueError as e:
        # Cover scenarios like "Patient not found"
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
