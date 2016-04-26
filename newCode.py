

######################### Main Program Loop ##################################
rootPath = os.path.join(os.getcwd(), 'python', 'test2')
for d in getSubFolders(rootPath):
    print "Processing", d
    sub = os.path.join(rootPath, d) 
    needToConvert(sub) 
    needToCombine(sub)
    if not countFiles(sub, '\*.MP3') == 1:
        print "Something went wrong.  Skipping import of ", d, "\n\n"
    else:
        outputFile = os.listdir(sub)
        print "Scraping Google for ", d
        id = '123456'
        #id = scrapeGoogleForID(d)
        print "Scraping Goodreads for ", id
        #info = scrapeGoodreads(id)
        print "Updating ID3 information"
        #writeID3(info)
        print "Reading ID3 for length"  #shouldn't have to write and then read back data from ID3
        #info = readID3(outputFile)
        print "Moving file "
        #moveFile(d, 'books_location/correctName')
        print "Downloading artwork"
        #wget info['imageURL'], info['id'].{extension}
        print "Moving artwork"
        #moveFile(imageFile, imageLocation)
        print "Writing info to the database"
        #writeToDB(info)
        print "Finished processing ", d
        print "\n\n"
        
######################### Main Program Loop ##################################   




    
######################### Creating RSS.XML ###################################
    
from datetime import datetime


def createRSSXML(infos, path):
    #deleteFile(os.path.join(path,'rssBackup.xml')
    #moveFile(os.path.join(path, 'rss.xml'), os.path.join(path, 'rssBackup.xml'))
    template = open('header.xml', 'r')
    rss = open('rss.xml', 'w')
    rss.write(template.read().format(datetime.today().strftime("%a, %d %b %Y %H:%M:%S GMT")))
    template.close()
    
    for info in infos:
        template = open('item.xml', 'r')
        print info['title']
        rss.write(template.read().format(**info))
        template.close()
    template = open('footer.xml', 'r')
    rss.write(template.read())
    template.close()
    rss.close()
    

infos = []
info = {'title' : 'My Book Title', 'author' : 'Mizzle', 'desc' : "This is my book's description", 'url' : 'http://www.google.com',
        'fileSize' : 1000, 'dateAdded' : '4/25/16', 'length' : 1800}
infos.append(info)


info = {'title' : 'My Second Book Title', 'author' : 'Mizzle', 'desc' : "This is my book's sequel description", 'url' : 'http://www.google.com',
        'fileSize' : 2586, 'dateAdded' : '4/25/16', 'length' : 1800}        
infos.append(info)

createRSSXML(infos, '')   
    
######################### Creating RSS.XML ###################################    