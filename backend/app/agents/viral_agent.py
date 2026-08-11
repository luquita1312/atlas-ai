from .base_agent import BaseAgent
from .content_analyzer import ContentAnalyzer
from ..models.schemas import ClipCandidate


class ViralAgent(BaseAgent):

    def __init__(self, name: str = "ViralAgent"):
        super().__init__(name)
        self.analyzer = ContentAnalyzer()

    def run(self, candidates: list[ClipCandidate]) -> list[ClipCandidate]:
        scored_candidates = []

        for candidate in candidates:
            duration = candidate.end - candidate.start
            text = candidate.text.strip()

            analysis = self.analyzer.analyze(text)

            duration_score = 0.0

            if 15 <= duration <= 45:
                duration_score = 0.20
            elif 45 < duration <= 60:
                duration_score = 0.10

            score = (
                duration_score
                + analysis.hook_strength * 0.25
                + analysis.curiosity * 0.20
                + analysis.information_value * 0.15
                + analysis.clarity * 0.15
                + analysis.emotional_intensity * 0.10
            )

            if duration < 10:
                score -= 0.20

            score = max(0.0, min(score, 1.0))

            scored_candidates.append(
                ClipCandidate(
                    start=candidate.start,
                    end=candidate.end,
                    text=text,
                    score=score,
                    hook_score=analysis.hook_strength * 0.25,
                    curiosity_score=analysis.curiosity * 0.20,
                    value_score=analysis.information_value * 0.15,
                    duration_score=duration_score,
                    content_score=analysis.clarity * 0.15,
                )
            )

        scored_candidates.sort(
            key=lambda candidate: candidate.score,
            reverse=True,
        )

        return scored_candidates


