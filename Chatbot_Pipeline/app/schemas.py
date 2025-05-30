from pydantic import BaseModel

class PredictRequest(BaseModel):
    session_id: str | None = None
    description: str | None = None
    user_replies: dict | None = None
