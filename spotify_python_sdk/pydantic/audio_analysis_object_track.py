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

from spotify_python_sdk.pydantic.key import Key
from spotify_python_sdk.pydantic.time_signature import TimeSignature

class AudioAnalysisObjectTrack(BaseModel):
    # The exact number of audio samples analyzed from this track. See also `analysis_sample_rate`.
    num_samples: typing.Optional[int] = Field(None, alias='num_samples')

    # Length of the track in seconds.
    duration: typing.Optional[typing.Union[int, float]] = Field(None, alias='duration')

    # This field will always contain the empty string.
    sample_md5: typing.Optional[str] = Field(None, alias='sample_md5')

    # An offset to the start of the region of the track that was analyzed. (As the entire track is analyzed, this should always be 0.)
    offset_seconds: typing.Optional[int] = Field(None, alias='offset_seconds')

    # The length of the region of the track was analyzed, if a subset of the track was analyzed. (As the entire track is analyzed, this should always be 0.)
    window_seconds: typing.Optional[int] = Field(None, alias='window_seconds')

    # The sample rate used to decode and analyze this track. May differ from the actual sample rate of this track available on Spotify.
    analysis_sample_rate: typing.Optional[int] = Field(None, alias='analysis_sample_rate')

    # The number of channels used for analysis. If 1, all channels are summed together to mono before analysis.
    analysis_channels: typing.Optional[int] = Field(None, alias='analysis_channels')

    # The time, in seconds, at which the track's fade-in period ends. If the track has no fade-in, this will be 0.0.
    end_of_fade_in: typing.Optional[typing.Union[int, float]] = Field(None, alias='end_of_fade_in')

    # The time, in seconds, at which the track's fade-out period starts. If the track has no fade-out, this should match the track's length.
    start_of_fade_out: typing.Optional[typing.Union[int, float]] = Field(None, alias='start_of_fade_out')

    # The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing relative loudness of tracks. Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude). Values typically range between -60 and 0 db. 
    loudness: typing.Optional[typing.Union[int, float]] = Field(None, alias='loudness')

    # The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration. 
    tempo: typing.Optional[typing.Union[int, float]] = Field(None, alias='tempo')

    # The confidence, from 0.0 to 1.0, of the reliability of the `tempo`.
    tempo_confidence: typing.Optional[typing.Union[int, float]] = Field(None, alias='tempo_confidence')

    time_signature: typing.Optional[TimeSignature] = Field(None, alias='time_signature')

    # The confidence, from 0.0 to 1.0, of the reliability of the `time_signature`.
    time_signature_confidence: typing.Optional[typing.Union[int, float]] = Field(None, alias='time_signature_confidence')

    key: typing.Optional[Key] = Field(None, alias='key')

    # The confidence, from 0.0 to 1.0, of the reliability of the `key`.
    key_confidence: typing.Optional[typing.Union[int, float]] = Field(None, alias='key_confidence')

    # Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived. Major is represented by 1 and minor is 0. 
    mode: typing.Optional[int] = Field(None, alias='mode')

    # The confidence, from 0.0 to 1.0, of the reliability of the `mode`.
    mode_confidence: typing.Optional[typing.Union[int, float]] = Field(None, alias='mode_confidence')

    # An [Echo Nest Musical Fingerprint (ENMFP)](https://academiccommons.columbia.edu/doi/10.7916/D8Q248M4) codestring for this track.
    codestring: typing.Optional[str] = Field(None, alias='codestring')

    # A version number for the Echo Nest Musical Fingerprint format used in the codestring field.
    code_version: typing.Optional[typing.Union[int, float]] = Field(None, alias='code_version')

    # An [EchoPrint](https://github.com/spotify/echoprint-codegen) codestring for this track.
    echoprintstring: typing.Optional[str] = Field(None, alias='echoprintstring')

    # A version number for the EchoPrint format used in the echoprintstring field.
    echoprint_version: typing.Optional[typing.Union[int, float]] = Field(None, alias='echoprint_version')

    # A [Synchstring](https://github.com/echonest/synchdata) for this track.
    synchstring: typing.Optional[str] = Field(None, alias='synchstring')

    # A version number for the Synchstring used in the synchstring field.
    synch_version: typing.Optional[typing.Union[int, float]] = Field(None, alias='synch_version')

    # A Rhythmstring for this track. The format of this string is similar to the Synchstring.
    rhythmstring: typing.Optional[str] = Field(None, alias='rhythmstring')

    # A version number for the Rhythmstring used in the rhythmstring field.
    rhythm_version: typing.Optional[typing.Union[int, float]] = Field(None, alias='rhythm_version')
    class Config:
        arbitrary_types_allowed = True
