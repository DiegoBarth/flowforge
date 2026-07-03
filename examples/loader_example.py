from flowforge.workflow.loader import WorkflowLoader
from flowforge.nodes.registry import NodeRegistry

from flowforge.nodes.log import LogNode
from flowforge.nodes.loop_node import LoopNode


registry = NodeRegistry()

registry.register("log", LogNode)
registry.register("loop", LoopNode)

loader = WorkflowLoader(registry)

try:
    loader.load("examples/workflows/loop.json")
except NotImplementedError:
    print("Workflow loader not implemented yet.")