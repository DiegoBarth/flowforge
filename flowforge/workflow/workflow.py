from dataclasses import dataclass


@dataclass
class Workflow:
    name: str
    nodes: dict
    start_node: str