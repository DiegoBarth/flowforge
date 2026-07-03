from dataclasses import dataclass
from typing import Callable
from flowforge.nodes import Node
from flowforge.context import Context


Condition = Callable[[Context], bool]


@dataclass
class Workflow:
    def __init__(self, name: str, nodes: dict, start_node: str):
        self.name = name
        self.nodes = nodes
        self.start_node = start_node