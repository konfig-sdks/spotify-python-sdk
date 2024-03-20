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

from spotify_python_sdk.type.explicit_content_settings_object import ExplicitContentSettingsObject
from spotify_python_sdk.type.external_url_object import ExternalUrlObject
from spotify_python_sdk.type.followers_object import FollowersObject
from spotify_python_sdk.type.image_object import ImageObject

class RequiredPrivateUserObject(TypedDict):
    pass

class OptionalPrivateUserObject(TypedDict, total=False):
    # The country of the user, as set in the user's account profile. An [ISO 3166-1 alpha-2 country code](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). _This field is only available when the current user has granted access to the [user-read-private](/documentation/web-api/concepts/scopes/#list-of-scopes) scope._ 
    country: str

    # The name displayed on the user's profile. `null` if not available. 
    display_name: str

    # The user's email address, as entered by the user when creating their account. _**Important!** This email address is unverified; there is no proof that it actually belongs to the user._ _This field is only available when the current user has granted access to the [user-read-email](/documentation/web-api/concepts/scopes/#list-of-scopes) scope._ 
    email: str

    # The user's explicit content settings. _This field is only available when the current user has granted access to the [user-read-private](/documentation/web-api/concepts/scopes/#list-of-scopes) scope._ 
    explicit_content: ExplicitContentSettingsObject

    # Known external URLs for this user.
    external_urls: ExternalUrlObject

    # Information about the followers of the user.
    followers: FollowersObject

    # A link to the Web API endpoint for this user. 
    href: str

    # The [Spotify user ID](/documentation/web-api/concepts/spotify-uris-ids) for the user. 
    id: str

    # The user's profile image.
    images: typing.List[ImageObject]

    # The user's Spotify subscription level: \"premium\", \"free\", etc. (The subscription level \"open\" can be considered the same as \"free\".) _This field is only available when the current user has granted access to the [user-read-private](/documentation/web-api/concepts/scopes/#list-of-scopes) scope._ 
    product: str

    # The object type: \"user\" 
    type: str

    # The [Spotify URI](/documentation/web-api/concepts/spotify-uris-ids) for the user. 
    uri: str

class PrivateUserObject(RequiredPrivateUserObject, OptionalPrivateUserObject):
    pass
