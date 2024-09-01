import os
from ytmusicapi import YTMusic

ytm = YTMusic()

for i in os.listdir():
    if "-" in i:
        video = ytm.search(i, filter="songs", limit=1)[0]

        with open(i + "/README.md", "w+", encoding="utf-8") as f:
            f.write(f"## Listen to {video['title']}\n")
            f.write(
                f"- YTMusic: [Click here](https://music.youtube.com/watch?v={video['videoId']})"
            )
