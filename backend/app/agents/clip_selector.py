from ..models.schemas import ClipCandidate


class ClipSelector:

    def __init__(
        self,
        max_clips: int = 3,
        overlap_threshold: float = 0.5,
        similarity_threshold: float = 0.75,
        semantic_similarity=None,
    ):
        self.max_clips = max_clips
        self.overlap_threshold = overlap_threshold
        self.similarity_threshold = similarity_threshold
        self.semantic_similarity = semantic_similarity

    def select(self, clips: list[ClipCandidate]) -> list[ClipCandidate]:
        selected = []

        for clip in clips:
            if len(selected) >= self.max_clips:
                break

            if self._is_too_similar(clip, selected):
                continue

            selected.append(clip)

        return selected

    def _is_too_similar(
        self,
        clip: ClipCandidate,
        selected: list[ClipCandidate],
    ) -> bool:

        for existing in selected:

            # 1. Similitud temporal
            overlap = self._calculate_overlap(clip, existing)

            if overlap >= self.overlap_threshold:
                return True

            # 2. Similitud semántica
            if self.semantic_similarity is not None:

                semantic_score = self.semantic_similarity.similarity(
                    clip.text,
                    existing.text,
                )

                if semantic_score >= self.similarity_threshold:
                    return True

        return False

    def _calculate_overlap(
        self,
        clip_a: ClipCandidate,
        clip_b: ClipCandidate,
    ) -> float:

        intersection_start = max(clip_a.start, clip_b.start)
        intersection_end = min(clip_a.end, clip_b.end)

        if intersection_end <= intersection_start:
            return 0.0

        intersection = intersection_end - intersection_start

        duration_a = clip_a.end - clip_a.start
        duration_b = clip_b.end - clip_b.start

        shorter_duration = min(duration_a, duration_b)

        if shorter_duration <= 0:
            return 0.0

        return intersection / shorter_duration
