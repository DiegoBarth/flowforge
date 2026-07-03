from flowforge.nodes.registry import NodeRegistry
from flowforge.nodes.log import LogNode
from flowforge.nodes.loop_node import LoopNode

registry = NodeRegistry()

registry.register("log", LogNode)
registry.register("loop", LoopNode)

print(registry.list())

print(registry.get("log"))
print(registry.get("loop"))