from flowforge.nodes.registry import NodeRegistry
from flowforge.nodes.log import LogNode
from flowforge.nodes.loop_node import LoopNode

registry = NodeRegistry()

registry.register("log", LogNode)
registry.register("loop", LoopNode)

print(registry.available_nodes())

log_node = registry.create(
    node_type="log",
    node_id="start",
    config={
        "message": "Hello FlowForge"
    }
)

loop_node = registry.create(
    node_type="loop",
    node_id="loop",
    config={
        "condition_key": "do_loop",
        "max_loops": 3
    }
)

print(type(log_node))
print(type(loop_node))

print(log_node.message)
print(loop_node.max_loops)