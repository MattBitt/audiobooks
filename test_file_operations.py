import unittest
from file_operations import make_dir, get_subfolders, move_file, create_file, remove_file
import os

class fileSystemTests(unittest.TestCase):
    def setUp(self):
        """ Testing folder setup the same way a downloads folder will be """
        self.path = "testing"
        make_dir(self.path)
        make_dir(os.path.join(self.path,"The Way of Kings"))
        make_dir(os.path.join(self.path,"The Price of Spring"))
        make_dir(os.path.join(self.path,"Mistborn The Final Empire"))
        create_file(os.path.join(self.path, "test1"))
        remove_file(os.path.join(self.path, "test4"))
    
    def tearDown(self):
        pass
    
    def testDirListing(self):
        subfolders = get_subfolders(self.path)
        self.assertEqual(len(subfolders), 3)
        self.assertTrue("Mistborn The Final Empire" in subfolders)
        self.assertTrue("The Way of Kings" in subfolders)
        self.assertTrue("The Price of Spring" in subfolders)
        
    def testMoveFile(self):
        move_file(os.path.join(self.path, "test1"), os.path.join(self.path, "test4"))
        self.assertFalse(os.path.exists(os.path.join(self.path, "test1")))
        self.assertTrue(os.path.exists(os.path.join(self.path, "test4")))
        
    def test_make_directory(self):
        tmp_path = 'tmp_path'
        self.assertFalse(os.path.exists(tmp_path))
        make_dir(tmp_path)
        self.assertTrue(os.path.exists(tmp_path))
        os.rmdir(tmp_path)
        
    def test_convert_m4b(self):
        SOURCE = 
unittest.main()