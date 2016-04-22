from bs4 import BeautifulSoup, NavigableString, Tag
import urllib2
from unidecode import unidecode
import requests
import re
import wget

BASE_URL = "http://www.goodreads.com/book/show/"

def get_author(soup):
    author = soup.select('.authorName span')
    if author:
        return author[0].contents[0]
    else:
        o = open("output.txt", "w")
        for l in soup.prettify('utf-8'):
            o.write(l)
        o.close()
        print "No author found"
        return None
def get_title(soup):
    title = soup.select('#bookTitle')
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
        return BeautifulSoup(open(path), "lxml")  

#def wget_function(goodreads_id):
#    BASE_URL = "http://www.goodreads.com/book/show/"
#    goodreads_url = BASE_URL + goodreads_id
#    wget.download(url=goodreads_url, out=goodreads_id+".html")

#def wgetScraper(url, dest):
#    return False
def downloadFile(url, dest):
    try:
        f = urllib2.urlopen(url)
        # Open our local file for writing
        with open(dest, "wb") as local_file:
            local_file.write(f.read())

    #handle errors
    except HTTPError, e:
        print "HTTP Error:", e.code, url
    except URLError, e:
        print "URL Error:", e.reason, url


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
    #soup = None
    return searchObj.group(1)
    
    
    
def scrapeGoodreads(path):
    #goodreads_id = scrape_google_for_id(bookTitle)    
    #print goodreads_id    
    info = {}

    #wget_function(goodreads_id)
   
    #soup = make_soup(DOWNLOADED_FILE)
    #soup = make_soup("7235533-the-way-of-kings") 
    #soup = make_soup("6065889-the-price-of-spring")
    #soup = make_soup("243272.Mistborn.html") 
    #goodreads_id = '10614'
    #soup = make_soup('10614.html')
    soup = makeSoup(path)

    info['title'] = get_title(soup)
    info['author'] = get_author(soup)
    series = get_series(soup)
    info['series'] = series[:-3]
    info['volume'] = series[-3:]
    info['year'] = get_year(soup)
    info['desc'] = get_description(soup)
    return info
    
if __name__ == "__main__":	    
    #title = "well of ascension" #68429
    #title = "final empire" #68428
    #title = "way of kings"
    title = "misery"
    scrape_goodreads(title)









