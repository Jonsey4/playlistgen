import spotipy
from spotipy.oauth2 import SpotifyOAuth

def connect(scopes):
    """Def: autorize the user, return api client for requests"""
    return spotipy.Spotify(auth_manager=SpotifyOAuth(scope = scopes))

def get_track_info(item):
    return {'name': item['track']['name'], 
                'url': item['track']['external_urls']['spotify'],
                'id': item['track']['id']}

def resolve_tracks(cred, result):
    for i in result['items']: yield get_track_info(i)
        
    while result['next']: 
        result = cred.next(result)
        for i in result['items']: yield get_track_info(i)



# Polling to trigger a refresh of the data
    # Poll the list of saved tracks at the previously determined "last track" to see if it still has no "next" page
        # Then just start the first request at that number 
        #alternatively, just have that trigger a full refresh of the data 