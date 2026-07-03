from flowforge.workflow.loader import WorkflowLoader

loader = WorkflowLoader()

workflow = loader.load("examples/workflows/loop.json")

print(workflow.name)
print(workflow.start_node)
print(workflow.edges)