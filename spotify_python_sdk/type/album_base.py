# coding: utf-8

"""
    Spotify Web API

    You can use Spotify's Web API to discover music and podcasts, manage your Spotify library, control audio playback, and much more. Browse our available Web API endpoints using the sidebar at left, or via the navigation bar on top of this page on smaller screens.  In order to make successful Web API requests your app will need a valid access token. One can be obtained through <a href=\"https://developer.spotify.com/documentation/general/guides/authorization-guide/\">OAuth 2.0</a>.  The base URI for all Web API requests is `https://api.spotify.com/v1`.  Need help? See our <a href=\"https://developer.spotify.com/documentation/web-api/guides/\">Web API guides</a> for more information, or visit the <a href=\"https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer\">Spotify for Developers community forum</a> to ask questions and connect with other developers. 

    The version of the OpenAPI document: 1.0.0
    Created by: https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from spotify_python_sdk.type.album_base_available_markets import AlbumBaseAvailableMarkets
from spotify_python_sdk.type.album_restriction_object import AlbumRestrictionObject
from spotify_python_sdk.type.external_url_object import ExternalUrlObject
from spotify_python_sdk.type.image_object import ImageObject

class RequiredAlbumBase(TypedDict):
    # The type of the album. 
    album_type: str

    # The number of tracks in the album.
    total_tracks: int

    available_markets: AlbumBaseAvailableMarkets

    # Known external URLs for this album. 
    external_urls: ExternalUrlObject

    # A link to the Web API endpoint providing full details of the album. 
    href: str

    # The [Spotify ID](/documentation/web-api/concepts/spotify-uris-ids) for the album. 
    id: str

    # The cover art for the album in various sizes, widest first. 
    images: typing.List[ImageObject]

    # The name of the album. In case of an album takedown, the value may be an empty string. 
    name: str

    # The date the album was first released. 
    release_date: str

    # The precision with which `release_date` value is known. 
    release_date_precision: str

    # The object type. 
    type: str

    # The [Spotify URI](/documentation/web-api/concepts/spotify-uris-ids) for the album. 
    uri: str

class OptionalAlbumBase(TypedDict, total=False):
    # Included in the response when a content restriction is applied. 
    restrictions: AlbumRestrictionObject

class AlbumBase(RequiredAlbumBase, OptionalAlbumBase):
    pass
