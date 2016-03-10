import os
from mutagen.easyid3 import EasyID3


env = os.environ['HOME']

if 'nick' in env:
    music_dir = '/Users/nick/Music/iTunes/iTunes Media/Music/'
    web_dir = 'static/music/'
else:
    music_dir = '/mnt/seagatehd/Music'
    web_dir = 'Music/'

music_dict = {}


def parser(attrib, audio):
    if not attrib in audio:
        audio[attrib] = 'None'
        audio.save()

def fetch_data():
    pk=1
    for root,dirs,files in os.walk(music_dir):
        for name in files:
            if name.endswith('.mp3'):
                full_path = os.path.join(root,name)
                audio = EasyID3(full_path)
                parser('artist', audio)
                parser('album', audio)
                parser('title', audio)
                entry = {}
                entry[pk] = {
                    'title': audio['title'][0],
                    'artist': audio['artist'][0],
                    'album': audio['album'][0],
                    'path': full_path.replace(music_dir, web_dir),
                    'pk': pk
                }
                pk += 1
                music_dict.update(entry)
                #print os.path.dirname(os.path.dirname(os.path.join(root, name)))


#fetch_data()
#print music_dict
