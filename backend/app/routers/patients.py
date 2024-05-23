from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, crud, dependencies

router = APIRouter()

@router.post("/patients/", response_model=schemas.Patient)
def create_patient(patient: schemas.PatientCreate, db: Session = Depends(dependencies.get_db)):
    db_patient = crud.get_patient_by_id(db, patient_id=patient.patient_id)
    if db_patient:
        raise HTTPException(status_code=400, detail="Patient already registered")
    return crud.create_patient(db=db, patient=patient)

@router.get("/patients/{patient_id}", response_model=schemas.Patient)
def read_patient(patient_id: str, db: Session = Depends(dependencies.get_db)):
    db_patient = crud.get_patient_by_id(db, patient_id=patient_id)
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return db_patient
