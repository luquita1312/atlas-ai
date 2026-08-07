from .base_agent import BaseAgent


class TestAgent(BaseAgent):

    def run(self, input_data):
        return {
            "agent": self.name,
            "input": input_data,
            "status": "completed"
        }
    