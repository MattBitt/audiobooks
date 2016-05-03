from scrapers import GoodreadsScraper, GoogleScraper
from downloader import Downloader
from bs4 import BeautifulSoup
import unittest
import os

class testGoodreadsScraperLocalFile(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        downloaded_file = '68428.html'
        if os.path.exists(downloaded_file):
            cls.soup = BeautifulSoup(open(downloaded_file), "html.parser")
            cls.grs = GoodreadsScraper(cls.soup)
        else:
            raise Exception("File not found")
        
    def tearDown(self):
        pass
        
    def test_title(self):
        self.assertEqual(self.grs.title, 'Mistborn: The Final Empire')
        
    def test_author(self):
        self.assertEqual(self.grs.author, 'Brandon Sanderson')
    
    def test_series(self):
        self.assertEqual(self.grs.series, 'Mistborn')

    def test_volume(self):
        self.assertEqual(self.grs.volume, '#1')
        
    def test_year(self):
        self.assertEqual(self.grs.year, '2006')
        
    def test_description(self):
        self.assertIsNotNone(self.grs.description)
        
    def test_image_url(self):
        self.assertTrue('http://' in self.grs.image_url)

@unittest.skip('skipping downloading file')
class testGoodreadsScraperDownloadedFile(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        id = '68428'
        d = Downloader()
        url = d.goodreads_url(id)
        results = d.download_ram(url)
        cls.soup = BeautifulSoup(results, "html.parser")
        cls.grs = GoodreadsScraper(cls.soup)

    def tearDown(self):
        pass
        
    def test_title(self):
        self.assertEqual(self.grs.title, 'Mistborn: The Final Empire')
        
    def test_author(self):
        self.assertEqual(self.grs.author, 'Brandon Sanderson')
    
    def test_series(self):
        self.assertEqual(self.grs.series, 'Mistborn')

    def test_volume(self):
        self.assertEqual(self.grs.volume, '#1')
        
    def test_year(self):
        self.assertEqual(self.grs.year, '2006')
        
    def test_description(self):
        self.assertIsNotNone(self.grs.description)
        
    def test_image_url(self):
        self.assertTrue('http://' in self.grs.image_url)
        
class testGoogleScraper(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    
    def test_id_from_local_file(self):
        downloaded_file = os.path.join('temp', 'google_results.html')
        if os.path.exists(downloaded_file):
            soup = BeautifulSoup(open(downloaded_file), "html.parser")
            gs = GoogleScraper(soup)
        else:
            raise Exception("File not found")
        self.assertEqual(gs.id, '68429')
    
    @unittest.skip('skip downloading file')    
    def test_id_from_downloads(self):
        query = 'Well of Ascension'
        d = Downloader()
        url = d.goodreads_id_query(query)
        results = d.download_ram(url)
        soup = BeautifulSoup(results, 'html.parser')
        gs = GoogleScraper(soup)
        self.assertEqual(gs.id, '68429')
   
unittest.main()