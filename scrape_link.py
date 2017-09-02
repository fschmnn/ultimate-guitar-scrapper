#==============================================================================
# scrape the content from https://www.ultimate-guitar.com/
#==============================================================================

# modules used to get and parse the content
import requests
from bs4 import BeautifulSoup

def scrape(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    # the main part of the song can be found under
    txt = soup.find_all('textarea')[1].get_text()

    info = soup.find('title').get_text().title()
    title = info[:info.find("By")-1]
    interpret = info[info.find("By")+3:info.find("@")-1]

    return (txt,title,interpret)
