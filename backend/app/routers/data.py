from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, crud, dependencies

router = APIRouter()

@router.post("/data/ehr", response_model=schemas.EHRData)
def create_ehr_data(ehr_data: schemas.EHRDataCreate, db: Session = Depends(dependencies.get_db)):
    return crud.create_ehr_data(db=db, ehr_data=ehr_data)

@router.post("/data/diabetes", response_model=schemas.DiabetesData)
def create_diabetes_data(diabetes_data: schemas.DiabetesDataCreate, db: Session = Depends(dependencies.get_db)):
    return crud.create_diabetes_data(db=db, diabetes_data=diabetes_data)

@router.get("/data/ehr/{patient_id}", response_model=schemas.EHRData)
def read_ehr_data(patient_id: str, db: Session = Depends(dependencies.get_db)):
    db_ehr_data = crud.get_ehr_data_by_patient_id(db, patient_id=patient_id)
    if db_ehr_data is None:
        raise HTTPException(status_code=404, detail="EHR data not found")
    return db_ehr_data

@router.get("/data/diabetes/{patient_id}", response_model=schemas.DiabetesData)
def read_diabetes_data(patient_id: str, db: Session = Depends(dependencies.get_db)):
    db_diabetes_data = crud.get_diabetes_data_by_patient_id(db, patient_id=patient_id)
    if db_diabetes_data is None:
        raise HTTPException(status_code=404, detail="Diabetes data not found")
    return db_diabetes_data
