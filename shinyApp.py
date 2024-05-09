from shiny import App, render, ui
import os
import main
import testLLM
import visualizer

# Define the user interface of the app
app_ui = ui.page_fluid(
    ui.input_text("ticker", "Enter company ticker:"),
    ui.output_image("output")
)


# Define the server logic of the app
def server(input, output, session):
    @output
    @render.image
    def output():
        # Use other files methods based on ticker input
        ticker = input.ticker().strip().upper()
        main.downloader(ticker)
        tempPath = "sec-edgar-filings/" + ticker + "/10-K"
        fileNo = os.listdir(tempPath)[0]
        finalPath = "sec-edgar-filings/" + ticker + "/10-K/" + fileNo + "/full-submission.txt"
        visualizer.wordCloud(testLLM.llmInput(finalPath)[0]["generated_text"])
        return {"src": "figure.png"}


# Create and run the Shiny app
app = App(app_ui, server)
app.run()
