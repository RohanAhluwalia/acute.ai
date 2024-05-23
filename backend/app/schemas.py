from pydantic import BaseModel
from typing import Optional
from datetime import date

class PatientBase(BaseModel):
    patient_id: str
    name: str
    birth_date: date
    gender: str

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    id: int

    class Config:
        orm_mode = True

class EHRDataBase(BaseModel):
    patient_id: str
    data: dict
    source: str

class EHRDataCreate(EHRDataBase):
    pass

class EHRData(EHRDataBase):
    id: int

    class Config:
        orm_mode = True

class DiabetesDataBase(BaseModel):
    patient_id: str
    data: dict
    source: str

class DiabetesDataCreate(DiabetesDataBase):
    pass

class DiabetesData(DiabetesDataBase):
    id: int

    class Config:
        orm_mode = True
