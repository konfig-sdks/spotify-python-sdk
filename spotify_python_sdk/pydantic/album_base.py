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
from pydantic import BaseModel, Field, RootModel

from spotify_python_sdk.pydantic.album_base_available_markets import AlbumBaseAvailableMarkets
from spotify_python_sdk.pydantic.album_restriction_object import AlbumRestrictionObject
from spotify_python_sdk.pydantic.external_url_object import ExternalUrlObject
from spotify_python_sdk.pydantic.image_object import ImageObject

class AlbumBase(BaseModel):
    # The type of the album. 
    album_type: Literal["album", "single", "compilation"] = Field(alias='album_type')

    # The number of tracks in the album.
    total_tracks: int = Field(alias='total_tracks')

    available_markets: AlbumBaseAvailableMarkets = Field(alias='available_markets')

    # Known external URLs for this album. 
    external_urls: ExternalUrlObject = Field(alias='external_urls')

    # A link to the Web API endpoint providing full details of the album. 
    href: str = Field(alias='href')

    # The [Spotify ID](/documentation/web-api/concepts/spotify-uris-ids) for the album. 
    id: str = Field(alias='id')

    # The cover art for the album in various sizes, widest first. 
    images: typing.List[ImageObject] = Field(alias='images')

    # The name of the album. In case of an album takedown, the value may be an empty string. 
    name: str = Field(alias='name')

    # The date the album was first released. 
    release_date: str = Field(alias='release_date')

    # The precision with which `release_date` value is known. 
    release_date_precision: Literal["year", "month", "day"] = Field(alias='release_date_precision')

    # The object type. 
    type: Literal["album"] = Field(alias='type')

    # The [Spotify URI](/documentation/web-api/concepts/spotify-uris-ids) for the album. 
    uri: str = Field(alias='uri')

    # Included in the response when a content restriction is applied. 
    restrictions: typing.Optional[AlbumRestrictionObject] = Field(None, alias='restrictions')
    class Config:
        arbitrary_types_allowed = True
