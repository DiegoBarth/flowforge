from flowforge.nodes.registry import NodeRegistry
from flowforge.workflow.loader import WorkflowLoader
from flowforge.engine.engine import Engine
from flowforge.context import Context

from flowforge.nodes.log import LogNode
from flowforge.nodes.loop_node import LoopNode

registry = NodeRegistry()
registry.register("log", LogNode)
registry.register("loop", LoopNode)

loader = WorkflowLoader(registry)

workflow = loader.load("examples/workflows/loop.json")

engine = Engine()
context = Context()

context.set("do_loop", True)

engine.run(workflow, context)