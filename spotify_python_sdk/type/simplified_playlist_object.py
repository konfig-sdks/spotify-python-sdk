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
from spotify_python_sdk.type.image_object import ImageObject
from spotify_python_sdk.type.playlist_owner_object import PlaylistOwnerObject
from spotify_python_sdk.type.playlist_tracks_ref_object import PlaylistTracksRefObject

class RequiredSimplifiedPlaylistObject(TypedDict):
    pass

class OptionalSimplifiedPlaylistObject(TypedDict, total=False):
    # The playlist description. _Only returned for modified, verified playlists, otherwise_ `null`. 
    description: str

    # `true` if the owner allows other users to modify the playlist. 
    collaborative: bool

    # Known external URLs for this playlist. 
    external_urls: ExternalUrlObject

    # A link to the Web API endpoint providing full details of the playlist. 
    href: str

    # The [Spotify ID](/documentation/web-api/concepts/spotify-uris-ids) for the playlist. 
    id: str

    # Images for the playlist. The array may be empty or contain up to three images. The images are returned by size in descending order. See [Working with Playlists](/documentation/web-api/concepts/playlists). _**Note**: If returned, the source URL for the image (`url`) is temporary and will expire in less than a day._ 
    images: typing.List[ImageObject]

    # The name of the playlist. 
    name: str

    # The user who owns the playlist 
    owner: PlaylistOwnerObject

    # The playlist's public/private status: `true` the playlist is public, `false` the playlist is private, `null` the playlist status is not relevant. For more about public/private status, see [Working with Playlists](/documentation/web-api/concepts/playlists) 
    public: bool

    # The version identifier for the current playlist. Can be supplied in other requests to target a specific playlist version 
    snapshot_id: str

    # A collection containing a link ( `href` ) to the Web API endpoint where full details of the playlist's tracks can be retrieved, along with the `total` number of tracks in the playlist. Note, a track object may be `null`. This can happen if a track is no longer available. 
    tracks: PlaylistTracksRefObject

    # The object type: \"playlist\" 
    type: str

    # The [Spotify URI](/documentation/web-api/concepts/spotify-uris-ids) for the playlist. 
    uri: str

class SimplifiedPlaylistObject(RequiredSimplifiedPlaylistObject, OptionalSimplifiedPlaylistObject):
    pass
