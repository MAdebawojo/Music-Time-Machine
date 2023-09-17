import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SPOTIPY_CLIENT_ID = os.environ.get('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.environ.get('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = os.environ.get('SPOTIPY_REDIRECT_URI')
END_POINT = 'https://api.spotify.com/v1/search'

# print(SPOTIPY_REDIRECT_URI)
print(SPOTIPY_CLIENT_ID)
# print(SPOTIPY_CLIENT_ID)

# ---------------Web Scraping of Songs Predicated on the Date Given by the User ------------------------------
year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")
url = f"https://www.billboard.com/charts/hot-100/{year}/"

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")
# print(soup.title)

markup_titles = soup.select(selector=".o-chart-results-list__item h3")
artists_html = soup.select(selector=".o-chart-results-list__item span")

#scrapes artists
artists = [artist.getText() for artist in artists_html]
artist_list = [artist.replace('\n', '').replace('\t', '') for artist in artists] #cleans the list
# print(artist_list)

song_titles = [markup_title.getText() for markup_title in markup_titles]
# cleaned list removes the \n and \t escape sequence from the extracted song titles
cleaned_list = [item.replace('\n', '').replace('\t', '') for item in song_titles]
# print(cleaned_list)
# #------------------------------End of Scraping------------------------------------------------------
#Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)

#Searching Spotify for songs by title
song_uris = []
for index in range(len(cleaned_list)):
    result = sp.search(q=f"track:{cleaned_list[index]} artist:{artist_list[index]}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{cleaned_list[index]} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{year} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)



