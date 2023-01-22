
import requests
from bs4 import BeautifulSoup
def rech(link):
    page = requests.get(link)
    print(page.status_code)
    wiki_page = BeautifulSoup(page.content, 'html.parser')
    print (wiki_page.title.text )
    X=wiki_page.find_all("h2",{"class=mp-h2"})
    for i in X:
        print (i.text )
    Y=wiki_page.find_all("a")
    for i in Y:
        print (i["href"] )
rech("https://en.wikipedia.org/wiki/Main_Page")
rech("https://en.wikipedia.org/wiki/WW2")