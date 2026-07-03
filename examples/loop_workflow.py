from flowforge.engine.engine import Engine
from flowforge.workflow import Workflow
from flowforge.context import Context
from flowforge.nodes.log import LogNode
from flowforge.nodes.loop_node import LoopNode


workflow = Workflow(
    name="Loop Workflow",
    nodes={
        "start": LogNode("start", "Start"),
        "loop": LoopNode("loop", "do_loop", max_loops=3),
        "work": LogNode("work", "Doing work inside loop"),
        "end": LogNode("end", "End"),
    },
    start_node="start"
)

engine = Engine()
context = Context()

context.set("do_loop", True)

engine.run(workflow, context)