import reflex as rx


def navbar():
    return rx.breadcrumb(
        rx.color_mode_button(
            rx.color_mode_icon(),
            float="left",
        ),
        rx.spacer(),
        rx.breadcrumb_item(rx.breadcrumb_link("Home", href="#")),
        rx.breadcrumb_item(rx.breadcrumb_link("blog", href="#")),
        rx.breadcrumb_item(rx.breadcrumb_link("jvaldez", href="#")),
        separator="/",
        color="rgb(107,99,246)",
    )
