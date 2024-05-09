# SEC-edgar-extractor

For the project, the key aspects of the tech stack used were Python, gpt2-xl, Shiny, BeautifulSoup, and MatplotLib

Python is used as the coding language since it's quick to write code with and has good documentation for the SEC-Edgar API. I'm also familiar with it from other projects so it made sense to us it

Shiny is used since it's quite quick and nice to code up a demo and visualization. I also have experience with Shiny and the dashboards end up looking quite nice.

BeautifulSoup was used since it's the defacto package used for extracting useful information from HTML and XML files. 

Matplotlib was used to draw the final wordcloud based off the LLM output.

gpt2-xl was used since it was suggested in the huggingface docs as the best for text generation. There were a lot of issues with it since the generation itself is not great and if I had more time I'd use a better model or have some other task for the LLM portion but in the given time I couldn't find a better alternative.

The insight is a visualization of the key words that the LLM generates based on the SEC filings on how susceptible the company is to interest rate changes.
I thought this would be an interesting subject for the LLM to investigate as it shows how the company's core revenue depends on aspects that can be affected by volatility in interest rates.
Particularly, looking at it over the long period of time may give insights as to how the company has responded to interest rate changes in the past which could be helpful for future forecases.

# How to Run

Download the files and run 

pip install -r requirements.txt

Then, run the shinyApp.py file and navigate to the corresponding port

You should have a textbox, fill it with the ticker you want

# Challenges / Future Improvements
