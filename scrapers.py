from bs4 import BeautifulSoup, NavigableString
from unidecode import unidecode
import os
import re


class GoodreadsScraper(object):
    def __init__(self, soup):
        self.soup = soup
        

    @property
    def title(self):
        title_section = self.soup.select('.bookTitle')
        if title_section:
            return title_section[0].contents[0].strip()
        else:
            print "No title found"
            return None
    
    @property
    def author(self):
        author_section = self.soup.select('.authorName span')
        if author_section:
            return author_section[0].contents[0]
        else:
            print "No author found"
            return None
    
    
    def series_string(self):
        series_section = self.soup.select('#bookTitle a')
        if series_section:
            series_name = series_section[0].contents[0].strip()
            return series_name[1:-1].strip()
        else:
            return None
    
    @property
    def series(self):
        ss = self.series_string()
        if ss:
            return ss[0:-3].strip()
        else:
            return ' '
    
    @property   
    def volume(self):
        ss = self.series_string()
        if ss:
            return ss[-3:].strip()
        else:
            return ' '
    
    @property
    def year(self):
        year_section = self.soup.select('#details')
        if year_section:
            con = year_section[0].contents[3].contents[0]
            con = con.replace('\n', '')
            pattern = r'Published(.*)by'
            searchObj = re.search(pattern, con)
            y = searchObj.group(1).strip()
            y = y[-4:]
            return y
        else:
            print "No year found"
            return None  
    
    @property
    def image_url(self):
        return self.soup.find('img', {'id' : 'coverImage'})['src']
    
    
    @property
    def description(self):
        description_section = self.soup.select('#description span')
        d = ""
        if description_section:
            for l in description_section[1].contents:
                if isinstance(l, NavigableString):
                    d = d + unidecode(l) + " "
            return d.replace("\"","").replace("\'","")
        else:
            return None
    

class GoogleScraper(object):
    def __init__(self, soup):
        self.soup = soup
                
    @property
    def id(self):
        linkElems = self.soup.select('.r a')
        raw_link = linkElems[0].get('href')
        pattern = r'book\/show\/(\d+)'
        searchObj = re.search(pattern, raw_link)
        if not searchObj:
            return None
        return searchObj.group(1)    
    
if __name__ == "__main__":
    soup = BeautifulSoup(open('68429.html'), "html.parser")
    grs = GoodreadsScraper(soup)
    print grs.year
    print grs.author
    print grs.title
    print grs.series
    print grs.volume
    print grs.image_url
    print grs.description
    
    
    soup = BeautifulSoup(open('google_results.html'), "html.parser")
    gs = GoogleScraper(soup)
    print gs.id