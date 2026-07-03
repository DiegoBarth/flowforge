import json

from flowforge.workflow import Workflow
from flowforge.nodes.registry import NodeRegistry


class WorkflowLoader:

    def __init__(self, registry: NodeRegistry):
        self.registry = registry

    def load(self, path: str) -> Workflow:
        raise NotImplementedError()