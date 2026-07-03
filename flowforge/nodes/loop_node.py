from flowforge.nodes.base import Node
from flowforge.context import Context


class LoopNode(Node):

    def __init__(self, node_id: str, condition_key: str, max_loops: int = 3):
        super().__init__(node_id)
        self.condition_key = condition_key
        self.max_loops = max_loops

    def execute(self, context: Context) -> None:

        count = context.get("loop_count", 0)
        should_continue = context.get(self.condition_key)

        print(f"[LOOP] count={count} continue={should_continue}")

        count += 1
        context.set("loop_count", count)

        context.set("loop_active", should_continue and count < self.max_loops)