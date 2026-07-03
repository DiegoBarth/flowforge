from flowforge.workflow import Workflow
from flowforge.context import Context


class Engine:
    def run(self, workflow: Workflow, context: Context):
        print(f"[ENGINE] Running workflow: {workflow.name}")

        current_nodes = [workflow.start_node]
        visited = set()

        while current_nodes:
            next_nodes = []

            for current_node_id in current_nodes:

                # 🔥 proteção contra execução duplicada
                if current_node_id in visited:
                    continue

                visited.add(current_node_id)

                node = workflow.nodes[current_node_id]

                print(f"[ENGINE] Executing node: {current_node_id}")

                context = node.execute(context)

                for frm, to, condition in workflow.edges:
                    if frm != current_node_id:
                        continue

                    if condition is None or condition(context):
                        next_nodes.append(to)

            current_nodes = next_nodes

        print("[ENGINE] Workflow finished")
        return context