from flowforge.engine import Engine
from flowforge.workflow import Workflow
from flowforge.context import Context
from flowforge.nodes import LogNode


workflow = Workflow(
    name="My First Workflow",
    nodes=[
        LogNode("1", "Hello FlowForge"),
        LogNode("2", "Processing..."),
        LogNode("3", "Done")
    ]
)

engine = Engine()
context = Context()

engine.run(workflow, context)