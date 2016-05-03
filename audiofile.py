from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import os

class Audiofile(object):
    VALID_FIELDS = ['title', 'artist', 'album', 'tracknumber', 'date']
    def __init__(self, filename):
        if os.path.exists(filename):
            if filename[-3:].lower() == 'mp3':
                self.filename = filename
                self.type = 'mp3'
        if not self.type:
            raise ValueError('Unable to determine the type of the audiofile {}'.format(filename))
    
    @property
    def duration(self):
        return int(MP3(self.filename).info.length)
    
    @property
    def file_size(self):
        return os.path.getsize(self.filename)
        
    @property
    def title(self):
        return EasyID3(self.filename).get('title')[0]
    
    @title.setter
    def title(self, new_title):
        audio = EasyID3(self.filename)
        audio['title'] = new_title
        audio.save()
        self._title = new_title
        
    @property
    def author(self):
        return EasyID3(self.filename).get('artist')[0]
    
    @author.setter
    def author(self, new_author):
        audio = EasyID3(self.filename)
        audio['artist'] = new_author
        audio.save()
        self._artist = new_author
        
    @property
    def series(self):
        return EasyID3(self.filename).get('album')[0]
    
    @series.setter
    def series(self, new_series):
        audio = EasyID3(self.filename)
        audio['album'] = new_series
        audio.save()
        self._series = new_series
        
    @property
    def volume(self):
        return EasyID3(self.filename).get('tracknumber')[0]
    
    @volume.setter
    def volume(self, new_volume):
        audio = EasyID3(self.filename)
        audio['tracknumber'] = new_volume
        audio.save()
        self._tracknumber = new_volume
    
    @property
    def year(self):
        return EasyID3(self.filename).get('date')[0]
    
    @year.setter
    def year(self, new_year):
        audio = EasyID3(self.filename)
        audio['date'] = new_year
        audio.save()
        self._year = new_year
    
if __name__ == "__main__":        
    af = Audiofile(r'18739426.mp3')
    print af.title
    print af.author
    print af.series
    print af.volume
    print af.year
    print af.duration

    property_names=[p for p in dir(Audiofile) if isinstance(getattr(Audiofile,p),property)]
    print property_names
    print getattr(af, property_names[0])
