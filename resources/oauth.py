import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_saved_tracks(limit=5,offset=618,market='US')
print(results)
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx+1, track['artists'][0]['name'], " – ", track['name'])