import requests

# Public FHIR Sandbox (you can replace with OpenMRS/OpenEMR later)
FHIR_BASE_URL = "https://hapi.fhir.org/baseR4"

def fetch_patient(patient_id: str):
    """
    Fetch patient details from FHIR server.
    """
    url = f"{FHIR_BASE_URL}/Patient/{patient_id}"
    response = requests.get(url)

    if response.status_code == 200:
        patient = response.json()
        
        # Extract some details
        name = patient.get("name", [{}])[0].get("given", ["Unknown"])[0]
        family = patient.get("name", [{}])[0].get("family", "Unknown")
        gender = patient.get("gender", "Unknown")
        birth_date = patient.get("birthDate", "Unknown")

        return {
            "id": patient_id,
            "name": f"{name} {family}",
            "gender": gender,
            "birth_date": birth_date
        }
    else:
        return {"error": f"Failed to fetch patient {patient_id}. Status code: {response.status_code}"}

if __name__ == "__main__":
    # Example: patient ID 'example'
    patient_id = "example"
    details = fetch_patient(patient_id)
    print("Patient Details:")
    print(details)
