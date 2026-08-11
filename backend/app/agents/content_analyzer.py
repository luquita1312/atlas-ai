from ..models.schemas import ContentAnalysis


class ContentAnalyzer:

    def analyze(self, text: str) -> ContentAnalysis:
        text_lower = text.lower()

        hook_strength = 0.0
        curiosity = 0.0
        clarity = 0.0
        information_value = 0.0
        emotional_intensity = 0.0

        # Hook
        hook_words = [
            "cómo",
            "por qué",
            "sabías",
            "nunca",
            "error",
            "secreto",
            "sorprendente",
        ]

        if any(word in text_lower for word in hook_words):
            hook_strength = 0.8

        # Curiosidad
        curiosity_phrases = [
            "pero",
            "sin embargo",
            "la razón",
            "el problema",
            "lo que",
            "resulta que",
        ]

        if any(phrase in text_lower for phrase in curiosity_phrases):
            curiosity = 0.8

        # Claridad
        word_count = len(text.split())

        if 20 <= word_count <= 100:
            clarity = 0.8
        elif word_count > 100:
            clarity = 0.5

        # Valor informativo
        value_words = [
            "porque",
            "significa",
            "explica",
            "permite",
            "funciona",
            "importante",
        ]

        if any(word in text_lower for word in value_words):
            information_value = 0.8

        # Intensidad emocional
        emotional_words = [
            "error",
            "problema",
            "sorprendente",
            "nunca",
            "increíble",
            "peligroso",
        ]

        if any(word in text_lower for word in emotional_words):
            emotional_intensity = 0.7

        return ContentAnalysis(
            hook_strength=hook_strength,
            curiosity=curiosity,
            clarity=clarity,
            information_value=information_value,
            emotional_intensity=emotional_intensity,
        )
    