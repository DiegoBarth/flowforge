from flowforge.engine import Engine
from flowforge.workflow import Workflow
from flowforge.context import Context
from flowforge.nodes import LogNode
from flowforge.nodes.if_node import IfNode


workflow = Workflow(
    name="IF Workflow",
    nodes={
        "start": LogNode("start", "Start"),
        "check": IfNode("check", "user_type", "admin"),
        "admin": LogNode("admin", "Admin path"),
        "user": LogNode("user", "User path"),
    },
    edges=[
        ("start", "check", None),
        ("check", "admin", "check_result"),
        ("check", "user", None),
    ],
    start_node="start"
)

engine = Engine()

context = Context()
context.set("user_type", "admin")

engine.run(workflow, context)