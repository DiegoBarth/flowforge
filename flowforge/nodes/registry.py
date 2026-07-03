from typing import Type

from flowforge.nodes.base import Node


class NodeRegistry:
    def __init__(self):
        self._registry = {}

    def register(self, node_type: str, node_class):
        self._registry[node_type] = node_class

    def get(self, node_type: str):
        return self._registry[node_type]

    def list(self):
        return list(self._registry.keys())

    def create(self, node_type: str, node_id: str, **kwargs):
        node_class = self.get(node_type)
        return node_class(node_id=node_id, **kwargs)