from shiny import render, ui
from shiny.express import hide, input

with ui.card(id="card"):
    ui.input_slider("s1", "A", 1, 100, 20)

    @hide
    @render.text
    def hidden():
        return input.s1()

    ui.input_slider("s2", "B", 1, 100, 40)

    # from shiny.express import ui_kwargs
    # @ui_kwargs(placeholder=False)
    # @ui_kwargs(placeholder=True)
    @render.text()
    def visible():
        # from shiny import req

        # req(False)
        return input.s2()
