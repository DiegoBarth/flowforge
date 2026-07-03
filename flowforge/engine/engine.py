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

            # pega próximo node via edge
            next_nodes = [
                to for (frm, to) in workflow.edges if frm == current_node_id
            ]

            if not next_nodes:
                break

            current_node_id = next_nodes[0]

        print("[ENGINE] Workflow finished")
        return context