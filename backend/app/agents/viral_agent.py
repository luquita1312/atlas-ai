from .base_agent import BaseAgent
from ..models.schemas import ClipCandidate


class ViralAgent(BaseAgent):

    def __init__(self, name: str = "ViralAgent"):
        super().__init__(name)

    def run(self, candidates: list[ClipCandidate]) -> list[ClipCandidate]:
        scored_candidates = []

        for candidate in candidates:
            duration = candidate.end - candidate.start
            text = candidate.text.strip()

            score = 0.0

            # Duración adecuada para un Short
            if 15 <= duration <= 60:
                score += 0.3

            # Suficiente contenido
            if len(text.split()) >= 20:
                score += 0.2

            # Palabras que pueden indicar un hook
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

            # Penalizamos clips demasiado cortos
            if duration < 10:
                score -= 0.2

            score = max(0.0, min(score, 1.0))

            scored_candidates.append(
                ClipCandidate(
                    start=candidate.start,
                    end=candidate.end,
                    text=text,
                    score=score,
                )
            )

        scored_candidates.sort(
            key=lambda candidate: candidate.score,
            reverse=True,
        )

        return scored_candidates
