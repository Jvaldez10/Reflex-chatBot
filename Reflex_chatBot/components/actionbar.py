import reflex as rx
from Reflex_chatBot import styles
from Reflex_chatBot.state import State


def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            placeholder="Hacer una pregunta",
            on_blur=State.set_question,
            style=styles.input_style,
        ),
        rx.button(
            "Preguntar",
            on_click=State.answer,
            style=styles.button_style,
        ),
    )
