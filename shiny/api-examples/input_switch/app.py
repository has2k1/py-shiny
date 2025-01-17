from shiny import App, Inputs, Outputs, Session, render, ui

app_ui = ui.page_fluid(
    ui.input_switch("somevalue", "Some value", False),
    ui.output_ui("value"),
)


def server(input: Inputs, output: Outputs, session: Session):
    @render.ui
    def value():
        return input.somevalue()


app = App(app_ui, server)
