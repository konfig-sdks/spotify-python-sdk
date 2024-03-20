# coding: utf-8
"""
    Spotify Web API

    You can use Spotify's Web API to discover music and podcasts, manage your Spotify library, control audio playback, and much more. Browse our available Web API endpoints using the sidebar at left, or via the navigation bar on top of this page on smaller screens.  In order to make successful Web API requests your app will need a valid access token. One can be obtained through <a href=\"https://developer.spotify.com/documentation/general/guides/authorization-guide/\">OAuth 2.0</a>.  The base URI for all Web API requests is `https://api.spotify.com/v1`.  Need help? See our <a href=\"https://developer.spotify.com/documentation/web-api/guides/\">Web API guides</a> for more information, or visit the <a href=\"https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer\">Spotify for Developers community forum</a> to ask questions and connect with other developers. 

    The version of the OpenAPI document: 1.0.0
    Created by: https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer
"""

import typing
import inspect
from datetime import date, datetime
from spotify_python_sdk.client_custom import ClientCustom
from spotify_python_sdk.configuration import Configuration
from spotify_python_sdk.api_client import ApiClient
from spotify_python_sdk.type_util import copy_signature
from spotify_python_sdk.apis.tags.albums_api import AlbumsApi
from spotify_python_sdk.apis.tags.artists_api import ArtistsApi
from spotify_python_sdk.apis.tags.audiobooks_api import AudiobooksApi
from spotify_python_sdk.apis.tags.categories_api import CategoriesApi
from spotify_python_sdk.apis.tags.chapters_api import ChaptersApi
from spotify_python_sdk.apis.tags.episodes_api import EpisodesApi
from spotify_python_sdk.apis.tags.genres_api import GenresApi
from spotify_python_sdk.apis.tags.library_api import LibraryApi
from spotify_python_sdk.apis.tags.markets_api import MarketsApi
from spotify_python_sdk.apis.tags.player_api import PlayerApi
from spotify_python_sdk.apis.tags.playlists_api import PlaylistsApi
from spotify_python_sdk.apis.tags.search_api import SearchApi
from spotify_python_sdk.apis.tags.shows_api import ShowsApi
from spotify_python_sdk.apis.tags.tracks_api import TracksApi
from spotify_python_sdk.apis.tags.users_api import UsersApi



class Spotify(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.albums: AlbumsApi = AlbumsApi(api_client)
        self.artists: ArtistsApi = ArtistsApi(api_client)
        self.audiobooks: AudiobooksApi = AudiobooksApi(api_client)
        self.categories: CategoriesApi = CategoriesApi(api_client)
        self.chapters: ChaptersApi = ChaptersApi(api_client)
        self.episodes: EpisodesApi = EpisodesApi(api_client)
        self.genres: GenresApi = GenresApi(api_client)
        self.library: LibraryApi = LibraryApi(api_client)
        self.markets: MarketsApi = MarketsApi(api_client)
        self.player: PlayerApi = PlayerApi(api_client)
        self.playlists: PlaylistsApi = PlaylistsApi(api_client)
        self.search: SearchApi = SearchApi(api_client)
        self.shows: ShowsApi = ShowsApi(api_client)
        self.tracks: TracksApi = TracksApi(api_client)
        self.users: UsersApi = UsersApi(api_client)
