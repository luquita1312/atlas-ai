from backend.app.agents.transcript_agent import TranscriptAgent
from backend.app.agents.viral_agent import ViralAgent


audio_path = "datasets/raw/test.mp3.mp3"


# 1. Transcribir audio
transcript_agent = TranscriptAgent()

transcript = transcript_agent.run(audio_path)


print("\n=== TRANSCRIPCIÓN ===")

for segment in transcript.segments:
    print(
        f"{segment.start:.2f}s - "
        f"{segment.end:.2f}s | "
        f"{segment.text}"
    )


# 2. Buscar clips candidatos
viral_agent = ViralAgent()

candidates = viral_agent.run(transcript)


print("\n=== CLIPS CANDIDATOS ===")

for candidate in candidates:
    print(
        f"Score: {candidate.score:.2f} | "
        f"{candidate.start:.2f}s - "
        f"{candidate.end:.2f}s | "
        f"{candidate.text}"
    )
    