import os
import json

music_dir = os.path.join(os.path.dirname(__file__), 'music')
output_file = os.path.join(os.path.dirname(__file__), './music/song.json')
exts = ['.mp3', '.ogg', '.flac', '.wav', '.m4a']

def parse_file_name(file):
    base = os.path.splitext(file)[0]
    name = base
    artist = 'artist'
    if ' - ' in base:
        artist, name = base.split(' - ', 1)
        artist = artist.strip()
        name = name.strip()
    elif '_' in base:
        idx = base.rfind('_')
        name = base[:idx].strip()
        artist = base[idx+1:].strip()
    return {"name": name, "artist": artist, "file": file}

files = [f for f in os.listdir(music_dir) if os.path.splitext(f)[1].lower() in exts]
song_list = [parse_file_name(f) for f in files]

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(song_list, f, ensure_ascii=False, indent=4)

print(f'song.json 已生成，共 {len(song_list)} 首')