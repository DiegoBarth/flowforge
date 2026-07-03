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

            node = workflow.nodes[current_node_id]

            print(f"[ENGINE] Executing node: {current_node_id}")

            next_node = node.execute(context)

            trace.add_step(current_node_id, context.data)

            if current_node_id == "end":
                break

            current_node_id = next_node
            steps += 1

        trace.print()

        print("[ENGINE] Workflow finished")

        return context