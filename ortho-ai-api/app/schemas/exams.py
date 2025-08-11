from pydantic import BaseModel
from typing import Optional
from datetime import date

class ExamCreate(BaseModel):
    patient_id: int
    doctor_id: int
    diagnosis: str
    diagnosis_photo_url: Optional[str] = None

class ExamResponse(BaseModel):
    patient_id: int
    doctor_id: int
    diagnosis: str
    diagnosis_photo_url: Optional[str] = None