import unittest
from filesystem import makeDir, getSubFolders, moveFile, createFile, removeFile
import os

class fileSystemTests(unittest.TestCase):
    def setUp(self):
        """ Testing folder setup the same way a downloads folder will be """
        self.path = "testing"
        makeDir(self.path)
        makeDir(os.path.join(self.path,"The Way of Kings"))
        makeDir(os.path.join(self.path,"The Price of Spring"))
        makeDir(os.path.join(self.path,"Mistborn The Final Empire"))
        createFile(os.path.join(self.path, "test1"))
        removeFile(os.path.join(self.path, "test4"))
    def tearDown(self):
        pass
    def testDirListing(self):
        subFolders = getSubFolders(self.path)
        self.assertTrue("Mistborn The Final Empire" in subFolders)
        self.assertTrue("The Way of Kings" in subFolders)
        self.assertTrue("The Price of Spring" in subFolders)
        
    def testMoveFile(self):
        move_file(os.path.join(self.path, "test1"), os.path.join(self.path, "test4"))
        self.assertFalse(os.path.exists(os.path.join(self.path, "test1")))
        self.assertTrue(os.path.exists(os.path.join(self.path, "test4")))
unittest.main()