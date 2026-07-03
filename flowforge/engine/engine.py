from flowforge.workflow import Workflow
from flowforge.context import Context


class Engine:
    def run(self, workflow, context):
        print(f"[ENGINE] Running workflow: {workflow.name}")

        current_node_id = workflow.start_node
        steps = 0
        max_steps = 1000

        while current_node_id:

            if steps > max_steps:
                raise Exception("Max steps reached")

            node = workflow.nodes[current_node_id]

            print(f"[ENGINE] Executing node: {current_node_id}")

            context = node.execute(context)

            next_node = context.get("next")

            context.set("next", None)

            if current_node_id == "end":
                break

            if not next_node:
                break

            current_node_id = next_node
            steps += 1

        print("[ENGINE] Workflow finished")
        return context