from downloader import Downloader
import unittest
import os


class testDownloader(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_fix_url(self):
        bad_url = "site:goodreads.com well of ascension"
        d = Downloader()
        good_url = d.fix_url(bad_url)
        self.assertEqual(good_url, 'site%3Agoodreads.com%20well%20of%20ascension')
    
    def test_goodreads_id_query(self):
        query = 'Well of Ascension'
        d = Downloader()
        good_url = 'https://www.google.com/search?&q=site%3Agoodreads.com%20well%20of%20ascension'
        self.assertEqual(d.goodreads_id_query(query), good_url)
    
    @unittest.skip('skipping download file')
    def test_download_google_results_file(self):
        query = 'Well of Ascension'
        file_name = os.path.join('temp','google_results.html')      
        if os.path.exists(file_name):
            os.remove(file_name)
        d = Downloader()
        url = d.goodreads_id_query(query)
        result = d.download_file(url, file_name)
        self.assertTrue(os.path.exists(file_name))
    
    @unittest.skip('skipping download file')
    def test_download_ram(self):
        query = 'Well of Ascension'
        d = Downloader()
        url = d.goodreads_id_query(query)
        results = d.download_ram(url)
        self.assertTrue('68429' in results)
    
    def test_goodreads_url(self):
        correct_url = 'http://www.goodreads.com/book/show/68429'
        id = '68429'
        d = Downloader()
        self.assertEqual(correct_url, d.goodreads_url(id))

unittest.main()