import time
import os
import json

from syncedlyrics import search

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opts = Options()
opts.headless = True
driver = Chrome(options=opts)

url = "https://music.apple.com/eg/playlist/zaid/pl.u-GgA5kl6coG9yXe2"

driver.get(url)

time.sleep(5)

songs = driver.find_elements(By.CSS_SELECTOR, ".songs-list-row")

for song in songs:
    title = song.find_element(By.CSS_SELECTOR, ".songs-list-row__song-name").text
    author = song.find_element(By.CSS_SELECTOR, ".songs-list-row__by-line").text
    dir_ = f"{title} - {author}"
    lyrics = search(dir_)

    song_url_element = song.find_element(By.CSS_SELECTOR, "a")  # Adjust if needed
    song_url = song_url_element.get_attribute("href") if song_url_element else "No URL"

    if not os.path.isdir(dir_):
        os.mkdir(dir_)
    with open("./" + dir_ + "/data.json", "w+", encoding="utf-8") as f:
        f.write(
            json.dumps(
                {
                    "title": title,
                    "author": author,
                    "song_url": song_url,
                    "lyrics": lyrics,
                },
                indent=2,
                ensure_ascii=False,
            )
        )


driver.quit()
