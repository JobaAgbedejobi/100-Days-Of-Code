from bs4 import BeautifulSoup
import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

date = input("What year would you like to travel to? Type the date in this format: "
             "YYYY-MM-DD\n")
year = date.split("-")[0]

header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 "
                        "Safari/537.36"}

URL = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(URL, headers=header)
website = BeautifulSoup(response.text, "html.parser")
songs = website.select("li ul li h3")

billboard = [song.getText().strip() for song in songs]

scope = "playlist-modify-private"
client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                client_secret=client_secret, redirect_uri=redirect_uri, scope=scope,
                                               username="Joba", show_dialog=True,
                                                cache_path=".cache-Joba"))


uris = []
for song in billboard:
    result = sp.search(q=f"track:{song} year:{year}", type="track", limit=1)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        uris.append(uri)
    except IndexError:
        print(f"Song: '{song}' is not on Spotify so it'll be skipped.")
user_id = sp.current_user()["id"]
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100",
                                   public=False, collaborative=False,
                                   description=f"Top 100 songs in the week of: {date}")
playlist_id = playlist["id"]
sp.playlist_add_items(playlist_id, uris)

# FOR SOME REASON, I CAN'T CREATE A PRIVATE PLAYLIST - MUST BE AN ERROR WITH SPOTIFY
import time
time.sleep(1)
# Can delete lines 49 onwards if I can't fix this issue later
# Then make it private
sp.playlist_change_details(
    playlist_id=playlist_id,
    public=False
)

# Verify the change
updated_playlist = sp.playlist(playlist_id, fields="public")
print(f"Playlist public status: {updated_playlist['public']}")
# 2016-11-12
