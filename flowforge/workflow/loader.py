from flowforge.nodes.registry import NodeRegistry
from flowforge.workflow import Workflow

class WorkflowLoader:
    def __init__(self, registry: NodeRegistry):
        self.registry = registry

    def load(self, path: str):
        import json

        with open(path, "r") as f:
            data = json.load(f)

        nodes = {}

        for node in data["nodes"]:
            node_id = node["id"]
            node_type = node["type"]
            params = node.get("params", {})

            nodes[node_id] = self.registry.create(
                node_type=node_type,
                node_id=node_id,
                **params
            )

        return Workflow(
            name=data["name"],
            nodes=nodes,
            start_node=data["start_node"],
            edges=data["edges"]
        )