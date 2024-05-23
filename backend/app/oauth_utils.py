import requests
from authlib.integrations.requests_client import OAuth2Session
from fastapi import HTTPException
from .config import settings

def get_oauth_session(client_id: str, client_secret: str, redirect_uri: str):
    return OAuth2Session(client_id, client_secret, redirect_uri=redirect_uri)

def get_ehr_source_config(ehr_source_id: str):
    for source in settings.ehr_sources:
        if source.id == ehr_source_id:
            return source
    raise ValueError(f"EHR source configuration for {ehr_source_id} not found")

def exchange_code_for_token(ehr_source_id: str, code: str) -> str:
    source_config = get_ehr_source_config(ehr_source_id)
    session = get_oauth_session(source_config.client_id, source_config.client_secret, "http://localhost:8000/api/oauth/callback")
    token = session.fetch_token(source_config.token_url, code=code)
    return token["access_token"]

def fetch_patient_data(ehr_source_id: str, access_token: str) -> dict:
    source_config = get_ehr_source_config(ehr_source_id)
    response = requests.get(f"{source_config.fhir_url}/Patient", headers={"Authorization": f"Bearer {access_token}"})
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch patient data")
