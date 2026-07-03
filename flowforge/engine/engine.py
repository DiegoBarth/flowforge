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

            node.execute(context)

            trace.add_step(current_node_id, context.data)

            # 🔥 EDGE RESOLUTION (NOW SUPPORTS CONDITIONAL EDGES)
            edge = workflow.edges.get(current_node_id)

            if edge is None:
                break

            # 🔥 se edge for string → fluxo normal
            if isinstance(edge, str):
                current_node_id = edge

            # 🔥 se edge for dict → decisão baseada em context
            elif isinstance(edge, dict):
                condition_key = edge.get("condition")
                true_path = edge.get("true")
                false_path = edge.get("false")

                condition_value = context.get(condition_key)

                current_node_id = true_path if condition_value else false_path

            else:
                raise Exception(f"Invalid edge format: {edge}")

            steps += 1

        trace.print()

        print("[ENGINE] Workflow finished")

        return context