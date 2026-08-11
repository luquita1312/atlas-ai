from abc import ABC, abstractmethod

from ..models.schemas import ContentAnalysis


class ContentAnalyzerBase(ABC):

    @abstractmethod
    def analyze(self, text: str) -> ContentAnalysis:
        pass
