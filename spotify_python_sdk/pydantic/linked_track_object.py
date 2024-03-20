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

from spotify_python_sdk.pydantic.external_url_object import ExternalUrlObject

class LinkedTrackObject(BaseModel):
    # Known external URLs for this track. 
    external_urls: typing.Optional[ExternalUrlObject] = Field(None, alias='external_urls')

    # A link to the Web API endpoint providing full details of the track. 
    href: typing.Optional[str] = Field(None, alias='href')

    # The [Spotify ID](/documentation/web-api/concepts/spotify-uris-ids) for the track. 
    id: typing.Optional[str] = Field(None, alias='id')

    # The object type: \"track\". 
    type: typing.Optional[str] = Field(None, alias='type')

    # The [Spotify URI](/documentation/web-api/concepts/spotify-uris-ids) for the track. 
    uri: typing.Optional[str] = Field(None, alias='uri')
    class Config:
        arbitrary_types_allowed = True
