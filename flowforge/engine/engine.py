from flowforge.workflow import Workflow
from flowforge.context import Context


class Engine:
    def run(self, workflow: Workflow, context: Context):
        print(f"[ENGINE] Running workflow: {workflow.name}")

        for node in workflow.nodes:
            print(f"[ENGINE] Executing node: {node.node_id}")
            context = node.execute(context)

        print("[ENGINE] Workflow finished")
        return context