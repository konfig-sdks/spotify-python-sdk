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


class RequiredDeviceObject(TypedDict):
    pass

class OptionalDeviceObject(TypedDict, total=False):
    # The device ID. This ID is unique and persistent to some extent. However, this is not guaranteed and any cached `device_id` should periodically be cleared out and refetched as necessary.
    id: typing.Optional[str]

    # If this device is the currently active device.
    is_active: bool

    # If this device is currently in a private session.
    is_private_session: bool

    # Whether controlling this device is restricted. At present if this is \"true\" then no Web API commands will be accepted by this device.
    is_restricted: bool

    # A human-readable name for the device. Some devices have a name that the user can configure (e.g. \\\"Loudest speaker\\\") and some devices have a generic name associated with the manufacturer or device model.
    name: str

    # Device type, such as \"computer\", \"smartphone\" or \"speaker\".
    type: str

    # The current volume in percent.
    volume_percent: typing.Optional[int]

    # If this device can be used to set the volume.
    supports_volume: bool

class DeviceObject(RequiredDeviceObject, OptionalDeviceObject):
    pass
