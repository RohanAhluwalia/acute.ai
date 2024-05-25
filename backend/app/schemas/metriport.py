from pydantic import BaseModel
from typing import List, Optional

class Address(BaseModel):
    addressLine1: str
    city: str
    state: str
    zip: str
    country: str

class PatientCreate(BaseModel):
    firstName: str
    lastName: str
    dob: str
    genderAtBirth: str
    address: List[Address]

class PatientResponse(BaseModel):
    id: str
    firstName: str
    lastName: str
    dob: str
    genderAtBirth: str
    address: List[Address]

class DocumentResponse(BaseModel):
    id: str
    type: str
    content: str
    date: str
