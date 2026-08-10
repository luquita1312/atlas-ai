from .base_agent import BaseAgent
from ..models.schemas import TranscriptResult, ClipCandidate


class ViralAgent(BaseAgent):

    def __init__(self, name: str = "ViralAgent"):
        super().__init__(name)

    def run(self, transcript: TranscriptResult) -> list[ClipCandidate]:
        candidates = []

        for segment in transcript.segments:
            duration = segment.end - segment.start
            text = segment.text.strip()

            score = 0.0

            # Duración adecuada para un fragmento corto
            if 5 <= duration <= 30:
                score += 0.3

            # El fragmento tiene suficiente contenido
            if len(text.split()) >= 8:
                score += 0.2

            # Detectamos palabras que pueden indicar un hook
            hook_words = [
                "cómo",
                "por qué",
                "secreto",
                "importante",
                "nunca",
                "error",
                "problema",
                "mejor",
                "peor",
                "sorprendente",
            ]

            text_lower = text.lower()

            if any(word in text_lower for word in hook_words):
                score += 0.3

            # Penalizamos fragmentos demasiado cortos
            if duration < 3:
                score -= 0.2

            score = max(0.0, min(score, 1.0))

            candidates.append(
                ClipCandidate(
                    start=segment.start,
                    end=segment.end,
                    text=text,
                    score=score,
                )
            )

        candidates.sort(
            key=lambda candidate: candidate.score,
            reverse=True
        )

        return candidates
    