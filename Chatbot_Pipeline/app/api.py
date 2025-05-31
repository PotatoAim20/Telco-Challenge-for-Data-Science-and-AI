from fastapi import APIRouter
from app.schemas import PredictRequest
from app.session import session_store, STATIC_SESSION_ID
from app.extractor import extract_json, generate_churn_explanation
from app.model import predict_churn

router = APIRouter()

required_fields = [
        "gender", "senior_citizen", "is_married", "dependents", "tenure",
        "phone_service", "dual", "internet_service", "online_security",
        "online_backup", "device_protection", "tech_support", "streaming_tv",
        "streaming_movies", "contract", "paperless_billing", "payment_method",
        "monthly_charges", "total_charges"
    ]

@router.post("/predict")
async def predict(req: PredictRequest):
    session_id = STATIC_SESSION_ID
    current_data = session_store.get(session_id) or {}

    if req.description:
        extracted = extract_json(req.description)
        if extracted:
            current_data.update(extracted)

    if req.user_replies:
        current_data.update(req.user_replies)

    missing = {f: current_data.get(f) for f in required_fields if current_data.get(f) is None}

    if missing:
        session_store[session_id] = current_data
        return {
            "status": "need_more_info",
            "missing_fields": missing,
            "partial_data": current_data,
            "session_id": session_id
        }

    prediction, probability = predict_churn(current_data)
    explanation = generate_churn_explanation("Yes" if prediction else "No", probability * 100)
    session_store.pop(session_id, None)

    return {
        "status": "success",
        "predicted_churn": "Yes" if prediction else "No",
        "churn_probability": f"{probability:.2%}",
        "explanation": explanation,
        "data": current_data
    }
