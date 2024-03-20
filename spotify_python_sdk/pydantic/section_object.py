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

from spotify_python_sdk.pydantic.time_signature import TimeSignature

class SectionObject(BaseModel):
    # The starting point (in seconds) of the section.
    start: typing.Optional[typing.Union[int, float]] = Field(None, alias='start')

    # The duration (in seconds) of the section.
    duration: typing.Optional[typing.Union[int, float]] = Field(None, alias='duration')

    # The confidence, from 0.0 to 1.0, of the reliability of the section's \"designation\".
    confidence: typing.Optional[typing.Union[int, float]] = Field(None, alias='confidence')

    # The overall loudness of the section in decibels (dB). Loudness values are useful for comparing relative loudness of sections within tracks.
    loudness: typing.Optional[typing.Union[int, float]] = Field(None, alias='loudness')

    # The overall estimated tempo of the section in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration.
    tempo: typing.Optional[typing.Union[int, float]] = Field(None, alias='tempo')

    # The confidence, from 0.0 to 1.0, of the reliability of the tempo. Some tracks contain tempo changes or sounds which don't contain tempo (like pure speech) which would correspond to a low value in this field.
    tempo_confidence: typing.Optional[typing.Union[int, float]] = Field(None, alias='tempo_confidence')

    # The estimated overall key of the section. The values in this field ranging from 0 to 11 mapping to pitches using standard Pitch Class notation (E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on). If no key was detected, the value is -1.
    key: typing.Optional[int] = Field(None, alias='key')

    # The confidence, from 0.0 to 1.0, of the reliability of the key. Songs with many key changes may correspond to low values in this field.
    key_confidence: typing.Optional[typing.Union[int, float]] = Field(None, alias='key_confidence')

    # Indicates the modality (major or minor) of a section, the type of scale from which its melodic content is derived. This field will contain a 0 for \"minor\", a 1 for \"major\", or a -1 for no result. Note that the major key (e.g. C major) could more likely be confused with the minor key at 3 semitones lower (e.g. A minor) as both keys carry the same pitches.
    mode: typing.Optional[Literal[-1, 0, 1]] = Field(None, alias='mode')

    # The confidence, from 0.0 to 1.0, of the reliability of the `mode`.
    mode_confidence: typing.Optional[typing.Union[int, float]] = Field(None, alias='mode_confidence')

    time_signature: typing.Optional[TimeSignature] = Field(None, alias='time_signature')

    # The confidence, from 0.0 to 1.0, of the reliability of the `time_signature`. Sections with time signature changes may correspond to low values in this field.
    time_signature_confidence: typing.Optional[typing.Union[int, float]] = Field(None, alias='time_signature_confidence')
    class Config:
        arbitrary_types_allowed = True
