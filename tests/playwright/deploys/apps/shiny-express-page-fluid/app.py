from shiny import render
from shiny.express import input, ui

ui.page_opts(full_width=True)

with ui.card(id="card"):
    ui.input_slider("a", "A", 1, 100, 50)

    @render.text
    def txt():
        return input.a()
