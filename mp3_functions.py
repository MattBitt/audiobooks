from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
FIELDS = {'title' : 'title', 'author' : 'artist', 'series' : 'album',
         'volume' : 'tracknumber', 'year' : 'date'}

def read_id3(path):
    book_info = {}
    if path:
        book_info = get_easy_id3(path)
        book_info['length'] = int(getLength(path))
    return book_info

def get_easyid3(path):
    book_info = {} 
    audio = EasyID3(path)
    for book, id3 in FIELDS.items():
        book_info[book] = audio.get(id3)[0]
    return book_info

def get_duration(path):
    audio = MP3(path)
    return audio.info.length
    
# def write_id3(path, info_dict):
    # """Takes the path of an audiobook file and sets the field to val """
    # audio = EasyID3(path)
    # for book, id3 in FIELDS.items():
        # audio[id3] = info_dict[book]
    
    
    # # if FIELDS[field] in EasyID3.valid_keys.keys():
        
        # # audio[FIELDS[field]] = val
        # # audio.save()
    # # else:
        # # raise ValueError('%s is not a valid field name' % (field))

def write_info_to_id3(book_file, info):
    return True
    audio = EasyID3(book_file)
    for book, id3 in FIELDS.items():
        audio[id3] = info_dict[book]
    audio.save()
    
if __name__ == "__main__":  
    bookname = "Shadows of Self - 26.mp3"
    print readID3(bookname, "artist")
    print readID3(bookname, "length")
    setID3(bookname, "artist", "Mizzle")
    print readID3(bookname, "artist")
    setID3(bookname, "mizzle", "asdf")