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
from spotify_python_sdk.pydantic.linked_track_object import LinkedTrackObject
from spotify_python_sdk.pydantic.simplified_artist_object import SimplifiedArtistObject
from spotify_python_sdk.pydantic.simplified_track_object_available_markets import SimplifiedTrackObjectAvailableMarkets
from spotify_python_sdk.pydantic.track_restriction_object import TrackRestrictionObject

class SimplifiedTrackObject(BaseModel):
    # The artists who performed the track. Each artist object includes a link in `href` to more detailed information about the artist.
    artists: typing.Optional[typing.List[SimplifiedArtistObject]] = Field(None, alias='artists')

    available_markets: typing.Optional[SimplifiedTrackObjectAvailableMarkets] = Field(None, alias='available_markets')

    # The disc number (usually `1` unless the album consists of more than one disc).
    disc_number: typing.Optional[int] = Field(None, alias='disc_number')

    # The track length in milliseconds.
    duration_ms: typing.Optional[int] = Field(None, alias='duration_ms')

    # Whether or not the track has explicit lyrics ( `true` = yes it does; `false` = no it does not OR unknown).
    explicit: typing.Optional[bool] = Field(None, alias='explicit')

    # External URLs for this track. 
    external_urls: typing.Optional[ExternalUrlObject] = Field(None, alias='external_urls')

    # A link to the Web API endpoint providing full details of the track.
    href: typing.Optional[str] = Field(None, alias='href')

    # The [Spotify ID](/documentation/web-api/concepts/spotify-uris-ids) for the track. 
    id: typing.Optional[str] = Field(None, alias='id')

    # Part of the response when [Track Relinking](/documentation/web-api/concepts/track-relinking/) is applied. If `true`, the track is playable in the given market. Otherwise `false`. 
    is_playable: typing.Optional[bool] = Field(None, alias='is_playable')

    # Part of the response when [Track Relinking](/documentation/web-api/concepts/track-relinking/) is applied and is only part of the response if the track linking, in fact, exists. The requested track has been replaced with a different track. The track in the `linked_from` object contains information about the originally requested track.
    linked_from: typing.Optional[LinkedTrackObject] = Field(None, alias='linked_from')

    # Included in the response when a content restriction is applied. 
    restrictions: typing.Optional[TrackRestrictionObject] = Field(None, alias='restrictions')

    # The name of the track.
    name: typing.Optional[str] = Field(None, alias='name')

    # A URL to a 30 second preview (MP3 format) of the track. 
    preview_url: typing.Optional[typing.Optional[str]] = Field(None, alias='preview_url')

    # The number of the track. If an album has several discs, the track number is the number on the specified disc. 
    track_number: typing.Optional[int] = Field(None, alias='track_number')

    # The object type: \"track\". 
    type: typing.Optional[str] = Field(None, alias='type')

    # The [Spotify URI](/documentation/web-api/concepts/spotify-uris-ids) for the track. 
    uri: typing.Optional[str] = Field(None, alias='uri')

    # Whether or not the track is from a local file. 
    is_local: typing.Optional[bool] = Field(None, alias='is_local')
    class Config:
        arbitrary_types_allowed = True
