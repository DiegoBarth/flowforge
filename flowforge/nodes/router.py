from flowforge.nodes.base import Node


class RouterNode(Node):

    def execute(self, context) -> None:
        print("[ROUTER] deciding flow based on status")