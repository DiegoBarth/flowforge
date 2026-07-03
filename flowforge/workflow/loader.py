import json

from flowforge.workflow import Workflow


class WorkflowLoader:

    def load(self, path: str) -> Workflow:

        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)

        return Workflow(
            name=data["name"],
            nodes={},
            start_node=data["start_node"],
            edges=data["edges"],
        )