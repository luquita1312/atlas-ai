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
            text_lower = text.lower()

            # Scores individuales
            duration_score = 0.0
            content_score = 0.0
            hook_score = 0.0
            curiosity_score = 0.0
            value_score = 0.0

            # 1. Duración
            if 15 <= duration <= 45:
                duration_score = 0.20
            elif 45 < duration <= 60:
                duration_score = 0.10

            # 2. Cantidad de contenido
            word_count = len(text.split())

            if 25 <= word_count <= 100:
                content_score = 0.15
            elif word_count > 100:
                content_score = 0.05

            # 3. Hook
            hook_words = [
                "cómo",
                "por qué",
                "sabías",
                "nunca",
                "error",
                "secreto",
                "importante",
                "sorprendente",
            ]

            if any(word in text_lower for word in hook_words):
                hook_score = 0.25

            # 4. Curiosidad
            curiosity_phrases = [
                "pero",
                "sin embargo",
                "la razón",
                "el problema",
                "lo que",
                "resulta que",
            ]

            if any(phrase in text_lower for phrase in curiosity_phrases):
                curiosity_score = 0.20

            # 5. Valor informativo
            value_words = [
                "porque",
                "significa",
                "explica",
                "permite",
                "funciona",
                "importante",
            ]

            if any(word in text_lower for word in value_words):
                value_score = 0.10

            # Score total
            score = (
                duration_score
                + content_score
                + hook_score
                + curiosity_score
                + value_score
            )

            # Penalización por clips demasiado cortos
            if duration < 10:
                score -= 0.20

            score = max(0.0, min(score, 1.0))

            scored_candidates.append(
                ClipCandidate(
                    start=candidate.start,
                    end=candidate.end,
                    text=text,
                    score=score,
                    hook_score=hook_score,
                    curiosity_score=curiosity_score,
                    value_score=value_score,
                    duration_score=duration_score,
                    content_score=content_score,
                )
            )

        scored_candidates.sort(
            key=lambda candidate: candidate.score,
            reverse=True,
        )

        return scored_candidates

