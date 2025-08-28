from pydantic import BaseModel
from datetime import datetime


class DataModelDto(BaseModel):
    regno_recognize: str
    afts_regno_ai: str
    recognition_accuracy: float
    afts_regno_ai_score: float
    afts_regno_ai_char_scores: str
    afts_regno_ai_length_scores: str
    camera_type: str
    camera_class: str
    time_check: datetime
    direction: int

    def get_attributes(self) -> tuple[str, str, float, float, str, str, str, str, datetime, int]:
        return (
            self.regno_recognize,
            self.afts_regno_ai,
            self.recognition_accuracy,
            self.afts_regno_ai_score,
            self.afts_regno_ai_char_scores,
            self.afts_regno_ai_length_scores,
            self.camera_type,
            self.camera_class,
            self.time_check,
            self.direction
        )
