from abc import ABC, abstractmethod


class BaseAgent(ABC):
    """
    Clase base para todos los agentes de Atlas.
    """

    def __init__(self, name: str):
        self.name = name


    @abstractmethod
    def run(self, input_data):
        """
        Cada agente debe implementar su propia lógica.
        """
        pass
    