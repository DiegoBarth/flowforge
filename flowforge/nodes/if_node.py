from flowforge.nodes.base import Node
from flowforge.context import Context


class IfNode(Node):
    def __init__(self, node_id: str, condition_key: str, expected_value):
        super().__init__(node_id)
        self.condition_key = condition_key
        self.expected_value = expected_value

    def execute(self, context: Context) -> Context:
        value = context.get(self.condition_key)

        result = value == self.expected_value

        context.set(f"{self.node_id}_result", result)

        print(f"[IF] {self.condition_key} == {self.expected_value} → {result}")

        return context