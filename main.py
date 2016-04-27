from file_operations import get_sub_folders, combine_mp3s, convert_from_m4b, count_files, move_goodreads_files, move_file, remove_file
from webscraper import scrape_google_for_id, wget_file, scrape_goodreads, get_image_url
from db_functions import add_book_to_db, get_all_info_from_db
from mp3_functions import write_info_to_id3
from datetime import datetime, date
import os
BASEURL = 'http://bittfurst.dynamic-dns.net:4041/books/'

def get_info(book_file, id):
    """ This function gets info from the MP3 file, google.com, and goodreads.com 
        book_file = The absolute path of a single MP3 file
        id = The scraped goodreads id number
        returns:  Dictionary containing all of the info from goodreads/mp3 file
    """
    book_name = os.path.basename(os.path.dirname(book_file))
    print "Getting Info about", book_name
    print "Scraping Google for ", book_name
    #id = scrape_google_for_id(book_name)
    
    #wget_file("http://www.goodreads/book/show/"+id, id + ".html")
    print "Scraping Goodreads for", id, "info"
    info_file = id +'.html'
    info = scrape_goodreads(id, info_file)
    
    #info['duration'] = read_duration(book_file)
    info['duration'] = 1800
    info['date_added'] = datetime.today()
    info['file_size'] = os.path.getsize(book_file)
    
    #TARGET_LOCATION = os.path.join(os.getcwd(), 'books', info['author'])
    AUTHOR_FOLDER = info['author'].lower().replace(' ', '_')
    print AUTHOR_FOLDER
    #info['url'] = generate_url('books_location/author_name/correctName')
    info['url'] = BASEURL + info['author'] + '/' + info['id'] + '.mp3'
    #wget info['imageURL'], info['id'].{extension}    
    info['image_url'] = BASEURL + info['author'] + '/' + info['id'] + '.jpg'
    
    info['deleted'] = 0
    return info
         
def get_goodreads_id(book_name):
    return scrape_google_for_id(book_name)

def download_goodreads_files(id):
    goodreads_url = 'http://www.goodreads.com/book/show/' + id
    out_file = id + '.html'
    print "Downloading Goodreads page"
    #successful = wget.download(goodreads_url, out=out_file)
    successful = True
    if successful:
        image_url = get_image_url(out_file)
        img_out_file = id + '.jpg' #need to get extension from actual file
        print "Downloading artwork"
        #successful = wget.download(image_url, img_out_file)
        successful = True
        if not successful:
            print "There was a problem downloading the image", image_url
            return False
        return True
    else:
        print "There was a problem downloading the info for id", id
    return False
           
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
    ROOTPATH = os.getcwd()
    DOWNLOADS = os.path.join(ROOTPATH, 'downloads')
    TARGET = os.path.join(ROOTPATH, 'books')
    DB = 'audiobooks.db'
    for book_folder_path in get_sub_folders(DOWNLOADS):
        book_name = os.path.basename(book_folder_path)
        print "Processing: ", book_name, book_folder_path
        convert_from_m4b(book_folder_path) 
        combine_mp3s(book_folder_path)
        if not count_files(book_folder_path, '\*.MP3') == 1:
            print "Something went wrong.  Skipping import of ", book_name, "\n\n"
        else:
            #id = get_goodreads_id(book_name)
            id = '7235533'
            file_name = os.listdir(book_folder_path)[0]
            book_file = os.path.join(book_folder_path, file_name)
            success = download_goodreads_files(id)
            if success:
                info = get_info(book_file, id)
                add_book_to_db(DB, info)
                write_info_to_id3(book_file, info)
                #move_goodreads_files(book_file, TARGET, info)
                print "Finished processing ", book_name
                print "\n\n"
            
    INFOS = get_all_info_from_db(DB)
    create_rss_xml(INFOS, os.path.join(os.getcwd(), 'podcast'))
    