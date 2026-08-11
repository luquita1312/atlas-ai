from pydantic import BaseModel


class TranscriptSegment(BaseModel):
    start: float
    end: float
    text: str


class TranscriptResult(BaseModel):
    language: str
    segments: list[TranscriptSegment]

class ClipCandidate(BaseModel):
    start: float
    end: float
    text: str
    score: float
    hook_score: float = 0.0
    curiosity_score: float = 0.0
    value_score: float = 0.0
    duration_score: float = 0.0
    content_score: float = 0.0
    
    