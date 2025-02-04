# coding: utf-8

"""
    Spotify Web API

    You can use Spotify's Web API to discover music and podcasts, manage your Spotify library, control audio playback, and much more. Browse our available Web API endpoints using the sidebar at left, or via the navigation bar on top of this page on smaller screens.  In order to make successful Web API requests your app will need a valid access token. One can be obtained through <a href=\"https://developer.spotify.com/documentation/general/guides/authorization-guide/\">OAuth 2.0</a>.  The base URI for all Web API requests is `https://api.spotify.com/v1`.  Need help? See our <a href=\"https://developer.spotify.com/documentation/web-api/guides/\">Web API guides</a> for more information, or visit the <a href=\"https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer\">Spotify for Developers community forum</a> to ask questions and connect with other developers. 

    The version of the OpenAPI document: 1.0.0
    Created by: https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer
"""

from spotify_python_sdk.paths.me_albums_contains.get import CheckSaved
from spotify_python_sdk.paths.artists_id_albums.get import GetAlbumsById
from spotify_python_sdk.paths.albums_id.get import GetInformation
from spotify_python_sdk.paths.browse_new_releases.get import GetNewReleases
from spotify_python_sdk.paths.me_albums.get import GetSaved
from spotify_python_sdk.paths.albums_id_tracks.get import GetTracksById
from spotify_python_sdk.paths.albums.get import ListSeveral
from spotify_python_sdk.paths.me_albums.delete import RemoveSaved
from spotify_python_sdk.paths.me_albums.put import SaveCurrentUserLibrary
from spotify_python_sdk.apis.tags.albums_api_raw import AlbumsApiRaw


class AlbumsApi(
    CheckSaved,
    GetAlbumsById,
    GetInformation,
    GetNewReleases,
    GetSaved,
    GetTracksById,
    ListSeveral,
    RemoveSaved,
    SaveCurrentUserLibrary,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: AlbumsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = AlbumsApiRaw(api_client)
