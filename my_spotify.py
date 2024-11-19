import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pyautogui
import webbrowser
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import psutil

import config
import refresh_token


def track_control(command: str):
    if command == 'next':
        pyautogui.press('nexttrack')
    elif command == 'previous':
        pyautogui.press('prevtrack')


def play_and_pause():
    if 'Spotify.exe' in (p.name() for p in psutil.process_iter()):
        pyautogui.press('playpause')
        return True
    return False


def play(url: str):
    webbrowser.open(url)
    time.sleep(1.0)
    pyautogui.press('enter')


# volume control
def set_volume(percent: int):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(percent / 100, None)


class MySpotify:
    def __init__(self):
        self.oauth_object = SpotifyOAuth(
            client_id=config.SPOTIFY_CLIENT_ID,
            client_secret=config.SPOTIFY_CLIENT_SECRET,
            redirect_uri=config.REDIRECT_URI
        )
        self.token = refresh_token.get_refreshed_access_token()
        self.spotify = spotipy.Spotify(auth=self.token)

    def get_song_uri(self, song_name: str) -> str:
        result = self.spotify.search(q=song_name, limit=1, type='track')

        if not result['tracks']['items']:
            raise Exception(f'Could not find the song named {song_name}')
        song_uri = result['tracks']['items'][0]['uri']
        return song_uri

    def get_album_uri(self, album_name: str) -> str:
        result = self.spotify.search(q=album_name, limit=1, type='album')

        if not result['albums']['items']:
            raise Exception(f'Could not find the album named {album_name}')
        album_uri = result['albums']['items'][0]['uri']
        return album_uri

    def get_artist_uri(self, artist_name: str) -> str:
        result = self.spotify.search(q=artist_name, limit=1, type='artist')

        if not result['artists']['items']:
            raise Exception(f'Could not find the artist named {artist_name}')
        artist_uri = result['artists']['items'][0]['uri']
        return artist_uri
