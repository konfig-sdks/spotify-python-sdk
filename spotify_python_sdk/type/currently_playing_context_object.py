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

from spotify_python_sdk.type.context_object import ContextObject
from spotify_python_sdk.type.device_object import DeviceObject
from spotify_python_sdk.type.disallows_object import DisallowsObject
from spotify_python_sdk.type.episode_object import EpisodeObject
from spotify_python_sdk.type.track_object import TrackObject

class RequiredCurrentlyPlayingContextObject(TypedDict):
    pass

class OptionalCurrentlyPlayingContextObject(TypedDict, total=False):
    # The device that is currently active. 
    device: DeviceObject

    # off, track, context
    repeat_state: str

    # If shuffle is on or off.
    shuffle_state: bool

    # A Context Object. Can be `null`.
    context: ContextObject

    # Unix Millisecond Timestamp when data was fetched.
    timestamp: int

    # Progress into the currently playing track or episode. Can be `null`.
    progress_ms: int

    # If something is currently playing, return `true`.
    is_playing: bool

    # The currently playing track or episode. Can be `null`.
    item: typing.Union[TrackObject, EpisodeObject]

    # The object type of the currently playing item. Can be one of `track`, `episode`, `ad` or `unknown`. 
    currently_playing_type: str

    # Allows to update the user interface based on which playback actions are available within the current context. 
    actions: DisallowsObject

class CurrentlyPlayingContextObject(RequiredCurrentlyPlayingContextObject, OptionalCurrentlyPlayingContextObject):
    pass
