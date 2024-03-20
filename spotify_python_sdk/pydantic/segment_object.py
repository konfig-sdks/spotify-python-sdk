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

from spotify_python_sdk.pydantic.segment_object_pitches import SegmentObjectPitches
from spotify_python_sdk.pydantic.segment_object_timbre import SegmentObjectTimbre

class SegmentObject(BaseModel):
    # The starting point (in seconds) of the segment.
    start: typing.Optional[typing.Union[int, float]] = Field(None, alias='start')

    # The duration (in seconds) of the segment.
    duration: typing.Optional[typing.Union[int, float]] = Field(None, alias='duration')

    # The confidence, from 0.0 to 1.0, of the reliability of the segmentation. Segments of the song which are difficult to logically segment (e.g: noise) may correspond to low values in this field. 
    confidence: typing.Optional[typing.Union[int, float]] = Field(None, alias='confidence')

    # The onset loudness of the segment in decibels (dB). Combined with `loudness_max` and `loudness_max_time`, these components can be used to describe the \"attack\" of the segment.
    loudness_start: typing.Optional[typing.Union[int, float]] = Field(None, alias='loudness_start')

    # The peak loudness of the segment in decibels (dB). Combined with `loudness_start` and `loudness_max_time`, these components can be used to describe the \"attack\" of the segment.
    loudness_max: typing.Optional[typing.Union[int, float]] = Field(None, alias='loudness_max')

    # The segment-relative offset of the segment peak loudness in seconds. Combined with `loudness_start` and `loudness_max`, these components can be used to desctibe the \"attack\" of the segment.
    loudness_max_time: typing.Optional[typing.Union[int, float]] = Field(None, alias='loudness_max_time')

    # The offset loudness of the segment in decibels (dB). This value should be equivalent to the loudness_start of the following segment.
    loudness_end: typing.Optional[typing.Union[int, float]] = Field(None, alias='loudness_end')

    pitches: typing.Optional[SegmentObjectPitches] = Field(None, alias='pitches')

    timbre: typing.Optional[SegmentObjectTimbre] = Field(None, alias='timbre')
    class Config:
        arbitrary_types_allowed = True
