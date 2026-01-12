import json
import os

class Memory:
    def __init__(self, path="logs/history.json"):
        self.path = path
        self._ensure_file()

    def _ensure_file(self):
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        if not os.path.exists(self.path):
            self._write({"mistakes": {}})
            return
        if os.path.getsize(self.path) == 0:
            self._write({"mistakes": {}})

    def record_mistake(self, mistake):
        data = self.load()
        data["mistakes"][mistake] = data["mistakes"].get(mistake, 0) + 1
        self._write(data)

    def get_constraints(self):
        data = self.load()
        constraints = []

        if data["mistakes"].get("tool_not_used", 0) >= 2:
            constraints.append("force_tool_first")

        if data["mistakes"].get("trusted_unknown_tool_output", 0) >= 1:
            constraints.append("avoid_unknown_answers")

        return constraints

    def load(self):
        with open(self.path, "r") as f:
            return json.load(f)

    def _write(self, data):
        with open(self.path, "w") as f:
            json.dump(data, f, indent=2)
