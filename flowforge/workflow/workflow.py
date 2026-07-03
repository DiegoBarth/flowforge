from dataclasses import dataclass
from flowforge.nodes import Node


@dataclass
class Workflow:
    name: str
    nodes: list[Node]