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

from spotify_python_sdk.pydantic.cursor_object import CursorObject

class CursorPagingObject(BaseModel):
    # A link to the Web API endpoint returning the full result of the request.
    href: typing.Optional[str] = Field(None, alias='href')

    # The maximum number of items in the response (as set in the query or by default).
    limit: typing.Optional[int] = Field(None, alias='limit')

    # URL to the next page of items. ( `null` if none)
    next: typing.Optional[str] = Field(None, alias='next')

    # The cursors used to find the next set of items.
    cursors: typing.Optional[CursorObject] = Field(None, alias='cursors')

    # The total number of items available to return.
    total: typing.Optional[int] = Field(None, alias='total')
    class Config:
        arbitrary_types_allowed = True
