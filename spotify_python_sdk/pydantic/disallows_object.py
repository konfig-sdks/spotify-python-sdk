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


class DisallowsObject(BaseModel):
    # Interrupting playback. Optional field.
    interrupting_playback: typing.Optional[bool] = Field(None, alias='interrupting_playback')

    # Pausing. Optional field.
    pausing: typing.Optional[bool] = Field(None, alias='pausing')

    # Resuming. Optional field.
    resuming: typing.Optional[bool] = Field(None, alias='resuming')

    # Seeking playback location. Optional field.
    seeking: typing.Optional[bool] = Field(None, alias='seeking')

    # Skipping to the next context. Optional field.
    skipping_next: typing.Optional[bool] = Field(None, alias='skipping_next')

    # Skipping to the previous context. Optional field.
    skipping_prev: typing.Optional[bool] = Field(None, alias='skipping_prev')

    # Toggling repeat context flag. Optional field.
    toggling_repeat_context: typing.Optional[bool] = Field(None, alias='toggling_repeat_context')

    # Toggling shuffle flag. Optional field.
    toggling_shuffle: typing.Optional[bool] = Field(None, alias='toggling_shuffle')

    # Toggling repeat track flag. Optional field.
    toggling_repeat_track: typing.Optional[bool] = Field(None, alias='toggling_repeat_track')

    # Transfering playback between devices. Optional field.
    transferring_playback: typing.Optional[bool] = Field(None, alias='transferring_playback')
    class Config:
        arbitrary_types_allowed = True
