from sentence_transformers import SentenceTransformer
import numpy as np


class SemanticSimilarity:

    def __init__(
        self,
        model_name: str = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
    ):
        self.model = SentenceTransformer(model_name)

    def encode(self, texts: list[str]) -> np.ndarray:
        return self.model.encode(
            texts,
            normalize_embeddings=True,
        )

    def similarity(self, text_a: str, text_b: str) -> float:
        embeddings = self.encode([text_a, text_b])

        return float(
            np.dot(
                embeddings[0],
                embeddings[1],
            )
        )
