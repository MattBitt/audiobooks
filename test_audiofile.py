from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from audiofile import Audiofile
import os
import unittest


class testAudiofile(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        audio_file = 'Well of Ascension\Well of Ascension.mp3'
        if os.path.exists(audio_file):
            cls.af = Audiofile(audio_file)
        else:
            raise Exception("File not found")
            
    @classmethod
    def tearDownClass(cls):
        cls.af.title = "Well of Ascension"
        cls.af.author = "Brandon Sanderson"
        cls.af.series = "Mistborn"
        cls.af.volume = "#5"
        cls.af.year = "2015"
        
    def test_title(self):
        self.assertEqual(self.af.title, 'Well of Ascension')
        self.af.title = 'Another Title'
        self.assertEqual(self.af.title, 'Another Title')
 
    def test_author(self):
        self.assertEqual(self.af.author, 'Brandon Sanderson')
        self.af.author = 'Another Author'
        self.assertEqual(self.af.author, 'Another Author') 
   
    def test_series(self):
        self.assertEqual(self.af.series, 'Mistborn')
        self.af.series = 'Another series'
        self.assertEqual(self.af.series, 'Another series') 
        
    def test_volume(self):
        self.assertEqual(self.af.volume, '#5')
        self.af.volume = '#2'
        self.assertEqual(self.af.volume, '#2') 
        
    def test_year(self):
        self.assertEqual(self.af.year, '2015')
        self.af.year = '2016'
        self.assertEqual(self.af.year, '2016') 
        
    def test_duration(self):
        self.assertEqual(self.af.duration, 407)
    
    def test_file_size(self):
        self.assertEqual(self.af.file_size, 16419170)
        
unittest.main()