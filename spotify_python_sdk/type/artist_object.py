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

from spotify_python_sdk.type.artist_object_genres import ArtistObjectGenres
from spotify_python_sdk.type.external_url_object import ExternalUrlObject
from spotify_python_sdk.type.followers_object import FollowersObject
from spotify_python_sdk.type.image_object import ImageObject

class RequiredArtistObject(TypedDict):
    pass

class OptionalArtistObject(TypedDict, total=False):
    # Known external URLs for this artist. 
    external_urls: ExternalUrlObject

    # Information about the followers of the artist. 
    followers: FollowersObject

    genres: ArtistObjectGenres

    # A link to the Web API endpoint providing full details of the artist. 
    href: str

    # The [Spotify ID](/documentation/web-api/concepts/spotify-uris-ids) for the artist. 
    id: str

    # Images of the artist in various sizes, widest first. 
    images: typing.List[ImageObject]

    # The name of the artist. 
    name: str

    # The popularity of the artist. The value will be between 0 and 100, with 100 being the most popular. The artist's popularity is calculated from the popularity of all the artist's tracks. 
    popularity: int

    # The object type. 
    type: str

    # The [Spotify URI](/documentation/web-api/concepts/spotify-uris-ids) for the artist. 
    uri: str

class ArtistObject(RequiredArtistObject, OptionalArtistObject):
    pass
