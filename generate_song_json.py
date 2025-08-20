import os
import json

# 配置
music_dir = "music"   # 音乐文件夹路径
output_file = os.path.join(music_dir, "song.json")

# 支持的音频格式
supported_ext = [".mp3", ".flac", ".wav", ".ogg", ".m4a"]

songs = []

# 扫描文件夹
for file in os.listdir(music_dir):
    ext = os.path.splitext(file)[1].lower()
    if ext in supported_ext:
        name = os.path.splitext(file)[0]
        songs.append({
            "name": name,
            "artist": "未知艺术家",
            "cover": "",
            "file": file
        })

# 保存为 JSON
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(songs, f, ensure_ascii=False, indent=2)

print(f"✅ 成功生成 {output_file}，共 {len(songs)} 首歌")
