from typing import Type

from flowforge.nodes.base import Node


class NodeRegistry:
    def __init__(self):
        self._nodes: dict[str, Type[Node]] = {}

    def register(self, node_type: str, node_class: Type[Node]):
        if node_type in self._nodes:
            raise ValueError(f"Node '{node_type}' is already registered.")

        self._nodes[node_type] = node_class

    def get(self, node_type: str) -> Type[Node]:
        if node_type not in self._nodes:
            raise ValueError(f"Unknown node type: '{node_type}'")

        return self._nodes[node_type]

    def exists(self, node_type: str) -> bool:
        return node_type in self._nodes

    def list(self) -> list[str]:
        return sorted(self._nodes.keys())