from sqlalchemy import Column, Integer, String, Date, JSON, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Patient(Base):
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    birth_date = Column(Date, nullable=False)
    gender = Column(String, nullable=False)

    # Relationship to EHRData and DiabetesData
    ehr_data = relationship("EHRData", back_populates="patient", cascade="all, delete-orphan")
    diabetes_data = relationship("DiabetesData", back_populates="patient", cascade="all, delete-orphan")

class EHRData(Base):
    __tablename__ = "ehr_data"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(String, ForeignKey("patients.patient_id"), nullable=False)
    data = Column(JSON, nullable=False)
    source = Column(String, nullable=False)
    fetched_at = Column(Date, nullable=False)

    # Relationship to Patient
    patient = relationship("Patient", back_populates="ehr_data")

class DiabetesData(Base):
    __tablename__ = "diabetes_data"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(String, ForeignKey("patients.patient_id"), nullable=False)
    data = Column(JSON, nullable=False)
    source = Column(String, nullable=False)
    fetched_at = Column(Date, nullable=False)

    # Relationship to Patient
    patient = relationship("Patient", back_populates="diabetes_data")
