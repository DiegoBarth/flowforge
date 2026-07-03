from flowforge.engine import Engine
from flowforge.workflow import Workflow
from flowforge.context import Context
from flowforge.nodes import LogNode


workflow = Workflow(
    name="Rule Workflow",
    nodes={
        "start": LogNode("start", "Start"),
        "check": LogNode("check", "Checking user"),
        "admin": LogNode("admin", "Admin path"),
        "user": LogNode("user", "User path"),
    },
    edges=[
        ("start", "check", None),

        ("check", "admin", lambda ctx: ctx.get("user_type") == "admin"),
        ("check", "user", lambda ctx: ctx.get("user_type") != "admin"),
    ],
    start_node="start"
)

engine = Engine()

context = Context()
context.set("user_type", "admin")

engine.run(workflow, context)