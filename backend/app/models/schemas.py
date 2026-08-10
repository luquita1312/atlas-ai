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
    