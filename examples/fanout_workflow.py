from flowforge.engine import Engine
from flowforge.workflow import Workflow
from flowforge.context import Context
from flowforge.nodes import LogNode


workflow = Workflow(
    name="Fanout Workflow",
    nodes={
        "start": LogNode("start", "Start"),
        "a": LogNode("a", "Path A"),
        "b": LogNode("b", "Path B"),
        "c": LogNode("c", "Path C"),
        "end": LogNode("end", "End"),
    },
    edges=[
        ("start", "a", None),
        ("start", "b", None),
        ("start", "c", None),

        ("a", "end", None),
        ("b", "end", None),
        ("c", "end", None),
    ],
    start_node="start"
)

engine = Engine()
context = Context()

engine.run(workflow, context)