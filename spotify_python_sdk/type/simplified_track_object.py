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

from spotify_python_sdk.type.external_url_object import ExternalUrlObject
from spotify_python_sdk.type.linked_track_object import LinkedTrackObject
from spotify_python_sdk.type.simplified_artist_object import SimplifiedArtistObject
from spotify_python_sdk.type.simplified_track_object_available_markets import SimplifiedTrackObjectAvailableMarkets
from spotify_python_sdk.type.track_restriction_object import TrackRestrictionObject

class RequiredSimplifiedTrackObject(TypedDict):
    pass

class OptionalSimplifiedTrackObject(TypedDict, total=False):
    # The artists who performed the track. Each artist object includes a link in `href` to more detailed information about the artist.
    artists: typing.List[SimplifiedArtistObject]

    available_markets: SimplifiedTrackObjectAvailableMarkets

    # The disc number (usually `1` unless the album consists of more than one disc).
    disc_number: int

    # The track length in milliseconds.
    duration_ms: int

    # Whether or not the track has explicit lyrics ( `true` = yes it does; `false` = no it does not OR unknown).
    explicit: bool

    # External URLs for this track. 
    external_urls: ExternalUrlObject

    # A link to the Web API endpoint providing full details of the track.
    href: str

    # The [Spotify ID](/documentation/web-api/concepts/spotify-uris-ids) for the track. 
    id: str

    # Part of the response when [Track Relinking](/documentation/web-api/concepts/track-relinking/) is applied. If `true`, the track is playable in the given market. Otherwise `false`. 
    is_playable: bool

    # Part of the response when [Track Relinking](/documentation/web-api/concepts/track-relinking/) is applied and is only part of the response if the track linking, in fact, exists. The requested track has been replaced with a different track. The track in the `linked_from` object contains information about the originally requested track.
    linked_from: LinkedTrackObject

    # Included in the response when a content restriction is applied. 
    restrictions: TrackRestrictionObject

    # The name of the track.
    name: str

    # A URL to a 30 second preview (MP3 format) of the track. 
    preview_url: typing.Optional[str]

    # The number of the track. If an album has several discs, the track number is the number on the specified disc. 
    track_number: int

    # The object type: \"track\". 
    type: str

    # The [Spotify URI](/documentation/web-api/concepts/spotify-uris-ids) for the track. 
    uri: str

    # Whether or not the track is from a local file. 
    is_local: bool

class SimplifiedTrackObject(RequiredSimplifiedTrackObject, OptionalSimplifiedTrackObject):
    pass
