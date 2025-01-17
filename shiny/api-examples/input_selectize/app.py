from shiny import App, Inputs, Outputs, Session, render, ui

app_ui = ui.page_fluid(
    ui.input_selectize(
        "state",
        "Choose a state:",
        {
            "East Coast": {"NY": "New York", "NJ": "New Jersey", "CT": "Connecticut"},
            "West Coast": {"WA": "Washington", "OR": "Oregon", "CA": "California"},
            "Midwest": {"MN": "Minnesota", "WI": "Wisconsin", "IA": "Iowa"},
        },
        multiple=True,
    ),
    ui.output_text("value"),
)


def server(input: Inputs, output: Outputs, session: Session):
    @render.text
    def value():
        return "You choose: " + str(input.state())


app = App(app_ui, server)
