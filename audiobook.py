from bs4 import BeautifulSoup, NavigableString
from audiofile import Audiofile
from scrapers import GoodreadsScraper
import os

class Audiobook(object):
    def __init__(self, path):
        """ Creates a new audiobook object as long as the folder exists """
        self.ID3_FIELDS = ['title', 'author', 'series', 'volume', 'year']
        self.GOODREADS_FIELDS = ['title', 'author', 'series', 'volume', 'year', \
                                 'description', 'image_url' ]
        if os.path.exists(path) and not (os.path.isfile(path)):
            self.path = path # path must be the "staging" folder path (not file)
            
            # this comes from the google scraper
            self.id = None
            
            # these come from the goodreads scraper
            self.title = os.path.basename(path)
            self.series = None
            self.volume = None
            self.author = None
            self.year = None
            self.description = None
            self.image_url = None
            
            # these come from the audio file
            self.duration = None
            self.file_size = None

            #these come from the system at the time
            self.date_added = None
            self.local_url = None
            self.local_image_url = None
            
            #future use?
            self.deleted = 0
            
        else:
            print """{} does not exist""".format(path)
    
    @property
    def initial_book_name(self):
        return os.path.basename(self.path)
    
    
    def need_to_combine(self):
        """ Checks if there are multiple audio files in the audiobook folder
        returns True/False """
        pass
    
    def need_to_convert(self):
        """ Checks if the audio files in the folder are acceptable format (MP3 for now)
        returns True/False """
        pass 
        
    def missing_any_fields(self):
        """ Checks appropriate fields to make sure they contain data 
        returns True if missing / False is complete """
    
    def read_from_id3(self, af):
        self.duration = af.duration
        self.file_size = af.file_size


    def write_to_id3(self, af):
        """ Writes the current data to the ID3 of an audiofile object"""
        for f in self.ID3_FIELDS:
            setattr(af, f, getattr(self, f))
    
    def update_from_goodreads(self, grs):
        """ Updates the current data from the goodreads html file """
        for f in self.GOODREADS_FIELDS:
            setattr(self, f, getattr(grs, f))

            
    def __str__(self):
        """ Prints the audiobook info nicely """
        return """{} - {} Volume {}""".format(self.title, self.series, self.volume)

if __name__ == "__main__":        
    #ab = Audiobook(r'c:\users\mbittinger\Desktop\python\audiobooks\downloads\Well of Ascension\')
    ab = Audiobook(r'Well of Ascension')
    af = Audiofile(r'Well of Ascension\Well of Ascension.mp3')

    soup = BeautifulSoup(open('68429.html'), "html.parser")
    grs = GoodreadsScraper(soup)
    abdict = ab.__dict__
    print """{title} - {series} Volume {volume} ({year})
    {description}""".format(**abdict)

    ab.update_from_goodreads(grs)

    print """{title} - {series} Volume {volume} ({year})
    {description}""".format(**abdict)

    ab.write_to_id3(af)
    print af.title
