from .base_agent import BaseAgent
from ..models.schemas import TranscriptResult


class TranscriptAgent(BaseAgent):

    def run(self, input_data) -> TranscriptResult:
        return TranscriptResult(
            language="es",
            segments=[
                {
                    "start": 0.0,
                    "end": 4.2,
                    "text": input_data
                }
            ]
        )
