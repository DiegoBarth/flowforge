from flowforge.workflow import Workflow


class WorkflowLoader:
    def load(self, path: str) -> Workflow:
        raise NotImplementedError()