import urllib2

class Downloader(object):
    def __init__(self):
        pass
        
    def download_file(self, url, file_name):
        req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
        con = urllib2.urlopen( req )
        f = open(file_name, 'w')
        f.write(con.read())
        f.close()
        
    def download_ram(self, url):
        req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
        con = urllib2.urlopen( req )
        return con.read()
    
    def fix_url(self, bad_url):
        bad_url = bad_url.lower()
        fixes = {' ' : '%20', ':' : '%3A'}
        for b, a in fixes.items():
            bad_url = bad_url.replace(b, a)
            
        return bad_url

    def goodreads_id_query(self, query):
        url = 'https://www.google.com/search?&q=site%3Agoodreads.com%20'
        url += self.fix_url(query)
        return url
        
    def goodreads_url(self, id):
        return 'http://www.goodreads.com/book/show/' + id
        
    def download_image(self, url, file):
        response = urllib2.urlopen(url)
        CHUNK = 16 * 1024
        with open(file, 'wb') as f:
           while True:
              chunk = response.read(CHUNK)
              if not chunk: break
              f.write(chunk)