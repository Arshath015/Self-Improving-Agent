import random
from agent.tools import search_tool, final_answer

class TaskAgent:
    def __init__(self, memory):
        self.memory = memory

    def run(self, question):
        actions = []
        constraints = self.memory.get_constraints()

        tool_output = search_tool(question)
        actions.append(("search_tool", tool_output))

        if tool_output == "Unknown":
            if "avoid_unknown_answers" in constraints:
                answer = final_answer("I am not confident about this. I should verify.")
                actions.append(("final_answer", answer))
                return actions

            answer = final_answer("Unknown")
            actions.append(("final_answer", answer))
            return actions

        answer = final_answer(tool_output)
        actions.append(("final_answer", answer))
        return actions




