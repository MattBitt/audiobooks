from scrapers import GoodreadsScraper, GoogleScraper
from bs4 import BeautifulSoup
import unittest
import os

class testGoodreadsScraper(unittest.TestCase):
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

class testGoogleScraper(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        downloaded_file = 'google_results.html'
        if os.path.exists(downloaded_file):
            cls.soup = BeautifulSoup(open(downloaded_file), "html.parser")
            cls.gs = GoogleScraper(cls.soup)
        else:
            raise Exception("File not found")
    
    def test_id(self):
        self.assertEqual(self.gs.id, '68429')
    
unittest.main()