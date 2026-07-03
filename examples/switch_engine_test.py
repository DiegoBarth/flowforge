from flowforge.nodes.registry import NodeRegistry
from flowforge.workflow.loader import WorkflowLoader
from flowforge.engine.engine import Engine
from flowforge.context import Context

from flowforge.nodes.log import LogNode


registry = NodeRegistry()
registry.register("log", LogNode)

loader = WorkflowLoader(registry)

workflow = loader.load("examples/workflows/switch.json")

engine = Engine()
context = Context()

context.set("status", "unknown")

engine.run(workflow, context)