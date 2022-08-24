import requests
from bs4 import BeautifulSoup
def trade_crawler(maximum_page):
    page=1
    while page<=maximum_page:
        url='https://buckysroom.org/trade/search.php?page='+str(page)
        source_code=requests.get(url)
        text=source_code.text
        soup=BeautifulSoup(text)
        for link in soup.findall('a',{'class':'item-name'}):
            href=link.get('href')
            print(href)
        page=page+1
trade_crawler(1)
        
