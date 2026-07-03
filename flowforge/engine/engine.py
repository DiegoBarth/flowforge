from flowforge.workflow import Workflow
from flowforge.context import Context


class Engine:
    def run(self, workflow: Workflow, context: Context):
        print(f"[ENGINE] Running workflow: {workflow.name}")

        current_node_id = workflow.start_node

        while current_node_id:
            node = workflow.nodes[current_node_id]

            print(f"[ENGINE] Executing node: {current_node_id}")

            context = node.execute(context)

            next_node = None

            for frm, to, condition in workflow.edges:
                if frm != current_node_id:
                    continue

                if condition is None:
                    next_node = to
                    break

                condition_result = context.get(condition)

                if condition_result is True:
                    next_node = to
                    break

            current_node_id = next_node

        print("[ENGINE] Workflow finished")

        return context