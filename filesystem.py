import os

def makeDir(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)
        
def getSubFolders(path):
    if os.path.exists(path):
        return os.listdir(path)
    return None
def moveFile(source, destination):
    os.rename(source, destination)
def createFile(path):
    if not os.path.exists(path):
        open(path, "w").close()
def removeFile(path):
    if os.path.exists(path):
        os.remove(path)