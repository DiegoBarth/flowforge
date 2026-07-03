from typing import Type

from flowforge.nodes.base import Node


class NodeRegistry:

    def __init__(self):
        self._nodes = {}

    def register(self, node_type: str, node_class):
        self._nodes[node_type] = node_class

    def create(self, node_type: str, node_id: str, config: dict) -> Node:

        if node_type not in self._nodes:
            raise ValueError(f"Unknown node type: {node_type}")

        node_class = self._nodes[node_type]

        return node_class(node_id=node_id, **config)

    def available_nodes(self):
        return list(self._nodes.keys())