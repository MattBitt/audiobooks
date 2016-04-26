import unittest
import sqlite3
import os
from dbFunctions import getBook, addBook
from mp3_functions import readID3

class dbTests(unittest.TestCase):
    def setUp(self):
        self.dbPath = "test.db"
        self.tblName = "books"
        self.mp3Path = "Shadows of Self - 02.mp3"
        
        
    def tearDown(self):
        pass
        
    def testAddBook(self):
        info = readID3(self.mp3Path)
        info['id'] = '123456'
        info['dateAdded'] = '4-24-2016'
        info['url'] = 'http://www.google.com'
        info['deleted'] = 0
        info['fileSize'] = 1000
        info['imagePath'] = 'http://www.google.com/img'
        addBook(self.dbPath, info)
        dbInfo = getBook(info['id'])
        self.assertEqual(info, dbInfo)
        
        

unittest.main()