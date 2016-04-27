import os
import glob

def make_dir(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)
        
def move_file(source, destination):
    os.rename(source, destination)

def create_file(path):
    if not os.path.exists(path):
        open(path, "w").close()

def remove_file(path):
    if os.path.exists(path):
        os.remove(path)
		
def get_sub_folders(path):
    """ This function takes a path and returns any subfolders 
        path = The root path to list the directories
        returns: A list of the absolute path of each subdirectory """
    subs = []
    for d in os.listdir(path):
        if not os.path.isfile(d):
            subs.append(os.path.abspath(os.path.join(path,d)))
    return subs
    
def count_files(path, extension):
    return len([f for f in glob.glob(path+extension)
                if os.path.isfile(os.path.join(path, f))])
   
def convert_from_m4b(path):
    num = count_files(path, '/*.txt') #m4b
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
        
def combine_mp3s(path):
    num = count_files(path , '/*.MP3') #m4b
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
    
def move_goodreads_files(book_file, target, info):
    print "Moving files"
    author_folder = info['author'].lower().replace(' ', '_')
    target_folder = os.path.join(target, author_folder)
    make_dir(target_folder)
    move_file(book_file, os.path.join(target_folder, info['id'] + '.mp3'))
    print "Moving artwork"
    #moveFile(imageFile, imageLocation)
    pass
    
if __name__ == "__main__":
    DOWNLOADS = os.path.join(os.getcwd(), 'downloads')
    print get_sub_folders(DOWNLOADS)