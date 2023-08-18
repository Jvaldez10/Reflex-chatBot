import reflex as rx


def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(question, text_align="right"),
        rx.box(answer, text_aling="left"),
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
