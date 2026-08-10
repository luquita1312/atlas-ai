from ..models.schemas import TranscriptResult, ClipCandidate


class ClipBuilder:

    def __init__(
        self,
        min_duration: float = 15.0,
        max_duration: float = 60.0,
    ):
        self.min_duration = min_duration
        self.max_duration = max_duration

    def build(self, transcript: TranscriptResult) -> list[ClipCandidate]:
        candidates = []

        segments = transcript.segments

        for start_index in range(len(segments)):
            start_segment = segments[start_index]

            text_parts = []

            for end_index in range(start_index, len(segments)):
                end_segment = segments[end_index]

                duration = end_segment.end - start_segment.start

                text_parts.append(end_segment.text.strip())

                if duration > self.max_duration:
                    break

                if duration >= self.min_duration:
                    candidates.append(
                        ClipCandidate(
                            start=start_segment.start,
                            end=end_segment.end,
                            text=" ".join(text_parts),
                            score=0.0,
                        )
                    )

        return candidates
