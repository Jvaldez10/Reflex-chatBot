import reflex as rx


def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(placeholder="Hacer una pregunta"),
        rx.button("Preguntar"),
    )
