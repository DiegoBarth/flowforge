from flowforge.engine.execution_trace import ExecutionTrace


class Engine:

    def run(self, workflow, context):

        print(f"[ENGINE] Running workflow: {workflow.name}")

        trace = ExecutionTrace()

        current_node_id = workflow.start_node
        steps = 0
        max_steps = 1000

        while current_node_id:

            if steps > max_steps:
                raise Exception("Max steps reached")

            if current_node_id not in workflow.nodes:
                raise Exception(f"Node not found: {current_node_id}")

            node = workflow.nodes[current_node_id]

            print(f"[ENGINE] Executing node: {current_node_id}")

            node.execute(context)

            if current_node_id == "loop" and not context.get("loop_active"):
                current_node_id = None
            else:
                current_node_id = workflow.edges.get(current_node_id)

            steps += 1

        trace.print()

        print("[ENGINE] Workflow finished")

        return context