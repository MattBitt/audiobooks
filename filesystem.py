import os
import glob

def makeDir(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)
        
def moveFile(source, destination):
    os.rename(source, destination)
def createFile(path):
    if not os.path.exists(path):
        open(path, "w").close()
def removeFile(path):
    if os.path.exists(path):
        os.remove(path)
		
		
		
def getSubFolders(path):
    return [f for f in os.listdir(path) if not os.path.isfile(os.path.join(path, f))]

def countFiles(path, extension):
    return len([f for f in glob.glob(path+extension)
                if os.path.isfile(os.path.join(path, f))])
   
def needToConvert(path):
    num = countFiles(path, '/*.txt') #m4b
    if num: #any m4b files need to be converted
        print "Converting: ", path 
        #need to call shell command to convert
        #move m4b files to a conversion folder
        outputFile = 'fdas' #{folderName}.mp3
        for f in os.listdir(path):
            if not f == outputFile:
                print "moving", f
                #moveFile(f, '../../converted')

        return True
    print "No need to convert"
    return False
        
def needToCombine(path):
    num = countFiles(path , '/*.MP3') #m4b
    if num > 1:
        print "Combining: ", path
        outputFile = 'fdsa' #{folderName}.mp3
        for f in os.listdir(path):
            if not f == outputFile:
                #moveFile(f, '../../combined')
                print "Moving", f
        #need to call shell command to combine MP3'seek
        #move MP3 pieces to combined folder
        return True
    print "No need to combine"
    return False