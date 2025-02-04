# coding: utf-8

"""
    Spotify Web API

    You can use Spotify's Web API to discover music and podcasts, manage your Spotify library, control audio playback, and much more. Browse our available Web API endpoints using the sidebar at left, or via the navigation bar on top of this page on smaller screens.  In order to make successful Web API requests your app will need a valid access token. One can be obtained through <a href=\"https://developer.spotify.com/documentation/general/guides/authorization-guide/\">OAuth 2.0</a>.  The base URI for all Web API requests is `https://api.spotify.com/v1`.  Need help? See our <a href=\"https://developer.spotify.com/documentation/web-api/guides/\">Web API guides</a> for more information, or visit the <a href=\"https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer\">Spotify for Developers community forum</a> to ask questions and connect with other developers. 

    The version of the OpenAPI document: 1.0.0
    Created by: https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from spotify_python_sdk import schemas  # noqa: F401


class PlaylistsRemoveItemsRequestTracks(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    An array of objects containing [Spotify URIs](/documentation/web-api/concepts/spotify-uris-ids) of the tracks or episodes to remove.
For example: `{ "tracks": [{ "uri": "spotify:track:4iV5W9uYEdYUVa79Axb7Rh" },{ "uri": "spotify:track:1301WleyT98MSxVHPZCA6M" }] }`. A maximum of 100 objects can be sent at once.

    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['PlaylistsRemoveItemsRequestTracksItem']:
            return PlaylistsRemoveItemsRequestTracksItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['PlaylistsRemoveItemsRequestTracksItem'], typing.List['PlaylistsRemoveItemsRequestTracksItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'PlaylistsRemoveItemsRequestTracks':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'PlaylistsRemoveItemsRequestTracksItem':
        return super().__getitem__(i)

from spotify_python_sdk.model.playlists_remove_items_request_tracks_item import PlaylistsRemoveItemsRequestTracksItem
