import unittest
import shutil, os
from mp3_functions import readID3, writeID3
from webscraper import scrape_google_for_id, wgetFile, scrapeGoodreads




class MP3ReadTests(unittest.TestCase):
    """ Tests reading ID3 information of MP3's """
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

#class WebScrapingTests(unittest.TestCase):
 #   def setUp(self):
 #        self.example = {'title' : 'way of kings', 'id' : '7235533'} 
 #        self.example = {'title' : 'price of spring', 'id' : '6065889'} 
 #        self.example = {'title' : 'final empire', 'id' : '68428'} 
 #        self.exampleInfo = {'id' : self.example['id'], 
 #                            'title' : "The Way of Kings", 
 #                            'author' : 'Brandon Sanderson', 
 #                            'year' : '2010', 'desc' : 'Some Description'}
        
 #   def tearDown(self):
 #       pass 
    
 #   def testGoogleScraper(self):
 #       self.assertEqual(self.example['id'], 
 #                      scrape_google_for_id(self.example['title']))
 #   def testDownloadFile(self):
 #       url = 'http://www.goodreads.com/book/show/' + self.example['id']
 #       dest = self.example['id'] + '.html'
 #       wgetFile(url, dest)
 #       self.assertTrue(os.path.isfile(dest))

     
   
class GoodReadsScrapingTests(unittest.TestCase):         
    def setUp(self):
        examples = []
        self.exampleInfo = {  'id': "68428", 'title' : "Mistborn: The Final Empire", 
                              'author' : 'Brandon Sanderson', 
                              'series' : "Mistborn", 'volume' : '#1',
                              'year' : '2006', 'desc' : 'In a world where ash '}
       # self.exampleInfo = {  'id': "6065889", 'title' : "The Price of Spring", 
       #                       'author' : 'Daniel Abraham', 
       #                       'series' : "Long Price Quartet", 'volume' : '#4',
       #                       'year' : '2009', 'desc' : 'Fifteen years have'}
       #self.exampleInfo = {  'id': "7235533", 'title' : "The Way of Kings", 
       #                       'author' : 'Brandon Sanderson', 
       #                       'series' : "The Stormlight Archive", 'volume' : '#1',
       #                       'year' : '2010', 'desc' : 'Speak again the ancient oaths'}        
        url = 'http://www.goodreads.com/book/show/' + self.exampleInfo['id']
        self.dest = self.exampleInfo['id'] + '.html'
        if (os.path.isfile(self.dest)):
            os.remove(self.dest)
        wgetFile(url, self.dest)
        
    
    def testGoodReadsTitle(self):
        """ Test if the the title is parsed correctly """
        info = scrapeGoodreads(self.dest)
        #print info
        #shutil.copy(dest, 'test.html')
        #print "GoodReadTest"
        #print os.stat(dest).st_size
        ##print os.stat('test.html').st_size
        self.assertEqual(self.exampleInfo['title'], info['title'])
        self.assertEqual(self.exampleInfo['author'], info['author'])
        self.assertEqual(self.exampleInfo['series'], info['series'])
        self.assertEqual(self.exampleInfo['volume'], info['volume'])
        self.assertEqual(self.exampleInfo['year'], info['year'])
        self.assertEqual(self.exampleInfo['desc'][:10], info['desc'][:10])


unittest.main()