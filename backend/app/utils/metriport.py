import requests
from app.core.config import settings

def create_patient(patient_data):
    url = f"{settings.METRIPORT_BASE_URL}/v1/patients"
    headers = {
        "Authorization": f"Bearer {settings.METRIPORT_API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, json=patient_data)
    return response.json()

def get_patient_documents(patient_id):
    url = f"{settings.METRIPORT_BASE_URL}/v1/patients/{patient_id}/documents"
    headers = {
        "Authorization": f"Bearer {settings.METRIPORT_API_KEY}"
    }
    response = requests.get(url, headers=headers)
    return response.json()
