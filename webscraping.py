# function that sources the following financial information for any UK share:
# market open price, day trade high price, year high price, market cap.
# previous day close price, day trade low price, year low price, P/E ratio
# volume of shares traded (daily), dividend yield, exchange market size

import requests
from bs4 import BeautifulSoup,NavigableString
import re
#print(result.status_code)    # checks if webpage accessible. prints http status code. 400 code = not accessible. 200 code = accessible. Ours is 200.
#print(result.headers)  # info re what's on homepage to use for basicfinancials function

def ataglance_financials(webaddress, sharename):
    result = requests.get(webaddress)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    links = soup.find_all("strong")
    figures = []
    for i in links:
        figures.append(i)
    figures = str(figures)
    matches = re.findall(r'[-]?\d[\d,]*[\.]?[\d{2}]*', figures)
    mydict = {"Open":matches[3], "Trade high":matches[4],"Year high":matches[5], "Market cap.":matches[6], "Previous Close":matches[7], "Trade low":matches[8], "Year low":matches[9], "P/E ratio":matches[10], "Volume":matches[11], "Dividend yield":matches[12], "EMS":matches[13]}
    print(sharename)
    print(mydict)

ataglance_financials("https://www.hl.co.uk/shares/shares-search-results/h/hochschild-mining-plc-ordinary-25p", "Hochschild")
