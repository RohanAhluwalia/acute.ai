from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.api.v1.endpoints.health import get_db
from app.utils.metriport import create_patient, get_patient_documents
from app.schemas.metriport import PatientCreate, PatientResponse, DocumentResponse

router = APIRouter()

@router.post("/patients", response_model=PatientResponse)
def add_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    patient_data = patient.dict()
    response = create_patient(patient_data)
    if "error" in response:
        raise HTTPException(status_code=400, detail=response["error"])
    return response

@router.get("/patients/{patient_id}/documents", response_model=DocumentResponse)
def fetch_patient_documents(patient_id: str, db: Session = Depends(get_db)):
    response = get_patient_documents(patient_id)
    if "error" in response:
        raise HTTPException(status_code=400, detail=response["error"])
    return response
