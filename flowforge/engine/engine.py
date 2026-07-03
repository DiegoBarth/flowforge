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

            edge = workflow.edges.get(current_node_id)

            if edge is None:
                break

            if isinstance(edge, str):
                current_node_id = edge

            elif isinstance(edge, dict) and edge.get("type") != "switch":
                condition_key = edge.get("condition")
                condition_value = context.get(condition_key)

                current_node_id = edge["true"] if condition_value else edge["false"]

            elif isinstance(edge, dict) and edge.get("type") == "switch":

                condition_key = edge.get("condition")
                value = context.get(condition_key)

                cases = edge.get("cases", {})
                default = edge.get("default")

                current_node_id = cases.get(value, default)

            else:
                raise Exception(f"Invalid edge format: {edge}")

            steps += 1

        trace.print()

        print("[ENGINE] Workflow finished")

        return context