from mydb import MYDB
from audiobook import Audiobook
import unittest



class testDBFunctions(unittest.TestCase):
    
    def setUp(self):
        self.db = MYDB('test.db')
        self.TOINSERT = {'id' : '123456', 'title' : 'my title', 'author' : 'mizzle', 'series' : 'bizzle',  'volume' : '#6', 'year' : 1981, \
                    'date_added' : '4-28-2016', 'duration' : 407, 'local_url' : 'http://www.google.com', 'file_size' : 16419170, 'deleted' : 0, \
                    'local_image_url' : 'http://www.myimage.com', 'description' : 'A very long description...'}
        
    
    def tearDown(self):
        self.db.delete_all('books')
        pass
    
    def test_insert_record(self):
        num_records = self.db.count_records('books')
        self.db.insert_record('books', self.TOINSERT)
        self.assertEqual(num_records + 1, self.db.count_records('books'))
    
    def test_select_all(self):
        results = self.db.select_all('books')
        self.assertEqual(len(results), self.db.count_records('books'))

    def test_add_book(self):
        ab = Audiobook(r'Well of Ascension')
        ab.title = 'Well of Ascension'
        ab.series = 'Mistborn'
        ab.volume = '#5'
        ab.author = 'Brandon Sanderson'
        ab.year = 2015
        ab.description = 'A long description ....'
        ab.local_image_url = 'http://image.url.com'
        ab.id = '123456'
        ab.date_added = '4-28-2016'
        ab.duration = 407
        ab.local_url = 'http://www.google.com'
        ab.file_size = 16419170
        ab.deleted = 0
        num_records = self.db.count_records('books')
        self.db.insert_record('books', ab.__dict__)
        self.assertEqual(num_records + 1, self.db.count_records('books'))

    def test_get_book(self):
        id = '123456'
        self.db.insert_record('books', self.TOINSERT)
        book = self.db.get_book('books', id)
        self.assertTrue(len(book)>0)
        id = '654321'
        book = self.db.get_book('books', id)
        self.assertFalse(len(book)>0)
    
    def test_insert_duplicate(self):
        self.db.insert_record('books', self.TOINSERT)
        self.db.insert_record('books', self.TOINSERT)
        self.assertEqual(1, self.db.count_records('books'))
        diff_record = self.TOINSERT
        diff_record['id'] = '123457'
        self.db.insert_record('books', diff_record)
        self.assertEqual(2, self.db.count_records('books'))
        
if __name__ == "__main__":
    unittest.main()