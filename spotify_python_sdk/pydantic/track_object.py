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

from spotify_python_sdk.pydantic.artist_object import ArtistObject
from spotify_python_sdk.pydantic.external_id_object import ExternalIdObject
from spotify_python_sdk.pydantic.external_url_object import ExternalUrlObject
from spotify_python_sdk.pydantic.simplified_album_object import SimplifiedAlbumObject
from spotify_python_sdk.pydantic.track_object_available_markets import TrackObjectAvailableMarkets
from spotify_python_sdk.pydantic.track_restriction_object import TrackRestrictionObject

class TrackObject(BaseModel):
    # The album on which the track appears. The album object includes a link in `href` to full information about the album. 
    album: typing.Optional[SimplifiedAlbumObject] = Field(None, alias='album')

    # The artists who performed the track. Each artist object includes a link in `href` to more detailed information about the artist. 
    artists: typing.Optional[typing.List[ArtistObject]] = Field(None, alias='artists')

    available_markets: typing.Optional[TrackObjectAvailableMarkets] = Field(None, alias='available_markets')

    # The disc number (usually `1` unless the album consists of more than one disc). 
    disc_number: typing.Optional[int] = Field(None, alias='disc_number')

    # The track length in milliseconds. 
    duration_ms: typing.Optional[int] = Field(None, alias='duration_ms')

    # Whether or not the track has explicit lyrics ( `true` = yes it does; `false` = no it does not OR unknown). 
    explicit: typing.Optional[bool] = Field(None, alias='explicit')

    # Known external IDs for the track. 
    external_ids: typing.Optional[ExternalIdObject] = Field(None, alias='external_ids')

    # Known external URLs for this track. 
    external_urls: typing.Optional[ExternalUrlObject] = Field(None, alias='external_urls')

    # A link to the Web API endpoint providing full details of the track. 
    href: typing.Optional[str] = Field(None, alias='href')

    # The [Spotify ID](/documentation/web-api/concepts/spotify-uris-ids) for the track. 
    id: typing.Optional[str] = Field(None, alias='id')

    # Part of the response when [Track Relinking](/documentation/web-api/concepts/track-relinking) is applied. If `true`, the track is playable in the given market. Otherwise `false`. 
    is_playable: typing.Optional[bool] = Field(None, alias='is_playable')

    # Part of the response when [Track Relinking](/documentation/web-api/concepts/track-relinking) is applied, and the requested track has been replaced with different track. The track in the `linked_from` object contains information about the originally requested track. 
    linked_from: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='linked_from')

    # Included in the response when a content restriction is applied. 
    restrictions: typing.Optional[TrackRestrictionObject] = Field(None, alias='restrictions')

    # The name of the track. 
    name: typing.Optional[str] = Field(None, alias='name')

    # The popularity of the track. The value will be between 0 and 100, with 100 being the most popular.<br/>The popularity of a track is a value between 0 and 100, with 100 being the most popular. The popularity is calculated by algorithm and is based, in the most part, on the total number of plays the track has had and how recent those plays are.<br/>Generally speaking, songs that are being played a lot now will have a higher popularity than songs that were played a lot in the past. Duplicate tracks (e.g. the same track from a single and an album) are rated independently. Artist and album popularity is derived mathematically from track popularity. _**Note**: the popularity value may lag actual popularity by a few days: the value is not updated in real time._ 
    popularity: typing.Optional[int] = Field(None, alias='popularity')

    # A link to a 30 second preview (MP3 format) of the track. Can be `null` 
    preview_url: typing.Optional[typing.Optional[str]] = Field(None, alias='preview_url')

    # The number of the track. If an album has several discs, the track number is the number on the specified disc. 
    track_number: typing.Optional[int] = Field(None, alias='track_number')

    # The object type: \"track\". 
    type: typing.Optional[Literal["track"]] = Field(None, alias='type')

    # The [Spotify URI](/documentation/web-api/concepts/spotify-uris-ids) for the track. 
    uri: typing.Optional[str] = Field(None, alias='uri')

    # Whether or not the track is from a local file. 
    is_local: typing.Optional[bool] = Field(None, alias='is_local')
    class Config:
        arbitrary_types_allowed = True
