from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import sys
import pprint






CLIENT_ID = " CREATE ID FROM :https://developer.spotify.com/dashboard"
CLIENT_SECRET = "CREATE SECRET FROM: https://developer.spotify.com/dashboard"
BILLBOARD_HOT_TOP_100_URL = "https://www.billboard.com/charts/hot-100/"
REDIRECT_URI = "http://example.com"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope="playlist-modify-public"))


date = input("Which year do you want to travel to? type the date in this format 'YYYY-MM-DD':\n")
response = requests.get(url=BILLBOARD_HOT_TOP_100_URL + date)
html_page = response.text
soup = BeautifulSoup(html_page, "html.parser")
music_list = soup.select(selector='li #title-of-a-story')
music_titles = [_.getText().strip() for _ in music_list]
print(music_titles)
#2000-07-28
spotify_music_list = []
for title in music_titles:
    if len(sys.argv) > 1:
        search_str = sys.argv[1]
    else:
        search_str = music_titles[music_titles.index(title)]
        result = sp.search(search_str)
        song_uri = result['tracks']['items'][0]['uri']
        spotify_music_list.append(song_uri)
        print(spotify_music_list)
username = "YOUR USERNAME AT www.spotify.com"
playlist_name = f"{date} Billboard 100"
playlist = sp.user_playlist_create(username, name=playlist_name)
playlist_id = playlist['id']
sp.playlist_add_items(playlist_id=playlist_id,items=spotify_music_list,position=None)


pprint.pprint(result)