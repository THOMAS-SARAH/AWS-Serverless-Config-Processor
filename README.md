# AWS Serverless Multi-Tenant Configuration Processor

An event-driven serverless microservice built on AWS to process and persist SaaS configuration payloads directly into cloud storage.

---

## 🛠️ Tech Stack & AWS Services

- **Compute:** AWS Lambda (Python 3.11 / Boto3)
- **API Management:** AWS API Gateway (HTTP API)
- **Object Storage:** AWS S3 Bucket (`saas-config-store-sarah`)
- **Access Control:** AWS IAM Execution Roles

---

## 📡 Live API Endpoint & Response

- **HTTP Endpoint:** `GET / POST` via AWS API Gateway

### Sample JSON Output:
```json
{
  "message": "Tenant configuration processed and persisted successfully",
  "bucket": "saas-config-store-sarah",
  "s3_key": "tenants/default_tenant/config_2026-10-07_16-18-13.json",
  "processed_at": "2026-10-07_16-18-13"
}
