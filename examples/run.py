from flowforge.engine import Engine
from flowforge.workflow import Workflow
from flowforge.context import Context
from flowforge.nodes import LogNode


workflow = Workflow(
    name="Graph Workflow",
    nodes={
        "1": LogNode("1", "Start"),
        "2": LogNode("2", "Middle"),
        "3": LogNode("3", "End"),
    },
    edges=[
        ("1", "2"),
        ("2", "3"),
    ],
    start_node="1"
)

engine = Engine()
context = Context()

engine.run(workflow, context)