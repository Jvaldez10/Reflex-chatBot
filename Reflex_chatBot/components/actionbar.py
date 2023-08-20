import reflex as rx
from Reflex_chatBot import styles


def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(placeholder="Hacer una pregunta", style=styles.input_style),
        rx.button("Preguntar", style=styles.button_style),
    )
