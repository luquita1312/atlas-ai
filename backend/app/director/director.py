from ..agents.test_agent import TestAgent


class Director:

    def execute(self, task):
        agent = TestAgent("TestAgent")

        result = agent.run(task)

        return result

