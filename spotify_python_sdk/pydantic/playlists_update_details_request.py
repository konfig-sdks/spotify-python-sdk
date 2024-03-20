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


class PlaylistsUpdateDetailsRequest(BaseModel):
    # Value for playlist description as displayed in Spotify Clients and in the Web API. 
    description: typing.Optional[str] = Field(None, alias='description')

    # The new name for the playlist, for example `\"My New Playlist Title\"` 
    name: typing.Optional[str] = Field(None, alias='name')

    # If `true` the playlist will be public, if `false` it will be private. 
    public: typing.Optional[bool] = Field(None, alias='public')

    # If `true`, the playlist will become collaborative and other users will be able to modify the playlist in their Spotify client. <br/> _**Note**: You can only set `collaborative` to `true` on non-public playlists._ 
    collaborative: typing.Optional[bool] = Field(None, alias='collaborative')
    class Config:
        arbitrary_types_allowed = True
