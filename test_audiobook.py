from scrapers import GoodreadsScraper, GoogleScraper
from mydb import MYDB
from audiobook import Audiobook
from audiofile import Audiofile
from bs4 import BeautifulSoup
import unittest

class testAudiobook(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ab = Audiobook(r'Well of Ascension')
        cls.af = Audiofile(r'Well of Ascension\Well of Ascension.mp3')
        
    def test_initial_name(self):
        self.assertEqual(self.ab.initial_book_name, 'Well of Ascension')
    
    def test_info_from_google(self):
        google_soup = BeautifulSoup(open('google_results.html'), 'html.parser')
        self.ab.id = GoogleScraper(google_soup).id 
        self.assertEqual(self.ab.id, '68429')
        
    def test_info_from_goodreads(self):
        good_reads_soup = BeautifulSoup(open('68429.html'), 'html.parser')
        grs = GoodreadsScraper(good_reads_soup)    
        self.ab.update_from_goodreads(grs)
        self.assertEqual(self.ab.title, 'The Well of Ascension')
        self.assertEqual(self.ab.series, 'Mistborn')
        self.assertEqual(self.ab.volume, '#2')
        self.assertEqual(self.ab.author, 'Brandon Sanderson')
        self.assertEqual(self.ab.year, '2007')
        self.assertIsNotNone(self.ab.description)
        self.assertTrue('http://' in self.ab.image_url)
        
    def test_info_from_audiofile(self):
        self.ab.read_from_id3(self.af)
        self.assertEqual(self.ab.duration, 407)
        self.assertEqual(self.ab.file_size, 16419170)
        
class testAudiofileFromAudiobook(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        good_reads_soup = BeautifulSoup(open('68429.html'), 'html.parser')
        cls.ab = Audiobook(r'Well of Ascension')
        grs = GoodreadsScraper(good_reads_soup)   
        cls.ab.update_from_goodreads(grs)
        cls.af = Audiofile(r'Well of Ascension\Well of Ascension.mp3')
        cls.af.title = 'Nonsense'
        cls.af.author = 'Mizzle'
        cls.af.series = 'Bizzle'
        cls.af.volume = '#99'
        cls.af.year = '1981'
        
    def test_write_to_id3(self):
        self.assertEqual(self.af.title, 'Nonsense')
        self.ab.write_to_id3(self.af)
        self.assertEqual(self.af.title, 'The Well of Ascension')
        
unittest.main()
    