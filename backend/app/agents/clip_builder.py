from ..models.schemas import TranscriptResult, ClipCandidate


class ClipBuilder:

    def __init__(
        self,
        min_duration: float = 15.0,
        max_duration: float = 60.0,
        step: float = 5.0,
    ):
        self.min_duration = min_duration
        self.max_duration = max_duration
        self.step = step

    def build(self, transcript: TranscriptResult) -> list[ClipCandidate]:
        candidates = []

        segments = transcript.segments

        if not segments:
            return candidates

        total_duration = segments[-1].end

        start_time = segments[0].start

        while start_time < total_duration:

            for target_duration in [20.0, 30.0, 45.0, 60.0]:

                if target_duration < self.min_duration:
                    continue

                if target_duration > self.max_duration:
                    continue

                target_end = start_time + target_duration

                matching_segments = [
                    segment
                    for segment in segments
                    if segment.start >= start_time
                    and segment.end <= target_end
                ]

                if not matching_segments:
                    continue

                end_time = matching_segments[-1].end

                duration = end_time - start_time

                if duration < self.min_duration:
                    continue

                if duration > self.max_duration:
                    continue

                text = " ".join(
                    segment.text.strip()
                    for segment in matching_segments
                )

                candidates.append(
                    ClipCandidate(
                        start=start_time,
                        end=end_time,
                        text=text,
                        score=0.0,
                    )
                )

            start_time += self.step

        return candidates
