from dataclasses import dataclass
from typing import Callable
from flowforge.nodes import Node
from flowforge.context import Context


Condition = Callable[[Context], bool]


@dataclass
class Workflow:
    name: str
    nodes: dict[str, Node]
    edges: list[tuple[str, str, Condition | None]]
    start_node: str