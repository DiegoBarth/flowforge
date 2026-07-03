from flowforge.workflow.loader import WorkflowLoader

loader = WorkflowLoader()

try:
    loader.load("examples/workflows/loop.json")
except NotImplementedError:
    print("Workflow loader not implemented yet.")