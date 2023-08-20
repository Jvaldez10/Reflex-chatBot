import reflex as rx
from Reflex_chatBot import styles


def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(
                question,
                style=styles.question_style,
            ),
            text_align="right",
        ),
        rx.box(
            rx.text(
                answer,
                style=styles.answer_style,
            ),
            text_aling="left",
        ),
        margin_y="1em",
    )


def chat() -> rx.Component:
    qa_pairs = [
        ("Que es Reflex?", "¡Una forma de crear aplicaciones web en Python puro!"),
        (
            "Que puedo hacer con el?",
            "¡Cualquier cosa, desde un sitio web simple hasta una aplicación web compleja!",
        ),
    ]
    return rx.box(*[qa(question, answer) for question, answer in qa_pairs])
