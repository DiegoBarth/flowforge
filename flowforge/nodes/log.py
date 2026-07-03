from flowforge.nodes.base import Node


class LogNode(Node):

    def __init__(self, node_id: str, message: str):
        super().__init__(node_id)
        self.message = message

    def execute(self, context) -> None:
        print(f"[LOG] {self.message}")