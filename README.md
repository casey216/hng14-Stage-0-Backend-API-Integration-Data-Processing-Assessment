# Gender Classification API

## 📌 Overview
This API classifies a name's likely gender using the Genderize API and applies additional processing rules.

---

## 🚀 Endpoint

GET /api/classify?name=<name>

### Example:
GET /api/classify?name=John

---

## ✅ Success Response

```json
{
  "status": "success",
  "data": {
    "name": "john",
    "gender": "male",
    "probability": 0.99,
    "sample_size": 1234,
    "is_confident": true,
    "processed_at": "2026-04-01T12:00:00Z"
  }
}
