# coding: utf-8

"""
    Spotify Web API

    You can use Spotify's Web API to discover music and podcasts, manage your Spotify library, control audio playback, and much more. Browse our available Web API endpoints using the sidebar at left, or via the navigation bar on top of this page on smaller screens.  In order to make successful Web API requests your app will need a valid access token. One can be obtained through <a href=\"https://developer.spotify.com/documentation/general/guides/authorization-guide/\">OAuth 2.0</a>.  The base URI for all Web API requests is `https://api.spotify.com/v1`.  Need help? See our <a href=\"https://developer.spotify.com/documentation/web-api/guides/\">Web API guides</a> for more information, or visit the <a href=\"https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer\">Spotify for Developers community forum</a> to ask questions and connect with other developers. 

    The version of the OpenAPI document: 1.0.0
    Created by: https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer
"""

from spotify_python_sdk.paths.me_audiobooks_contains.get import CheckUserSaved
from spotify_python_sdk.paths.audiobooks_id.get import GetCatalogInfo
from spotify_python_sdk.paths.audiobooks_id_chapters.get import GetChaptersById
from spotify_python_sdk.paths.audiobooks.get import GetSeveral
from spotify_python_sdk.paths.me_audiobooks.get import ListSaved
from spotify_python_sdk.paths.me_audiobooks.delete import RemoveFromLibrary
from spotify_python_sdk.paths.me_audiobooks.put import SaveCurrentUserLibrary
from spotify_python_sdk.apis.tags.audiobooks_api_raw import AudiobooksApiRaw


class AudiobooksApi(
    CheckUserSaved,
    GetCatalogInfo,
    GetChaptersById,
    GetSeveral,
    ListSaved,
    RemoveFromLibrary,
    SaveCurrentUserLibrary,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: AudiobooksApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = AudiobooksApiRaw(api_client)
