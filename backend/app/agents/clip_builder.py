from ..models.schemas import TranscriptResult, ClipCandidate


class ClipBuilder:

    def __init__(
        self,
        min_duration: float = 15.0,
        max_duration: float = 60.0,
        target_durations: tuple[float, ...] = (20.0, 30.0, 45.0, 60.0),
    ):
        self.min_duration = min_duration
        self.max_duration = max_duration
        self.target_durations = target_durations

    def build(self, transcript: TranscriptResult) -> list[ClipCandidate]:
        candidates = []

        segments = transcript.segments

        if not segments:
            return candidates

        for start_index, start_segment in enumerate(segments):

            start_time = start_segment.start

            for target_duration in self.target_durations:

                if target_duration < self.min_duration:
                    continue

                if target_duration > self.max_duration:
                    continue

                target_end = start_time + target_duration

                matching_segments = []

                for segment in segments[start_index:]:

                    if segment.end > target_end:
                        break

                    matching_segments.append(segment)

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
                    if segment.text.strip()
                )

                if not text:
                    continue

                candidates.append(
                    ClipCandidate(
                        start=start_time,
                        end=end_time,
                        text=text,
                        score=0.0,
                    )
                )

        return candidates
