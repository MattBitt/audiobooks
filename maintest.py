import unittest
import shutil, os
from mp3_functions import readID3, writeID3
from webscraper import scrape_google_for_id, downloadFile, scrapeGoodreads

class MP3ReadTests(unittest.TestCase):
    """ Tests reading writing ID3 information of MP3's """
    def setUp(self):
        self.file = "Shadows of Self - 02.mp3"
        self.example = {'title': 'Shadows of Self', 'author' : 'Brandon Sanderson',
                        'series' : 'Mistborn', 'volume' : '5', 'year' : '2015',
                        'length' : 1800}
        
    def tearDown(self):
        pass
    
    def testReadTitle(self):
        id3 = readID3(self.file)
        self.assertEqual(id3['title'], self.example['title'])

    def testReadAuthor(self):
        id3 = readID3(self.file)
        self.assertEqual(id3['author'], self.example['author'])
    
    def testReadSeries(self):
        id3 = readID3(self.file)
        self.assertEqual(id3['series'], self.example['series'])
    
    def testReadVolume(self):
        id3 = readID3(self.file)
        self.assertEqual(id3['volume'], self.example['volume'])
    
    def testReadYear(self):
        id3 = readID3(self.file)
        self.assertEqual(id3['year'], self.example['year'])

    def testReadLength(self):
        id3 = readID3(self.file)
        self.assertEqual(int(id3['length']), int(self.example['length']))

   
class MP3WriteTests(unittest.TestCase):
    """ Tests reading writing ID3 information of MP3's """
    def setUp(self):
        self.file = "Shadows of Self - 02.mp3"
        shutil.copyfile(self.file, "tmp" + self.file)
        self.file = "tmp" + self.file
        self.changed = {'title': 'Mizzle', 'author' : 'MizzleBizzle',
                        'series' : 'Bittinger', 'volume' : '1', 'year' : '1981',
                        'length' : 35}   
  
    def tearDown(self):
        os.remove(self.file)
    def testWriteTitle(self):
        writeID3(self.file, 'title', self.changed['title'])
        id3 = readID3(self.file)
        self.assertEqual(id3['title'], self.changed['title'])

    def testWriteAuthor(self):
        writeID3(self.file, 'author', self.changed['author'])
        id3 = readID3(self.file)
        self.assertEqual(id3['author'], self.changed['author'])
    
    def testWriteSeries(self):
        writeID3(self.file, 'series', self.changed['series'])
        id3 = readID3(self.file)
        self.assertEqual(id3['series'], self.changed['series'])
    
    def testWriteVolume(self):
        writeID3(self.file, 'volume', self.changed['volume'])
        id3 = readID3(self.file)
        self.assertEqual(id3['volume'], self.changed['volume'])
    
    def testWriteYear(self):
        writeID3(self.file, 'year', self.changed['year'])
        id3 = readID3(self.file)
        self.assertEqual(id3['year'], self.changed['year'])



class WebScrapingTests(unittest.TestCase):
    """ Tests reading writing ID3 information of MP3's """
    def setUp(self):
        self.example = {'title' : 'way of kings', 'id' : '7235533'} 
        #self.example = {'title' : 'price of spring', 'id' : '6065889'} 
        #self.example = {'title' : 'final empire', 'id' : '68428'} 
        self.exampleInfo = {'id' : self.example['id'], 
                              'title' : "The Way of Kings", 
                              'author' : 'Brandon Sanderson', 
                              'series' : "The Stormlight Archive", 'volume' : '1',
                              'year' : '2010', 'desc' : 'Some Description'}
        
    def tearDown(self):
        pass 
    def testGoogleScraperBad(self):
        self.assertIsNone(scrape_google_for_id("mizzle"))   
    def testGoogleScraper(self):
        self.assertEqual(self.example['id'], 
                         scrape_google_for_id(self.example['title']))
    def testDownloadFile(self):
        url = 'http://www.goodreads.com/book/show/' + self.example['id']
        dest = self.example['id'] + '.html'
        downloadFile(url, dest)
        self.assertTrue(os.path.isfile(dest))
   
            
    def testGoodReadsTitle(self):
        dest = self.example['id'] + '.html'
        info = scrapeGoodreads(dest)
        self.assertEqual(self.exampleInfo['title'], info['title'])

unittest.main()