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
from spotify_python_sdk.pydantic.image_object import ImageObject
from spotify_python_sdk.pydantic.playlist_owner_object import PlaylistOwnerObject
from spotify_python_sdk.pydantic.playlist_tracks_ref_object import PlaylistTracksRefObject

class SimplifiedPlaylistObject(BaseModel):
    # The playlist description. _Only returned for modified, verified playlists, otherwise_ `null`. 
    description: typing.Optional[str] = Field(None, alias='description')

    # `true` if the owner allows other users to modify the playlist. 
    collaborative: typing.Optional[bool] = Field(None, alias='collaborative')

    # Known external URLs for this playlist. 
    external_urls: typing.Optional[ExternalUrlObject] = Field(None, alias='external_urls')

    # A link to the Web API endpoint providing full details of the playlist. 
    href: typing.Optional[str] = Field(None, alias='href')

    # The [Spotify ID](/documentation/web-api/concepts/spotify-uris-ids) for the playlist. 
    id: typing.Optional[str] = Field(None, alias='id')

    # Images for the playlist. The array may be empty or contain up to three images. The images are returned by size in descending order. See [Working with Playlists](/documentation/web-api/concepts/playlists). _**Note**: If returned, the source URL for the image (`url`) is temporary and will expire in less than a day._ 
    images: typing.Optional[typing.List[ImageObject]] = Field(None, alias='images')

    # The name of the playlist. 
    name: typing.Optional[str] = Field(None, alias='name')

    # The user who owns the playlist 
    owner: typing.Optional[PlaylistOwnerObject] = Field(None, alias='owner')

    # The playlist's public/private status: `true` the playlist is public, `false` the playlist is private, `null` the playlist status is not relevant. For more about public/private status, see [Working with Playlists](/documentation/web-api/concepts/playlists) 
    public: typing.Optional[bool] = Field(None, alias='public')

    # The version identifier for the current playlist. Can be supplied in other requests to target a specific playlist version 
    snapshot_id: typing.Optional[str] = Field(None, alias='snapshot_id')

    # A collection containing a link ( `href` ) to the Web API endpoint where full details of the playlist's tracks can be retrieved, along with the `total` number of tracks in the playlist. Note, a track object may be `null`. This can happen if a track is no longer available. 
    tracks: typing.Optional[PlaylistTracksRefObject] = Field(None, alias='tracks')

    # The object type: \"playlist\" 
    type: typing.Optional[str] = Field(None, alias='type')

    # The [Spotify URI](/documentation/web-api/concepts/spotify-uris-ids) for the playlist. 
    uri: typing.Optional[str] = Field(None, alias='uri')
    class Config:
        arbitrary_types_allowed = True
