from faster_whisper import WhisperModel

from .base_agent import BaseAgent
from ..models.schemas import TranscriptResult


class TranscriptAgent(BaseAgent):

    def __init__(
        self,
        name: str = "TranscriptAgent",
        model_size: str = "tiny"
    ):
        super().__init__(name)

        self.model = WhisperModel(
            model_size,
            device="cpu",
            compute_type="int8"
        )

    def run(self, input_data) -> TranscriptResult:

        segments, info = self.model.transcribe(
            input_data,
            beam_size=5
        )

        transcript_segments = [
            {
                "start": segment.start,
                "end": segment.end,
                "text": segment.text.strip()
            }
            for segment in segments
        ]

        return TranscriptResult(
            language=info.language,
            segments=transcript_segments
        )
