from dataclasses import dataclass
from flowforge.nodes import Node


@dataclass
class Workflow:
    name: str
    nodes: dict[str, Node]
    edges: list[tuple[str, str]]
    start_node: str