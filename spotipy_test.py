import spotipy
import spotipy.util as util
import yaml

CLIENT_ID = ''
CLIENT_SECRET = ''
MR_ROBOTO = ["spotify:track:7C0rG4oWO7VeZcffyW1sK9", "spotify:track:5fpizYGbi5IQoEraj6FP0R", "spotify:track:439TlnnznSiBbQbgXiBqAd", "spotify:track:7h2yhVxcZOGyQdOwD4Hu8J"]
SCOPE = 'user-modify-playback-state'
USERNAME = ''

with open(r'./spotify.yaml') as file:
    CREDENTIALS_LIST = yaml.load(file, Loader=yaml.FullLoader)
    CLIENT_ID = CREDENTIALS_LIST['CLIENT_ID']
    CLIENT_SECRET = CREDENTIALS_LIST['CLIENT_SECRET']
    USERNAME = CREDENTIALS_LIST['USERNAME']

TOKEN = util.prompt_for_user_token(USERNAME, SCOPE, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri="http://localhost:8888/callback")
if TOKEN:
    SP = spotipy.Spotify(auth=TOKEN)
    SP.start_playback(uris=MR_ROBOTO)
else:
    print("Can't get token for", USERNAME)
