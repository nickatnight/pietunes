import os
from mutagen.easyid3 import EasyID3


env = os.environ['HOME']

if 'nick' in env:
    music_dir = '/Users/nick/Music/iTunes/iTunes Media/Music/'
else:
    music_dir = '/mnt/seagatehd/Music'

music_dict = {}

def fetch_data():
    pk=1
    for root,dirs,files in os.walk(music_dir):
        for name in files:
            if name.endswith('.mp3'):
                full_path = os.path.join(root,name)
                audio = EasyID3(full_path)
                #print audio['album'][0] || None
                if not 'album' in audio:
                    audio['album'] = 'No album title.'
                    audio.save()
                if not 'artist' in audio:
                    audio['artist'] = 'No artist name.'
                    audio.save()
                if not 'title' in audio:
                    audio['title'] = 'No title name.'
                    audio.save()
                entry = {}
                entry[pk] = {
                    'title': audio['title'][0],
                    'artist': audio['artist'][0],
                    'album': audio['album'][0],
                    'path': full_path.replace("/Users/nick/Music/iTunes/iTunes Media/Music/","static/music/"),
                    'pk': pk
                }
                pk += 1
                music_dict.update(entry)
                #print os.path.dirname(os.path.dirname(os.path.join(root, name)))




fetch_data()
print music_dict
#print music_dict
