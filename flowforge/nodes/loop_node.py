from flowforge.nodes.base import Node
from flowforge.context import Context


class LoopNode(Node):
    def __init__(self, node_id: str, condition_key: str, max_loops: int = 3):
        super().__init__(node_id)
        self.condition_key = condition_key
        self.max_loops = max_loops

    def execute(self, context: Context) -> Context:
        count = context.get(f"{self.node_id}_count", 0)

        print(f"[LOOP] count={count} continue={count < self.max_loops}")

        count += 1
        context.set(f"{self.node_id}_count", count)

        if count < self.max_loops:
            context.set("next", "work")
        else:
            context.set("next", "end")

        return context