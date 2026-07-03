class ExecutionStep:
    def __init__(self, node_id: str, context_snapshot: dict):
        self.node_id = node_id
        self.context_snapshot = context_snapshot


class ExecutionTrace:
    def __init__(self):
        self.steps = []

    def add_step(self, node_id: str, context: dict):
        # copia leve do contexto
        self.steps.append(
            ExecutionStep(node_id, dict(context))
        )

    def print(self):
        print("\n[TRACE]")
        for step in self.steps:
            print(f"- {step.node_id} -> {step.context_snapshot}")