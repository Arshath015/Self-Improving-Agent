import os
import sys
# Ensure the project root is on sys.path so sibling packages can be imported when
# running this script directly (e.g., `python run/run_agent.py`).
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from agent.agent import TaskAgent
from agent.evaluator import evaluate_run
from agent.memory import Memory

memory = Memory()
agent = TaskAgent(memory)

question = "Tesla founder?"

actions = agent.run(question)
success, reason = evaluate_run(question, actions)

print(actions)
print(success, reason)

if not success:
    memory.record_mistake(reason)
