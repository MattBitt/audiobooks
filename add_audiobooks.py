from file_operations import get_subfolders, get_files, move_file, remove_file
from audiobook import Audiobook
from audiofile import Audiofile
from downloader import Downloader
from scrapers import GoogleScraper, GoodreadsScraper
from mydb import MYDB
from bs4 import BeautifulSoup
from datetime import datetime
import os

BOOK_DEST = os.path.join(os.getcwd(), 'books')
IMG_DEST = os.path.join(BOOK_DEST, 'images')
BASE_URL = 'http://bittfurst.dynamic-dns.net:4041/books/'


def create_rss_xml(infos, path):
    #RSS XML Files
    BACKUP = os.path.join(path, 'rss_backup.xml')
    RSS = os.path.join(path, 'rss.xml')
    #XML Template files
    HEADER = os.path.join(path, 'header.xml')
    ITEM = os.path.join(path, 'item.xml')
    FOOTER = os.path.join(path, 'footer.xml')
    remove_file(BACKUP)
    move_file(RSS, BACKUP)
    template = open(HEADER, 'r')
    rss = open(RSS, 'w')
    rss.write(template.read().format(datetime.today().strftime("%a, %d %b %Y %H:%M:%S GMT")))
    template.close()
    
    for info in infos:
        template = open(ITEM, 'r')
        rss.write(template.read().format(**info))
        template.close()
    template = open(FOOTER, 'r')
    rss.write(template.read())
    template.close()
    rss.close()


if __name__ == "__main__":
    DOWNLOADS = 'downloads'
    LIVE_DOWNLOADS = True #set equal to true after testing
    for direc in get_subfolders(DOWNLOADS):
        d = os.path.join(os.getcwd(), DOWNLOADS, direc)
        print ""
        ab = Audiobook(d)
        print "Started Processing: {}".format(ab.title)
        files = get_files(d)
        if len(files) == 1 and '.mp3' in files[0]:
            af_path = os.path.join(d, files[0])
            af = Audiofile(af_path)
            dl = Downloader()
            url = dl.goodreads_id_query(ab.title)
            print 'Getting Goodreads ID from Google'
            if LIVE_DOWNLOADS:
                results = dl.download_ram(url)
                soup = BeautifulSoup(results, 'html.parser')
                gs = GoogleScraper(soup)
                ab.id = gs.id
            else:
                ab.id = '18007564' #id for the Martian
            print 'ID: {}'.format(ab.id)
            url = dl.goodreads_url(ab.id)
            print 'Downloading info from Goodreads'
            if LIVE_DOWNLOADS:
                results = dl.download_ram(url)
                soup = BeautifulSoup(results, 'html.parser')
            else:
                #enable the following line to initially download the 
                #info file.  Then comment out for testing on local file
                #results = dl.download_file(url, ab.id + '.html')
                soup = BeautifulSoup(open(ab.id + '.html'), "html.parser")
            grs = GoodreadsScraper(soup)
            
            ab.update_from_goodreads(grs)
            img_name = ab.id + '.' + ab.image_url[-3:]
            print 'Downloading image file'
            if LIVE_DOWNLOADS:
                url = ab.image_url
                results = dl.download_image(url, img_name)
                
            print 'Writing ID3 to file'
            ab.write_to_id3(af)
            ab.read_from_id3(af)
            ab.date_added = datetime.today()
            ab.local_url = BASE_URL + ab.id + '.mp3'
            ab.local_image_url = BASE_URL + 'images/{}'.format(img_name)
            print 'Adding book to Database'
            db = MYDB('audiobooks.db')
            db.insert_record('books', ab.__dict__)
            print "Moving files"
            move_file(af_path, os.path.join(BOOK_DEST, ab.id + '.mp3'))
            move_file(img_name, os.path.join(IMG_DEST, img_name))
            
        else:
            print "too many files (or not enough)"
    db = MYDB('audiobooks.db')
    infos = db.get_all_info_from_db()
    create_rss_xml(infos, os.path.join(os.getcwd(), 'podcast'))
            