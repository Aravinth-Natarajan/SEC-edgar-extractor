from sec_edgar_downloader import Downloader
import time

# Used to download the edgar filings to local machine
dl = Downloader("Rand", "someEmail@gmail.com")


def downloader(ticker):
    randString = ''
    while randString == '':
        try:
            dl.get("10-K", ticker, after="1995-01-01", before="2023-12-31")
            randString = "Not"
            break
        except:
            print("Connection refused by the server..")
            print("ZZzzzz...")
            time.sleep(100)
            continue
