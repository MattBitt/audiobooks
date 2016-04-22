from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
#book_fields = ['title', 'author', 'series', 'volume', 'year']
#id3_fields = ['title', 'artist', 'album', 'tracknumber', 'date']
fields = {'title' : 'title', 'author' : 'artist', 'series' : 'album',
		 'volume' : 'tracknumber', 'year' : 'date'}
def readID3(path):
	book_info = {}
	if path:
		book_info = getEasyID3(path)
		book_info['length'] = getLength(path)
	return book_info
def getEasyID3(path):
	book_info = {} 
	audio = EasyID3(path)
	for book, id3 in fields.items():	#zip(book_fields, id3_fields):
			book_info[book] = audio.get(id3)[0]
	return book_info
def getLength(path):
	audio = MP3(path)
	return audio.info.length
	
def writeID3(path, field, val):
	"""Takes the path of an audiobook file and sets the field to val """
	if fields[field] in EasyID3.valid_keys.keys():
		audio = EasyID3(path)
		audio[fields[field]] = val
		audio.save()
	else:
		raise ValueError('%s is not a valid field name' % (field))
		
if __name__ == "__main__":	
	bookname = "Shadows of Self - 26.mp3"
	print readID3(bookname, "artist")
	print readID3(bookname, "length")
	setID3(bookname, "artist", "Mizzle")
	print readID3(bookname, "artist")
	setID3(bookname, "mizzle", "asdf")