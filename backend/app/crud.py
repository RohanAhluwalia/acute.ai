from sqlalchemy.orm import Session
from . import models, schemas

def get_patient_by_id(db: Session, patient_id: str):
    return db.query(models.Patient).filter(models.Patient.patient_id == patient_id).first()

def create_patient(db: Session, patient: schemas.PatientCreate):
    db_patient = models.Patient(
        patient_id=patient.patient_id,
        name=patient.name,
        birth_date=patient.birth_date,
        gender=patient.gender
    )
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def create_ehr_data(db: Session, ehr_data: schemas.EHRDataCreate):
    db_ehr_data = models.EHRData(
        patient_id=ehr_data.patient_id,
        data=ehr_data.data,
        source=ehr_data.source
    )
    db.add(db_ehr_data)
    db.commit()
    db.refresh(db_ehr_data)
    return db_ehr_data

def create_diabetes_data(db: Session, diabetes_data: schemas.DiabetesDataCreate):
    db_diabetes_data = models.DiabetesData(
        patient_id=diabetes_data.patient_id,
        data=diabetes_data.data,
        source=diabetes_data.source
    )
    db.add(db_diabetes_data)
    db.commit()
    db.refresh(db_diabetes_data)
    return db_diabetes_data

def get_ehr_data_by_patient_id(db: Session, patient_id: str):
    return db.query(models.EHRData).filter(models.EHRData.patient_id == patient_id).first()

def get_diabetes_data_by_patient_id(db: Session, patient_id: str):
    return db.query(models.DiabetesData).filter(models.DiabetesData.patient_id == patient_id).first()
