import json
import requests
import webbrowser

import config
import refresh_token


class MySpotify:
    def __init__(self):
        self.token = refresh_token.get_refreshed_access_token()
        self.my_spotify_id = config.MY_SPOTIFY_USERNAME
        self.laptop_id = config.SPOTIFY_DEVICE_ID

    def search(self, playback_name: str, playback_type: str):
        pass
