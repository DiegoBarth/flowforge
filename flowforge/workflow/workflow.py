from dataclasses import dataclass, field


@dataclass
class Workflow:
    name: str
    nodes: dict
    start_node: str
    edges: dict = field(default_factory=dict)