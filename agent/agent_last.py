import random
from agent.tools import search_tool, final_answer

class TaskAgent:
    def __init__(self, memory):
        self.memory = memory

    def run(self, question):
        actions = []
        behavior_constraints = self.memory.get_constraints()

        if "force_tool_first" in behavior_constraints:
            tool_output = search_tool(question)
            actions.append(("search_tool", tool_output))
            answer = final_answer(tool_output)
            actions.append(("final_answer", answer))
            return actions

        if random.choice([True, False]):
            answer = final_answer("I think the answer is Paris")
            actions.append(("final_answer", answer))
        else:
            tool_output = search_tool(question)
            actions.append(("search_tool", tool_output))
            answer = final_answer(tool_output)
            actions.append(("final_answer", answer))

        return actions
