import os
from eyed3.id3 import Tag

env = os.environ['HOME']

if 'nick' in env:
    music_dir = '/Users/nick/Music/iTunes/iTunes Media/Music/'
else:
    music_dir = '/mnt/seagatehd/Music'

tag = Tag()
music_dict = {}

def fetch_data():
    pk=1
    for root,dirs,files in os.walk(music_dir):
        for name in files:
            if name.endswith('.mp3'):
                full_path = os.path.join(root,name)
                tag.parse(full_path)
                entry = {}
                entry[pk] = {
                    'title': tag._getTitle(),
                    'artist': tag._getArtist(),
                    'album': tag._getAlbum(),
                    'path': full_path.replace("/Users/nick/Music/iTunes/iTunes Media/Music/","static/music/"),
                    'pk': pk
                }
                pk += 1
                music_dict.update(entry)
                #tag.parse(full_path)
                #print os.path.dirname(os.path.dirname(os.path.join(root, name)))

fetch_data()
#print music_dict
