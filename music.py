import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# ⚡ YOUR SPOTIFY KEYS HERE
client_id = 'c86e51255d5e4197ac80c0d488e1a1ec'
client_secret = '3c81bd48b0444b079d4fb67d2254b434'

# Authenticate
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

def search_song(song_name):
    result = sp.search(q=song_name, type='track', limit=5)
    tracks = result['tracks']['items']
    songs_list = []
    for track in tracks:
        song_info = {
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'url': track['external_urls']['spotify'],
            'image': track['album']['images'][0]['url']
        }
        songs_list.append(song_info)
    return songs_list
