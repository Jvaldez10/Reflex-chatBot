from .components.navbar import navbar
from .components.chat import chat
from .components.actionbar import action_bar
import reflex as rx


def index() -> rx.Component:
    return rx.container(
        navbar(),
        chat(),
        action_bar(),
        # rx.divider(),
        # rx.box(
        #     "Que es Reflex?",
        #     text_align="right",
        # ),
        # rx.box(
        #     "Sirver para construir web apps con Python puro",
        #     text_align="left",
        # ),
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()
