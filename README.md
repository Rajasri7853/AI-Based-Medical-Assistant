# 🏥 Medical Record Analysis Automation with n8n  

This project automates the processing and analysis of medical records using **n8n workflows** integrated with OCR and AI services. It extracts key medical information from uploaded documents, summarizes potential health issues, recommends diagnostic tests, and generates a concise patient email report.  

---

## ✨ Features  

- **File Upload via Webhook:** Accepts medical record files (PDF/image) through an HTTP webhook.  
- **OCR Processing:** Uses OCR.space API to extract text from uploaded medical records.  
- **Information Extraction:** Extracts important patient data such as name, age, symptoms, diagnosis, and treatment details.  
- **AI-powered Medical Summary:** Utilizes Google Gemini (PaLM) AI models to analyze the extracted information and create a clear, concise medical summary email.  
- **Automated Email Sending:** Sends the summary directly to the patient via Gmail integration.  
- **Error Handling:** Validates file uploads and ensures smooth workflow execution.  
- **NEW → EHR Integration:** Supports basic integration with **FHIR APIs** for Electronic Health Records.  

---

## 🛠 Technologies Used  

- [n8n](https://n8n.io/) - Workflow automation platform  
- [OCR.space API](https://ocr.space/) - Optical character recognition  
- Google Gemini (PaLM) API - AI language model for medical text analysis  
- Gmail API - Email sending integration  
- [FHIR API](https://www.hl7.org/fhir/) - Open healthcare interoperability standard  

---

## 📊 Workflow Overview  

1. **Webhook Node:** Receives medical record files via HTTP POST request.  
2. **HTTP Request Node:** Sends the file to OCR.space for text extraction.  
3. **Information Extractor Node:** Parses the OCR output for relevant medical data.  
4. **AI Agent Node:** Generates a patient-friendly medical summary email using AI.  
5. **Gmail Node:** Sends the generated email to the patient.  
6. **(New) FHIR Integration Script:** Connects to FHIR EHR servers to fetch basic patient details.  

---

## ⚙️ Setup Instructions  

1. Clone this repository.  
2. Import the included n8n workflow JSON file into your n8n instance.  
3. Configure credentials for:  
   - OCR.space API (get your API key at https://ocr.space/ocrapi)  
   - Google Gemini (PaLM) API  
   - Gmail OAuth2 credentials  
4. (Optional) Run the **EHR integration script** for FHIR API connectivity.  

---

## ▶️ Usage  

### For n8n Workflow  
- Send a POST request to the webhook URL with a medical record file (PDF or image).  
- The workflow will process the file and send a summarized medical report email automatically.  

### For EHR Integration (FHIR)  
1. Install dependencies:  
   ```bash
   pip install requests
2. Run the script :
   ```bash
   python ehr_integration.py
3. example output :
   Patient Details:
   {'id': 'example', 'name': 'Peter Chalmers', 'gender': 'male', 'birth_date': '1974-12-25'}

## Important Notes

- This tool is for informational and demonstration purposes only. It is **not a substitute for professional medical advice or diagnosis**.  
- Ensure compliance with all relevant patient data privacy laws (e.g., HIPAA, GDPR) when handling medical records.  

---

## License

This project is licensed under the MIT License.

---

## Contact

For questions or support, please contact: [Your Email]

---

*This email was sent automatically with n8n*  
https://n8n.io
