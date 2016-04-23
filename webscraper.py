from bs4 import BeautifulSoup, NavigableString, Tag
import urllib2
from unidecode import unidecode
import requests
import re
import wget
import os

BASE_URL = "http://www.goodreads.com/book/show/"

def get_author(soup):
    author = soup.select('.authorName span')
    if author:
        return author[0].contents[0]
    else:
        print "No author found"
        return None

def get_title(soup):
    title = soup.select('.bookTitle')
    if title:
        return title[0].contents[0].strip()
    else:
        print "No title found"
        return None    

def get_series(soup):
    series = soup.select('#bookTitle a')
    if series:
        seriesName = series[0].contents[0].strip()
        return seriesName[1:-1]
    else:
        return None

def get_description(soup):
    description = soup.select('#description span')
    
    d = ""
    if description:
        for l in description[1].contents:
            if isinstance(l, NavigableString):
                d = d + unidecode(l) + " "
        return d
    else:
        return None

def get_year(soup):
    year = soup.select('#details')
    if year:
        con = year[0].contents[3].contents[0]
        con = con.replace('\n','')
        pattern = r'Published(.*)by'
        searchObj = re.search(pattern, con)
        y = searchObj.group(1).strip()
        y = y[-4:]
        return y
    else:
        print "No year found"
        return None  

def makeSoup(path):
        return BeautifulSoup(open(path), "html.parser")  

def wgetFile(url, dest):
    if (os.path.isfile(dest)):
            os.remove(dest)
    filename = wget.download(url, out = dest)
    return filename



def scrape_google_for_id(booktitle):
    booktitle = booktitle.replace(' ', '+')
    booktitle = booktitle.lower()
    res = requests.get('http://google.com/search?q=site:goodreads.com+%s' % (booktitle))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    linkElems = soup.select('.r a')
    raw_link =  linkElems[0].get('href')
    pattern = r'book\/show\/(\d+)'
    
    searchObj = re.search(pattern, raw_link)
    if not searchObj:
        return None
    return searchObj.group(1)
    
    
    
def scrapeGoodreads(path):
    info = {}
    soup = makeSoup(path)
    info['title'] = get_title(soup)
    info['author'] = get_author(soup)
    series = get_series(soup)
    info['series'] = series[:-3].strip()
    info['volume'] = series[-3:].strip()
    info['year'] = get_year(soup)
    info['desc'] = get_description(soup)
    return info
    
if __name__ == "__main__":	    
    #title = "well of ascension" #68429
    #title = "final empire" #68428
    #title = "way of kings"
    #title = "misery"
    #scrape_goodreads(title)
    #print scrapeGoodreads("6065889.html")
    print scrapeGoodreads("7235533.html")
    








